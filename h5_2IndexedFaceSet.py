####################################################################
# Test Demos from the book The Inventor Mentor in a workbench      #
# By ceanwu@yahoo.com                                              #
# No warranty.                                                     #
# Modified Mariwan Jalal's FreeCAD macro to be a command           #
####################################################################
###
# This is an example from the Inventor Mentor,
# chapter 5, example 2.
#
# This example creates an IndexedFaceSet. It creates
# the first stellation of the dodecahedron.
#
import os
import sys
import FreeCAD as App
import FreeCADGui as Gui
import pivy.coin as coin

##############################################################
# CODE FOR The Inventor Mentor STARTS HERE

#
# Positions of all of the vertices:
#

# set this variable to 0 if you want to use the other method
IV_STRICT = 1

# Routine to create a scene graph representing a dodecahedron
So_END_FACE_INDEX=-1

def makeStellatedDodecahedron():

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

#
# Connectivity, information 12 faces with 5 vertices each ),
# (plus the end-of-face indicator for each face):
#

    Indices = (
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

    result = coin.SoSeparator()

    if IV_STRICT:
        # This is the preferred code for Inventor 2.1

        # Using the new coin.SoVertexProperty node is more efficient
        myVertexProperty = coin.SoVertexProperty()

        # Define colors for the faces
        for i in range(12):
            myVertexProperty.orderedRGBA.set1Value(
                i, coin.SbColor(colors[i]).getPackedValue())
            myVertexProperty.materialBinding = coin.SoMaterialBinding.PER_FACE

        # Define coordinates for vertices
        myVertexProperty.vertex.setValues(0, 12, vertexPositions)

        # Define the IndexedFaceSet, with Indices into
        # the vertices:
        myFaceSet = coin.SoIndexedFaceSet()
        myFaceSet.coordIndex.setValues(0, 72, Indices)

        myFaceSet.vertexProperty = myVertexProperty
        result.addChild(myFaceSet)

    else:
        # Define colors for the faces
        myMaterials = coin.SoMaterial()
        myMaterials.diffuseColor.setValues(0, 12, colors)
        result.addChild(myMaterials)
        myMaterialBinding = coin.SoMaterialBinding()
        myMaterialBinding.value = coin.SoMaterialBinding.PER_FACE
        result.addChild(myMaterialBinding)

        # Define coordinates for vertices
        myCoords = coin.SoCoordinate3()
        myCoords.point.setValues(0, 12, vertexPositions)
        result.addChild(myCoords)

        # Define the IndexedFaceSet, with Indices into
        # the vertices:
        myFaceSet = coin.SoIndexedFaceSet()
        myFaceSet.coordIndex.setValues(0, 72, Indices)
        result.addChild(myFaceSet)
        
    return result    

class hIndexedFaceSet:
    "hIndexedFaceSet"
    def GetResources(self):
        return {"MenuText": "hIndexedFaceSet",
                "Accel": "Ctrl+t",
                "ToolTip": "Creates the first stellation of the dodecahedron.",
                "Pixmap": os.path.dirname(__file__)+"./resources/5.2.svg"
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
        Gui.SendMsgToActiveView('ViewFit')
    
Gui.addCommand('hIndexedFaceSet',hIndexedFaceSet())