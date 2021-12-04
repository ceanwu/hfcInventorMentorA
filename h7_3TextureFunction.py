####################################################################
# Test Demos from the book The Inventor Mentor in a workbench      #
# By ceanwu@yahoo.com                                              #
# No warranty.                                                     #
# Modified Mariwan Jalal's FreeCAD macro to be a command           #
#####################################################################!/usr/bin/env python
# This is an example from the Inventor Mentor,
# chapter 7, example 3.
#
# This example illustrates using texture functions to
# generate texture coordinates on a sphere.
# It draws three texture mapped spheres, each with a 
# different repeat frequency as defined by the fields of the 
# coin.SoTextureCoordinatePlane node.
#
import os
import sys
import FreeCAD as App
import FreeCADGui as Gui
import pivy.coin as coin

class hTextureFunction:
    "hTextureFunction"
    def GetResources(self):
        return {"MenuText": "hTextureFunction",
                "Accel": "Ctrl+t",
                "ToolTip": "Illustrates using texture functions to generate texture coordinates on a sphere.",
                "Pixmap": os.path.dirname(__file__)+"./resources/7.3.svg"
        }

    def IsActive(self):

        if App.ActiveDocument == None:
            return False
        else:
            return True

    def Activated(self):

        root = coin.SoSeparator()

        # Choose a texture.
        faceTexture = coin.SoTexture2()
        root.addChild(faceTexture)
        #TODO: FIXME: Change path
        Frgb=os.path.dirname(__file__)+"./iv/sillyFace.rgb"
        faceTexture.filename = Frgb           

        # Make the diffuse color pure white
        myMaterial = coin.SoMaterial()
        myMaterial.diffuseColor = (1,1,1)
        root.addChild(myMaterial)

        # This texture2Transform centers the texture about (0,0,0) 
        myTexXf = coin.SoTexture2Transform()
        myTexXf.translation = (.5,.5)
        root.addChild(myTexXf)

        # Define a texture coordinate plane node.  This one will 
        # repeat with a frequency of two times per unit length.
        # Add a sphere for it to affect.
        texPlane1 = coin.SoTextureCoordinatePlane()
        texPlane1.directionS = (2,0,0)
        texPlane1.directionT = (0,2,0)
        root.addChild(texPlane1)
        root.addChild(coin.SoSphere())

        # A translation node for spacing the three spheres.
        myTranslation = coin.SoTranslation()
        myTranslation.translation = (2.5,0,0)

        # Create a second sphere with a repeat frequency of 1.
        texPlane2 = coin.SoTextureCoordinatePlane()
        texPlane2.directionS = (1,0,0)
        texPlane2.directionT = (0,1,0)
        root.addChild(myTranslation)
        root.addChild(texPlane2)
        root.addChild(coin.SoSphere())

        # The third sphere has a repeat frequency of .5
        texPlane3 = coin.SoTextureCoordinatePlane()
        texPlane3.directionS = (.5,0,0)
        texPlane3.directionT = (0,.5,0)
        root.addChild(myTranslation)
        root.addChild(texPlane3)
        root.addChild(coin.SoSphere())
        
        #Main function 
        view = Gui.ActiveDocument.ActiveView
        sg = view.getSceneGraph()
        sg.addChild(root)
        Gui.SendMsgToActiveView('ViewFit')
    
Gui.addCommand('hTextureFunction',hTextureFunction())