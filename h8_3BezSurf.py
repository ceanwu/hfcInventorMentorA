####################################################################
# Test Demos from the book The Inventor Mentor in a workbench      #
# By ceanwu@yahoo.com                                              #
# No warranty.                                                     #
# Modified Mariwan Jalal's FreeCAD macro to be a command           #
####################################################################
###
# This is an example from the Inventor Mentor,
# chapter 8, example 3.
#
# This example creates and displays a Bezier surface.
# The surface is order 4 with 16 control points and U and V
# knot vectors of length 8.  The knot vectors have two values
# each with multipliciy 4 to define the Bezier surface.
#
import os
import sys
import FreeCAD as App
import FreeCADGui as Gui
import pivy.coin as coin

floorData = """#Inventor V2.0 ascii
Separator {
   SpotLight {
   cutOffAngle 0.9
   dropOffRate 0.2 
   location 6 12 2 
   direction 0 -1 0
   }
   ShapeHints {
   faceType UNKNOWN_FACE_TYPE
   }
   Texture2Transform {
   #rotation 1.57
   scaleFactor 8 8
   }
   Texture2 {
   filename oak.rgb
   }
   NormalBinding {
  value  PER_PART
   }
   Material { diffuseColor 1 1 1 specularColor 1 1 1 shininess 0.4 }
   DEF FloorPanel Separator {
   DEF FloorStrip Separator {
   DEF FloorBoard Separator {
   Normal { vector 0 1 0 }
   TextureCoordinate2 {
  point [ 0 0, 0.5 0, 0.5 2, 0.5 4, 0.5 6,
0.5 8, 0 8, 0 6, 0 4, 0 2 ] }
   Coordinate3 {
  point [ 0 0 0, .5 0 0, .5 0 -2, .5 0 -4, .5 0 -6,
.5 0 -8, 0 0 -8, 0 0 -6, 0 0 -4, 0 0 -2, ]
   }
   FaceSet { numVertices 10 }
   BaseColor { rgb 0.3 0.1 0.0 }
   Translation { translation 0.125 0 -0.333 }
   Cylinder { parts TOP radius 0.04167 height 0.002 }
   Translation { translation 0.25 0 0 }
   Cylinder { parts TOP radius 0.04167 height 0.002 }
   Translation { translation 0 0 -7.333 }
   Cylinder { parts TOP radius 0.04167 height 0.002 }
   Translation { translation -0.25 0 0 }
   Cylinder { parts TOP radius 0.04167 height 0.002 }
   }
   Translation { translation 0 0 8.03 }
   USE FloorBoard
   Translation { translation 0 0 8.04 }
   USE FloorBoard
   }
   Translation { translation 0.53 0 -0.87 }
   USE FloorStrip
   Translation { translation 0.53 0 -2.3 }
   USE FloorStrip
   Translation { translation 0.53 0 1.3 }
   USE FloorStrip
   Translation { translation 0.53 0 1.1 }
   USE FloorStrip
   Translation { translation 0.53 0 -0.87 }
   USE FloorStrip
   Translation { translation 0.53 0 1.7 }
   USE FloorStrip
   Translation { translation 0.53 0 -0.5 }
   USE FloorStrip
   }
   Translation { translation 4.24 0 0 }
   USE FloorPanel
   Translation { translation 4.24 0 0 }
   USE FloorPanel
}"""

############################################################
## CODE FOR The Inventor Mentor STARTS HERE

# The control points for this surface
pts = (
   (-4.5, -2.0,  8.0),
   (-2.0,  1.0,  8.0),
   ( 2.0, -3.0,  6.0),
   ( 5.0, -1.0,  8.0),
   (-3.0,  3.0,  4.0),
   ( 0.0, -1.0,  4.0),
   ( 1.0, -1.0,  4.0),
   ( 3.0,  2.0,  4.0),
   (-5.0, -2.0, -2.0),
   (-2.0, -4.0, -2.0),
   ( 2.0, -1.0, -2.0),
   ( 5.0,  0.0, -2.0),
   (-4.5,  2.0, -6.0),
   (-2.0, -4.0, -5.0),
   ( 2.0,  3.0, -5.0),
   ( 4.5, -2.0, -6.0))

# The knot vector
knots = (0, 0, 0, 0, 1, 1, 1, 1)

# Create the nodes needed for the Bezier surface.
def makeSurface():
   surfSep = coin.SoSeparator()
   
   # Define the Bezier surface including the control
   # points and a complexity.
   complexity = coin.SoComplexity()
   controlPts = coin.SoCoordinate3()
   surface = coin.SoNurbsSurface()
   complexity.value = 0.7
   controlPts.point.setValues(0, 16, pts)
   surface.numUControlPoints = 4
   surface.numVControlPoints = 4
   surface.uKnotVector.setValues(0, 8, knots)
   surface.vKnotVector.setValues(0, 8, knots)
   surfSep.addChild(complexity)
   surfSep.addChild(controlPts)
   surfSep.addChild(surface)
   
   return surfSep

   #CODE FOR The Inventor Mentor ENDS HERE
   ###########################################################


class hBezSurf:
    "hBezSurf"
    def GetResources(self):
        return {"MenuText": "hBezSurf",
                "Accel": "Ctrl+t",
                "ToolTip": "Creates and displays a Bezier surface.",
                "Pixmap": os.path.dirname(__file__)+"./resources/8.3.svg"
        }

    def IsActive(self):

        if App.ActiveDocument == None:
            return False
        else:
            return True

    def Activated(self):

        root = coin.SoSeparator()

        rot = coin.SoRotation()
        rot.rotation.setValue(coin.SbRotation(coin.SbVec3f(0.0, 1.0, 0.0), 22/7/2.0))
        root.addChild(rot)

        # Create the scene graph for the carpet
        carpet = coin.SoSeparator()
        surf   = makeSurface()
        tex = coin.SoTexture2()

        tex.filename = "diamondRug.rgb"
        carpet.addChild(tex)
        carpet.addChild(surf)
        root.addChild(carpet)

        # Create the scene graph for the floor
        floor = coin.SoSeparator()
        xlate = coin.SoTranslation()
        scale = coin.SoScale()
        input = coin.SoInput()

        input.setBuffer(floorData)
        result = coin.SoDB.readAll(input)
        xlate.translation = (-12.0, -5.0, -5.0)
        scale.scaleFactor = (2.0, 1.0, 2.0)
        floor.addChild(xlate)
        floor.addChild(scale)
        floor.addChild(result)
        root.addChild(floor)

        # Create the scene graph for the carpet's shadow
        shadow = coin.SoSeparator()
        shmdl  = coin.SoLightModel()
        shmtl  = coin.SoMaterial()
        shclr  = coin.SoBaseColor()
        shxl   = coin.SoTranslation()
        shscl  = coin.SoScale()

        shmdl.model = coin.SoLightModel.BASE_COLOR
        shclr.rgb = (0.21, 0.15, 0.09)
        shmtl.transparency = 0.3
        shxl.translation = (0.0, -4.9, 0.0)
        shscl.scaleFactor = (1.0, 0.0, 1.0)
        shadow.addChild(shmtl)
        shadow.addChild(shmdl)
        shadow.addChild(shclr)
        shadow.addChild(shxl)
        shadow.addChild(shscl)
        shadow.addChild(surf)
        root.addChild
        #Main function 
        view = Gui.ActiveDocument.ActiveView
        sg = view.getSceneGraph()
        sg.addChild(root)
        Gui.SendMsgToActiveView('ViewFit')
    
Gui.addCommand('hBezSurf',hBezSurf())