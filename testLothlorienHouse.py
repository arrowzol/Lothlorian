from mcpi.minecraft import Minecraft
import mcpi.block as block
import random
import lothlorienHouse
mc = Minecraft.create()

#def main():
    #for i in range(50):
        #x = random.randint(-10, 500)
        #z = random.randint(-10, 500)
        #y = mc.getHeight(x, z)
        #s = random.randint(5, 10)
        #odd sizes keep door in center
lothlorienHouse.buildHouse(mc,17,4,891,7)


#main()
