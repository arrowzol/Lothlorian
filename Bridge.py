from mcpi.minecraft import Minecraft
import math

GOLD = 41
LEAVES = 18


def line(mc, x1, y1, z1, x2, y2, z2):
    dx = x2 - x1
    dy = y2 - y1
    dz = z2 - z1

    steps = int(math.ceil(max(abs(dx), abs(dy), abs(dz))))

    dx /= steps
    dy /= steps
    dz /= steps

    for i in range(steps + 1):
        mc.setBlock(x1 + dx*i, y1 + dy*i, z1 + dz*i, GOLD)


def bridge(mc, x1, y1, z1, x2, y2, z2, width=4, railings=True):
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
        line(mc, x1 + ux*i, y1, z1 + uz*i, x2 + ux*i, y2, z2 + uz*i)

    # railings
    if railings:
        i = -width*2
        line(mc, x1 + ux * i, y1 + 2, z1 + uz * i, x2 + ux * i, y2 + 2, z2 + uz * i)
        i = width*2
        line(mc, x1 + ux * i, y1 + 2, z1 + uz * i, x2 + ux * i, y2 + 2, z2 + uz * i)


if __name__ == "__main__":
    mc = Minecraft.create()
    pos = mc.player.getPos()
    bridge(mc, pos.x-10, pos.y+10, pos.z-10, pos.x+10, pos.y+14, pos.z+15, 4)
