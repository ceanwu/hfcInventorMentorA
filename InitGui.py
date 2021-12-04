####################################################################
# Test Demos from the book The Inventor Mentor in a workbench      #
# By ceanwu@yahoo.com                                              #
# No warranty.                                                     #
####################################################################
class hfcInventorMentorA (Workbench):
    "hfcInventorMentorA object"
    Icon = """
        /* XPM */
        static char * hpBox_Workbench_Main_xpm[] = {
        "16 16 48 1",
        " 	c None",
        ".	c #171D96",
        "+	c #1A229B",
        "@	c #222CA1",
        "#	c #181D95",
        "$	c #232DA2",
        "%	c #3344B3",
        "&	c #2A36A9",
        "*	c #181C96",
        "=	c #181B94",
        "-	c #161C96",
        ";	c #4961C8",
        ">	c #5776D5",
        ",	c #192098",
        "'	c #171C96",
        ")	c #394DB9",
        "!	c #5C7DDB",
        "~	c #5B7BDA",
        "{	c #465FC5",
        "]	c #384AB5",
        "^	c #4D67CB",
        "/	c #4D67CC",
        "(	c #171D97",
        "_	c #3D51BC",
        ":	c #181E96",
        "<	c #181E97",
        "[	c #4961C7",
        "}	c #1B2099",
        "|	c #1F269E",
        "1	c #506DCF",
        "2	c #516ED0",
        "3	c #171F96",
        "4	c #4861C8",
        "5	c #5A7BDA",
        "6	c #2631A5",
        "7	c #191E97",
        "8	c #181F99",
        "9	c #1B229A",
        "0	c #445AC3",
        "a	c #597AD9",
        "b	c #1F279E",
        "c	c #2E3BAD",
        "d	c #181D97",
        "e	c #192097",
        "f	c #181D98",
        "g	c #181F97",
        "h	c #3C51BC",
        "i	c #10128F",
        "                ",
        "                ",
        "          ..    ",
        "          +@    ",
        "  #$%&*= -;>,   ",
        " ')!!!~{]^!!/(  ",
        " '!!!!!!!!!!!_: ",
        " <[!!!!!!!!!!!} ",
        "  |!!!!11!!!!23 ",
        "  :4!567890!ab  ",
        "   |!c    def   ",
        "   gh(          ",
        "    i           ",
        "                ",
        "                ",
        "                "};
        """
    MenuText = "hfcInventorMentorA"
    ToolTip = "This is hfcInventorMentorA workbench"
	
    def GetClassName(self):
        return "Gui::PythonWorkbench"

    def Initialize(self):
	
        #
        #B
        #
        import h2_1Cone
        self.appendToolbar("Tools2", ["hCone"])

        import h2_2EngineSpin
        self.appendToolbar("Tools2", ["hEngineSpin"])

        import h2_3Trackball
        self.appendToolbar("Tools2", ["hTrackball"])

        import h2_4Examiner
        self.appendToolbar("Tools2", ["hExaminer"])
        #
        #C
        #
        import h3_1Molecule
        self.appendToolbar("Tools3", ["hMolecule"])

        import h3_2Robot
        self.appendToolbar("Tools3", ["hRobot"])

        import h3_3Naming
        self.appendToolbar("Tools3", ["hNaming"])
        #
        #D
        #
        import h4_1Cameras
        self.appendToolbar("Tools4", ["hCameras"])

        import h4_2Lights
        self.appendToolbar("Tools4", ["hLights"])
        #
        #E
        #
        import h5_1FaceSet
        self.appendToolbar("Tools5", ["hFaceSet"])
		
        import h5_2IndexedFaceSet
        self.appendToolbar("Tools5", ["hIndexedFaceSet"])

        import h5_3TriangleStripSet
        self.appendToolbar("Tools5", ["hTriangleStripSet"])

        import h5_4QuadMesh
        self.appendToolbar("Tools5", ["hQuadMesh"])

        import h5_5Binding
        self.appendToolbar("Tools5", ["hBinding"])

        import h5_6TransformOrdering
        self.appendToolbar("Tools5", ["hTransformOrdering"])
        #
        #F
        #
        import h6_1Text
        self.appendToolbar("Tools6", ["hText"])
        
        import h6_2Simple3DText
        self.appendToolbar("Tools6", ["hSimple3DText"])
		
        import h6_3Complex3DText
        self.appendToolbar("Tools6", ["hComplex3DText"])
        #
        #G
        #
        import h7_1BasicTexture
        self.appendToolbar("Tools7", ["hBasicTexture"])
		
        import h7_2TextureCoordinates
        self.appendToolbar("Tools7", ["hTextureCoordinates"])
		
        import h7_3TextureFunction
        self.appendToolbar("Tools7", ["hTextureFunction"])
        #
        #H
        #
        import h8_1BSCurve
        self.appendToolbar("Tools8", ["hBSCurve"])

        import h8_2UniCurve
        self.appendToolbar("Tools8", ["hUniCurve"])
        
        import h8_3BezSurf
        self.appendToolbar("Tools8", ["hBezSurf"])
        
        import h8_4TrimSurf
        self.appendToolbar("Tools8", ["hTrimSurf"])
        #
        #I
        #
        import h9_1Print
        self.appendToolbar("Tools9", ["hPrint"])

        import h9_2Texture
        self.appendToolbar("Tools9", ["hTexture"])

        import h9_3Search
        self.appendToolbar("Tools9", ["hSearch"])

        import h9_4PickAction
        self.appendToolbar("Tools9", ["hPickAction"])

        import h9_5GenSph
        self.appendToolbar("Tools9", ["hGenSph"])

		#
        Log("Loading hfcInventorMentorA... done\n")

    def Activated(self):
        # do something here if needed...
        Msg("hfcInventorMentorA.Activated()\n")

    def Deactivated(self):
        # do something here if needed...
        Msg("hfcInventorMentorA.Deactivated()\n")

FreeCADGui.addWorkbench(hfcInventorMentorA)