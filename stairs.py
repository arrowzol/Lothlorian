from math import pi, sin, cos, ceil


def spiral(mc, x, y, z, radius, height=0, turns=1, start=0):
    start *= 2*pi/360
    if radius < 1:
        mc.setBlocks(x, y, z, x, y + height, z, 17, 2)
    radius_squared = radius**2
    yy = int(round(y))

    turn_clockwise = turns < 0
    distance = int(ceil(1.01*2*pi*radius*abs(turns)))
    px = int(round(x + radius))
    pz = int(round(z))

    py = yy
    for i in range(distance + 1):
        theta = start + i*2*pi/distance*turns
        xx = int(round(x + radius*cos(theta)))
        zz = int(round(z + radius*sin(theta)))

        dx = xx - px
        dz = zz - pz
        dy = (yy + i/distance*height) - py

        if not i or dx or dz:
            mc.setBlock(xx, yy + i/distance*height, zz, 17, 2)
            mc.setBlocks(xx, yy + i/distance*height, zz, xx, yy + i/distance*height + dy, zz, 17, 2)
            if i and dx and dz:
                mx = px + dx/2 - x
                mz = pz + dz/2 - z
                dist_squared = mx**2 + mz**2
                if (dist_squared > radius_squared) ^ turn_clockwise:
                    delta_px = (dx - dz)/2
                    delta_pz = (dz + dx)/2
                else:
                    delta_px = (dx + dz)/2
                    delta_pz = (dz - dx)/2

                mc.setBlock(px + delta_px, yy + i/distance*height, pz + delta_pz, 17, 2)

            py = yy + i/distance*height
            px = xx
            pz = zz


def stais(radius, width, height=0, turns=1, start=0, railings=False):
    import remoteMCServer
    mc = remoteMCServer.create("")

    pos = mc.player.getPos()
    x = round(pos.x)
    z = round(pos.z)
    y = round(pos.y)

    for stair in range(width):
        spiral(mc, x, y, z, radius + stair, height, turns, start)

    if railings == True:
        spiral(mc, x, y + 2, z, radius - 1, height, turns, start)
        spiral(mc, x, y + 2, z, radius + width, height, turns, start)

stais(5, 5, 50, 2, 0, True)