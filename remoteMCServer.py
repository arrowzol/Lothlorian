#! /usr/bin/env python3
# Alexis Perumal, 7/30/17
# remoteMCServer.py
# Use this module to connect to non-localhost Minecraft servers.
# To use it:
#   1. The shebang string at the top of this file is for the Mac. You may need
#      to change it for your OS if you want to run this from the command line.
#       Mac: #! /usr/bin/env python3
#       Win: #! python3
#       Linux:#! /usr/bin/python3
#   2. At (or near) the top of your program, include:
#        import remoteMCServer
#   3. In your code, connect with a statement like:
#        mc = remoteMCServer.create("")
#
# You should be good to go! If it doesn't work, contact me.

from mcpi.minecraft import Minecraft

import shelve

# create()
#
# Requires:
#   from mcpi.minecraft import Minecraft
#   import shelve
#
# Parameter:
#   server (string), defaults to 'localhost'. Passing a string, opens that location. An empty string prompts the user considering a previous value
#
# Desciption:
#   Connects to a minecraft server and world, and returns the object pointing to it.
#   You can pass an IP address as a string and it will attempt to connect.
#   If an empty string isn't passed, then we'll check the shelf file for a previous value and propose it in a prompt.
#   If one isn't there, then we'll prompt.
def create(server="localhost"):
    if len(server) == 0: # Means we should do something other than the default of 'localhost'         
        shelfFile = shelve.open('myMCserverData')
        if 'server' in shelfFile: # There was a previous entry which should be considered
            usrInput = input("Enter the server IP Address (or hit return to get " + shelfFile['server'] + "): ")
            if len(usrInput) == 0:
                server = shelfFile['server']
            else:
                server = usrInput
        else: # The shelfFile didn't have anything in it. Prompt the user.
            usrInput = input("Enter the server IP address (or hit return if local): ")
            if len(usrInput) == 0:
                server = 'localhost'
            else:
                server = usrInput
    # Finally, create the connection to the Minecraft server
    mc = Minecraft.create(server)

    # Assuming we didn't bomb out due to a bad server value, write out the server value to the shelf file
    shelfFile['server'] = server

    # Now do some minimal interaction with the server, letting it know we are here, and get the position, then return.
    if 'userName' in shelfFile:
        yourName = input("Enter your name (or hit return to get '" + shelfFile['userName'] + "'): ")
        if len(yourName) == 0:
            yourName = shelfFile['userName']
    else:
        yourName = input("Enter your name: ")
    shelfFile['userName'] = yourName
    shelfFile.close()
    mc.postToChat(yourName + ": Connected")
    pos = mc.player.getTilePos()
    msg = "Player position: (" + str(pos.x) + ", " + str(pos.y) + ", " + str(pos.z) + ")"
    print(msg)
    return mc



