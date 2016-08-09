import nuke, nukescripts

def extractSelectedShapes():
    panel = nuke.Panel("extractSelectedShapes", 200)
    panel.addEnumerationPulldown('shapes goes to:\nroto node', 'single each')
    panel.addButton("cancel")
    panel.addButton("ok")
    showPanel = panel.show()
    userChoice = panel.value('shapes goes to:\nroto node')
    if showPanel == 0:
        return
    if showPanel == 1:
        selNode = None
        try:
            selNode = nuke.selectedNode()
            selXpos = selNode.xpos()
            selYpos = selNode.ypos()
        except ValueError: # no node selected
            pass

        if selNode:
            if userChoice == 'single':
                newRotoNode = nuke.createNode('RotoPaint')
                print newRotoNode
                newRotoNode['xpos'].setValue(selXpos+200)
                newRotoNode['ypos'].setValue(selYpos)
                newRotoNode['curves'].rootLayer.setTransform(selNode['curves'].rootLayer.getTransform())
                newRotoNode.setSelected('True')
                for selShape in selNode['curves'].getSelected():
                    shapeName = selShape.name
 #                  newRotoNode.setName('Converted')
                    newRotoNode['curves'].rootLayer.append(selShape.clone())
                    nuke.selectedNode()['scale'].setValue(2)
                    nuke.selectedNode()['center'].setValue(0)
                    nuke.selectedNode()['label'].setValue("converted")
                    getval = nuke.selectedNode()['brush_size'].value()
                    
                  #  getVal = newRotoNode['brush_size'].getValue()
                    print getval
                    newVal = getval *2
                    print newVal
                    #a = newRotoNode['brush_size'].setValue(newVal)

            if userChoice == 'each':
                for selShape in selNode['curves'].getSelected():
                    selXpos = selXpos + 200
                    shapeName = selShape.name
                    newRotoNode = nuke.nodes.Roto()
                    newRotoNode['curves'].rootLayer.setTransform(selNode['curves'].rootLayer.getTransform())
                    newRotoNode['xpos'].setValue(selXpos)
                    newRotoNode['ypos'].setValue(selYpos)
#                    newRotoNode.setName(selNode)
                    newRotoNode['curves'].rootLayer.append(selShape.clone())
                    
        else:
            nuke.message('<center>make sure you have selected your roto node\n<center>then try again :)')
