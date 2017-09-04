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

x = 1000000
y = 4
z = 1000000

def treeHouse(mc, x, y, z):
    treeBuilder.treeBuilder(mc, x, y, z, 2)
    lothlorienHouse.buildHouse(mc, x - 2, y + 52, z - 3, 5)

treeHouse(mc, x + 10, y, z)
treeHouse(mc, x + 30, y, z + 60)
Bridge.bridge(mc, x + 10, y + 52, z, x + 30, y + 52, z + 60, 17, railings=False)