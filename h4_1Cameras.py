####################################################################
# Test Demos from the book The Inventor Mentor in a workbench      #
# By ceanwu@yahoo.com                                              #
# No warranty.                                                     #
# Modified Mariwan Jalal's FreeCAD macro to be a command           #
####################################################################
###
# This is an example from the Inventor Mentor,
# chapter 4, example 1.
#
# Camera example.  
# A blinker node is used to switch between three 
# different views of the same scene. The cameras are 
# switched once per second.
#
import os,sys
import FreeCAD as App
import FreeCADGui as Gui
import pivy.coin as coin

class hCameras:
    "hCameras"
    def GetResources(self):
        return {"MenuText": "hCameras",
                "Accel": "Ctrl+t",
                "ToolTip": "A blinker node is used to switch between three different views of the same scene.",
                "Pixmap": os.path.dirname(__file__)+"./resources/4.1.svg"
        }

    def IsActive(self):

        if App.ActiveDocument == None:
            return False
        else:
            return True

    def Activated(self):

        root = coin.SoSeparator()

        # Create a blinker node and put it in the scene. A blinker
        # switches between its children at timed intervals.
        myBlinker = coin.SoBlinker()
        root.addChild(myBlinker)

        # Create three cameras. Their positions will be set later.
        # This is because the viewAll method depends on the size
        # of the render area, which has not been created yet.
        orthoViewAll = coin.SoOrthographicCamera()
        perspViewAll = coin.SoPerspectiveCamera()
        perspOffCenter = coin.SoPerspectiveCamera()
        myBlinker.addChild(orthoViewAll)
        myBlinker.addChild(perspViewAll)
        myBlinker.addChild(perspOffCenter)

        # Create a light
        root.addChild(coin.SoDirectionalLight())

        # Read the object from a file and add to the scene
        myInput = coin.SoInput()
        # You have to give the file path                                TODO: FIX THE PATH!!!!
        Fiv=os.path.dirname(__file__)+"./iv/parkbench.iv"
        #if not myInput.openFile("E:\\TEMP\\fix some drawing\\Mentor_Freecad\\parkbench.iv"):
        if not myInput.openFile(Fiv):
            sys.exit(1)

        fileContents = coin.SoDB.readAll(myInput)
        if fileContents == None:
            sys.exit(1)

        myMaterial = coin.SoMaterial()
        myMaterial.diffuseColor = (0.8, 0.23, 0.03) 
        root.addChild(myMaterial)
        root.addChild(fileContents)
        
        #Main function 
        view = Gui.ActiveDocument.ActiveView
        sg = view.getSceneGraph()
        sg.addChild(root)
        Gui.SendMsgToActiveView('ViewFit')
    
Gui.addCommand('hCameras',hCameras())