####################################################################
# Test Demos from the book The Inventor Mentor in a workbench      #
# By ceanwu@yahoo.com                                              #
# No warranty.                                                     #
# Modified Mariwan Jalal's FreeCAD macro to be a command           #
####################################################################
###
# This is an example from the Inventor Mentor,
# chapter 9, example 3.
#
# Search Action example.
# Read in a scene from a file.
# Search through the scene looking for a light.
# If none exists, add a directional light to the scene
# and print out the modified scene.
#
import os
import sys
import FreeCAD as App
import FreeCADGui as Gui
import pivy.coin as coin

class hSearch:
    "hSearch"
    def GetResources(self):
        return {"MenuText": "hSearch",
                "Accel": "Ctrl+t",
                "ToolTip": "Search through the scene looking for a light.",
                "Pixmap": os.path.dirname(__file__)+"./resources/9.3.svg"
        }

    def IsActive(self):

        if App.ActiveDocument == None:
            return False
        else:
            return True

    def Activated(self):

        # Initialize Inventor
        # coin.SoDB.init() invoked automatically upon coin module import

        # Open and read input scene graph
        sceneInput = coin.SoInput()
        #TODO Change path and file name 
        Fiv=os.path.dirname(__file__)+"./iv/bird.iv"
        if not sceneInput.openFile(Fiv):        
            return 1

        root = coin.SoDB.readAll(sceneInput)
        if root == None:
            return 1

        ##############################################################
        # CODE FOR The Inventor Mentor STARTS HERE

        mySearchAction = coin.SoSearchAction()

        # Look for first existing light derived from class coin.SoLight
        mySearchAction.setType(coin.SoLight.getClassTypeId())
        mySearchAction.setInterest(coin.SoSearchAction.FIRST)

        mySearchAction.apply(root)
        if mySearchAction.getPath() == None: # No lights found
            # Add a default directional light to the scene
            myLight = coin.SoDirectionalLight()
            root.insertChild(myLight, 0)

        # CODE FOR The Inventor Mentor ENDS HERE
        ##############################################################

        myWriteAction = coin.SoWriteAction()
        myWriteAction.apply(root)
        #Main function 
        view = Gui.ActiveDocument.ActiveView
        sg = view.getSceneGraph()
        sg.addChild(root)
        Gui.SendMsgToActiveView('ViewFit')
    
Gui.addCommand('hSearch',hSearch())