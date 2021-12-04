####################################################################
# Test Demos from the book The Inventor Mentor in a workbench      #
# By ceanwu@yahoo.com                                              #
# No warranty.                                                     #
# Modified Mariwan Jalal's FreeCAD macro to be a command           #
####################################################################
###
# This is an example from the Inventor Mentor,
# chapter 6, example 1.
#
# This example renders a globe and uses 2D text to label the
# continents Africa and Asia.
#
import os
import sys
import FreeCAD as App
import FreeCADGui as Gui
import pivy.coin as coin

class hText:
    "hText"
    def GetResources(self):
        return {"MenuText": "hText",
                "Accel": "Ctrl+t",
                "ToolTip": "Renders a globe and uses 2D text to label the continents Africa and Asia.",
                "Pixmap": os.path.dirname(__file__)+"./resources/6.1.svg"
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
        myFont.size = 24.0
        root.addChild(myFont)

        # Add the globe, a sphere with a texture map.
        # Put it within a separator.
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

        # Add Text2 for AFRICA, translated to proper location.
        africaSep = coin.SoSeparator()
        africaTranslate = coin.SoTranslation()
        africaText = coin.SoText2()
        africaTranslate.translation = (.25,.0,1.25)
        africaText.string = "AFRICA"
        root.addChild(africaSep)
        africaSep.addChild(africaTranslate)
        africaSep.addChild(africaText)

        # Add Text2 for ASIA, translated to proper location.
        asiaSep = coin.SoSeparator()
        asiaTranslate = coin.SoTranslation()
        asiaText = coin.SoText2()
        asiaTranslate.translation = (.8,.8,0)
        asiaText.string = "ASIA"
        root.addChild(asiaSep)
        asiaSep.addChild(asiaTranslate)
        asiaSep.addChild(asiaText)
        #Main function 
        view = Gui.ActiveDocument.ActiveView
        sg = view.getSceneGraph()
        sg.addChild(root)
        Gui.SendMsgToActiveView('ViewFit')
    
Gui.addCommand('hText',hText())