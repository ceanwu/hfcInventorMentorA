####################################################################
# Test Demos from the book The Inventor Mentor in a workbench      #
# By ceanwu@yahoo.com                                              #
# No warranty.                                                     #
# Modified Mariwan Jalal's FreeCAD macro to be a command           #
####################################################################
###
# This is an example from the Inventor Mentor,
# chapter 2, example 3.
#
# Use the trackball manipulator to edit/rotate a red cone
#
import os
import sys
import FreeCAD as App
import FreeCADGui as Gui
import pivy.coin as coin

# Great Example how you can use this to rotate objects :)

class hTrackball:
    "hTrackball"
    """
    Note:
    There are many other kind of this manupulation widget. Please choose the following classes to get other types.add()
    
    #link : http://webcache.googleusercontent.com/search?q=cache:9kTXW4u5hIkJ:www-evasion.inrialpes.fr/people/Francois.Faure/doc/inventor_doc.con3d.org/Coin/group__manips.html+&cd=12&hl=sv&ct=clnk&gl=se&client=firefox-b-d

    coin.SoCenterballManip()   	        #The SoCenterballManip wraps an SoCenterballDragger for convenience. More...
    coin.SoClipPlaneManip()      	    #The SoClipPlaneManip class is used to manipulate clip planes. More...
    coin.SoDirectionalLightManip()  	#The SoDirectionalLightManip class is used to manipulate SoDirectionalLight nodes. More...
    coin.SoHandleBoxManip()         	#The SoHandleBoxManip class wraps an SoHandleBoxDragger for manipulating a transformation. More...
    coin.SoJackManip()              	#The SoJackManip wraps an SoJackDragger for convenience. More...
    coin.SoPointLightManip()       	    #The SoPointLightManip class is used to manipulate point light nodes. More...
    coin.SoSpotLightManip()         	#The SoSpotLightManip class is used to manipulate spot light nodes. More...
    coin.SoTabBoxManip()            	#The SoTabBoxManip class wraps an SoTabBoxDragger. More...
    coin.SoTrackballManip()    	        # The SoTrackballManip wraps an SoTrackballDragger for convenience. More...
    coin.SoTransformBoxManip()       	#The SoTransformBoxManip wraps an SoTransformBoxDragger for convenience. More...
    coin.SoTransformManip()         	#The SoTransformManip class is used to manipulate transformations. More...
    coin.SoTransformerManip()           #The SoTransformerManip wraps an SoTransformerDragger for convenience
    """

    
    def GetResources(self):
        return {"MenuText": "hTrackball",
                "Accel": "Ctrl+t",
                "ToolTip": "Use the trackball manipulator to edit/rotate a red cone",
                "Pixmap": os.path.dirname(__file__)+"./resources/2.3.svg"
        }

    def IsActive(self):

        if App.ActiveDocument == None:
            return False
        else:
            return True

    def Activated(self):

        root = coin.SoSeparator()

        root.addChild(coin.SoDirectionalLight())  # child 1
        # child 2     # You can choose other types .. Look at the note bellow the code
        root.addChild(coin.SoTrackballManip())

        myMaterial = coin.SoMaterial()
        myMaterial.diffuseColor = (1.0, 0.0, 0.0)
        root.addChild(myMaterial)
        root.addChild(coin.SoCone())

        view = Gui.ActiveDocument.ActiveView
        sg = view.getSceneGraph()
        sg.addChild(root)
        Gui.SendMsgToActiveView('ViewFit')

Gui.addCommand('hTrackball',hTrackball())

