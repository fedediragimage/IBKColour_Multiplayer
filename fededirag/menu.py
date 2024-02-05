import nuke

nuke.pluginAddPath('./Gizmos')

print("\033[33mfededirag Toolkit: Loading...\033[00m")

#setup menu
toolbar = nuke.toolbar('Nodes')
rebelNode = toolbar.addMenu('fededirag', 'fededirag.png')

#add gizmos
rebelNode.addCommand('Credits', 'nuke.createNode(\"Credits_fededirag\")', icon="fededirag.png")
rebelNode.addCommand('IBKColour_Multiplayer', 'nuke.createNode(\"IBKColour_Multiplayer\")', icon="IBKColour.png")
rebelNode.addCommand('fd_LensCompressionCalc', 'nuke.createNode(\"fd_LensCompressionCalc\")', icon="2DMasked.png")


print("\033[92mfededirag Toolkit: Successfully Loaded\033[00m")
