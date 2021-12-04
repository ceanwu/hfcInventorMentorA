####################################################################
# Test Demos from the book The Inventor Mentor in a workbench      #
# By ceanwu@yahoo.com                                              #
# No warranty.                                                     #
# Modified Mariwan Jalal's FreeCAD macro to be a command           #
####################################################################
###
# This is an example from the Inventor Mentor,
# chapter 2, example 4.
#
# Use the Examiner Viewer to look at a red cone
#
import os,sys
import FreeCAD as App
import FreeCADGui as Gui
import pivy.coin as coin

class hExaminer:
    "hExaminer"
    def GetResources(self):
        return {"MenuText": "hExaminer",
                "Accel": "Ctrl+t",
                "ToolTip": "Use the Examiner Viewer to look at a red cone",
                "Pixmap": os.path.dirname(__file__)+"./resources/2.4.svg"
        }

    def IsActive(self):

        if App.ActiveDocument == None:
            return False
        else:
            return True

    def Activated(self):

        # Read the geometry from a file and add to the scene
        myInput = coin.SoInput()
        Fiv=os.path.dirname(__file__)+"./iv/dogDish.iv"
        if not myInput.openFile(Fiv):
            sys.exit(1)
        geomObject = coin.SoDB.readAll(myInput)
        if geomObject == None:
            sys.exit(1)
        view = Gui.ActiveDocument.ActiveView
        sg = view.getSceneGraph()
        sg.addChild(geomObject)
        Gui.SendMsgToActiveView('ViewFit')
    
Gui.addCommand('hExaminer',hExaminer())