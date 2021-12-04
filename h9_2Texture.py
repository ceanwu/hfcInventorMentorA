####################################################################
# Test Demos from the book The Inventor Mentor in a workbench      #
# By ceanwu@yahoo.com                                              #
# No warranty.                                                     #
# Modified Mariwan Jalal's FreeCAD macro to be a command           #
####################################################################
###
# This is an example from the Inventor Mentor,
# chapter 9, example 2.
#
# Using the offscreen renderer to generate a texture map.
# Generate simple scene and grab the image to use as
# a texture map.
#
from __future__ import print_function

import os
import sys
import FreeCAD as App
import FreeCADGui as Gui
import pivy.coin as coin


def generateTextureMap(root, texture, textureWidth, textureHeight):
    myViewport = coin.SbViewportRegion(textureWidth, textureHeight)

    # Render the scene
    myRenderer = coin.SoOffscreenRenderer(myViewport)
    myRenderer.setBackgroundColor(coin.SbColor(0.3, 0.3, 0.3))
    if not myRenderer.render(root):
        del myRenderer
        return False

    # Generate the texture
    texture.image.setValue(coin.SbVec2s(textureWidth, textureHeight),
                           coin.SoOffscreenRenderer.RGB, myRenderer.getBuffer())

    del myRenderer
    return True


class hTexture:
    "hTexture"
    def GetResources(self):
        return {"MenuText": "hTexture",
                "Accel": "Ctrl+t",
                "ToolTip": "Using the offscreen renderer to generate a texture map.",
                "Pixmap": os.path.dirname(__file__)+"./resources/9.2.svg"
        }

    def IsActive(self):

        if App.ActiveDocument == None:
            return False
        else:
            return True

    def Activated(self):

        # Make a scene from reading in a file
        texRoot = coin.SoSeparator()
        input = coin.SoInput()

        #TODO : Change the path and file name if you want
        Fiv=os.path.dirname(__file__)+"./iv/jumpyMan.iv"
        input.openFile(Fiv)           
        result = coin.SoDB.readAll(input)

        myCamera = coin.SoPerspectiveCamera()
        rot = coin.SoRotationXYZ()
        rot.axis = coin.SoRotationXYZ.X
        rot.angle = 22/7/2
        myCamera.position = (-0.2, -0.2, 2.0)
        myCamera.scaleHeight(0.4)
        texRoot.addChild(myCamera)
        texRoot.addChild(coin.SoDirectionalLight())
        texRoot.addChild(rot)
        texRoot.addChild(result)

        # Generate the texture map
        texture = coin.SoTexture2()
        if generateTextureMap(texRoot, texture, 64, 64):
            print("Successfully generated texture map")
        else:
            print("Could not generate texture map")

        # Make a scene with a cube and apply the texture to it
        root = coin.SoSeparator()
        root.addChild(texture)
        root.addChild(coin.SoCube())
        #Main function 
        view = Gui.ActiveDocument.ActiveView
        sg = view.getSceneGraph()
        sg.addChild(root)
        Gui.SendMsgToActiveView('ViewFit')
    
Gui.addCommand('hTexture',hTexture())