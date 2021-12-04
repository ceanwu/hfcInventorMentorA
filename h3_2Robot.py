####################################################################
# Test Demos from the book The Inventor Mentor in a workbench      #
# By ceanwu@yahoo.com                                              #
# No warranty.                                                     #
# Modified Mariwan Jalal's FreeCAD macro to be a command           #
####################################################################
###
# This is an example from the Inventor Mentor,
# chapter 3, example 2.
#
# This code shows how to create a robot out of various nodes.
# It introduces shared instancing of nodes to create two legs
# using two instances of the same subgraph.
#
import os,sys
import FreeCAD as App
import FreeCADGui as Gui
import pivy.coin as coin


def makeRobot():
##############################################################
# CODE FOR The Inventor Mentor STARTS HERE
    # Robot with legs

    # Construct parts for legs (thigh, calf and foot)
    thigh = coin.SoCube()
    thigh.width = 1.2
    thigh.height = 2.2
    thigh.depth = 1.1
    
    calfTransform = coin.SoTransform()
    calfTransform.translation.setValue(0, -2.25, 0.0)
    
    calf = coin.SoCube()
    calf.width, calf.height, calf.depth = 1, 2.2, 1

    footTransform = coin.SoTransform()
    footTransform.translation = (0, -1.5, .5)

    foot = coin.SoCube()
    foot.width, foot.height, foot.depth = 0.8, 0.8, 2

    # Put leg parts together
    leg = coin.SoGroup()
    leg.addChild(thigh)
    leg.addChild(calfTransform)
    leg.addChild(calf)
    leg.addChild(footTransform)
    leg.addChild(foot)
    
    leftTransform = coin.SoTransform()
    leftTransform.translation = (1, -4.25, 0)
    
    # Left leg
    leftLeg = coin.SoSeparator()
    leftLeg.addChild(leftTransform)
    leftLeg.addChild(leg)
    
    rightTransform = coin.SoTransform()
    rightTransform.translation = (-1, -4.25, 0)
    
    # Right leg
    rightLeg = coin.SoSeparator()
    rightLeg.addChild(rightTransform)
    rightLeg.addChild(leg)
    
    # Parts for body
    bodyTransform = coin.SoTransform()
    bodyTransform.translation = (0.0, 3.0, 0.0)
    
    bronze = coin.SoMaterial()
    bronze.ambientColor = (.33, .22, .27)
    bronze.diffuseColor = (.78, .57, .11)
    bronze.specularColor = (.99, .94, .81)
    bronze.shininess = .28
    
    bodyCylinder = coin.SoCylinder()
    bodyCylinder.radius = 2.5
    bodyCylinder.height = 6
    
    # Construct body out of parts 
    body = coin.SoSeparator()
    body.addChild(bodyTransform)      
    body.addChild(bronze)
    body.addChild(bodyCylinder)
    body.addChild(leftLeg)
    body.addChild(rightLeg)
    
    # Head parts
    headTransform = coin.SoTransform()
    headTransform.translation = (0, 7.5, 0)
    headTransform.scaleFactor = (1.5, 1.5, 1.5)
    
    silver = coin.SoMaterial()
    silver.ambientColor = (.2, .2, .2)
    silver.diffuseColor = (.6, .6, .6)
    silver.specularColor = (.5, .5, .5)
    silver.shininess = .5
    
    headSphere = coin.SoSphere()
    
    # Construct head
    head = coin.SoSeparator()
    head.addChild(headTransform)
    head.addChild(silver)
    head.addChild(headSphere)
    
    # Robot is just head and body
    robot = coin.SoSeparator()
    robot.addChild(body)               
    robot.addChild(head)
    
# CODE FOR The Inventor Mentor ENDS HERE
##############################################################

    return robot

class hRobot:
    "hRobot"
    def GetResources(self):
        return {"MenuText": "hRobot",
                "Accel": "Ctrl+t",
                "ToolTip": "Create a robot out of various nodes.",
                "Pixmap": os.path.dirname(__file__)+"./resources/3.2.svg"
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
        sg.addChild(makeRobot())
        Gui.SendMsgToActiveView('ViewFit')
    
Gui.addCommand('hRobot',hRobot())