#!python
#  This is a program by me, the Curtis. It is the master program that puts all the Lothlorian stuff together. Yup.
#  The day is September 4th 2017.

import remoteMCServer

import lothlorienHouse, treeBuilder, Bridge

mc = remoteMCServer.create("")


pos = mc.player.getPos()
x = round(pos.x)
z = round(pos.z)
y = round(pos.y)

x = 100100
y = 4
z = 100000

def treeHouse(mc, x, y, z):
    treeTop = treeBuilder.treeBuilder(mc, x, y, z)
    lothlorienHouse.buildHouse(mc, x, treeTop, z, 5)
    return treeTop

treeTop1 = treeHouse(mc, x + 10, y, z)
treeTop2 = treeHouse(mc, x + 30, y, z + 60)
Bridge.bridge(mc, x + 10, treeTop1, z, x + 30, treeTop2, z + 60, 17, railings=False)