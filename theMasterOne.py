#!python
#  This is a program by me, the Curtis. It is the master program that puts all the Lothlorian stuff together. Yup.
#  The day is September 4th 2017.

import remoteMCServer

import lothlorienHouse, treeBuilder, stairs

mc = remoteMCServer.create("")


pos = mc.player.getPos()
x = round(pos.x)
z = round(pos.z)
y = round(pos.y)

# x = 1000000
# y = 4
# z = 1000000


def treeHouse(mc, x, y, z):
    treeTop = treeBuilder.treeBuilder(mc, x, y, z)
    lothlorienHouse.buildHouse(mc, x, treeTop, z)
    return treeTop

treeTop = treeHouse(mc, x, y, z)
for daOne in range(3):
    stairs.stairs(x, y + 1 + daOne, z, 6, 3, 0, False, height=treeTop - y, turns=4)
    stairs.stairs(x, y + 1 + daOne, z, 6, 3, 0, False, height=treeTop - y, turns=4)
stairs.stairs(x, y, z, 6, 3, 17, 2, treeTop - y, 4)
