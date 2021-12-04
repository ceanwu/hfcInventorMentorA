####################################################################
# Test Demos from the book The Inventor Mentor in a workbench      #
# By ceanwu@yahoo.com                                              #
# No warranty.                                                     #
# Modified Mariwan Jalal's FreeCAD macro to be a command           #
####################################################################
###
# This is an example from the Inventor Mentor,
# chapter 5, example 1.
#
# This example builds an obelisk using the Face Set node.
#
import os,sys
import FreeCAD as App
import FreeCADGui as Gui
import pivy.coin as coin

##############################################################
# CODE FOR The Inventor Mentor STARTS HERE

# Eight polygons. The first four are triangles
# The second four are quadrilaterals for the sides.
vertices = (
    (0, 30, 0), (-2, 27, 2), (2, 27, 2),  # front tri
    (0, 30, 0), (-2, 27, -2), (-2, 27, 2),  # left  tri
    (0, 30, 0), (2, 27, -2), (-2, 27, -2),  # rear  tri
    (0, 30, 0), (2, 27, 2), (2, 27, -2),  # right tri
    (-2, 27, 2), (-4, 0, 4), (4, 0, 4), (2, 27, 2),  # front quad
    (-2, 27, -2), (-4, 0, -4), (-4, 0, 4), (-2, 27, 2),  # left  quad
    (2, 27, -2), (4, 0, -4), (-4, 0, -4), (-2, 27, -2),  # rear  quad
    (2, 27, 2), (4, 0, 4), (4, 0, -4), (2, 27, -2)  # right quad
)

# Number of vertices in each polygon:
numvertices = (3, 3, 3, 3, 4, 4, 4, 4)

# Normals for each polygon:
norms = (
    (0, .555,  .832), (-.832, .555, 0),  # front, left tris
    (0, .555, -.832), (.832, .555, 0),  # rear, right tris

    (0, .0739,  .9973), (-.9972, .0739, 0),  # front, left quads
    (0, .0739, -.9973), (.9972, .0739, 0),  # rear, right quads
)

# set this variable to 0 if you want to use the other method
IV_STRICT = 1

def makeObeliskFaceSet():
    obelisk = coin.SoSeparator()

    if IV_STRICT:
        # This is the preferred code for Inventor 2.1

        # Using the new SoVertexProperty node is more efficient
        myVertexProperty = coin.SoVertexProperty()

        # Define the normals used:
        myVertexProperty.normal.setValues(0, 8, norms)
        myVertexProperty.normalBinding = coin.SoNormalBinding.PER_FACE

        # Define material for obelisk
        myVertexProperty.orderedRGBA = coin.SbColor(.4, .4, .4).getPackedValue()

        # Define coordinates for vertices
        myVertexProperty.vertex.setValues(0, 28, vertices)

        # Define the FaceSet
        myFaceSet = coin.SoFaceSet()
        myFaceSet.numVertices.setValues(0, 8, numvertices)

        myFaceSet.vertexProperty = myVertexProperty
        obelisk.addChild(myFaceSet)

    else:
        # Define the normals used:
        myNormals = coin.SoNormal()
        myNormals.vector.setValues(0, 8, norms)
        obelisk.addChild(myNormals)
        myNormalBinding = coin.SoNormalBinding()
        myNormalBinding.value = coin.SoNormalBinding.PER_FACE
        obelisk.addChild(myNormalBinding)

        # Define material for obelisk
        myMaterial = coin.SoMaterial()
        myMaterial.diffuseColor = (.4, .4, .4)
        obelisk.addChild(myMaterial)

        # Define coordinates for vertices
        myCoords = coin.SoCoordinate3()
        myCoords.point.setValues(0, 28, vertices)
        obelisk.addChild(myCoords)

        # Define the FaceSet
        myFaceSet = coin.SoFaceSet()
        myFaceSet.numVertices.setValues(0, 8, numvertices)
        obelisk.addChild(myFaceSet)
        
    return obelisk

# CODE FOR The Inventor Mentor ENDS HERE
##############################################################
class hFaceSet:
    "hFaceSet"
    def GetResources(self):
        return {"MenuText": "hFaceSet",
                "Accel": "Ctrl+t",
                "ToolTip": "Builds an obelisk using the Face Set node.",
                "Pixmap": os.path.dirname(__file__)+"./resources/5.1.svg"
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
        sg.addChild(makeObeliskFaceSet())
        Gui.SendMsgToActiveView('ViewFit')
    
Gui.addCommand('hFaceSet',hFaceSet())