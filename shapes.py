from math import pi, sin, cos, ceil


def spiral(mc, x, y, z, radius, height=0, turns=1, start=0, btype=41):
    start *= 2*pi/360
    if radius < 1:
        mc.setBlocks(x, y, z, x, y + height, z, btype)
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
            mc.setBlock(xx, yy + i/distance*height, zz, btype)
            mc.setBlocks(xx, yy + i/distance*height, zz, xx, yy + i/distance*height + dy, zz, btype)
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

                mc.setBlock(px + delta_px, yy + i/distance*height, pz + delta_pz, btype)

            py = yy + i/distance*height
            px = xx
            pz = zz


if __name__ == "__main__":
    import remoteMCServer
    mc = remoteMCServer.create("")

    import Bridge

    pos = mc.player.getPos()
    x = round(pos.x)
    z = round(pos.z)
    y = round(pos.y)


    h = 20
    r = 5
    l=30
    numOfSpirals = 3

    for i in range(numOfSpirals):
        spiral(mc, x - r - 3, y, z + 1, r + i, height=h, turns=-2)

    railings = True
    if railings:
        spiral(mc, x - r - 3, y + 2, z + 1, r + i + 1, height=h, turns=-2)
        spiral(mc, x - r - 3, y + 2, z + 1, r - 1, height=h, turns=-2)
    # Bridge.bridge(mc, x, y+h, z, x, y+h, z+l, width=5)
    # for i in range(5):
    #     spiral(mc, x-r-3, y, z, r + i, height=h, turns=2)
    #     spiral(mc, x-r-3, y, z+l, r + i, height=h, turns=-2)
