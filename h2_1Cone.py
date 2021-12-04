####################################################################
# Test Demos from the book The Inventor Mentor in a workbench      #
# By ceanwu@yahoo.com                                              #
# No warranty.                                                     #
# Modified Mariwan Jalal's FreeCAD macro to be a command           #
####################################################################
###
# This is an example from the Inventor Mentor,
# chapter 2, example 1.
#
# Hello Cone example program; draws a red cone in a window.
#
import os,sys
import FreeCAD as App
import FreeCADGui as Gui
import pivy.coin as coin

class hCone:
    "hCone"
    def GetResources(self):
        return {"MenuText": "hCone",
                "Accel": "Ctrl+t",
                "ToolTip": "Draws a red cone in a window",
                "Pixmap": os.path.dirname(__file__)+"./resources/2.1.svg"
        }

    def IsActive(self):

        if App.ActiveDocument == None:
            return False
        else:
            return True

    def Activated(self):

        #Create Cone
        # Initialize Inventor. This returns a main window to use.
        # If unsuccessful, exit.
        # Make a scene containing a red cone
        root = coin.SoSeparator()
        myMaterial = coin.SoMaterial()
        root.addChild(coin.SoDirectionalLight())
        myMaterial.diffuseColor = (1.0, 0.0, 0.0)   # Red
        root.addChild(myMaterial)
        root.addChild(coin.SoCone())

        #Main function 
        view = Gui.ActiveDocument.ActiveView
        sg = view.getSceneGraph()
        sg.addChild(root)
        Gui.SendMsgToActiveView('ViewFit')
        #sg.addChild(makeObeliskFaceSet())
    
Gui.addCommand('hCone',hCone())