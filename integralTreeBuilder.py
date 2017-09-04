def intregralTreeBuilder(mc, x, input, z, scale):
    treeHeight = input
    y = treeHeight
    for i in range(treeHeight + scale *3):
        makeCircle(mc, x, y, z, scale, (17, 2))
        y += 1
        buildSphere(mc, x, y, x, 3 * scale)
        mc = remoteMCServer.create("")

integralTreeBuilder(mc, x, input, z, scale)
