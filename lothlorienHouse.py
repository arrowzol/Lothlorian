#Mason J. Settergren
from mcpi.minecraft import Minecraft
import mcpi.block as block
import math



def buildHouse(mc,ctrx,y,ctrz,width=7):

    height = width
    length = int(width)

    # Find the corner
    x = ctrx - int(width / 2)
    z = ctrz - int(length / 2)

    air = 0
    doorx = x + int(width * 0.5)

    #make a cuboid
    mc.setBlocks(x, y, z, x + width-1, y + height-1, z + length-1, 5,2)
    #hollow it out
    mc.setBlocks(x+1,y+1,z+1,x+width-2,y+height-2,z+length-2,air)
    #add carpets
    mc.setBlocks(x + 1, y + 1, z + 1, x + width - 2, y+1, z + length - 2, 171,13)

    #make layer 1 of roof with overhang
    roofx = x - 1
    roofy = y + height
    roofw = width
    while roofw >= 0:
        mc.setBlocks(roofx, roofy, z, roofx + roofw + 1, roofy, z + length-1, 18,6)
        roofx += 1
        roofy += 1
        roofw -= 2
    #2 part door, torch, and windows
    mc.setBlock(doorx, y + 1, z, 193)
    mc.setBlock(doorx, y + 2, z, 193)
    mc.setBlock(doorx, y + 3, z + 1, 5,2)
    mc.setBlock(doorx, y + 4, z + 1, 50)
    mc.setBlocks(x, y + 2, z + 2, x, y + 3, z + int(5/7 * length), 102)
    mc.setBlocks(x + width - 1, y + 2, z + 2, x + width - 1, y + 3, z + int(5 / 7 * length), 102)

    #circular porch
    #radius of circle is different from center to corner
    r = int(width/math.sqrt(2) + 3)
    mc.setBlocks(x - 2, y, z - 2, x + width + 1, y, z + length + 1, 5,2)

    #finding the circle
    for dx in range(-r,r+1):
        for dz in range(-r,r+1):
            if dx*dx + dz*dz <= r*r:#pythagoras
                mc.setBlock(ctrx + dx,y,ctrz + dz, 5,2)

if __name__ == "__main__":
    import remoteMCServer
    mc = remoteMCServer.create("")
    #Clear out area before testing again
    mc.setBlocks(-20,4,-20,20,20,20,0)
    buildHouse(mc, 0, 4, 0)



