####################################################################
# Test Demos from the book The Inventor Mentor in a workbench      #
# By ceanwu@yahoo.com                                              #
# No warranty.                                                     #
# Modified Mariwan Jalal's FreeCAD macro to be a command           #
####################################################################
###
# This is an example from the Inventor Mentor,
# chapter 5, example 5.
#
# This example illustrates a variety of ways to bind
# materials to a polygon object.
# Three cases of a switch statement show various ways of
# binding materials to objects.
# The object used for all three examples is the stellated
# dodecahedron from an earlier example in this chapter.
#
import os
import sys
import FreeCAD as App
import FreeCADGui as Gui
import pivy.coin as coin

So_END_FACE_INDEX=-1
# Positions of all of the vertices:
vertexPositions = (
    (0.0000,  1.2142,  0.7453),  # top

    (0.0000,  1.2142, -0.7453),  # points surrounding top
    (-1.2142,  0.7453,  0.0000),
    (-0.7453,  0.0000,  1.2142),
    (0.7453,  0.0000,  1.2142),
    (1.2142,  0.7453,  0.0000),

    (0.0000, -1.2142,  0.7453),  # points surrounding bottom
    (-1.2142, -0.7453,  0.0000),
    (-0.7453,  0.0000, -1.2142),
    (0.7453,  0.0000, -1.2142),
    (1.2142, -0.7453,  0.0000),

    (0.0000, -1.2142, -0.7453),  # bottom
)

# Connectivity, information 12 faces with 5 vertices each ),
# (plus the end-of-face indicator for each face):

indices = (
    1,  2,  3,  4, 5, So_END_FACE_INDEX,  # top face

    0,  1,  8,  7, 3, So_END_FACE_INDEX,  # 5 faces about top
    0,  2,  7,  6, 4, So_END_FACE_INDEX,
    0,  3,  6, 10, 5, So_END_FACE_INDEX,
    0,  4, 10,  9, 1, So_END_FACE_INDEX,
    0,  5,  9,  8, 2, So_END_FACE_INDEX,

    9,  5, 4, 6, 11, So_END_FACE_INDEX,  # 5 faces about bottom
    10,  4, 3, 7, 11, So_END_FACE_INDEX,
    6,  3, 2, 8, 11, So_END_FACE_INDEX,
    7,  2, 1, 9, 11, So_END_FACE_INDEX,
    8,  1, 5, 10, 11, So_END_FACE_INDEX,

    6,  7, 8, 9, 10, So_END_FACE_INDEX,  # bottom face
)

# Colors for the 12 faces
colors = (
    (1.0, .0, 0), (.0,  .0, 1.0), (0, .7,  .7), (.0, 1.0,  0),
    (.7, .7, 0), (.7,  .0,  .7), (0, .0, 1.0), (.7,  .0, .7),
    (.7, .7, 0), (.0, 1.0,  .0), (0, .7,  .7), (1.0,  .0,  0)
)

# set this variable to 0 if you want to use the other method
IV_STRICT = 1

# Routine to create a scene graph representing a dodecahedron


def makeStellatedDodecahedron():
    result = coin.SoSeparator()

    if IV_STRICT:
        # This is the preferred code for Inventor 2.1

        # Using the new coin.SoVertexProperty node is more efficient
        myVertexProperty = coin.SoVertexProperty()

        # The material binding.
        myVertexProperty.materialBinding = coin.SoMaterialBinding.PER_FACE

        # Define colors for the faces
        for i in range(12):
            myVertexProperty.orderedRGBA.set1Value(
                i, coin.SbColor(colors[i]).getPackedValue())

        # Define coordinates for vertices
        myVertexProperty.vertex.setValues(0, 12, vertexPositions)

        # Define the IndexedFaceSet, with indices into
        # the vertices:
        myFaceSet = coin.SoIndexedFaceSet()
        myFaceSet.coordIndex.setValues(0, 72, indices)

        myFaceSet.vertexProperty = myVertexProperty
        result.addChild(myFaceSet)

    else:
        # The material binding node.
        myBinding = coin.SoMaterialBinding()
        myBinding.value(coin.SoMaterialBinding.PER_FACE)
        result.addChild(myBinding)

        # Define colors for the faces
        myMaterials = coin.SoMaterial()
        myMaterials.diffuseColor.setValues(0, 12, colors)
        result.addChild(myMaterials)

        # Define coordinates for vertices
        myCoords = coin.SoCoordinate3()
        myCoords.point.setValues(0, 12, vertexPositions)
        result.addChild(myCoords)

        # Define the IndexedFaceSet, with indices into
        # the vertices:
        myFaceSet = coin.SoIndexedFaceSet()
        myFaceSet.coordIndex.setValues(0, 72, indices)
        result.addChild(myFaceSet)

    return result


def ExecutemakeStellatedDodecahedron():
    whichBinding = 0
    
    
    whichBinding = 1      #TODO : Change this to get other effects

    if whichBinding > 2 or whichBinding < 0 :
        sys.stderr.write("Argument must be 0, 1 or 2\n")
        sys.stderr.write("\t0 = PER_FACE\n")
        sys.stderr.write("\t1 = PER_VERTEX_INDEXED\n")
        sys.stderr.write("\t2 = PER_FACE_INDEXED\n")
        sys.exit(1)

    root = makeStellatedDodecahedron()

    if IV_STRICT:
        # Get the indexed face set for editing
        myIndexedFaceSet = root.getChild(0)

        # Get the coin.SoVertexProperty node for editing the material binding
        myVertexProperty = myIndexedFaceSet.vertexProperty.getValue()

##############################################################
# CODE FOR The Inventor Mentor STARTS HERE (Inventor 2.1)

        # Which material to use to color the faces
        # half red & half blue
        materialIndices = (
            0, 0, 0, 0, 0, 0,
            1, 1, 1, 1, 1, 1
        )

        if whichBinding == 0:
            # Set up binding to use a different color for each face
            myVertexProperty.materialBinding = coin.SoMaterialBinding.PER_FACE
        elif whichBinding == 1:
            # Set up binding to use a different color at each
            # vertex, BUT, vertices shared between faces will
            # have the same color.
            myVertexProperty.materialBinding = coin.SoMaterialBinding.PER_VERTEX_INDEXED
        elif whichBinding == 2:
            myVertexProperty.materialBinding = coin.SoMaterialBinding.PER_FACE_INDEXED
            myIndexedFaceSet.materialIndex.setValues(0, 12, materialIndices)

# CODE FOR The Inventor Mentor ENDS HERE
##############################################################

    else:   # old style
        # Get the material binding node for editing
        myBinding = root.getChild(0)

        # Get the indexed face set for editing
        myIndexedFaceSet = root.getChild(3)

##############################################################
# CODE FOR The Inventor Mentor STARTS HERE

        # Which material to use to color the faces
        # half red & half blue
        materialIndices = (
            0, 0, 0, 0, 0, 0,
            1, 1, 1, 1, 1, 1,
        )

        if whichBinding == 0:
            # Set up binding to use a different color for each face
            myBinding.value = coin.SoMaterialBinding.PER_FACE
        elif whichBinding == 1:
            # Set up binding to use a different color at each
            # vertex, BUT, vertices shared between faces will
            # have the same color.
            myBinding.value = coin.SoMaterialBinding.PER_VERTEX_INDEXED
        elif whichBinding == 2:
            myBinding.value = coin.SoMaterialBinding.PER_FACE_INDEXED
            myIndexedFaceSet.materialIndex.setValues(0, 12, materialIndices)

class hBinding:
    "hBinding"
    def GetResources(self):
        return {"MenuText": "hBinding",
                "Accel": "Ctrl+t",
                "ToolTip": "Illustrates a variety of ways to bind materials to a polygon object.",
                "Pixmap": os.path.dirname(__file__)+"./resources/5.5.svg"
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
        sg.addChild(makeStellatedDodecahedron())
    
Gui.addCommand('hBinding',hBinding())