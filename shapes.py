from math import pi, sin, cos, ceil


def spiral(mc, x, y, z, radius, height=0, turns=1, start=0, btype=41):
    start *= 2*pi/360
    if radius < 1:
        mc.setBlocks(x, y, z, x, y + height, z, btype)
    radSquordy = radius**2
    yy = int(round(y))

    distance = int(ceil(1.01*2*pi*radius*abs(turns)))
    px = int(round(x + radius))
    pz = int(round(z))

    for i in range(distance + 1):
        if i == 0:
            py = yy + i/distance*height
        theta = start + i*2*pi/distance*turns
        xx = int(round(x + radius*cos(theta)))
        zz = int(round(z + radius*sin(theta)))

        test1 = yy + i/distance*height
        dx = xx - px
        dz = zz - pz
        dy = (yy + i/distance*height) - py

        if dx or dz:
            mc.setBlock(xx, yy + i/distance*height, zz, btype)
            mc.setBlocks(xx, yy + i/distance*height, zz, xx, yy + i/distance*height + dy, zz, btype)
            if dx and dz:
                mx = px + dx/2 - x
                mz = pz + dz/2 - z
                distSquard = mx**2 + mz**2
                if distSquard > radSquordy:
                    dpx = (dx - dz)/2
                    dpz = (dz + dx)/2
                else:
                    dpx = (dx + dz)/2
                    dpz = (dz - dx)/2

                mc.setBlock(px + dpx, yy + i/distance*height, pz + dpz, btype)

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

    Bridge.bridge(mc, x, y+h, z, x, y+h, z+l, width=5)
    for i in range(5):
        spiral(mc, x-r-3, y, z, r + i, height=h, turns=2)
        spiral(mc, x-r-3, y, z+l, r + i, height=h, turns=-2)
