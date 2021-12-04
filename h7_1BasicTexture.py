####################################################################
# Test Demos from the book The Inventor Mentor in a workbench      #
# By ceanwu@yahoo.com                                              #
# No warranty.                                                     #
# Modified Mariwan Jalal's FreeCAD macro to be a command           #
####################################################################
###
# This is an example from the Inventor Mentor,
# chapter 7, example 1.
#
# This example displays a textured cube (default 
# texture coords).
#
import os
import sys
import FreeCAD as App
import FreeCADGui as Gui
import pivy.coin as coin

class hBasicTexture:
    "hBasicTexture"
    def GetResources(self):
        return {"MenuText": "hBasicTexture",
                "Accel": "Ctrl+t",
                "ToolTip": "Displays a textured cube (default texture coords).",
                "Pixmap": os.path.dirname(__file__)+"./resources/7.1.svg"
        }

    def IsActive(self):

        if App.ActiveDocument == None:
            return False
        else:
            return True

    def Activated(self):

        # Initialize Inventor and Qt
        texRoot = coin.SoSeparator()
        input = coin.SoInput()
        Frgb=os.path.dirname(__file__)+"./iv/brick.1.rgb"
        input.openFile(Frgb)           
        result = coin.SoDB.readAll(input)

        texRoot.addChild(result)

        # Choose a texture 
        texture = coin.SoTexture2()
        if generateTextureMap(texRoot, texture, 64, 64):
            print("Successfully generated texture map")
        else:
            print("Could not generate texture map")
        #TODO : FIXME : CHANGE THE PATH
        #Frgb=os.path.dirname(__file__)+"./iv/brick.1.rgb"
        #rock.filename = Frgb   

        root = coin.SoSeparator()
        root.addChild(texture)
        # Make a cube
        root.addChild(coin.SoCube())
        
        #Main function 
        view = Gui.ActiveDocument.ActiveView
        sg = view.getSceneGraph()
        sg.addChild(root)
        Gui.SendMsgToActiveView('ViewFit')
    
Gui.addCommand('hBasicTexture',hBasicTexture())