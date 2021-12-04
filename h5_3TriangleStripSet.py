####################################################################
# Test Demos from the book The Inventor Mentor in a workbench      #
# By ceanwu@yahoo.com                                              #
# No warranty.                                                     #
# Modified Mariwan Jalal's FreeCAD macro to be a command           #
####################################################################
###
# This is an example from the Inventor Mentor,
# chapter 5, example 3.
#
# This example creates a TriangleStripSet. It creates
# a pennant-shaped flag.
#
import os,sys
import FreeCAD as App
import FreeCADGui as Gui
import pivy.coin as coin

##############################################################
## CODE FOR The Inventor Mentor STARTS HERE

#
# Positions of all of the vertices:
#
vertexPositions = (
   (  0,   12,    0 ), (   0,   15,    0),
   (2.1, 12.1,  -.2 ), ( 2.1, 14.6,  -.2),
   (  4, 12.5,  -.7 ), (   4, 14.5,  -.7),
   (4.5, 12.6,  -.8 ), ( 4.5, 14.4,  -.8),
   (  5, 12.7,   -1 ), (   5, 14.4,   -1),
   (4.5, 12.8, -1.4 ), ( 4.5, 14.6, -1.4),
   (  4, 12.9, -1.6 ), (   4, 14.8, -1.6),
   (3.3, 12.9, -1.8 ), ( 3.3, 14.9, -1.8),
   (  3,   13, -2.0 ), (   3, 14.9, -2.0), 
   (3.3, 13.1, -2.2 ), ( 3.3, 15.0, -2.2),
   (  4, 13.2, -2.5 ), (   4, 15.0, -2.5),
   (  6, 13.5, -2.2 ), (   6, 14.8, -2.2),
   (  8, 13.4,   -2 ), (   8, 14.6,   -2),
   ( 10, 13.7, -1.8 ), (  10, 14.4, -1.8),
   ( 12,   14, -1.3 ), (  12, 14.5, -1.3),
   ( 15, 14.9, -1.2 ), (  15,   15, -1.2),

   (-.5, 15,   0 ), ( -.5, 0,   0),   # the flagpole
   (  0, 15,  .5 ), (   0, 0,  .5),
   (  0, 15, -.5 ), (   0, 0, -.5),
   (-.5, 15,   0 ), ( -.5, 0,   0)
)


# Number of vertices in each strip.
numVertices = (
   32, # flag
   8   # pole
)
 
# Colors for the 12 faces
colors = (
   ( .5, .5,  1 ), # purple flag
   ( .4, .4, .4 ), # grey flagpole
)

# set this variable to 0 if you want to use the other method
IV_STRICT = 1

# Routine to create a scene graph representing a pennant.
def makePennant():
    result = coin.SoSeparator()

    # A shape hints tells the ordering of polygons. 
    # This insures double sided lighting.
    myHints = coin.SoShapeHints()
    myHints.vertexOrdering = coin.SoShapeHints.COUNTERCLOCKWISE
    result.addChild(myHints)

    if IV_STRICT:
        # This is the preferred code for Inventor 2.1 

        # Using the new coin.SoVertexProperty node is more efficient
        myVertexProperty = coin.SoVertexProperty()

        # Define colors for the strips
        for i in range(2):
            myVertexProperty.orderedRGBA.set1Value(i, coin.SbColor(colors[i]).getPackedValue())
            myVertexProperty.materialBinding = coin.SoMaterialBinding.PER_PART

        # Define coordinates for vertices
        myVertexProperty.vertex.setValues(0, 40, vertexPositions)

        # Define the TriangleStripSet, made of two strips.
        myStrips = coin.SoTriangleStripSet()
        myStrips.numVertices.setValues(0, 2, numVertices)
 
        myStrips.vertexProperty = myVertexProperty
        result.addChild(myStrips)

    else:
        # Define colors for the strips
        myMaterials = coin.SoMaterial()
        myMaterials.diffuseColor.setValues(0, 2, colors)
        result.addChild(myMaterials)
        myMaterialBinding = coin.SoMaterialBinding()
        myMaterialBinding.value = coin.SoMaterialBinding.PER_PART
        result.addChild(myMaterialBinding)

        # Define coordinates for vertices
        myCoords = coin.SoCoordinate3()
        myCoords.point.setValues(0, 40, vertexPositions)
        result.addChild(myCoords)

        # Define the TriangleStripSet, made of two strips.
        myStrips = coin.SoTriangleStripSet()
        myStrips.numVertices.setValues(0, 2, numVertices)
        result.addChild(myStrips)

    return result


class hTriangleStripSet:
    "hTriangleStripSet"
    def GetResources(self):
        return {"MenuText": "hTriangleStripSet",
                "Accel": "Ctrl+t",
                "ToolTip": "Creates a pennant-shaped flag.",
                "Pixmap": os.path.dirname(__file__)+"./resources/5.3.svg"
        }

    def IsActive(self):

        if App.ActiveDocument == None:
            return False
        else:
            return True

    def Activated(self):

        #Main function 
        view = Gui.ActiveDocument.ActiveView
        sg = view.getSceneGraph()
        sg.addChild(makePennant())
        Gui.SendMsgToActiveView('ViewFit')
    
Gui.addCommand('hTriangleStripSet',hTriangleStripSet())