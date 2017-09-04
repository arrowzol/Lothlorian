#!python
#  This is a program by me, the Curtis. It is the master program that puts all the Lothlorian stuff together. Yup.
#  The day is September 4th 2017.

import remoteMCServer

import lothlorienHouse, treeBuilder

mc = remoteMCServer.create("")


pos = mc.player.getPos()
x = round(pos.x)
z = round(pos.z)
y = round(pos.y)


def treeHouse(mc, x, y, z):
    treeBuilder.treeBuilder(mc, x, y, z, 2)
    lothlorienHouse.buildHouse(mc, x - 2, y + 52, z  - 3, 5)
