# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'guilayout.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# GUI by Kenneth Marshall, PDFGetX3 was made by Simon Billinge and Pavol Juhás

from PyQt6 import QtCore, QtWidgets, QtGui
import os
from pdfgetx3gui import pdffunctions
from diffpy.pdfgetx import __version__ as pgxversion
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import time
from scipy.interpolate import interp1d
matplotlib.rcParams.update({'font.size': 10})
import sys
import re
from glob import glob
from .pdfworker import Worker, SaveDirWorker

def text_to_bool(text: str) -> bool:
	if 'True' in text:
		return True
	elif 'False' in text:
		return False
	else:
		raise ValueError('text_to_bool function argument must be \'True\' or \'False\' as a string')

def loadData(filename):
	try:
		x,y = np.loadtxt(filename,unpack=True,comments='#', usecols = (0,1))
		return x,y
	except ValueError:
		print('couldn\'t read file with default # comments, trying by line')
		pass
	f = open(filename,'r')
	lines = f.read().split('\n')
	f.close()
	for c,line in enumerate(lines):
		if not line:
			continue
		if re.search('[0-9]',line.replace(' ','')[0].lower()):
			x,y = np.loadtxt(filename,unpack=True, skiprows=c, usecols=(0,1))
			return x,y
	raise ValueError(f'couldn\'t find data in {filename}')	


class Ui_MainWindow(QtWidgets.QMainWindow):
	def setupUi(self):
		super().__init__()
		self.configfilepath = os.path.dirname(os.path.realpath(__file__))
		#self.setObjectName("PDFGetX3GUI")
		self.centralwidget = QtWidgets.QWidget()
		self.centralwidget.setObjectName("centralwidget")

		self.setWindowIcon(QtGui.QIcon(f'{self.configfilepath}/icon/icon.ico'))
		
		self.grid = QtWidgets.QGridLayout()

		self.filename = QtWidgets.QLineEdit()
		self.filename.setObjectName("filename")
		self.filename.setEnabled(False)
		self.filename.setFont(QtGui.QFont('Calibiri',7))
		self.filename.setStyleSheet("color: black;")
		self.filename.setText(f"{self.configfilepath}/exampleFiles/LaB6_0p4mm_011_av10_monitor.xye")
		self.grid.addWidget(self.filename, 0,0, 1, 3)
		
		

		self.bkgfilename = QtWidgets.QLineEdit()
		self.bkgfilename.setObjectName("bkgfilename")
		self.bkgfilename.setEnabled(False)
		self.bkgfilename.setFont(QtGui.QFont('Calibiri',7))
		self.bkgfilename.setStyleSheet("color: black;")
		self.bkgfilename.setText(f"{self.configfilepath}/exampleFiles/0p4mm_capillary_018_av17_monitor.xye")
		self.grid.addWidget(self.bkgfilename, 1,0, 1, 3)

		self.fileLabel = QtWidgets.QLabel()
		self.fileLabel.setObjectName("fileLabel")
		self.grid.addWidget(self.fileLabel, 0, 4)
		
		self.fileButton = QtWidgets.QPushButton()
		self.fileButton.setObjectName("fileButton")
		self.fileButton.setMaximumWidth(25)
		self.grid.addWidget(self.fileButton, 0,3)

		self.bkgFileLabel = QtWidgets.QLabel()
		self.bkgFileLabel.setObjectName("bkgFileLabel")
		self.bkgFileLabel.setText("background\nfile")
		self.grid.addWidget(self.bkgFileLabel,1, 4)

		self.bkgfilebutton = QtWidgets.QPushButton()
		self.bkgfilebutton.setObjectName("bkgfilebutton")
		self.bkgfilebutton.setMaximumWidth(25)
		self.grid.addWidget(self.bkgfilebutton, 1,3)

		self.compositionBox = QtWidgets.QLineEdit()
		self.compositionBox.setObjectName("compositionBox")
		self.grid.addWidget(self.compositionBox, 2, 0)

		self.compositionLabel = QtWidgets.QLabel()
		self.compositionLabel.setObjectName("compositionLabel")
		self.grid.addWidget(self.compositionLabel, 2, 1)
		
		self.wavelengthBox = QtWidgets.QLineEdit()
		self.wavelengthBox.setObjectName("wavelengthBox")
		self.grid.addWidget(self.wavelengthBox, 3, 0)

		self.wavelengthLabel = QtWidgets.QLabel()
		self.wavelengthLabel.setObjectName("wavelengthLabel")
		self.grid.addWidget(self.wavelengthLabel, 3, 1)

		self.filelistBox = QtWidgets.QComboBox()
		self.filelistBox.setObjectName("filelistBox")
		self.grid.addWidget(self.filelistBox, 4,0,1,2)

		self.fileListLabel = QtWidgets.QLabel()
		self.fileListLabel.setObjectName("fileListLabel")
		self.grid.addWidget(self.fileListLabel, 4,2)

		self.bkgfilelistBox = QtWidgets.QComboBox()
		self.bkgfilelistBox.setObjectName("bkgfilelistBox")
		self.grid.addWidget(self.bkgfilelistBox, 6,0,1,2)

		self.bkgfileListLabel = QtWidgets.QLabel()
		self.bkgfileListLabel.setObjectName("bkgfileListLabel")
		self.bkgfileListLabel.setText('background\nfiles')
		self.bkgfileListLabel.adjustSize()
		self.grid.addWidget(self.bkgfileListLabel, 6,2)

		self.removeButton = QtWidgets.QPushButton()
		self.removeButton.setObjectName("removeButton")
		self.grid.addWidget(self.removeButton, 5, 0)

		self.bkgremoveButton = QtWidgets.QPushButton()
		self.bkgremoveButton.setObjectName("bkgremoveButton")
		self.bkgremoveButton.setText('remove bkg file')
		self.grid.addWidget(self.bkgremoveButton, 7, 0)

		self.inputFormatGroup = QtWidgets.QButtonGroup()
		self.inputFormatLabel = QtWidgets.QLabel()
		self.inputFormatLabel.setObjectName("inputFormatLabel")
		self.grid.addWidget(self.inputFormatLabel, 0,5, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)

		self.formatgrid = QtWidgets.QHBoxLayout()
		self.QButton = QtWidgets.QRadioButton()
		self.QButton.setChecked(True)
		self.QButton.setObjectName("QButton")
		
		self.formatgrid.addWidget(self.QButton)

		self.twothetaButton = QtWidgets.QRadioButton()
		self.twothetaButton.setObjectName("twothetaButton")
		self.formatgrid.addWidget(self.twothetaButton)

		self.inputFormatGroup.addButton(self.QButton)
		self.inputFormatGroup.addButton(self.twothetaButton)
		self.grid.addLayout(self.formatgrid, 1,5)

		self.atomDensityBox = QtWidgets.QDoubleSpinBox()
		self.atomDensityBox.setValue(0)
		self.atomDensityBox.setObjectName("atomDensityBox")
		self.atomDensityBox.setDecimals(3)
		self.atomDensityBox.setSingleStep(0.001)
		self.atomDensityBox.setKeyboardTracking(False)
		self.atomDensityBox.valueChanged.connect(self.runUpdate)
		self.grid.addWidget(self.atomDensityBox, 2, 5)

		self.atomDensityLabel = QtWidgets.QLabel()
		self.atomDensityLabel.setText("atom density (\u00C5\u207B\u00B3)")
		self.atomDensityLabel.adjustSize()
		self.grid.addWidget(self.atomDensityLabel, 2, 6)

		self.atomDensityExtent = QtWidgets.QDoubleSpinBox()
		self.atomDensityExtent.setValue(2)
		self.atomDensityExtent.setObjectName("atomDensityExtent")
		self.atomDensityExtent.setDecimals(1)
		self.atomDensityExtent.setSingleStep(0.1)
		self.atomDensityExtent.setKeyboardTracking(False)
		self.atomDensityExtent.valueChanged.connect(self.runUpdate)
		self.grid.addWidget(self.atomDensityExtent, 3, 5)

		self.atomDensityExtentLabel = QtWidgets.QLabel()
		self.atomDensityExtentLabel.setText("density line extent")
		self.atomDensityExtentLabel.adjustSize()
		self.grid.addWidget(self.atomDensityExtentLabel, 3, 6)

		self.outputFormatGroup = QtWidgets.QButtonGroup()
		

		self.settingsGrid = QtWidgets.QGridLayout()

		self.relLabel = QtWidgets.QLabel()
		self.relLabel.setObjectName("relLabel")
		self.relLabel.setText('step size')
		self.settingsGrid.addWidget(self.relLabel, 0,2)
		
		self.bkgscalebox = QtWidgets.QDoubleSpinBox()
		self.bkgscalebox.setProperty("value", 1)
		self.bkgscalebox.setObjectName("bkgscalebox")
		self.bkgscalebox.setDecimals(3)
		self.bkgscalebox.setSingleStep(0.1)
		self.bkgscalebox.setKeyboardTracking(False)
		self.settingsGrid.addWidget(self.bkgscalebox, 1, 1)

		self.bkgscalerel = QtWidgets.QDoubleSpinBox()
		self.bkgscalerel.setProperty("value", 0.1)
		self.bkgscalerel.setObjectName("bkgscalerel")
		self.bkgscalerel.setDecimals(3)
		self.bkgscalerel.setSingleStep(0.01)
		self.bkgscalerel.setMinimum(-1)
		self.bkgscalerel.setMaximum(1)
		self.settingsGrid.addWidget(self.bkgscalerel, 1,2)

		self.bkgscaleLabel = QtWidgets.QLabel()
		self.bkgscaleLabel.setObjectName("bkgscaleLabel")
		self.settingsGrid.addWidget(self.bkgscaleLabel, 1,0)

		self.qminbox = QtWidgets.QDoubleSpinBox()
		self.qminbox.setProperty("value", 1)
		self.qminbox.setObjectName("qminbox")
		self.qminbox.setDecimals(2)
		self.qminbox.setSingleStep(0.1)
		self.qminbox.setKeyboardTracking(False)
		self.settingsGrid.addWidget(self.qminbox, 2, 1)

		self.qminrel = QtWidgets.QDoubleSpinBox()
		self.qminrel.setProperty("value", 0.1)
		self.qminrel.setObjectName("qminrel")
		self.qminrel.setDecimals(2)
		self.qminrel.setSingleStep(0.01)
		self.qminrel.setMinimum(-1)
		self.qminrel.setMaximum(1)
		self.settingsGrid.addWidget(self.qminrel, 2, 2)

		self.QminLabel = QtWidgets.QLabel()
		self.QminLabel.setObjectName("QminLabel")
		self.settingsGrid.addWidget(self.QminLabel, 2, 0)
		
		self.qmaxbox = QtWidgets.QDoubleSpinBox()
		self.qmaxbox.setProperty("value", 23)
		self.qmaxbox.setObjectName("qmaxbox")
		self.qmaxbox.setDecimals(2)
		self.qmaxbox.setSingleStep(0.1)
		self.qmaxbox.setMinimum(self.qminbox.value()+1)
		self.qmaxbox.setKeyboardTracking(False)
		self.settingsGrid.addWidget(self.qmaxbox, 3, 1)

		self.qmaxrel = QtWidgets.QDoubleSpinBox()
		self.qmaxrel.setProperty("value", 0.1)
		self.qmaxrel.setObjectName("qmaxrel")
		self.qmaxrel.setDecimals(2)
		self.qmaxrel.setSingleStep(0.1)
		self.qmaxrel.setMinimum(-1)
		self.qmaxrel.setMaximum(1)
		self.settingsGrid.addWidget(self.qmaxrel, 3, 2)

		self.qmaxtogether = QtWidgets.QCheckBox()
		self.qmaxtogether.setObjectName('qmaxtogether')
		self.qmaxtogether.setText('Qmax together?')
		self.qmaxtogether.adjustSize()
		self.settingsGrid.addWidget(self.qmaxtogether, 3, 4)

		self.QmaxLabel = QtWidgets.QLabel()
		self.QmaxLabel.setObjectName("QmaxLabel")
		self.settingsGrid.addWidget(self.QmaxLabel, 3, 0)
		
				
		self.qmaxinstbox = QtWidgets.QDoubleSpinBox()
		self.qmaxinstbox.setProperty("value", 23)
		self.qmaxinstbox.setObjectName("qmaxinstbox")
		self.qmaxinstbox.setDecimals(2)
		self.qmaxinstbox.setSingleStep(0.1)
		self.qmaxinstbox.setMinimum(self.qminbox.value()+1)
		self.qmaxinstbox.setKeyboardTracking(False)
		self.settingsGrid.addWidget(self.qmaxinstbox, 4, 1)

		self.qmaxinstrel = QtWidgets.QDoubleSpinBox()
		self.qmaxinstrel.setProperty("value", 0.1)
		self.qmaxinstrel.setObjectName("qmaxinstrel")
		self.qmaxinstrel.setDecimals(2)
		self.qmaxinstrel.setSingleStep(0.1)
		self.qmaxinstrel.setMaximum(1)
		self.qmaxinstrel.setMinimum(-1)
		self.settingsGrid.addWidget(self.qmaxinstrel, 4, 2)

		self.qmaxinstLabel = QtWidgets.QLabel()
		self.qmaxinstLabel.setObjectName("qmaxinstLabel")
		self.settingsGrid.addWidget(self.qmaxinstLabel, 4, 0)

		self.rpolybox = QtWidgets.QDoubleSpinBox()
		self.rpolybox.setMaximum(3)
		self.rpolybox.setProperty("value", 1)
		self.rpolybox.setObjectName("rpolybox")
		self.rpolybox.setSingleStep(0.1)
		self.rpolybox.setDecimals(2)
		self.rpolybox.setKeyboardTracking(False)
		self.settingsGrid.addWidget(self.rpolybox, 5, 1)

		self.rpolyrel = QtWidgets.QDoubleSpinBox()
		self.rpolyrel.setMaximum(5)
		self.rpolyrel.setProperty("value", 0.1)
		self.rpolyrel.setObjectName("rpolyrel")
		self.rpolyrel.setSingleStep(0.01)
		self.rpolyrel.setDecimals(2)
		self.rpolyrel.setMaximum(1)
		self.rpolyrel.setMinimum(-1)
		self.settingsGrid.addWidget(self.rpolyrel, 5, 2)

		self.rpolyLabel = QtWidgets.QLabel()
		self.rpolyLabel.setObjectName("rpolyLabel")
		self.settingsGrid.addWidget(self.rpolyLabel, 5, 0)

		self.scaleBox = QtWidgets.QDoubleSpinBox()
		self.scaleBox.setMaximum(100)
		self.scaleBox.setMinimum(0.01)
		self.scaleBox.setValue(1)
		self.scaleBox.setObjectName("scaleBox")
		self.scaleBox.setSingleStep(0.1)
		self.scaleBox.setDecimals(2)
		self.scaleBox.setKeyboardTracking(False)
		self.settingsGrid.addWidget(self.scaleBox, 6, 1)
	
		self.scalerel = QtWidgets.QDoubleSpinBox()
		self.scalerel.setMaximum(5)
		self.scalerel.setProperty("value", 0.1)
		self.scalerel.setObjectName("scalerel")
		self.scalerel.setSingleStep(0.01)
		self.scalerel.setDecimals(2)
		self.scalerel.setMaximum(1)
		self.scalerel.setMinimum(-1)
		self.settingsGrid.addWidget(self.scalerel, 6, 2)

		self.scaleLabel = QtWidgets.QLabel()
		self.scaleLabel.setObjectName("scaleLabel")
		self.scaleLabel.setText("scale")
		self.settingsGrid.addWidget(self.scaleLabel, 6, 0)

		self.scaleLabel2 = QtWidgets.QLabel()
		self.scaleLabel2.setObjectName("scaleLabel2")
		self.scaleLabel2.setText("(doesn't currently\ndo anything)")
		self.scaleLabel2.adjustSize()
		self.settingsGrid.addWidget(self.scaleLabel2, 6, 4)

		self.grid.addLayout(self.settingsGrid, 6, 3, 7, 5)

		self.bingrid = QtWidgets.QHBoxLayout()
		self.regridGroup = QtWidgets.QButtonGroup()

		self.noRebin = QtWidgets.QRadioButton()
		self.noRebin.setText('no rebin')
		self.noRebin.setChecked(True)
		self.noRebin.adjustSize()
		self.noRebin.setObjectName('noRebin')
		self.bingrid.addWidget(self.noRebin)
		
		self.linearRebin = QtWidgets.QRadioButton()
		self.linearRebin.setText('linear rebin')
		self.linearRebin.setChecked(False)
		self.linearRebin.adjustSize()
		self.linearRebin.setObjectName('linearRebin')
		self.bingrid.addWidget(self.linearRebin)

		self.exponentialRebin = QtWidgets.QRadioButton()
		self.exponentialRebin.setText('exponential rebin')
		self.exponentialRebin.setChecked(False)
		self.exponentialRebin.adjustSize()
		self.exponentialRebin.setObjectName('exponentialRegrid')
		self.bingrid.addWidget(self.exponentialRebin)

		self.grid.addLayout(self.bingrid, 13, 4, 1, 3)

		self.linearRebinLabel = QtWidgets.QLabel()
		self.linearRebinLabel.setText('linear rebin\ngradient')
		self.linearRebinLabel.adjustSize()
		self.linearRebinLabel.setObjectName('linearRebinLabel')
		self.grid.addWidget(self.linearRebinLabel, 14, 5)
		
		self.linearRebinGradientBox = QtWidgets.QDoubleSpinBox()
		self.linearRebinGradientBox.setObjectName('linearRebinGradientBox')
		self.linearRebinGradientBox.setValue(1.1)
		self.linearRebinGradientBox.setDecimals(2)
		self.linearRebinGradientBox.setMinimum(1.0)
		self.linearRebinGradientBox.setMaximum(5.0)
		self.linearRebinGradientBox.setSingleStep(0.1)
		self.linearRebinGradientBox.setKeyboardTracking(False)
		self.grid.addWidget(self.linearRebinGradientBox, 15,5)

		self.exponentialRebinLabel = QtWidgets.QLabel()
		self.exponentialRebinLabel.setText('exponential\nconstant')
		self.exponentialRebinLabel.adjustSize()
		self.exponentialRebinLabel.setObjectName('exponentialRebinLabel')
		self.grid.addWidget(self.exponentialRebinLabel, 14,6)

		self.exponentialRebinConstant = QtWidgets.QDoubleSpinBox()
		self.exponentialRebinConstant.setObjectName('exponentialRebinConstant')
		self.exponentialRebinConstant.setDecimals(5)
		self.exponentialRebinConstant.setValue(0.0005)
		self.exponentialRebinConstant.setMinimum(0)
		self.exponentialRebinConstant.setMaximum(0.01)
		self.exponentialRebinConstant.setSingleStep(0.0001)
		self.exponentialRebinConstant.setKeyboardTracking(False)
		self.grid.addWidget(self.exponentialRebinConstant, 15,6)

		
		'''
		self.exponentialRebinOrderLabel = QtWidgets.QLabel()
		self.exponentialRebinOrderLabel.setText('exponential\norder')
		self.exponentialRebinOrderLabel.adjustSize()
		self.exponentialRebinOrderLabel.setObjectName('exponentialRebinOrderLabel')

		self.exponentialRebinOrder = QtWidgets.QSpinBox()
		self.exponentialRebinOrder.setObjectName('exponentialRebinOrder')
		self.exponentialRebinOrder.setValue(1)
		self.exponentialRebinOrder.setMinimum(1)
		self.exponentialRebinOrder.setMaximum(5)
		self.exponentialRebinOrder.setSingleStep(1)
		self.exponentialRebinOrder.setKeyboardTracking(False)			
		'''
		self.regridGroup.addButton(self.noRebin)
		self.regridGroup.addButton(self.linearRebin)
		self.regridGroup.addButton(self.exponentialRebin)

		self.plotLabel = QtWidgets.QLabel()
		self.plotLabel.setObjectName("plotLabel")
		self.grid.addWidget(self.plotLabel, 4, 5, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)

		self.plotGrid = QtWidgets.QHBoxLayout()
		self.iqCheckBox = QtWidgets.QCheckBox()
		self.iqCheckBox.setObjectName("iqCheckBox")
		self.plotGrid.addWidget(self.iqCheckBox)
		self.sqCheckBox = QtWidgets.QCheckBox()
		self.sqCheckBox.setObjectName("sqCheckBox")
		self.plotGrid.addWidget(self.sqCheckBox)
		self.fqCheckBox = QtWidgets.QCheckBox()
		self.fqCheckBox.setObjectName("fqCheckBox")
		self.plotGrid.addWidget(self.fqCheckBox)
		self.grCheckBox = QtWidgets.QCheckBox()
		self.grCheckBox.setObjectName("grCheckBox")
		self.plotGrid.addWidget(self.grCheckBox)

		self.grid.addLayout(self.plotGrid, 5, 4, 1, 3)
		
		self.buttongrid = QtWidgets.QGridLayout()
		self.plotButton = QtWidgets.QPushButton()
		self.plotButton.setObjectName("plotButton")
		self.buttongrid.addWidget(self.plotButton,0,0)

		
		self.saveButton = QtWidgets.QPushButton()
		self.saveButton.setObjectName("saveButton")
		self.buttongrid.addWidget(self.saveButton, 0,1)

		self.saveDirButton = QtWidgets.QPushButton()
		self.saveDirButton.setObjectName("saveDirButton")
		self.saveDirButton.setText('run directory')
		self.buttongrid.addWidget(self.saveDirButton, 1,0)

		self.stopSave = QtWidgets.QPushButton()
		self.stopSave.setObjectName("stopSave")
		self.stopSave.setText('stop saving')
		self.stopSave.setEnabled(False)
		self.buttongrid.addWidget(self.stopSave, 1,1)

		self.grid.addLayout(self.buttongrid, 16, 2, 2, 3)

		self.axisCheckBox = QtWidgets.QCheckBox()
		self.axisCheckBox.setObjectName("axisCheckBox")
		self.axisCheckBox.setText("reset axis on update?")
		self.axisCheckBox.adjustSize()
		self.grid.addWidget(self.axisCheckBox, 15, 2)


		self.rsettingGrid = QtWidgets.QGridLayout()
		self.rminBox = QtWidgets.QDoubleSpinBox()
		self.rminBox.setMinimum(0.01)
		self.rminBox.setMaximum(100.0)
		self.rminBox.setSingleStep(0.1)
		self.rminBox.setProperty("value", 0.5)
		self.rminBox.setObjectName("rminBox")
		self.rminBox.setKeyboardTracking(False)
		self.rsettingGrid.addWidget(self.rminBox, 0, 0)

		self.rmaxBox = QtWidgets.QDoubleSpinBox()
		self.rmaxBox.setMinimum(3.0)
		self.rmaxBox.setMaximum(10000.0)
		self.rmaxBox.setProperty("value", 30.0)
		self.rmaxBox.setObjectName("rmaxBox")
		self.rmaxBox.setKeyboardTracking(False)
		self.rsettingGrid.addWidget(self.rmaxBox, 1, 0)

		self.rstepBox = QtWidgets.QDoubleSpinBox()
		self.rstepBox.setDecimals(3)
		self.rstepBox.setMinimum(0.005)
		self.rstepBox.setMaximum(1.0)
		self.rstepBox.setSingleStep(0.01)
		self.rstepBox.setProperty("value", 0.01)
		self.rstepBox.setObjectName("rstepBox")
		self.rstepBox.setKeyboardTracking(False)
		self.rsettingGrid.addWidget(self.rstepBox, 2, 0)
		
		self.rminLabel = QtWidgets.QLabel()
		self.rminLabel.setObjectName("rminLabel")
		self.rsettingGrid.addWidget(self.rminLabel, 0, 1)

		self.rmaxLablel = QtWidgets.QLabel()
		self.rmaxLablel.setObjectName("rmaxLablel")
		self.rsettingGrid.addWidget(self.rmaxLablel, 1, 1)

		self.rstepLabel = QtWidgets.QLabel()
		self.rstepLabel.setObjectName("rstepLabel")
		self.rsettingGrid.addWidget(self.rstepLabel, 2, 1)

		self.grid.addLayout(self.rsettingGrid, 8, 1, 4, 2)

		self.lorchBox = QtWidgets.QCheckBox()
		self.lorchBox.setObjectName('lorchBox')
		self.lorchBox.setText('Lorch termination')
		self.grid.addWidget(self.lorchBox, 13, 0)

		self.stepBox = QtWidgets.QCheckBox()
		self.stepBox.setObjectName('stepBox')
		self.stepBox.setText('step termination')
		self.grid.addWidget(self.stepBox, 13,1)

		self.terminationLabel = QtWidgets.QLabel()
		self.terminationLabel.setObjectName('terminationLabel')
		self.terminationLabel.setText('termination functions (for pdfgetx3 2.4.0+)')
		self.grid.addWidget(self.terminationLabel, 12,0, 1,2)

		self.lorchBox.stateChanged.connect(self.updateTermination)
		self.stepBox.stateChanged.connect(self.updateTermination)
		
		self.errorMessageLabel = QtWidgets.QLabel()
		self.errorMessageLabel.setObjectName('errorMessageLabel')

		self.grid.addWidget(self.errorMessageLabel, 15, 0, 2,2)





		
		self.centralwidget.setLayout(self.grid)
		self.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(self)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 702, 26))
		self.menubar.setObjectName("menubar")
		self.menuFile = QtWidgets.QMenu(self.menubar)
		self.menuFile.setObjectName("menuFile")
		self.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(self)
		self.statusbar.setObjectName("statusbar")
		self.setStatusBar(self.statusbar)
		self.actionOpen = QtGui.QAction(self)
		self.actionOpen.setObjectName("actionOpen")
		self.menuFile.addAction(self.actionOpen)
		self.menubar.addAction(self.menuFile.menuAction())
		#self.retranslateUi()

		self.setWindowTitle( "PDFgetX3GUI")
		self.fileLabel.setText( "file")
	
		self.bkgscaleLabel.setText( "background\nscale")
		#self.bkgscaleLabel.adjustSize()
		self.rpolyLabel.setText( "rpoly")
		self.QminLabel.setText( "Qmin")
		self.QmaxLabel.setText( "Qmax")
		self.qmaxinstLabel.setText( "Qmax inst")
	
		self.fileListLabel.setText( "File list")
		self.compositionBox.setText( "LaB6")
		self.wavelengthBox.setText( "0.270793")
		self.compositionLabel.setText( "composition")
		self.bkgfilebutton.setText( "...")
		self.removeButton.setText( "remove from list")
		self.iqCheckBox.setText( "I(Q)")
		self.sqCheckBox.setText( "S(Q)")
		self.fqCheckBox.setText( "F(Q)")
		self.saveButton.setText( "Save")
		self.plotLabel.setText( "Plot")
		self.grCheckBox.setText( "G(r)")
		self.fileButton.setText( "...")
		self.fileButton.setShortcut( "Ctrl+O")
		self.QButton.setText( "Q (\u00C5\u207B\u00B9)")
		self.twothetaButton.setText( "2theta (\u00B0)")
		self.wavelengthLabel.setText( "wavelength")
		self.plotButton.setText( "Plot")
		self.inputFormatLabel.setText( "Input format")
		self.menuFile.setTitle( "File")
		self.actionOpen.setText( "Open")
		self.actionOpen.setShortcut( "Ctrl+O")
		self.rminLabel.setText( "rmin (\u00C5)")
		self.rmaxLablel.setText( "rmax (\u00C5)")
		self.rstepLabel.setText( "rstep (\u00C5)")

		QtCore.QMetaObject.connectSlotsByName(self)
		
		
		self.fig = None
		self.ax = None
		self.noplots = 0
		self.dataformat = None
		self.plotlist = []

		self.iqcheck = None
		self.sqcheck = None
		self.fqcheck = None
		self.grcheck = None
		self.plotted = False
		
		self.qmaxbox.setMaximum(self.qmaxinstbox.value())
		self.actionOpen.triggered.connect(self.open_file)
		self.fileButton.clicked.connect(self.open_file)
		self.bkgfilebutton.clicked.connect(self.open_bkgfile)
		self.removeButton.clicked.connect(self.removeFile)
		self.bkgremoveButton.clicked.connect(self.removeBkgFile)
		self.saveButton.clicked.connect(self.saveFile)
		self.saveButton.clicked.connect(self.write_iq_file)

		self.running = False
		self.fileList = []
		self.bkgfileList = []
		if self.filename.text():
			self.fileList.append(self.filename.text())
			self.filelistBox.addItem('')
			self.filelistBox.setItemText(self.filelistBox.count()-1,os.path.basename(self.filename.text()))
			self.filelistBox.setCurrentIndex(self.filelistBox.count()-1)

		if self.bkgfilename.text():
			self.bkgfileList.append(self.bkgfilename.text())
			self.bkgfilelistBox.addItem(os.path.basename(self.bkgfilename.text()))
			#self.bkgfilelistBox.setItemText(self.bkgfilelistBox.count()-1,os.path.basename(self.bkgfilename.text()))
			#self.bkgfilelistBox.setCurrentIndex(self.bkgfilelistBox.count()-1)

		self.plotButton.clicked.connect(self.updateConfigFile)
		self.plotButton.clicked.connect(self.startWorker)


		self.updateParamDct()
		
		self.configFile = f'{self.configfilepath}/pdfConfigFile.dat'
		self.fileListFile = f'{self.configfilepath}/pdfFileList.dat'
		self.bkgfileListFile = f'{self.configfilepath}/pdfBkgFileList.dat'
		if os.path.exists(self.configFile):
			self.readConfigFile()
			
		if os.path.exists(self.fileListFile):
			self.readFileconfig()
		self.filelistBox.currentTextChanged.connect(self.changeFile)
		self.bkgfilelistBox.currentTextChanged.connect(self.bkgchangeFile)
		


		self.bkgscalebox.valueChanged.connect(self.updateBkgscale)
		self.rminBox.valueChanged.connect(self.updateRmin)
		self.rmaxBox.valueChanged.connect(self.updateRmax)
		self.rstepBox.valueChanged.connect(self.updateRstep)
		self.qminbox.valueChanged.connect(self.updateQmin)
		self.qminbox.valueChanged.connect(self.setQmax_lims)
		self.qmaxbox.valueChanged.connect(self.updateQmax)
		self.qmaxinstbox.valueChanged.connect(self.setQmax_lims)
		self.qmaxinstbox.valueChanged.connect(self.updateQmaxinst)
		self.rpolybox.valueChanged.connect(self.updateRpoly)
		self.linearRebinGradientBox.valueChanged.connect(self.updatexy)
		self.exponentialRebinConstant.valueChanged.connect(self.updatexy)
		self.scaleBox.valueChanged.connect(self.runUpdate)

		self.bkgscalebox.valueChanged.connect(self.updateConfigFile)
		self.rminBox.valueChanged.connect(self.updateConfigFile)
		self.rmaxBox.valueChanged.connect(self.updateConfigFile)
		self.rstepBox.valueChanged.connect(self.updateConfigFile)
		self.compositionBox.textChanged.connect(self.updateConfigFile)
		self.qminbox.valueChanged.connect(self.updateConfigFile)
		self.qmaxbox.valueChanged.connect(self.updateConfigFile)
		self.qmaxinstbox.valueChanged.connect(self.updateConfigFile)
		self.rpolybox.valueChanged.connect(self.updateConfigFile)
		self.qmaxinstbox.valueChanged.connect(self.updateConfigFile)
		self.iqCheckBox.clicked.connect(self.updateConfigFile)
		self.sqCheckBox.clicked.connect(self.updateConfigFile)
		self.fqCheckBox.clicked.connect(self.updateConfigFile)
		self.grCheckBox.clicked.connect(self.updateConfigFile)
		self.QButton.clicked.connect(self.updateConfigFile)
		self.twothetaButton.clicked.connect(self.updateConfigFile)
		self.qmaxtogether.clicked.connect(self.updateConfigFile)
		self.linearRebinGradientBox.valueChanged.connect(self.updateConfigFile)
		self.exponentialRebinConstant.valueChanged.connect(self.updateConfigFile)
		self.linearRebin.clicked.connect(self.updatexy)
		self.exponentialRebin.clicked.connect(self.updatexy)
		self.noRebin.clicked.connect(self.stopRebin)
		self.noRebin.clicked.connect(self.updateConfigFile)
		self.linearRebin.clicked.connect(self.updateConfigFile)
		self.exponentialRebin.clicked.connect(self.updateConfigFile)

		self.bkgscalerel.setKeyboardTracking(False)
		self.bkgscalerel.valueChanged.connect(lambda: self.changeStep(self.bkgscalebox))
		self.qminrel.setKeyboardTracking(False)
		self.qminrel.valueChanged.connect(lambda: self.changeStep(self.qminbox))
		self.qmaxrel.setKeyboardTracking(False)
		self.qmaxrel.valueChanged.connect(lambda: self.changeStep(self.qmaxbox))
		self.qmaxinstrel.setKeyboardTracking(False)
		self.qmaxinstrel.valueChanged.connect(lambda: self.changeStep(self.qmaxinstbox))
		self.rpolyrel.setKeyboardTracking(False)
		self.rpolyrel.valueChanged.connect(lambda: self.changeStep(self.rpolybox))
		self.saveDirButton.clicked.connect(self.saveAll)
		self.stopSave.clicked.connect(self.stop_worker2)

	


	def startWorker(self):
		self.plotted = False
		if self.running:
			plt.close()
			self.thread.stop()
		
		inputfile=self.filename.text()
		x,y = loadData(inputfile)
		if self.noRebin.isChecked():
			xrebin = None
			yrebin = None
		else:
			xrebin,yrebin = self.qRebin(x,y)
		bkgfile= self.updatebkgfile()
		bkgscale=self.bkgscalebox.value()
		composition = self.compositionBox.text()
		qmin=self.qminbox.value()
		qmax=self.qmaxbox.value()
		qmaxinst=self.qmaxinstbox.value()
		rpoly=self.rpolybox.value()
		rmin = self.rminBox.value()
		rmax = self.rmaxBox.value()
		rstep = self.rstepBox.value()
		wavelength = float(self.wavelengthBox.text())
		terminationfunctions = self.terminationfunctionlist()

		if self.QButton.isChecked():
			dataformat = 'QA'
			self.qmaxinstbox.setMaximum(x[-1])
		elif self.twothetaButton.isChecked():
			dataformat = 'twotheta'
			self.qmaxinstbox.setMaximum(4*np.pi*np.sin(x[-1]*np.pi/(2*180))/wavelength)

		self.iqcheck = self.iqCheckBox.isChecked()
		self.sqcheck = self.sqCheckBox.isChecked()
		self.fqcheck = self.fqCheckBox.isChecked()
		self.grcheck = self.grCheckBox.isChecked()
		self.plotlist = np.array([self.iqcheck,self.sqcheck,self.fqcheck,self.grcheck])
		self.noplots = len(self.plotlist[self.plotlist==True])


		
		if len(self.plotlist[self.plotlist == True])==0:
			message = 'no outputs selected to plot'
			print(message)
			self.errorMessage(message)
			self.running = False
			return
		self.errorMessage('')

		self.fig,self.ax = plt.subplots(self.noplots,1,dpi = 150)

		if self.QButton.isChecked():
			self.dataformat = 'QA'
		elif self.twothetaButton.isChecked():
			self.dataformat = 'twotheta'
		self.running = True

		self.thread = Worker(file = inputfile, bkgfile = bkgfile, bkgscale = bkgscale, composition = composition, dataformat= dataformat,
		qmin = qmin, qmax = qmax, qmaxinst = qmaxinst, rpoly = rpoly, rmin = rmin, rmax = rmax, rstep = rstep, wavelength = wavelength, 
		x = xrebin,	y = yrebin, terminationfunctions=terminationfunctions)
		
		self.thread.start()
		self.thread.outputs.connect(self.plotUpdate)
		



	def plotUpdate(self,outputs: list):
		if len(outputs) >1:
			self.qi,self.iq,self.bkg,self.q,self.sq,self.fq,self.r, self.gr = outputs
		elif len(outputs) == 1:
			self.errorMessage(outputs[0])
			del self.fig
			del self.ax
			return
		plt.ion()
		self.errorMessage('')
		plotDct = {'I(Q)':[self.qi,self.iq,'Q (\u00C5$^{-1}$)',self.plotlist[0]],
					'S(Q)': [self.q,self.sq,'Q (\u00C5$^{-1}$)',self.plotlist[1]],
					'F(Q)': [self.q,self.fq,'Q (\u00C5$^{-1}$)',self.plotlist[2]],
					'G(r)': [self.r,self.gr,'r (\u00C5)',self.plotlist[3]]}
		grscale = self.gr*self.scaleBox.value()
		if not self.plotted:	
			self.q0 = self.q
			self.sq0 = self.sq
			self.fq0 = self.fq
			self.gr0 = grscale #self.gr
			self.r0 = self.r
		
		holdAxes = self.plotted and self.noplots != 1 and not self.axisCheckBox.isChecked()
		if holdAxes:
			#get plot limits so updates don't reset axes
			xlims = {}
			ylims = {}
			plotno = 0
			
			for c,plot in enumerate(self.plotlist):
				if not plot:
					continue
				if c == 0:
					xlims['iq'] = self.ax[plotno].get_xlim()
					ylims['iq'] = self.ax[plotno].get_ylim()
				elif c == 1:
					xlims['sq'] = self.ax[plotno].get_xlim()
					ylims['sq'] = self.ax[plotno].get_ylim()
				elif c == 2:
					xlims['fq'] = self.ax[plotno].get_xlim()
					ylims['fq'] = self.ax[plotno].get_ylim()
				elif c == 3:
					xlims['gr'] = self.ax[plotno].get_xlim()
					ylims['gr'] = self.ax[plotno].get_ylim()
				plotno += 1

		linethickness = 1
		tranparency0 = 0.5
		
		if self.noplots == 1:
			self.ax.cla()
			for item in plotDct:
				if plotDct[item][-1]:
					x = plotDct[item][0]
					y = plotDct[item][1]
					if item == 'S(Q)':
						self.ax.plot(self.q0,self.sq0,alpha = tranparency0, color = 'gray')
					elif item == 'F(Q)':
						self.ax.plot(self.q0,self.fq0,alpha = tranparency0, color = 'gray')
					elif item == 'G(r)':
						self.ax.plot(self.r0,self.gr0,alpha = tranparency0, color = 'gray')
						y = grscale
						atomdensity = self.atomDensityBox.value()
						densityExtent = self.atomDensityExtent.value()
						atomr = np.array([0,densityExtent])
						atomDensityPlot = -4*np.pi*atomdensity*atomr
						self.ax.plot(atomr, atomDensityPlot, '--', color = 'tab:orange')

						
					self.ax.plot(x,y,label = 'measured',linewidth = linethickness)
					if item == 'I(Q)':
						self.ax.plot(x,self.bkg, label = 'background',linewidth = linethickness)
						self.ax.plot(x,y-self.bkg,label = 'difference',linewidth = linethickness)
						self.ax.legend()
					
					self.ax.set_xlabel(plotDct[item][2])
					self.ax.set_xlim(x[0],x[-1])
					self.ax.set_ylabel(item)
		else:
			for n in range(self.noplots):
				self.ax[n].cla()

			plotno = 0
			
			for c,plot in enumerate(self.plotlist):
				if not plot:
					continue
				if c == 0:
					self.ax[plotno].plot(self.qi,self.iq,label = 'total scattering',linewidth = linethickness)
					self.ax[plotno].plot(self.qi,self.bkg,label = 'background',linewidth = linethickness)
					self.ax[plotno].plot(self.qi,self.iq-self.bkg,label = 'difference',linewidth = linethickness)
					if not self.plotlist[1] and not self.plotlist[2]:
						self.ax[plotno].set_xlabel('Q (\u00C5$^{-1}$)')
					self.ax[plotno].set_ylabel('Intensity')
					self.ax[plotno].legend()
					if holdAxes:
						self.ax[plotno].set_xlim(*xlims['iq'])
						self.ax[plotno].set_ylim(*ylims['iq'])
					else:
						self.ax[plotno].set_xlim(self.qi[0],self.qi[-1])
					self.ax[plotno].xaxis.set_label_coords(0.5,-0.08)

				elif c == 1:
					self.ax[plotno].plot(self.q0,self.sq0*((np.max(self.sq)-np.min(self.sq))/(np.max(self.sq0)-np.min(self.sq0))), 
			  alpha = tranparency0, color = 'gray')
					self.ax[plotno].plot(self.q,self.sq,linewidth = linethickness)
					if not self.plotlist[2]:
						self.ax[plotno].set_xlabel('Q (\u00C5$^{-1}$)')
					self.ax[plotno].set_ylabel('S(Q)')
					
					if holdAxes:
						self.ax[plotno].set_xlim(*xlims['sq'])
						self.ax[plotno].set_ylim(*ylims['sq'])
					else:
						self.ax[plotno].set_xlim(self.q[0],self.q[-1])
					self.ax[plotno].xaxis.set_label_coords(0.5,-0.08)

				elif c == 2:
					self.ax[plotno].plot(self.q0,self.fq0*((np.max(self.fq)-np.min(self.fq))/(np.max(self.fq0)-np.min(self.fq0))), 
			  alpha = tranparency0, color = 'gray',  markersize = 2)
					self.ax[plotno].plot(self.q,self.fq,linewidth = linethickness, markersize = 2)
					self.ax[plotno].set_xlabel('Q (\u00C5$^{-1}$)')
					self.ax[plotno].set_ylabel('F(Q)')
					
					
					if holdAxes:
						self.ax[plotno].set_xlim(*xlims['fq'])
						self.ax[plotno].set_ylim(*ylims['fq'])
					else:
						self.ax[plotno].set_xlim(self.q[0],self.q[-1])
					self.ax[plotno].xaxis.set_label_coords(0.5,-0.08)

				elif c == 3:
					self.ax[plotno].plot(self.r0,self.gr0*((np.max(self.gr)-np.min(self.gr))/(np.max(self.gr0)-np.min(self.gr0))), 
			  		alpha = tranparency0, color = 'gray')
					
					self.ax[plotno].plot(self.r,grscale,linewidth = linethickness)
					self.ax[plotno].set_xlabel('r (\u00C5)')
					self.ax[plotno].set_ylabel('G(r)')
					atomdensity = self.atomDensityBox.value()
					densityExtent = self.atomDensityExtent.value()
					atomr = np.array([0,densityExtent])
					atomDensityPlot = -4*np.pi*atomdensity*atomr
					self.ax[plotno].plot(atomr, atomDensityPlot, '--')
					
					if holdAxes:
						self.ax[plotno].set_xlim(*xlims['gr'])
						self.ax[plotno].set_ylim(*ylims['gr'])
					else:
						self.ax[plotno].set_xlim(self.r[0],self.r[-1])	
					self.ax[plotno].xaxis.set_label_coords(0.5,-0.08)			
				plotno += 1

		plt.subplots_adjust(top = 0.99, bottom = 0.07, right = 0.99, left = 0.07, 
            hspace = 0.2, wspace = 0)
		if not self.plotted:
			self.fig.show()
		self.plotted = True
		#plt.pause(0.01)
		time.sleep(0.01)

		#self.centralwidget.activateWindow()

	def qRebin(self, q, intensity):
		if self.noRebin.isChecked():
			return q, intensity
		
		qspacing = (q[-1] - q[0])/(len(q)-1)
		qovergrid = np.arange(q[0],q[-1], qspacing/15)
		regridfunc = interp1d(q,intensity) #from scipy
		intovergrid = regridfunc(qovergrid)
		if self.linearRebin.isChecked():
			gradient = self.linearRebinGradientBox.value()
			newq = np.array([qn*gradient - (q[0]*gradient - q[0]) for qn in q if qn*gradient - (q[0]*gradient - q[0])  < q[-1]])
		elif self.exponentialRebin.isChecked():
			power = 1 #self.exponentialRebinOrder.value()
			exponent = self.exponentialRebinConstant.value()
			newq = np.array([qn*np.exp((exponent*i)**power) for i,qn in enumerate(q) if qn*np.exp((exponent*i)**power) < q[-1]])

		newint = np.array([])
		for n in range(len(newq)):
			if n == 0:
				qminval = newq[n]
			else:
				qminval = (newq[n] + newq[n-1])/2
			if n == len(newq)-1:
				qmaxval = newq[n]
			else:
				qmaxval = (newq[n+1] + newq[n])/2
			qominindex = np.abs(qovergrid - qminval).argmin()
			qomaxindex = np.abs(qovergrid - qmaxval).argmin()
			intensityn = np.average(intovergrid[qominindex:qomaxindex])
			newint = np.append(newint,intensityn)
		newqmaxindex = np.abs(q-newq[-1]).argmin()
		regridfunc2 = interp1d(newq,newint)
		newintRG = regridfunc2(q[1:newqmaxindex])

		return q[1:newqmaxindex], newintRG
	
	def saveAll(self):
		inputfile = self.filename.text()
		bkgfile= self.updatebkgfile()
		bkgscale=self.bkgscalebox.value()
		composition = self.compositionBox.text()
		qmin=self.qminbox.value()
		qmax=self.qmaxbox.value()
		qmaxinst=self.qmaxinstbox.value()
		if self.QButton.isChecked():
			dataformat = 'QA'
		elif self.twothetaButton.isChecked():
			dataformat = 'twotheta'

		rpoly=self.rpolybox.value()
		rmin = self.rminBox.value()
		rmax = self.rmaxBox.value()
		rstep = self.rstepBox.value()
		wavelength = float(self.wavelengthBox.text())
		#self.saveDirButton.setEnabled(False)
		self.thread2 = SaveDirWorker(inputfile,bkgfile,bkgscale,composition,qmin,qmax,qmaxinst,rpoly,dataformat,rmin,rmax, rstep, wavelength)
		self.thread2.start()
		self.saveDirButton.setEnabled(False)
		self.stopSave.setEnabled(True)
		self.thread2.outputs.connect(self.swapSaveButtons)

	
	def swapSaveButtons(self, setting):
		self.saveDirButton.setEnabled(setting)
		self.stopSave.setEnabled(not setting)

	def twothetaoffset(self,x):
		ttho = 0
		if ttho < 10**(-5) or self.QButton.isChecked():
			return x
		else:
			return x - ttho
		
	def updateParamDct(self):
		self.paramDct = {self.filename.objectName(): [self.filename,self.filename.text()],
					self.bkgfilename.objectName(): [self.bkgfilename, self.bkgfilename.text()],
					self.compositionBox.objectName(): [self.compositionBox, self.compositionBox.text()],
					self.wavelengthBox.objectName(): [self.wavelengthBox,self.wavelengthBox.text()],
					self.filelistBox.objectName(): [self.filelistBox,','.join([self.filelistBox.itemText(i) for 
					i in range(self.filelistBox.count())])],
					self.bkgfilelistBox.objectName(): [self.bkgfilelistBox,','.join([self.bkgfilelistBox.itemText(i) for 
					i in range(self.bkgfilelistBox.count())])],
					self.QButton.objectName():  [self.QButton, str(self.QButton.isChecked())],
					self.twothetaButton.objectName(): [self.twothetaButton, str(self.twothetaButton.isChecked())],
					self.iqCheckBox.objectName(): [self.iqCheckBox,str(self.iqCheckBox.isChecked())],
					self.sqCheckBox.objectName(): [self.sqCheckBox,str(self.sqCheckBox.isChecked())],
					self.fqCheckBox.objectName(): [self.fqCheckBox, str(self.fqCheckBox.isChecked())],
					self.grCheckBox.objectName(): [self.grCheckBox, str(self.grCheckBox.isChecked())],
					self.rminBox.objectName(): [self.rminBox, self.rminBox.value()],
					self.rmaxBox.objectName(): [self.rmaxBox,self.rmaxBox.value()],
					self.rstepBox.objectName(): [self.rstepBox,self.rstepBox.value()],
					self.bkgscalebox.objectName(): [self.bkgscalebox, self.bkgscalebox.value()],
					self.qminbox.objectName(): [self.qminbox,self.qminbox.value()],
					self.qmaxinstbox.objectName(): [self.qmaxinstbox, self.qmaxinstbox.value()],
					self.qmaxbox.objectName(): [self.qmaxbox, self.qmaxbox.value()],
					self.rpolybox.objectName(): [self.rpolybox, self.rpolybox.value()],
					self.bkgscalerel.objectName(): [self.bkgscalerel,self.bkgscalerel.value()],
					self.qminrel.objectName(): [self.qminrel,self.qminrel.value()],
					self.qmaxrel.objectName(): [self.qmaxrel,self.qmaxrel.value()],
					self.qmaxinstrel.objectName(): [self.qmaxinstrel, self.qmaxinstrel.value()],
					self.rpolyrel.objectName(): [self.rpolyrel,self.rpolyrel.value()],
					self.qmaxtogether.objectName(): [self.qmaxtogether, str(self.qmaxtogether.isChecked())],
					self.axisCheckBox.objectName(): [self.axisCheckBox, str(self.axisCheckBox.isChecked())],
					self.noRebin.objectName(): [self.noRebin, str(self.noRebin.isChecked())],
					self.linearRebin.objectName(): [self.linearRebin, str(self.linearRebin.isChecked())],
					self.exponentialRebin.objectName(): [self.exponentialRebin, str(self.exponentialRebin.isChecked())],
					self.linearRebinGradientBox.objectName():[self.linearRebinGradientBox, self.linearRebinGradientBox.value()],
					self.exponentialRebinConstant.objectName(): [self.exponentialRebinConstant, self.exponentialRebinConstant.value()] }
	def open_file(self):
		filter = "data file (*.txt *.dat *.xy *.xye *.csv)"
		dialog = QtWidgets.QFileDialog.getOpenFileName(caption = 'select data file', filter = filter,
		directory=os.path.dirname(self.filename.text()))

		basefilename = os.path.basename(dialog[0])
		
		if dialog[0] != '':
			self.filename.setText(dialog[0])
			self.fileList.append(dialog[0])
			self.filelistBox.addItem('')
			self.filelistBox.setItemText(self.filelistBox.count()-1,basefilename)
			self.filelistBox.setCurrentIndex(self.filelistBox.count()-1)
		self.updateFileConfig()
		self.updateConfigFile()

	def changeFile(self):
		fileindex = self.filelistBox.currentIndex()
		newfile = self.fileList[fileindex]
		self.filename.setText(newfile)
		self.updateConfigFile()
	

	def removeFile(self):
		if len(self.fileList) > 1:
			fileindex = self.filelistBox.currentIndex()
			self.filelistBox.removeItem(fileindex)
			self.fileList.pop(fileindex)
			self.changeFile()
			self.updateFileConfig()
			self.updateConfigFile()
			self.errorMessage('')
		else:
			message = 'can\'t remove last file'
			print(message)
			self.errorMessage(message)

	def removeBkgFile(self):
		if len(self.bkgfileList) > 1:
			fileindex = self.bkgfilelistBox.currentIndex()
			self.bkgfilelistBox.removeItem(fileindex)
			self.bkgfileList.pop(fileindex)
			self.bkgchangeFile()
			self.updateBkgFileConfig()
			self.updateConfigFile()
			self.errorMessage('')
		else:
			print('can\'t remove last file')
			message = 'can\'t remove last file'
			print(message)
			self.errorMessage(message)
	def open_bkgfile(self):
		#dialog.setFileMode(QtWidgets.QFileDialog.AnyFile)
		filter = "data file (*.txt *.dat *.xy *.xye *.csv)"
		dialog = QtWidgets.QFileDialog.getOpenFileName(caption = 'select background file',	filter = filter,
		directory=os.path.dirname(self.bkgfilename.text()))
		if dialog[0] != '':
			self.bkgfileList.append(dialog[0])
			basefilename = os.path.basename(dialog[0])
			self.bkgfilename.setText(dialog[0])
			self.bkgfilelistBox.addItem('')
			self.bkgfilelistBox.setItemText(self.bkgfilelistBox.count()-1,basefilename)
			self.bkgfilelistBox.setCurrentIndex(self.bkgfilelistBox.count()-1)
		self.updateBkgFileConfig()
		self.updateConfigFile()

	def bkgchangeFile(self):
		fileindex = self.bkgfilelistBox.currentIndex()
		newfile = self.bkgfileList[fileindex]
		self.bkgfilename.setText(newfile)
		self.updateBkgFileConfig()
		self.updateConfigFile()

	def saveFile(self):
		if not self.plotted:
			self.errorMessage('data not plotted/calculated yet, files not saved')
			return
		if len(self.plotlist[self.plotlist == True])==0:
			print('no outputs selected to save')
			self.errorMessage('no outputs selected to save')
			return
		try:
			pdffunctions.writeOutput(file=self.filename.text(),bkgfile=self.bkgfilename.text(),bkgscale=self.bkgscalebox.value(),
		composition = self.compositionBox.text(),qmin=self.qminbox.value(),qmax=self.qmaxbox.value(),qmaxinst=self.qmaxinstbox.value(),
		rpoly=self.rpolybox.value(),dataformat = self.dataformat, rmin = self.rminBox.value(), rmax = self.rmaxBox.value(),
		rstep = self.rstepBox.value(),wavelength = float(self.wavelengthBox.text()),iqcheck = self.iqcheck, sqcheck = self.sqcheck, 
		fqcheck = self.fqcheck, grcheck = self.grcheck)
		except PermissionError as p:
			print(p)
			print('file not saved')
			self.errorMessage('permission error, file not saved')
			return
		

		self.errorMessage('')

	def setQmax_lims(self):
		self.qmaxbox.setMaximum(self.qmaxinstbox.value())
		self.qmaxbox.setMinimum(self.qminbox.value()+1)
		self.qmaxinstbox.setMinimum(self.qminbox.value()+1)

	def changeStep(self,parameter):
		relParamDct = {self.bkgscalebox:self.bkgscalerel,
					   self.qminbox:self.qminrel,
					   self.qmaxbox:self.qmaxrel,
					   self.qmaxinstbox:self.qmaxinstrel,
					   self.rpolybox:self.rpolyrel}
		parameter.setSingleStep(relParamDct[parameter].value())

	def stop_worker(self):
		self.thread.stop()
	
	def stop_worker2(self):
		self.thread2.stop()
		self.saveDirButton.setEnabled(True)
		self.stopSave.setEnabled(False)

	def write_iq_file(self):
		if self.iqcheck:
			basename = os.path.splitext(self.filename.text())[0]
			outfile = f'{basename}.iq'
			iqsub = self.iq-self.bkg
			print(f'writing {outfile}')
			try:
				np.savetxt(outfile,np.array([self.qi,iqsub]).transpose())
			except PermissionError as p:
				print(p)
				print('file not saved')
				self.errorMessage('permission error, file not saved')
				return
			if self.twothetaButton.isChecked():
				outfilexy = f'{basename}_bkgsub.xy'
				print(f'writing {outfilexy}')
				twotheta = 2*np.arcsin(float(self.wavelengthBox.text())*self.qi/(4*np.pi))*180/np.pi
				try:
					np.savetxt(outfilexy,np.array([twotheta,iqsub]).transpose())
				except PermissionError as p:
					print(p)
					print('file not saved')
					self.errorMessage('permission error, file not saved')
					return
			self.errorMessage('')			
	def updateQmin(self):
		if self.running:
			self.thread.qmin = self.qminbox.value()
			self.thread.repeat = True

	def updateQmax(self):
		if self.qmaxtogether.isChecked():
			self.qmaxinstbox.setValue(self.qmaxbox.value())
		if self.running:
			self.thread.qmax = self.qmaxbox.value()
			self.thread.repeat = True

	def updateQmaxinst(self):
		if self.qmaxtogether.isChecked():
			self.qmaxbox.setValue(self.qmaxinstbox.value())
		if self.running:
			self.thread.qmaxinst = self.qmaxinstbox.value()
			self.thread.repeat = True

	def updateRmax(self):
		if self.running:
			self.thread.rmax = self.rmaxBox.value()
			self.thread.repeat = True
	def updateRmin(self):
		if self.running:
			self.thread.rmin = self.rminBox.value()
			self.thread.repeat = True		
	def updateRstep(self):
		if self.running:
			self.thread.rstep = self.rstepBox.value()
			self.thread.repeat = True
	def updateRpoly(self):
		if self.running:
			self.thread.rpoly = self.rpolybox.value()
			self.thread.repeat = True
	def updateBkgscale(self):
		if self.running:
			self.thread.bkgscale = self.bkgscalebox.value()
			self.thread.repeat = True
	def updateComposition(self):
		if self.running:
			self.thread.composition = self.compositionBox.text()
			self.thread.repeat = True
	def updatexy(self):
		
		if self.running and not self.noRebin.isChecked():

			#x,y = np.loadtxt(self.filename.text(),unpack=True,usecols=(0,1),comments='#')
			x,y = loadData(self.filename.text())
			self.thread.x, self.thread.y = self.qRebin(x,y)
			newbkgfile = self.updatebkgfile()
			self.thread.bkgfile = newbkgfile
			self.thread.repeat = True

	def updatebkgfile(self):
		bkgfile = self.bkgfilename.text()
		if not self.noRebin.isChecked():
			#xback, yback = np.loadtxt(bkgfile,comments = '#', unpack = True, usecols = (0,1))
			xback, yback = loadData(bkgfile)
			xbrebin,ybrebin = self.qRebin(xback,yback)
			if not os.path.exists('tmp/'):
				os.makedirs('tmp/')
			tmpbkgfile = 'tmp/tmp_bkg.xy'
			np.savetxt(tmpbkgfile,np.array([xbrebin,ybrebin]).transpose(),fmt = '%.6f')
			return tmpbkgfile
		else:
			return bkgfile
	def terminationfunctionlist(self):
		tdct = {self.lorchBox: 'lorch', self.stepBox:'step'}
		return [tdct[key] for key in tdct if key.isChecked()]
	def updateTermination(self):
		if self.running:
			if not pdffunctions.versionCheck():
				print(f'termination functions not avaiable in PDFgetX3 {pgxversion} (need 2.4.0+)')
			tfunctions = self.terminationfunctionlist()
			self.thread.terminationfunctions = tfunctions

			self.thread.repeat = True
	def stopRebin(self):
		if self.running and self.noRebin.isChecked():
			self.thread.x = None
			self.thread.y = None
			self.thread.repeat = True
			self.thread.bkgfile = self.bkgfilename.text()
	
	def updateConfigFile(self):

		self.updateParamDct()
		string = ''
		for item in self.paramDct:
			newline = f'{item}: {self.paramDct[item][1]}'
			if not newline.endswith('\n'):
				newline += '\n'
			string += newline
		f = open(self.configFile,'w')
		f.write(string)
		f.close()
	def runUpdate(self):
		if self.running:
			self.thread.repeat = True

	def readConfigFile(self):
		f = open(self.configFile,'r')
		lines = f.readlines()
		f.close()
		for line in lines:
			line = line.replace('\n','')
			linesplit = line.split(': ')
			widgetname = linesplit[0]
			widgetvalue = linesplit[1]

			if type(self.paramDct[widgetname][0]) == QtWidgets.QDoubleSpinBox:
				self.paramDct[widgetname][0].setValue(float(widgetvalue))
				if 'qmax' in widgetname:
					self.setQmax_lims()
			elif type(self.paramDct[widgetname][0]) == QtWidgets.QLineEdit:
				self.paramDct[widgetname][0].setText(widgetvalue)
			elif type(self.paramDct[widgetname][0]) == QtWidgets.QCheckBox or type(self.paramDct[widgetname][0]) == QtWidgets.QRadioButton:
				self.paramDct[widgetname][0].setChecked(text_to_bool(widgetvalue))
			'''
			elif type(self.paramDct[widgetname][0]) == QtWidgets.QComboBox:
				widgetlist = widgetvalue.split(',')
				for item in widgetlist:
					self.paramDct[widgetname][0].addItem('')
					self.paramDct[widgetname][0].setItemText(self.filelistBox.count()-1,widgetname)
					self.paramDct[widgetname][0].setCurrentIndex(self.filelistBox.count()-1)
			'''
		self.setQmax_lims()
		self.bkgscalebox.setSingleStep(self.bkgscalerel.value())
		self.qminbox.setSingleStep(self.qminrel.value())
		self.qmaxbox.setSingleStep(self.qmaxrel.value())
		self.qmaxinstbox.setSingleStep(self.qmaxinstrel.value())
		self.rpolybox.setSingleStep(self.rpolyrel.value())

	def readFileconfig(self):
		f = open(self.fileListFile,'r')
		lines = f.readlines()
		f.close()
		self.fileList = []
		self.filelistBox.clear()
		self.bkgfileList = []
		self.bkgfilelistBox.clear()
		for line in lines:
			line = line.replace('\n','')
			self.fileList.append(line)
			basefilename = os.path.basename(line)
			self.filelistBox.addItem('')
			self.filelistBox.setItemText(self.filelistBox.count()-1,basefilename)
			self.filelistBox.setCurrentIndex(self.filelistBox.count()-1)
		currentFile = self.filename.text()
		startIndex = self.fileList.index(currentFile)
		self.filelistBox.setCurrentIndex(startIndex)

		if not os.path.exists(self.bkgfileListFile):
			return
		f = open(self.bkgfileListFile,'r')
		lines = f.readlines()
		f.close()
		for line in lines:
			line = line.replace('\n','')
			self.bkgfileList.append(line)
			basefilename = os.path.basename(line)
			self.bkgfilelistBox.addItem('')
			self.bkgfilelistBox.setItemText(self.bkgfilelistBox.count()-1,basefilename)
			self.bkgfilelistBox.setCurrentIndex(self.bkgfilelistBox.count()-1)
		currentbkgFile = self.bkgfilename.text()
		startbkgIndex = self.bkgfileList.index(currentbkgFile)
		self.bkgfilelistBox.setCurrentIndex(startbkgIndex)
	def updateFileConfig(self):
		string = ''
		for item in self.fileList:
			string += f'{item}\n'
		f = open(self.fileListFile,'w')
		f.write(string)
		f.close()
	def updateBkgFileConfig(self):
		string = ''
		for item in self.bkgfileList:
			string += f'{item}\n'
		f = open(self.bkgfileListFile,'w')
		f.write(string)
		f.close()

	def errorMessage(self,message):
		self.errorMessageLabel.setText(message)
		self.errorMessageLabel.adjustSize()

	def closeEvent(self, a0):
		plt.close()
		return super().closeEvent(a0)


def main():
	app = QtWidgets.QApplication(sys.argv)
	ui = Ui_MainWindow()
	ui.setupUi()
	ui.show()
	sys.exit(app.exec())

if __name__ == "__main__":
	main()
	


