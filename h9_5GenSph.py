####################################################################
# Test Demos from the book The Inventor Mentor in a workbench      #
# By ceanwu@yahoo.com                                              #
# No warranty.                                                     #
# Modified Mariwan Jalal's FreeCAD macro to be a command           #
####################################################################
###
# This is an example from The Inventor Mentor,
# chapter 9, example 5.
#
# Using a callback for generated primitives.
# A simple scene with a sphere is created.
# A callback is used to write out the triangles that
# form the sphere in the scene.
#
from __future__ import print_function

import os
import sys
import FreeCAD as App
import FreeCADGui as Gui
import pivy.coin as coin

##############################################################
# CODE FOR The Inventor Mentor STARTS HERE

def printVertex(vertex):
    point = vertex.getPoint()
    print("\tCoords     = (%g, %g, %g)" % (point[0], point[1], point[2]))

    normal = vertex.getNormal()
    print("\tNormal     = (%g, %g, %g)" % (normal[0], normal[1], normal[2]))

def printHeaderCallback(void, callbackAction, node):
    print("\n Sphere ")
    # Print the node name (if it exists) and address
    if not not node.getName():
        print('named "%s" ' % node.getName().getString())
    print("at address %r\n" % node.this)

    return coin.SoCallbackAction.CONTINUE

def printTriangleCallback(void, callbackAction, vertex1, vertex2, vertex3):
    print("Triangle:")
    printVertex(vertex1)
    printVertex(vertex2)
    printVertex(vertex3)

def printSpheres(root):
    myAction = coin.SoCallbackAction()
    
    myAction.addPreCallback(coin.SoSphere.getClassTypeId(), printHeaderCallback, None)
    myAction.addTriangleCallback(coin.SoSphere.getClassTypeId(), printTriangleCallback, None)

    myAction.apply(root)
    
# CODE FOR The Inventor Mentor ENDS HERE
##############################################################


class hGenSph:
    "hGenSph"
    def GetResources(self):
        return {"MenuText": "hGenSph",
                "Accel": "Ctrl+t",
                "ToolTip": "Using a callback for generated primitives.",
                "Pixmap": os.path.dirname(__file__)+"./resources/9.5.svg"
        }

    def IsActive(self):

        if App.ActiveDocument == None:
            return False
        else:
            return True

    def Activated(self):

        # Initialize Inventor
        # coin.SoDB.init() invoked automatically upon coin module import

        # Make a scene containing a red sphere
        root = coin.SoSeparator()
        myCamera = coin.SoPerspectiveCamera()
        myMaterial = coin.SoMaterial()
        root.addChild(myCamera)
        root.addChild(coin.SoDirectionalLight())
        myMaterial.diffuseColor = (1.0, 0.0, 0.0)   # Red
        root.addChild(myMaterial)
        root.addChild(coin.SoSphere())
        # Write out the triangles that form the sphere in the scene
        printSpheres(root)
        #Main function 
        #view = Gui.ActiveDocument.ActiveView
        #sg = view.getSceneGraph()
        #sg.addChild(root)
        #Gui.SendMsgToActiveView('ViewFit')
    
Gui.addCommand('hGenSph',hGenSph())