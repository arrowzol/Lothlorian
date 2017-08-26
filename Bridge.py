from mcpi.minecraft import Minecraft
import math

GOLD = 41
LEAVES = 18


def line(mc, x1, y1, z1, x2, y2, z2):
    dx = x2 - x1
    dy = y2 - y1
    dz = z2 - z1

    steps = int(math.ceil(max(abs(dx), abs(dy), abs(dz))))
    print("Steps %d"%steps)

    dx /= steps
    dy /= steps
    dz /= steps

    for i in range(steps + 1):
        mc.setBlock(x1 + dx*i, y1 + dy*i, z1 + dz*i, GOLD)


def bridge(mc, x1, y1, z1, x2, y2, z2):
    dx = x2 - x1
    dz = z2 - z1
    math.sqrt(dx*dx + dz*dz)

    steps = int(math.ceil(max(abs(dx), abs(dy), abs(dz))))
    line(mc, x1, y1, z1, x2, y2, z2)


if __name__ == "__main__":
    mc = Minecraft.create()
    pos = mc.player.getPos()
    bridge(mc, pos.x-10, pos.y+10, pos.z-10, pos.x+10, pos.y+14, pos.z+15)

