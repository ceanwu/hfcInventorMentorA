####################################################################
# Test Demos from the book The Inventor Mentor in a workbench      #
# By ceanwu@yahoo.com                                              #
# No warranty.                                                     #
# Modified Mariwan Jalal's FreeCAD macro to be a command           #
#####################################################################!/usr/bin/env python
###
# This is an example from the Inventor Mentor
# chapter 7, example 2.
#
# This example illustrates using texture coordinates on
# a Face Set.
#
import os
import sys
import FreeCAD as App
import FreeCADGui as Gui
import pivy.coin as coin

# set this variable to 0 if you want to use the other method
IV_STRICT = 1

class hTextureCoordinates:
    "hTextureCoordinates"
    def GetResources(self):
        return {"MenuText": "hTextureCoordinates",
                "Accel": "Ctrl+t",
                "ToolTip": "Illustrates using texture coordinates on a Face Set.",
                "Pixmap": os.path.dirname(__file__)+"./resources/7.2.svg"
        }

    def IsActive(self):

        if App.ActiveDocument == None:
            return False
        else:
            return True

    def Activated(self):

        root = coin.SoSeparator()

        # Choose a texture
        brick = coin.SoTexture2()
        root.addChild(brick)
        brick.filename = "E:\\TEMP\\fix some drawing\\Mentor\\brick.1.rgb"     #TODO : FIXME : CHANGE PATH

        if IV_STRICT:
            # This is the preferred code for Inventor 2.1 

            # Using the new coin.SoVertexProperty node is more efficient
            myVertexProperty = coin.SoVertexProperty()

            # Define the square's spatial coordinates
            myVertexProperty.vertex.set1Value(0, coin.SbVec3f(-3, -3, 0))
            myVertexProperty.vertex.set1Value(1, coin.SbVec3f( 3, -3, 0))
            myVertexProperty.vertex.set1Value(2, coin.SbVec3f( 3,  3, 0))
            myVertexProperty.vertex.set1Value(3, coin.SbVec3f(-3,  3, 0))

            # Define the square's normal
            myVertexProperty.normal.set1Value(0, coin.SbVec3f(0, 0, 1))

            # Define the square's texture coordinates
            myVertexProperty.texCoord.set1Value(0, coin.SbVec2f(0, 0))
            myVertexProperty.texCoord.set1Value(1, coin.SbVec2f(1, 0))
            myVertexProperty.texCoord.set1Value(2, coin.SbVec2f(1, 1))
            myVertexProperty.texCoord.set1Value(3, coin.SbVec2f(0, 1))

            # coin.SoTextureCoordinateBinding node is now obSolete--in Inventor 2.1,
            # texture coordinates will always be generated if none are 
            # provided.
            #
            # tBind = coin.SoTextureCoordinateBinding()
            # root.addChild(tBind)
            # tBind.value(coin.SoTextureCoordinateBinding.PER_VERTEX)
            #
            # Define normal binding
            myVertexProperty.normalBinding = coin.SoNormalBinding.OVERALL

            # Define a FaceSet
            myFaceSet = coin.SoFaceSet()
            root.addChild(myFaceSet)
            myFaceSet.numVertices.set1Value(0, 4)

            myFaceSet.vertexProperty.setValue(myVertexProperty)

        else:
            # Define the square's spatial coordinates
            coord = coin.SoCoordinate3()
            root.addChild(coord)
            coord.point.set1Value(0, coin.SbVec3f(-3, -3, 0))
            coord.point.set1Value(1, coin.SbVec3f( 3, -3, 0))
            coord.point.set1Value(2, coin.SbVec3f( 3,  3, 0))
            coord.point.set1Value(3, coin.SbVec3f(-3,  3, 0))

            # Define the square's normal
            normal = coin.SoNormal()
            root.addChild(normal)
            normal.vector.set1Value(0, coin.SbVec3f(0, 0, 1))

            # Define the square's texture coordinates
            texCoord = coin.SoTextureCoordinate2()
            root.addChild(texCoord)
            texCoord.point.set1Value(0, coin.SbVec2f(0, 0))
            texCoord.point.set1Value(1, coin.SbVec2f(1, 0))
            texCoord.point.set1Value(2, coin.SbVec2f(1, 1))
            texCoord.point.set1Value(3, coin.SbVec2f(0, 1))

            # Define normal binding
            nBind = coin.SoNormalBinding()
            root.addChild(nBind)
            nBind.value = coin.SoNormalBinding.OVERALL

            # coin.SoTextureCoordinateBinding node is now obSolete--in Inventor 2.1,
            # texture coordinates will always be generated if none are 
            # provided.
            #
            # tBind = coin.SoTextureCoordinateBinding()
            # root.addChild(tBind)
            # tBind.value.setValue(coin.SoTextureCoordinateBinding.PER_VERTEX)
            #

            # Define a FaceSet
            myFaceSet = coin.SoFaceSet()
            root.addChild(myFaceSet)
            myFaceSet.numVertices.set1Value(0, 4)
        #Main function 
        view = Gui.ActiveDocument.ActiveView
        sg = view.getSceneGraph()
        sg.addChild(root)
        Gui.SendMsgToActiveView('ViewFit')
    
Gui.addCommand('hTextureCoordinates',hTextureCoordinates())