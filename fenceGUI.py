from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import Qt
import maya.OpenMayaUI as omui
from shiboken6 import wrapInstance

from fence import FenceGen


def get_main_maya_win():
    main_win = omui.MQtUtil.mainWindow()
    return wrapInstance(int(main_win), QtWidgets.QWidget)


class FenceGUI(QtWidgets.QDialog):


    def __init__(self):
        super().__init__(parent=get_main_maya_win())
        self.fence_generator = FenceGen()
        self.setWindowTitle("Fence GUI")
        self.create_layout()
        self.create_connections()

    def create_layout(self):
        self.main_lay = QtWidgets.QVBoxLayout()
        self.resize(300, 300)
        self._form_UI()
        self.create_btn = QtWidgets.QPushButton("Create")
        self.main_lay.addWidget(self.create_btn)
        self.setLayout(self.main_lay)


    def _form_UI(self):
        self.form_lay = QtWidgets.QFormLayout()
        self._panel_UI()
        self._spacing_UI()
        self._curve_UI()
        self._worn_UI()
        self.main_lay.addLayout(self.form_lay)


    def _panel_UI(self):    
        self.panel_amt_spinbx = QtWidgets.QSpinBox()
        self.panel_amt_spinbx.setValue(3)
        self.panel_amt_spinbx.setMinimum(2)
        self.form_lay.addRow("Fence Panels", self.panel_amt_spinbx)


    def _spacing_UI(self):
        self.spacing_dspinbx = QtWidgets.QDoubleSpinBox()
        self.spacing_dspinbx.setValue(2)
        self.spacing_dspinbx.setMinimum(0)
        self.form_lay.addRow("Distance Between Posts", self.spacing_dspinbx)
        self.fence_height_slider = QtWidgets.QSlider(Qt.Orientation.Horizontal)
        self.fence_height_slider.setRange(1,25)
        self.fence_height_slider.setFixedWidth(300)
        self.form_lay.addRow("Fence Height", self.fence_height_slider)


    def _curve_UI(self):
        self.curve_height_dspinbx = QtWidgets.QDoubleSpinBox()
        self.curve_height_dspinbx.setValue(0)
        self.form_lay.addRow("Curve Height", self.curve_height_dspinbx)
        self.curve_width_dspinbx = QtWidgets.QDoubleSpinBox()
        self.curve_width_dspinbx.setValue(0)
        self.form_lay.addRow("Curve Width", self.curve_width_dspinbx)


    def _worn_UI(self):
        self.worn_checkbx = QtWidgets.QCheckBox()
        self.worn_checkbx.setChecked(False)
        self.form_lay.addRow("Enable Missing Panels", self.worn_checkbx)

    def create_connections(self):
        self.create_btn.clicked.connect(self.create)

    @QtCore.Slot()
    def create(self):
        self.fence_generator.fence_spacing = self.spacing_dspinbx.value()
        self.fence_generator.fencePanels_amount = self.panel_amt_spinbx.value()
        self.fence_generator.fence_height = self.fence_height_slider.value()
        self.fence_generator.create()
