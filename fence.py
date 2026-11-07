import maya.cmds as cmds

class FenceGen():

    def __init__(self):
        self.fence_height = 3
        self.fencePanels_amount = 5
        self.fence_width = .5
        self.fence_depth = .1
        self.fence_spacing = 0

    def create(self):
        for i in range(self.fencePanels_amount):
            panel = self.create_panel()
            spacing = (self.fence_spacing+self.fence_width)*i
            cmds.setAttr(f"{panel}.translateX", spacing)
        self.create_bars()

    def create_panel(self):
        self.panel_obj, self.panel_node = cmds.polyCube(name="Panel1", height=self.fence_height, depth=self.fence_depth, width=self.fence_width)
        cmds.setAttr(f"{self.panel_obj}.translateY", self.fence_height/2)
        return self.panel_obj

    def create_bars(self):
        bar_width = ((self.fencePanels_amount*self.fence_width)+(self.fencePanels_amount*self.fence_spacing))
        bar_center = ((self.fencePanels_amount*self.fence_width)+((self.fencePanels_amount-2)*self.fence_spacing))
        self.bar_obj, self.bar_node = cmds.polyCube(name="Bar1", height=self.fence_width, depth=self.fence_depth, width= bar_width)
        cmds.setAttr(f"{self.bar_obj}.translateY", self.fence_height-(self.fence_width/2)-.5)
        cmds.setAttr(f"{self.bar_obj}.translateZ", self.fence_depth)
        cmds.setAttr(f"{self.bar_obj}.translateX", (bar_center/2))
        self.bar2_obj, self.bar2_node = cmds.polyCube(name="Bar2", height=self.fence_width, depth=self.fence_depth, width= bar_width)
        cmds.setAttr(f"{self.bar2_obj}.translateY", self.fence_width/2+.5)
        cmds.setAttr(f"{self.bar2_obj}.translateZ", self.fence_depth)
        cmds.setAttr(f"{self.bar2_obj}.translateX", (bar_center/2))
        return self.bars_obj