#!python
#  This is a program by me, the Curtis. It is the master program that puts all the Lothlorian stuff together. Yup.
#  The day is September 4th 2017.

import remoteMCServer

import lothlorienHouse

mc = remoteMCServer.create("")


pos = mc.player.getPos()
x = round(pos.x)
z = round(pos.z)
y = round(pos.y)

lothlorienHouse.buildHouse(mc, x, y, z, 10)
lothlorienHouse.buildHouse(mc, x + 50, y + 10, z + 32, 20)