####################################################################
# Test Demos from the book The Inventor Mentor in a workbench      #
# By ceanwu@yahoo.com                                              #
# No warranty.                                                     #
# Modified Mariwan Jalal's FreeCAD macro to be a command           #
####################################################################
###
# This is an example from the Inventor Mentor,
# chapter 3.
#
# Create a little scene graph and then name coin.Some nodes and
# get back nodes by name.
#
import os,sys
import FreeCAD as App
import FreeCADGui as Gui
import pivy.coin as coin

class hNaming:
    "hNaming"
    def GetResources(self):
        return {"MenuText": "hNaming",
                "Accel": "Ctrl+t",
                "ToolTip": "Remove a child named myCube",
                "Pixmap": os.path.dirname(__file__)+"./resources/3.3.svg"
        }

    def IsActive(self):

        if App.ActiveDocument == None:
            return False
        else:
            return True

    def Activated(self):

        myRoot = coin.SoNode.getByName("Root")

        myCube = coin.SoNode.getByName("MyCube")

        myRoot.removeChild(myCube)
        
        #Main function 
        view = Gui.ActiveDocument.ActiveView
        Gui.SendMsgToActiveView('ViewFit')
    
Gui.addCommand('hNaming',hNaming())