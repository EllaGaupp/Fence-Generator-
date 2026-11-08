import maya.cmds as cmds
import random

class FenceGen():

    def __init__(self):
        self.fence_height = 3.0
        self.fencePanels_amount = 5
        self.fence_width = .5
        self.fence_depth = .1
        self.fence_spacing = 0.0
        self.height_random = False
        self.rand_height = 0.0
        self.missing = False

    def create(self):
        if cmds.objExists("fence_GRP"):
            cmds.delete("fence_GRP")

        created_fence = []
        for i in range(self.fencePanels_amount):
            if self.height_random:
                self.random_height()
            else:
                self.rand_height = self.fence_height

            if self.missing and self.missing_panel():
                continue
                            
            panel = self.create_panel()
            created_fence.append(panel)
            spacing = (self.fence_spacing+self.fence_width)*i
            cmds.setAttr(f"{panel}.translateX", spacing)
        bars = self.create_bars()
        created_fence.append(bars)
        fence_GRP = cmds.group(created_fence, name="fence_GRP")
        return fence_GRP

    def random_height(self):
        var_amount = (self.fence_height*.1)
        self.rand_height = random.uniform((self.fence_height-var_amount), (self.fence_height+var_amount))

    def missing_panel(self):
        return random.randint(1,6) == random.randint(1,6)
    
    def create_panel(self):
        self.panel_obj, self.panel_node = cmds.polyCube(name="Panel1", height=self.rand_height, depth=self.fence_depth, width=self.fence_width)
        cmds.setAttr(f"{self.panel_obj}.translateY", self.rand_height/2)
        return self.panel_obj

    def create_bars(self):
        bar_width = ((self.fencePanels_amount*self.fence_width)+(self.fencePanels_amount*self.fence_spacing))
        bar_center = ((self.fence_spacing+self.fence_width)*(self.fencePanels_amount-1.0))
        bar_height = ((self.fence_height/5))
        self.bar_obj, self.bar_node = cmds.polyCube(name="Bar1", height=bar_height, depth=self.fence_depth, width= bar_width)
        cmds.setAttr(f"{self.bar_obj}.translateY", self.fence_height-(bar_height/2)-.75)
        cmds.setAttr(f"{self.bar_obj}.translateZ", self.fence_depth)
        cmds.setAttr(f"{self.bar_obj}.translateX", (bar_center/2.0))
        self.bar2_obj, self.bar2_node = cmds.polyCube(name="Bar2", height=bar_height, depth=self.fence_depth, width= bar_width)
        cmds.setAttr(f"{self.bar2_obj}.translateY", bar_height/2+.75)
        cmds.setAttr(f"{self.bar2_obj}.translateZ", self.fence_depth)
        cmds.setAttr(f"{self.bar2_obj}.translateX", (bar_center/2.0))
        self.bars_grp = cmds.group([self.bar_obj, self.bar2_obj], name="bars_GRP")        
        return self.bars_grp
