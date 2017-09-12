from math import pi, sin, cos, ceil


def spiral(mc, x, y, z, radius, btype, subtype, height=0, turns=1, start=0):
    start *= 2*pi/360
    if radius < 1:
        if subtype == False:
            mc.setBlocks(x, y, z, x, y + height, z, btype, subtype)
        else:
            mc.setBlocks(x, y, z, x, y + height, z, btype, subtype)
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
            if subtype == False:
                mc.setBlock(xx, yy + i / distance * height, zz, btype)
                mc.setBlocks(xx, yy + i / distance * height, zz, xx, yy + i / distance * height + dy, zz, btype)
            else:
                mc.setBlock(xx, yy + i/distance*height, zz,  btype, subtype)
                mc.setBlocks(xx, yy + i/distance*height, zz, xx, yy + i/distance*height + dy, zz,  btype, subtype)
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

                if subtype == False:
                    mc.setBlock(px + delta_px, yy + i / distance * height, pz + delta_pz, btype)
                else:
                    mc.setBlock(px + delta_px, yy + i/distance*height, pz + delta_pz,  btype, subtype)

            py = yy + i/distance*height
            px = xx
            pz = zz


def stairs(x, y, z, radius, width, btype, subtype, height=0, turns=1, start=0, railings=False):
    import remoteMCServer
    mc = remoteMCServer.create("")

    for stair in range(width):
        spiral(mc, x, y, z, radius + stair, btype, subtype, height, turns, start)

    if railings == True:
        spiral(mc, x, y + 2, z, radius - 1, height, turns, start)
        spiral(mc, x, y + 2, z, radius + width, height, turns, start)
