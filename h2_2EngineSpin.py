####################################################################
# Test Demos from the book The Inventor Mentor in a workbench      #
# By ceanwu@yahoo.com                                              #
# No warranty.                                                     #
# Modified Mariwan Jalal's FreeCAD macro to be a command           #
####################################################################
###
# This is an example from the Inventor Mentor
# chapter 2, example 2.
#
# Use an engine to make the cone spin.
#
import os,sys
import FreeCAD as App
import FreeCADGui as Gui
import pivy.coin as coin

class hEngineSpin:
    "hEngineSpin"
    def GetResources(self):
        return {"MenuText": "hEngineSpin",
                "Accel": "Ctrl+t",
                "ToolTip": "Use an engine to make the cone spin",
                "Pixmap": os.path.dirname(__file__)+"./resources/2.2.svg"
        }

    def IsActive(self):

        if App.ActiveDocument == None:
            return False
        else:
            return True

    def Activated(self):

        root = coin.SoSeparator()

        root.addChild(coin.SoDirectionalLight())
        
        # This transformation is modified to rotate the cone
        myRotXYZ = coin.SoRotationXYZ()
        root.addChild(myRotXYZ)

        myMaterial = coin.SoMaterial()
        myMaterial.diffuseColor = (1.0, 0.0, 0.0)   # Red
        root.addChild(myMaterial)
        root.addChild(coin.SoCone())

        # An engine rotates the object. The output of myCounter 
        # is the time in seconds since the program started.
        # Connect this output to the angle field of myRotXYZ
        myRotXYZ.axis = coin.SoRotationXYZ.X     # rotate about X axis
        myCounter = coin.SoElapsedTime()
        myRotXYZ.angle.connectFrom(myCounter.timeOut)

        view = Gui.ActiveDocument.ActiveView
        sg = view.getSceneGraph()
        sg.addChild(root)
        Gui.SendMsgToActiveView('ViewFit')
    
Gui.addCommand('hEngineSpin',hEngineSpin())