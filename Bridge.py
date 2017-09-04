import math

GOLD = 41
LEAVES = 18
TNT = 49


def line(mc, x1, y1, z1, x2, y2, z2, dip=0, btype=GOLD, stype=None):
    dx = x2 - x1
    dy = y2 - y1
    dz = z2 - z1

    steps = int(math.ceil(max(abs(dx), abs(dy), abs(dz))))

    dx /= steps
    dy /= steps
    dz /= steps

    for i in range(steps + 1):
        f = i / steps
        g = 1 - i/steps
        y_dip = 4*dip*f*g
        if stype:
            mc.setBlock(int(round(x1 + dx*i)), int(round(y1 + dy*i - y_dip)), int(round(z1 + dz*i)), btype, stype)
        else:
            mc.setBlock(int(round(x1 + dx*i)), int(round(y1 + dy*i - y_dip)), int(round(z1 + dz*i)), btype)


def bridge(mc, x1, y1, z1, x2, y2, z2, width=4, dip=0, railings=True, btype=GOLD, stype=None):
    # calculate distance between two points, in 2D
    dx = x2 - x1
    dz = z2 - z1

    # shrink d by its length, making it length 1
    length = math.sqrt(dx*dx + dz*dz)
    dx /= length*4
    dz /= length*4

    # rotate D by 90
    ux = -dz
    uz = dx

    # main path
    for i in range(-width*2, width*2+1):
        line(mc, x1 + ux*i, y1, z1 + uz*i, x2 + ux*i, y2, z2 + uz*i, dip, btype, stype)

    # railings
    if railings:
        i = -width*2
        line(mc, x1 + ux * i, y1 + 2, z1 + uz * i, x2 + ux * i, y2 + 2, z2 + uz * i, dip, btype, stype)
        i = width*2
        line(mc, x1 + ux * i, y1 + 2, z1 + uz * i, x2 + ux * i, y2 + 2, z2 + uz * i, dip, btype, stype)


if __name__ == "__main__":
    import remoteMCServer

    mc = remoteMCServer.create("")

    pos = mc.player.getPos()
    bridge(mc, pos.x-10, pos.y+2, pos.z-10, pos.x+10, pos.y+5, pos.z+15, 4, dip=5)
