import nuke

nuke.pluginAddPath('./Gizmos')

print("\033[33mToolkit: Loading...\033[00m")

toolbar = nuke.toolbar('Nodes')
rebelNode = toolbar.addMenu('IBKColour_Multiplier', 'IBKColour.png')

rebelNode.addCommand('Credits', 'nuke.createNode(\"Credits_fededirag\")', icon="Backdrop.png")
rebelNode.addCommand('IBKColour_Multiplier', 'nuke.createNode(\"IBKColour_Multiplier\")', icon="IBKColour.png")


print("\033[92mToolkit: Successfully Loaded\033[00m")
