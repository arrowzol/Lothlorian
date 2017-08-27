import remoteMCServer
from math import pi, sin, cos, ceil
from mcpi.minecraft import Minecraft
mc = remoteMCServer.create("")

def spiral(x, y, z, radius, height=0, turns=1, start=0, btype=41):
    start *= 2*pi/360
    end = start + 2*pi*turns
    if radius < 1:
        mc.setBlocks(x, y, z, x, y + height, z, btype)
    radSquordy = radius**2
    yy = int(round(y))

    distance = int(ceil(1.01*2*pi*radius*turns))
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


pos = mc.player.getPos()
x = round(pos.x)
z = round(pos.z)
y = round(pos.y)

for blahdy in range(5):
    spiral(x, y, z, 15 + blahdy, 256, 5)