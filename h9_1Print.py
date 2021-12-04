####################################################################
# Test Demos from the book The Inventor Mentor in a workbench      #
# By ceanwu@yahoo.com                                              #
# No warranty.                                                     #
# Modified Mariwan Jalal's FreeCAD macro to be a command           #
####################################################################
###
# This is an example from the Inventor Mentor,
# chapter 9, example 1.
#
# Printing example.
# Read in an Inventor file and display it in ExaminerViewer.  Press
# the "p" key and the scene renders into a PostScript
# file for printing.
#
from __future__ import print_function

import os
import sys
import FreeCAD as App
import FreeCADGui as Gui
import pivy.coin as coin

class callbackData:
    vwr = None
    filename = None
    scene = None

##############################################################
## CODE FOR The Inventor Mentor STARTS HERE

#Warning: This file might not works as it should. But I put the idea here. Mariwan TODO: FIXME:


def printToPostScript(root, file, viewer, printerDPI):
    # Calculate size of the images in inches which is equal to
    # the size of the viewport in pixels divided by the number
    # of pixels per inch of the screen device.  This size in
    # inches will be the size of the Postscript image that will
    # be generated.
    vp  = viewer.getViewportRegion()
    imagePixSize = vp.getViewportSizePixels()
    imageInches = coin.SbVec2f()

    pixPerInch = coin.SoOffscreenRenderer.getScreenPixelsPerInch()
    imageInches.setValue(imagePixSize[0] / pixPerInch,
                         imagePixSize[1] / pixPerInch)

    # The resolution to render the scene for the printer
    # is equal to the size of the image in inches times
    # the printer DPI
    postScriptRes = coin.SbVec2s()
    postScriptRes.setValue(int(imageInches[0]*printerDPI),
                           int(imageInches[1]*printerDPI))

    # Create a viewport to render the scene into.
    myViewport = coin.SbViewportRegion()
    myViewport.setWindowSize(postScriptRes)
    myViewport.setPixelsPerInch(printerDPI)
    
    # Render the scene
    myRenderer = coin.SoOffscreenRenderer(myViewport)

    if not myRenderer.render(root):
        return False

    # Generate PostScript and write it to the given file
    myRenderer.writeToPostScript(file)

    return True

# CODE FOR The Inventor Mentor ENDS HERE
##############################################################


def processKeyEvents(data, cb):
    if coin.SoKeyboardEvent_isKeyPressEvent(cb.getEvent(), coin.SoKeyboardEvent.P):
        myFile = open(data.filename, "w")

        if myFile == None:
            sys.stderr.write("Cannot open output file\n")
            sys.exit(1)

        sys.stdout.write("Printing scene... ")
        sys.stdout.flush()
        if not printToPostScript(data.scene, myFile, data.vwr, 75):
            sys.stderr.write("Cannot print image\n")
            myFile.close()
            sys.exit(1)

        myFile.close()
        sys.stdout.write("  ...done printing.\n")
        sys.stdout.flush()
        cb.setHandled()


class hPrint:
    "hPrint"
    def GetResources(self):
        return {"MenuText": "hPrint",
                "Accel": "Ctrl+t",
                "ToolTip": "Press the P key and the scene renders into a PostScript file for printing.",
                "Pixmap": os.path.dirname(__file__)+"./resources/9.1.svg"
        }

    def IsActive(self):

        if App.ActiveDocument == None:
            return False
        else:
            return True

    def Activated(self):
        #TODO::CHANGE THIS FILE NAME WITH THE PATH
        Fps=os.path.dirname(__file__)+"./iv/changeme.ps"
        filename=Fps            

        print("To print the scene: press the 'p' key while in picking mode")

        # Make a scene containing an event callback node
        root = coin.SoSeparator()
        eventCB = coin.SoEventCallback()
        root.addChild(eventCB)

        # Read the geometry from a file and add to the scene
        myInput = coin.SoInput()
        #TODO::CHANGE THIS FILE NAME WITH THE PATH
        Fiv=os.path.dirname(__file__)+"./iv/duck.iv"
        if not myInput.openFile(Fiv):    
            sys.exit(1)
        geomObject = coin.SoDB.readAll(myInput)
        if geomObject == None:
            sys.exit(1)
        root.addChild(geomObject)

        view = Gui.ActiveDocument.ActiveView    
        # Setup the event callback data and routine for performing the print
        data = callbackData()
        data.vwr = view
        #TODO::CHANGE THIS FILE NAME WITH THE PATH
        Fcvs=os.path.dirname(__file__)+"./iv/DATA.cvs"
        data.filename = (Fcvs)          
        data.scene = view.getSceneGraph()
        eventCB.addEventCallback(coin.SoKeyboardEvent.getClassTypeId(), processKeyEvents, data)
        #Main function 
        view = Gui.ActiveDocument.ActiveView
        sg = view.getSceneGraph()
        sg.addChild(root)
        Gui.SendMsgToActiveView('ViewFit')
    
Gui.addCommand('hPrint',hPrint())