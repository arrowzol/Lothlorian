import remoteMCServer

import math
from mcpi.minecraft import Minecraft

'''def makeCircle(mc, x, y, z, radius=3):
    pos = mc.player.getPos()

    blockType = 0

    for i in range(360):
        x = x+((math.cos(i)) * radius)
        z = z+((math.sin(i)) * radius)
        mc. setBlock(x, y, z, (17, 2))
'''


def makeCircle(mc, x, y, z, radius, btype):
    radius = int(radius)
    x = int(x)
    if radius < 1:
        mc.setBlock(x, y, z, btype)
    radSquordy = radius ** 2
    yy = int(round(y))
    distance = int(math.ceil(1.01 * 2 * math.pi * radius))
    px = int(round(x + radius))
    pz = int(round(z))
    for i in range(distance + 1):
        theta = i * 2 * math.pi / distance
        xx = int(round(x + radius * math.cos(theta)))
        zz = int(round(z + radius * math.sin(theta)))

        dx = xx - px
        dz = zz - pz

        if dx or dz:
            mc.setBlock(xx, yy, zz, btype)
            if dx and dz:
                mx = px + dx / 2 - x
                mz = pz + dz / 2 - z
                distSquard = mx ** 2 + mz ** 2
                if distSquard > radSquordy:
                    dpx = (dx - dz) / 2
                    dpz = (dz + dx) / 2
                else:
                    dpx = (dx + dz) / 2
                    dpz = (dz - dx) / 2
                mc.setBlock(px + dpx, yy, pz + dpz, btype)
            px = xx
            pz = zz


def buildSphere(mc, x, y, z, r=10, blockType=(18, 6)):
    if r == 15:
        y += 13
        r += 1

    if r == 3:
        r = 5

    # Define the building square for the sphere
    xMin = x - r
    xMax = x + r
    #    yMin = y - r*sin(yAngleStart)
    yMin = y - r
    yMax = y + r
    zMin = z - r
    zMax = z + r

    for ix in range(xMin, xMax + 1):
        for iy in range(yMin, yMax + 1):
            for iz in range(zMin, zMax + 1):
                if (((ix - x) ** 2 + (iy - y) ** 2 + (iz - z) ** 2) ** 0.5) < r:
                    mc.setBlock(ix, iy, iz, blockType)


def treeBuilder(mc, x, y, z, scale):
    for i in range(30 + (scale * 3)):
        makeCircle(mc, x, y, z, scale, (17, 2))
        y += 1
    buildSphere(mc, x, y, z, 3 * scale)
    mc = remoteMCServer.create("")


treeBuilder(142, 25, 26, 5)