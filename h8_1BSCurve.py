####################################################################
# Test Demos from the book The Inventor Mentor in a workbench      #
# By ceanwu@yahoo.com                                              #
# No warranty.                                                     #
# Modified Mariwan Jalal's FreeCAD macro to be a command           #
####################################################################
###
# This is an example from the Inventor Mentor,
# chapter 8, example 1.
#
# This example creates and displays a B-Spline curve.
# The curve is order 3 with 7 control points and a knot
# vector of length 10.  One of its knots has multiplicity
# 2 to illustrate a curve with a spike in it.
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

##############################################################
# CODE FOR The Inventor Mentor STARTS HERE

# The control points for this curve
pts = (
    (4.0, -6.0,  6.0),
    (-4.0,  1.0,  0.0),
    (-1.5,  5.0, -6.0),
    (0.0,  2.0, -2.0),
    (1.5,  5.0, -6.0),
    (4.0,  1.0,  0.0),
    (-4.0, -6.0,  6.0))

# The knot vector
knots = (1, 2, 3, 4, 5, 5, 6, 7, 8, 9)

# Create the nodes needed for the B-Spline curve.


def makeCurve():
    curveSep = coin.SoSeparator()

    # Set the draw style of the curve.
    drawStyle = coin.SoDrawStyle()
    drawStyle.lineWidth = 4
    curveSep.addChild(drawStyle)

    # Define the NURBS curve including the control points
    # and a complexity.
    complexity = coin.SoComplexity()
    controlPts = coin.SoCoordinate3()
    curve = coin.SoNurbsCurve()
    complexity.value = 0.8
    controlPts.point.setValues(0, 7, pts)
    curve.numControlPoints = 7
    curve.knotVector.setValues(0, 10, knots)
    curveSep.addChild(complexity)
    curveSep.addChild(controlPts)
    curveSep.addChild(curve)

    return curveSep

# CODE FOR The Inventor Mentor ENDS HERE
##############################################################



class hBSCurve:
    "hBSCurve"
    def GetResources(self):
        return {"MenuText": "hBSCurve",
                "Accel": "Ctrl+t",
                "ToolTip": "Creates and displays a B-Spline curve.",
                "Pixmap": os.path.dirname(__file__)+"./resources/8.1.svg"
        }

    def IsActive(self):

        if App.ActiveDocument == None:
            return False
        else:
            return True

    def Activated(self):

        # Initialize Inventor and Qt
        root = coin.SoSeparator()
        # Create the scene graph for the heart
        heart = coin.SoSeparator()
        curveSep = makeCurve()
        lmodel = coin.SoLightModel()
        clr = coin.SoBaseColor()
        lmodel.model = coin.SoLightModel.BASE_COLOR
        clr.rgb = (1.0, 0.0, 0.1)
        heart.addChild(lmodel)
        heart.addChild(clr)
        heart.addChild(curveSep)
        root.addChild(heart)
        # Create the scene graph for the floor
        floor = coin.SoSeparator()
        xlate = coin.SoTranslation()
        rot = coin.SoRotation()
        scale = coin.SoScale()
        input = coin.SoInput()
        input.setBuffer(floorData)
        result = coin.SoDB.readAll(input)
        xlate.translation = (-12.0, -5.0, -5.0)
        scale.scaleFactor = (2.0, 1.0, 2.0)
        rot.rotation.setValue(coin.SbRotation(coin.SbVec3f(0.0, 1.0, 0.0), 22/7/2.0))
        floor.addChild(rot)
        floor.addChild(xlate)
        floor.addChild(scale)
        floor.addChild(result)
        root.addChild(floor)
        # Create the scene graph for the heart's shadow
        shadow = coin.SoSeparator()
        shmdl = coin.SoLightModel()
        shmtl = coin.SoMaterial()
        shclr = coin.SoBaseColor()
        shxl = coin.SoTranslation()
        shscl = coin.SoScale()
        shmdl.model = coin.SoLightModel.BASE_COLOR
        shclr.rgb = (0.21, 0.15, 0.09)
        shmtl.transparency = 0.5
        shxl.translation = (0.0, -4.9, 0.0)
        shscl.scaleFactor = (1.0, 0.0, 1.0)
        shadow.addChild(shmtl)
        shadow.addChild(shmdl)
        shadow.addChild(shclr)
        shadow.addChild(shxl)
        shadow.addChild(shscl)
        shadow.addChild(curveSep)
        root.addChild(shadow)
        #Main function 
        view = Gui.ActiveDocument.ActiveView
        sg = view.getSceneGraph()
        sg.addChild(root)
        Gui.SendMsgToActiveView('ViewFit')
    
Gui.addCommand('hBSCurve',hBSCurve())