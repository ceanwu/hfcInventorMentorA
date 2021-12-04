####################################################################
# Test Demos from the book The Inventor Mentor in a workbench      #
# By ceanwu@yahoo.com                                              #
# No warranty.                                                     #
# Modified Mariwan Jalal's FreeCAD macro to be a command           #
####################################################################
###
# This is an example from the Inventor Mentor,
# chapter 5, example 6.
#
# This example shows the effect of different order of
# operation of transforms.  The left object is first
# scaled, then rotated, and finally translated to the left.  
# The right object is first rotated, then scaled, and finally
# translated to the right.
#
import os
import sys
import FreeCAD as App
import FreeCADGui as Gui
import pivy.coin as coin

class hTransformOrdering:
    "hTransformOrdering"
    def GetResources(self):
        return {"MenuText": "hTransformOrdering",
                "Accel": "Ctrl+t",
                "ToolTip": "Shows the effect of different order of operation of transforms.",
                "Pixmap": os.path.dirname(__file__)+"./resources/5.6.svg"
        }

    def IsActive(self):

        if App.ActiveDocument == None:
            return False
        else:
            return True

    def Activated(self):

        root = coin.SoSeparator()

        # Create two separators, for left and right objects.
        leftSep = coin.SoSeparator()
        rightSep = coin.SoSeparator()
        root.addChild(leftSep)
        root.addChild(rightSep)

        # Create the transformation nodes
        leftTranslation  = coin.SoTranslation()
        rightTranslation = coin.SoTranslation()
        myRotation = coin.SoRotationXYZ()
        myScale = coin.SoScale()

        # Fill in the values
        leftTranslation.translation = (-1.0, 0.0, 0.0)
        rightTranslation.translation = (1.0, 0.0, 0.0)
        myRotation.angle = 22/7/2   # 90 degrees
        myRotation.axis = coin.SoRotationXYZ.X
        myScale.scaleFactor = (2., 1., 3.)                   #Hint:This line scale the object unciform which deform the drawing (Mariwan)

        # Add transforms to the scene.
        leftSep.addChild(leftTranslation)   # left graph
        leftSep.addChild(myRotation)        # then rotated
        leftSep.addChild(myScale)           # first scaled

        rightSep.addChild(rightTranslation) # right graph
        rightSep.addChild(myScale)          # then scaled
        rightSep.addChild(myRotation)       # first rotated

        # Read an object from file. (as in example 4.2.Lights)
        myInput = coin.SoInput()
        Fin=os.path.dirname(__file__)+"./iv/temple.iv"
        if not myInput.openFile(Fin):             #TODO: You have to change the path to let this works.

            sys.exit(1)

        fileContents = coin.SoDB.readAll(myInput)
        if fileContents == None: 
            sys.exit(1)

        # Add an instance of the object under each separator.
        leftSep.addChild(fileContents)
        rightSep.addChild(fileContents)

        view = Gui.ActiveDocument.ActiveView
        sg = view.getSceneGraph()
        sg.addChild(leftSep)
        sg.addChild(rightSep)
        Gui.SendMsgToActiveView('ViewFit')
        
        #Main function 
        #view = Gui.ActiveDocument.ActiveView
        #sg = view.getSceneGraph()
        #sg.addChild(makeObeliskFaceSet())
    
Gui.addCommand('hTransformOrdering',hTransformOrdering())