####################################################################
# Test Demos from the book The Inventor Mentor in a workbench      #
# By ceanwu@yahoo.com                                              #
# No warranty.                                                     #
# Modified Mariwan Jalal's FreeCAD macro to be a command           #
####################################################################
###
# This is an example from the Inventor Mentor,
# chapter 4, example 2.
#
# Lights example.  
# Read in an object from a file.
# Use the ExaminerViewer to view it with two light coin.Sources.
# The red directional light doesn't move; the green point 
# light is moved back and forth using a shuttle node.
#
import os,sys
import FreeCAD as App
import FreeCADGui as Gui
import pivy.coin as coin

class hLights:
    "hLights"
    def GetResources(self):
        return {"MenuText": "hLights",
                "Accel": "Ctrl+t",
                "ToolTip": "Use the ExaminerViewer to view it with two light coin.Sources. The red directional light doesn't move; the green point light is moved back and forth using a shuttle node.",
                "Pixmap": os.path.dirname(__file__)+"./resources/4.2.svg"
        }

    def IsActive(self):

        if App.ActiveDocument == None:
            return False
        else:
            return True

    def Activated(self):

        root = coin.SoSeparator()

        # Add a directional light
        myDirLight = coin.SoDirectionalLight()
        myDirLight.direction = (0, -1, -1)
        myDirLight.color = (1, 0, 0)
        root.addChild(myDirLight)

        # Put the shuttle and the light below a transform separator.
        # A transform separator pushes and pops the transformation 
        # just like a separator node, but other aspects of the state 
        # are not pushed and popped. coin.So the shuttle's translation 
        # will affect only the light. But the light will shine on 
        # the rest of the scene.
        myTransformSeparator = coin.SoTransformSeparator()
        root.addChild(myTransformSeparator)

        # A shuttle node translates back and forth between the two
        # fields translation0 and translation1.  
        # This moves the light.
        myShuttle = coin.SoShuttle()
        myTransformSeparator.addChild(myShuttle)
        myShuttle.translation0 = (-2, -1, 3)
        myShuttle.translation1 = ( 1,  2, -3)

        # Add the point light below the transformSeparator
        myPointLight = coin.SoPointLight()
        myTransformSeparator.addChild(myPointLight)
        myPointLight.color = (0, 1, 0)

        root.addChild(coin.SoCone())
        #Main function 
        view = Gui.ActiveDocument.ActiveView
        sg = view.getSceneGraph()
        sg.addChild(root)
        Gui.SendMsgToActiveView('ViewFit')
    
Gui.addCommand('hLights',hLights())