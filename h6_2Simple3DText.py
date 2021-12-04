####################################################################
# Test Demos from the book The Inventor Mentor in a workbench      #
# By ceanwu@yahoo.com                                              #
# No warranty.                                                     #
# Modified Mariwan Jalal's FreeCAD macro to be a command           #
####################################################################
###
# This is an example from the Inventor Mentor,
# chapter 6, example 2.
#
# This example renders a globe and uses 3D text to label the
# continents Africa and Asia.
#
import os
import sys
import FreeCAD as App
import FreeCADGui as Gui
import pivy.coin as coin

class hSimple3DText:
    "hSimple3DText"
    def GetResources(self):
        return {"MenuText": "hSimple3DText",
                "Accel": "Ctrl+t",
                "ToolTip": "Renders a globe and uses 3D text to label the continents Africa and Asia.",
                "Pixmap": os.path.dirname(__file__)+"./resources/6.2.svg"
        }

    def IsActive(self):

        if App.ActiveDocument == None:
            return False
        else:
            return True

    def Activated(self):

        root = coin.SoGroup()

        # Choose a font
        myFont = coin.SoFont()
        myFont.name = "Times-Roman"
        myFont.size = .2
        root.addChild(myFont)

        # We'll color the front of the text white, and the sides 
        # dark grey. coin.So use a materialBinding of PER_PART and
        # two diffuseColor values in the material node.
        myMaterial = coin.SoMaterial()
        myBinding = coin.SoMaterialBinding()
        myMaterial.diffuseColor.set1Value(0, coin.SbColor(1,1,1))
        myMaterial.diffuseColor.set1Value(1, coin.SbColor(.1,.1,.1))
        myBinding.value = coin.SoMaterialBinding.PER_PART
        root.addChild(myMaterial)
        root.addChild(myBinding)

        # Create the globe
        sphereSep = coin.SoSeparator()
        myTexture2 = coin.SoTexture2()
        sphereComplexity = coin.SoComplexity()
        sphereComplexity.value = 0.55
        root.addChild(sphereSep)
        sphereSep.addChild(myTexture2)
        sphereSep.addChild(sphereComplexity)
        sphereSep.addChild(coin.SoSphere())
        #TODO: FIXME : CHANGE PATH
        Frgb=os.path.dirname(__file__)+"./iv/globe.rgb"
        #myTexture2.filename = "E:\\TEMP\\fix some drawing\\Mentor_Freecad\\globe.rgb"  
        myTexture2.filename = Frgb  

        # Add Text3 for AFRICA, transformed to proper location.
        africaSep = coin.SoSeparator()
        africaTransform = coin.SoTransform()
        africaText = coin.SoText3()
        africaTransform.rotation.setValue(coin.SbVec3f(0,1,0), .4)
        africaTransform.translation = (.25, .0, 1.25)
        africaText.parts = coin.SoText3.ALL
        africaText.string = "AFRICA"
        root.addChild(africaSep)
        africaSep.addChild(africaTransform)
        africaSep.addChild(africaText)

        # Add Text3 for ASIA, transformed to proper location.
        asiaSep = coin.SoSeparator()
        asiaTransform = coin.SoTransform()
        asiaText = coin.SoText3()
        asiaTransform.rotation.setValue(coin.SbVec3f(0,1,0), 1.5)
        asiaTransform.translation = (.8, .6, .5)
        asiaText.parts = coin.SoText3.ALL
        asiaText.string = "ASIA"
        root.addChild(asiaSep)
        asiaSep.addChild(asiaTransform)
        asiaSep.addChild(asiaText)
        #Main function 
        view = Gui.ActiveDocument.ActiveView
        sg = view.getSceneGraph()
        sg.addChild(root)
        Gui.SendMsgToActiveView('ViewFit')
    
Gui.addCommand('hSimple3DText',hSimple3DText())