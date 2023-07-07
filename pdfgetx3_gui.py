# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'guilayout.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# GUI by Kenneth Marshall, PDFGetX3 was made by Simon Billinge and Pavol Juhás


from PyQt5 import QtCore, QtWidgets, QtGui
import os
import pdffunctions
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import time
from scipy.interpolate import interp1d
matplotlib.rcParams.update({'font.size': 10})


def text_to_bool(text: str) -> bool:
	if 'True' in text:
		return True
	elif 'False' in text:
		return False


class Worker(QtCore.QThread):
	outputs = QtCore.pyqtSignal(list)


	def __init__(self,file: str,bkgfile: str,bkgscale: float,composition: str, dataformat: str,qmin: float,qmax: float,qmaxinst: float, 
	rmin: float, rmax: float, rstep: float, rpoly: float,wavelength: float, x, y):
		super(Worker,self).__init__()
		self.file = file
		self.bkgfile = bkgfile
		self.bkgscale = bkgscale
		self.composition = composition
		self.dataformat = dataformat
		self.rpoly = rpoly
		self.qmin = qmin
		self.qmax = qmax
		self.qmaxinst = qmaxinst
		self.rmin = rmin
		self.rmax = rmax
		self.rstep = rstep
		self.wavelength = wavelength
		self.running = True
		self.x = x
		self.y = y

	def run(self):
		while self.running:
			qi,iq,bkg,q,sq,fq,r, gr = pdffunctions.run_pdfgetx3(file=self.file, bkgfile=self.bkgfile, bkgscale=self.bkgscale,
			composition = self.composition, qmin=self.qmin, qmax=self.qmax, qmaxinst=self.qmaxinst,
			rpoly=self.rpoly,dataformat = self.dataformat, rmin = self.rmin, rmax = self.rmax, 
			rstep = self.rstep,wavelength = self.wavelength, x = self.x, y = self.y)
			self.repeat = False
			self.outputs.emit([qi,iq,bkg,q,sq,fq,r, gr])


			while self.repeat == False:
				time.sleep(0.01)
		return
	def stop(self):
		self.running = False

class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("PDFGetX3 GUI")
		MainWindow.resize(702, 657)
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		
		self.filename = QtWidgets.QLineEdit(self.centralwidget)
		self.filename.setGeometry(QtCore.QRect(20, 10, 350, 22))
		self.filename.setObjectName("filename")
		self.filename.setEnabled(False)
		self.filename.setFont(QtGui.QFont('Calibiri',7))

		self.bkgfilename = QtWidgets.QLineEdit(self.centralwidget)
		self.bkgfilename.setGeometry(QtCore.QRect(20, 40, 350, 22))
		self.bkgfilename.setObjectName("bkgfilename")
		self.bkgfilename.setEnabled(False)
		self.bkgfilename.setFont(QtGui.QFont('Calibiri',7))

		self.fileLabel = QtWidgets.QLabel(self.centralwidget)
		self.fileLabel.setGeometry(QtCore.QRect(400, 10, 55, 16))
		self.fileLabel.setObjectName("fileLabel")
		
		self.fileButton = QtWidgets.QPushButton(self.centralwidget)
		self.fileButton.setGeometry(QtCore.QRect(375, 10, 20, 20))
		self.fileButton.setObjectName("fileButton")

		self.bkgFileLabel = QtWidgets.QLabel(self.centralwidget)
		self.bkgFileLabel.setGeometry(QtCore.QRect(400, 40, 101, 31))
		self.bkgFileLabel.setObjectName("bkgFileLabel")

		self.bkgfilebutton = QtWidgets.QPushButton(self.centralwidget)
		self.bkgfilebutton.setGeometry(QtCore.QRect(375, 40, 20, 20))
		self.bkgfilebutton.setObjectName("bkgfilebutton")

		self.compositionBox = QtWidgets.QLineEdit(self.centralwidget)
		self.compositionBox.setGeometry(QtCore.QRect(20, 80, 141, 22))
		self.compositionBox.setObjectName("compositionBox")


		self.compositionLabel = QtWidgets.QLabel(self.centralwidget)
		self.compositionLabel.setGeometry(QtCore.QRect(170, 80, 81, 16))
		self.compositionLabel.setObjectName("compositionLabel")
		
		self.wavelengthBox = QtWidgets.QLineEdit(self.centralwidget)
		self.wavelengthBox.setGeometry(QtCore.QRect(20, 110, 141, 22))
		self.wavelengthBox.setObjectName("wavelengthBox")
		self.wavelengthLabel = QtWidgets.QLabel(self.centralwidget)
		self.wavelengthLabel.setGeometry(QtCore.QRect(170, 110, 81, 16))
		self.wavelengthLabel.setObjectName("wavelengthLabel")

		self.filelistBox = QtWidgets.QComboBox(self.centralwidget)
		self.filelistBox.setGeometry(QtCore.QRect(20, 150, 280, 22))
		self.filelistBox.setObjectName("filelistBox")
		self.fileListLabel = QtWidgets.QLabel(self.centralwidget)
		self.fileListLabel.setGeometry(QtCore.QRect(310, 150, 55, 16))
		self.fileListLabel.setObjectName("fileListLabel")

		self.bkgfilelistBox = QtWidgets.QComboBox(self.centralwidget)
		self.bkgfilelistBox.setGeometry(QtCore.QRect(20, 220, 280, 22))
		self.bkgfilelistBox.setObjectName("bkgfilelistBox")
		self.bkgfileListLabel = QtWidgets.QLabel(self.centralwidget)
		self.bkgfileListLabel.setGeometry(QtCore.QRect(310, 220, 55, 16))
		self.bkgfileListLabel.setObjectName("bkgfileListLabel")
		self.bkgfileListLabel.setText('background\nfiles')
		self.bkgfileListLabel.adjustSize()

		self.removeButton = QtWidgets.QPushButton(self.centralwidget)
		self.removeButton.setGeometry(QtCore.QRect(20, 180, 111, 28))
		self.removeButton.setObjectName("removeButton")

		self.bkgremoveButton = QtWidgets.QPushButton(self.centralwidget)
		self.bkgremoveButton.setGeometry(QtCore.QRect(20, 250, 111, 28))
		self.bkgremoveButton.setObjectName("bkgremoveButton")
		self.bkgremoveButton.setText('remove bkg file')

		self.inputFormatGroup = QtWidgets.QButtonGroup(self.centralwidget)

		self.inputFormatLabel = QtWidgets.QLabel(self.centralwidget)
		self.inputFormatLabel.setGeometry(QtCore.QRect(480, 10, 81, 16))
		self.inputFormatLabel.setObjectName("inputFormatLabel")

		self.QButton = QtWidgets.QRadioButton(self.centralwidget)
		self.QButton.setGeometry(QtCore.QRect(460, 30, 121, 20))
		self.QButton.setChecked(True)
		self.QButton.setObjectName("QButton")
		self.twothetaButton = QtWidgets.QRadioButton(self.centralwidget)
		self.twothetaButton.setGeometry(QtCore.QRect(530, 30, 121, 20))
		self.twothetaButton.setObjectName("twothetaButton")
		
		self.inputFormatGroup.addButton(self.QButton)
		self.inputFormatGroup.addButton(self.twothetaButton)

		self.outputFormatGroup = QtWidgets.QButtonGroup(self.centralwidget)
		
		
		self.relLabel = QtWidgets.QLabel(self.centralwidget)
		self.relLabel.setGeometry(QtCore.QRect(520, 170, 121, 16))
		self.relLabel.setObjectName("relLabel")
		self.relLabel.setText('step size')
		
		self.bkgscalebox = QtWidgets.QDoubleSpinBox(self.centralwidget)
		self.bkgscalebox.setGeometry(QtCore.QRect(450, 190, 61, 22))
		self.bkgscalebox.setProperty("value", 1)
		self.bkgscalebox.setObjectName("bkgscalebox")
		self.bkgscalebox.setDecimals(3)
		self.bkgscalebox.setSingleStep(0.1)
		self.bkgscalebox.setKeyboardTracking(False)

		self.bkgscalerel = QtWidgets.QDoubleSpinBox(self.centralwidget)
		self.bkgscalerel.setGeometry(QtCore.QRect(520, 190, 61, 22))
		self.bkgscalerel.setProperty("value", 0.1)
		self.bkgscalerel.setObjectName("bkgscalerel")
		self.bkgscalerel.setDecimals(3)
		self.bkgscalerel.setSingleStep(0.01)
		self.bkgscalerel.setMinimum(-1)
		self.bkgscalerel.setMaximum(1)

		self.bkgscaleLabel = QtWidgets.QLabel(self.centralwidget)
		self.bkgscaleLabel.setGeometry(QtCore.QRect(371, 190, 121, 16))
		self.bkgscaleLabel.setObjectName("bkgscaleLabel")

		self.qminbox = QtWidgets.QDoubleSpinBox(self.centralwidget)
		self.qminbox.setGeometry(QtCore.QRect(450, 230, 61, 22))
		self.qminbox.setProperty("value", 1)
		self.qminbox.setObjectName("qminbox")
		self.qminbox.setDecimals(2)
		self.qminbox.setSingleStep(0.1)
		self.qminbox.setKeyboardTracking(False)

		self.qminrel = QtWidgets.QDoubleSpinBox(self.centralwidget)
		self.qminrel.setGeometry(QtCore.QRect(520, 230, 61, 22))
		self.qminrel.setProperty("value", 0.1)
		self.qminrel.setObjectName("qminrel")
		self.qminrel.setDecimals(2)
		self.qminrel.setSingleStep(0.01)
		self.qminrel.setMinimum(-1)
		self.qminrel.setMaximum(1)

		self.QminLabel = QtWidgets.QLabel(self.centralwidget)
		self.QminLabel.setGeometry(QtCore.QRect(371, 230, 71, 16))
		self.QminLabel.setObjectName("QminLabel")
		
		self.qmaxbox = QtWidgets.QDoubleSpinBox(self.centralwidget)
		self.qmaxbox.setGeometry(QtCore.QRect(450, 270, 61, 22))
		self.qmaxbox.setProperty("value", 23)
		self.qmaxbox.setObjectName("qmaxbox")
		self.qmaxbox.setDecimals(2)
		self.qmaxbox.setSingleStep(0.1)
		self.qmaxbox.setMinimum(self.qminbox.value()+1)
		self.qmaxbox.setKeyboardTracking(False)

		self.qmaxrel = QtWidgets.QDoubleSpinBox(self.centralwidget)
		self.qmaxrel.setGeometry(QtCore.QRect(520, 270, 61, 22))
		self.qmaxrel.setProperty("value", 0.1)
		self.qmaxrel.setObjectName("qmaxrel")
		self.qmaxrel.setDecimals(2)
		self.qmaxrel.setSingleStep(0.1)
		self.qmaxrel.setMinimum(-1)
		self.qmaxrel.setMaximum(1)

		self.qmaxtogether = QtWidgets.QCheckBox(self.centralwidget)
		self.qmaxtogether.setGeometry(590, 270, 80, 20)
		self.qmaxtogether.setObjectName('qmaxtogether')
		self.qmaxtogether.setText('Qmax together?')
		self.qmaxtogether.adjustSize()

		self.QmaxLabel = QtWidgets.QLabel(self.centralwidget)
		self.QmaxLabel.setGeometry(QtCore.QRect(371, 270, 71, 16))
		self.QmaxLabel.setObjectName("QmaxLabel")
				
		self.qmaxinstbox = QtWidgets.QDoubleSpinBox(self.centralwidget)
		self.qmaxinstbox.setGeometry(QtCore.QRect(450, 310, 61, 21))
		self.qmaxinstbox.setProperty("value", 23)
		self.qmaxinstbox.setObjectName("qmaxinstbox")
		self.qmaxinstbox.setDecimals(2)
		self.qmaxinstbox.setSingleStep(0.1)
		self.qmaxinstbox.setMinimum(self.qminbox.value()+1)
		self.qmaxinstbox.setKeyboardTracking(False)

		self.qmaxinstrel = QtWidgets.QDoubleSpinBox(self.centralwidget)
		self.qmaxinstrel.setGeometry(QtCore.QRect(520, 310, 61, 21))
		self.qmaxinstrel.setProperty("value", 0.1)
		self.qmaxinstrel.setObjectName("qmaxinstrel")
		self.qmaxinstrel.setDecimals(2)
		self.qmaxinstrel.setSingleStep(0.1)
		self.qmaxinstrel.setMaximum(1)
		self.qmaxinstrel.setMinimum(-1)

		self.qmaxinstLabel = QtWidgets.QLabel(self.centralwidget)
		self.qmaxinstLabel.setGeometry(QtCore.QRect(371, 310, 81, 16))
		self.qmaxinstLabel.setObjectName("qmaxinstLabel")

		self.rpolybox = QtWidgets.QDoubleSpinBox(self.centralwidget)
		self.rpolybox.setGeometry(QtCore.QRect(450, 350, 61, 21))
		self.rpolybox.setMaximum(3)
		self.rpolybox.setProperty("value", 1)
		self.rpolybox.setObjectName("rpolybox")
		self.rpolybox.setSingleStep(0.1)
		self.rpolybox.setDecimals(2)
		self.rpolybox.setKeyboardTracking(False)

		self.rpolyrel = QtWidgets.QDoubleSpinBox(self.centralwidget)
		self.rpolyrel.setGeometry(QtCore.QRect(520, 350, 61, 21))
		self.rpolyrel.setMaximum(5)
		self.rpolyrel.setProperty("value", 0.1)
		self.rpolyrel.setObjectName("rpolyrel")
		self.rpolyrel.setSingleStep(0.01)
		self.rpolyrel.setDecimals(2)
		self.rpolyrel.setMaximum(1)
		self.rpolyrel.setMinimum(-1)

		self.rpolyLabel = QtWidgets.QLabel(self.centralwidget)
		self.rpolyLabel.setGeometry(QtCore.QRect(371, 350, 81, 16))
		self.rpolyLabel.setObjectName("rpolyLabel")

		self.regridGroup = QtWidgets.QButtonGroup(self.centralwidget)

		self.noRebin = QtWidgets.QRadioButton(self.centralwidget)
		self.noRebin.setGeometry(QtCore.QRect(350, 380, 81, 16))
		self.noRebin.setText('no rebin')
		self.noRebin.setChecked(True)
		self.noRebin.adjustSize()
		self.noRebin.setObjectName('noRebin')
		
		self.linearRebin = QtWidgets.QRadioButton(self.centralwidget)
		self.linearRebin.setGeometry(QtCore.QRect(420, 380, 81, 16))
		self.linearRebin.setText('linear rebin')
		self.linearRebin.setChecked(False)
		self.linearRebin.adjustSize()
		self.linearRebin.setObjectName('linearRebin')

		self.linearRebinLabel = QtWidgets.QLabel(self.centralwidget)
		self.linearRebinLabel.setGeometry(QtCore.QRect(420, 400, 100, 18))
		self.linearRebinLabel.setText('linear rebin\ngradient')
		self.linearRebinLabel.adjustSize()
		self.linearRebinLabel.setObjectName('linearRebinLabel')
		
		self.linearRebinGradientBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
		self.linearRebinGradientBox.setGeometry(420,430, 50, 20)
		self.linearRebinGradientBox.setObjectName('linearRebinGradientBox')
		self.linearRebinGradientBox.setValue(1.1)
		self.linearRebinGradientBox.setDecimals(2)
		self.linearRebinGradientBox.setMinimum(1.0)
		self.linearRebinGradientBox.setMaximum(5.0)
		self.linearRebinGradientBox.setSingleStep(0.1)
		self.linearRebinGradientBox.setKeyboardTracking(False)

		self.exponentialRebin = QtWidgets.QRadioButton(self.centralwidget)
		self.exponentialRebin.setGeometry(QtCore.QRect(510, 380, 81, 16))
		self.exponentialRebin.setText('exponential rebin')
		self.exponentialRebin.setChecked(False)
		self.exponentialRebin.adjustSize()
		self.exponentialRebin.setObjectName('exponentialRegrid')

		self.exponentialRebinLabel = QtWidgets.QLabel(self.centralwidget)
		self.exponentialRebinLabel.setGeometry(QtCore.QRect(510, 400, 100, 16))
		self.exponentialRebinLabel.setText('exponential\nconstant')
		self.exponentialRebinLabel.adjustSize()
		self.exponentialRebinLabel.setObjectName('exponentialRebinLabel')

		self.exponentialRebinConstant = QtWidgets.QDoubleSpinBox(self.centralwidget)
		self.exponentialRebinConstant.setGeometry(510,430, 70, 20)
		self.exponentialRebinConstant.setObjectName('exponentialRebinConstant')
		self.exponentialRebinConstant.setDecimals(5)
		self.exponentialRebinConstant.setValue(0.0005)
		self.exponentialRebinConstant.setMinimum(0)
		self.exponentialRebinConstant.setMaximum(0.01)
		self.exponentialRebinConstant.setSingleStep(0.0001)
		self.exponentialRebinConstant.setKeyboardTracking(False)
		
		'''
		self.exponentialRebinOrderLabel = QtWidgets.QLabel(self.centralwidget)
		self.exponentialRebinOrderLabel.setGeometry(QtCore.QRect(600, 400, 100, 16))
		self.exponentialRebinOrderLabel.setText('exponential\norder')
		self.exponentialRebinOrderLabel.adjustSize()
		self.exponentialRebinOrderLabel.setObjectName('exponentialRebinOrderLabel')

		self.exponentialRebinOrder = QtWidgets.QSpinBox(self.centralwidget)
		self.exponentialRebinOrder.setGeometry(600,430, 40, 20)
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

		self.plotLabel = QtWidgets.QLabel(self.centralwidget)
		self.plotLabel.setGeometry(QtCore.QRect(480, 110, 41, 16))
		self.plotLabel.setObjectName("plotLabel")

		self.iqCheckBox = QtWidgets.QCheckBox(self.centralwidget)
		self.iqCheckBox.setGeometry(QtCore.QRect(370, 130, 81, 20))
		self.iqCheckBox.setObjectName("iqCheckBox")
		self.sqCheckBox = QtWidgets.QCheckBox(self.centralwidget)
		self.sqCheckBox.setGeometry(QtCore.QRect(440, 130, 81, 20))
		self.sqCheckBox.setObjectName("sqCheckBox")
		self.fqCheckBox = QtWidgets.QCheckBox(self.centralwidget)
		self.fqCheckBox.setGeometry(QtCore.QRect(510, 130, 81, 20))
		self.fqCheckBox.setObjectName("fqCheckBox")
		self.saveButton = QtWidgets.QPushButton(self.centralwidget)
		self.saveButton.setGeometry(QtCore.QRect(410, 470, 93, 28))
		self.saveButton.setObjectName("saveButton")
		self.grCheckBox = QtWidgets.QCheckBox(self.centralwidget)
		self.grCheckBox.setGeometry(QtCore.QRect(590, 130, 81, 20))
		self.grCheckBox.setObjectName("grCheckBox")



		self.rminBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
		self.rminBox.setGeometry(QtCore.QRect(120, 290, 62, 22))
		self.rminBox.setMinimum(0.01)
		self.rminBox.setMaximum(100.0)
		self.rminBox.setSingleStep(0.1)
		self.rminBox.setProperty("value", 0.5)
		self.rminBox.setObjectName("rminBox")
		self.rminBox.setKeyboardTracking(False)

		self.rmaxBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
		self.rmaxBox.setGeometry(QtCore.QRect(120, 330, 62, 22))
		self.rmaxBox.setMinimum(3.0)
		self.rmaxBox.setMaximum(10000.0)
		self.rmaxBox.setProperty("value", 30.0)
		self.rmaxBox.setObjectName("rmaxBox")
		self.rmaxBox.setKeyboardTracking(False)

		self.rstepBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
		self.rstepBox.setGeometry(QtCore.QRect(120, 370, 62, 22))
		self.rstepBox.setDecimals(3)
		self.rstepBox.setMinimum(0.005)
		self.rstepBox.setMaximum(1.0)
		self.rstepBox.setSingleStep(0.01)
		self.rstepBox.setProperty("value", 0.01)
		self.rstepBox.setObjectName("rstepBox")
		self.rstepBox.setKeyboardTracking(False)

		self.rminLabel = QtWidgets.QLabel(self.centralwidget)
		self.rminLabel.setGeometry(QtCore.QRect(200, 290, 55, 16))
		self.rminLabel.setObjectName("rminLabel")
		self.rmaxLablel = QtWidgets.QLabel(self.centralwidget)
		self.rmaxLablel.setGeometry(QtCore.QRect(200, 330, 55, 16))
		self.rmaxLablel.setObjectName("rmaxLablel")
		self.rstepLabel = QtWidgets.QLabel(self.centralwidget)
		self.rstepLabel.setGeometry(QtCore.QRect(200, 370, 55, 16))
		self.rstepLabel.setObjectName("rstepLabel")
		
		self.errorMessageLabel = QtWidgets.QLabel(self.centralwidget)
		self.errorMessageLabel.setGeometry(QtCore.QRect(20, 470, 55, 16))
		self.errorMessageLabel.setObjectName('errorMessageLabel')

		self.plotButton = QtWidgets.QPushButton(self.centralwidget)
		self.plotButton.setGeometry(QtCore.QRect(310, 470, 93, 28))
		self.plotButton.setObjectName("plotButton")

		self.axisCheckBox = QtWidgets.QCheckBox(self.centralwidget)
		self.axisCheckBox.setGeometry(QtCore.QRect(310, 450, 100, 20))
		self.axisCheckBox.setObjectName("axisCheckBox")
		self.axisCheckBox.setText("reset axis on update?")
		self.axisCheckBox.adjustSize()

		

		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 702, 26))
		self.menubar.setObjectName("menubar")
		self.menuFile = QtWidgets.QMenu(self.menubar)
		self.menuFile.setObjectName("menuFile")
		MainWindow.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)
		self.actionOpen = QtWidgets.QAction(MainWindow)
		self.actionOpen.setObjectName("actionOpen")
		self.menuFile.addAction(self.actionOpen)
		self.menubar.addAction(self.menuFile.menuAction())
		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)
		
		
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
		if self.filename != '':
			self.fileList.append(self.filename.text())
			self.filelistBox.addItem('')
			self.filelistBox.setItemText(self.filelistBox.count()-1,os.path.basename(self.filename.text()))
			self.filelistBox.setCurrentIndex(self.filelistBox.count()-1)

		self.plotButton.clicked.connect(self.updateConfigFile)
		self.plotButton.clicked.connect(self.startWorker)


		self.updateParamDct()
		self.configfilepath = os.path.dirname(os.path.realpath(__file__))
		print()
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
		#self.compositionBox.textChanged.connect(self.updateComposition)
		self.qminbox.valueChanged.connect(self.updateQmin)
		self.qminbox.valueChanged.connect(self.setQmax_lims)
		self.qmaxbox.valueChanged.connect(self.updateQmax)
		self.qmaxinstbox.valueChanged.connect(self.setQmax_lims)
		self.qmaxinstbox.valueChanged.connect(self.updateQmaxinst)
		self.rpolybox.valueChanged.connect(self.updateRpoly)
		self.linearRebinGradientBox.valueChanged.connect(self.updatexy)
		self.exponentialRebinConstant.valueChanged.connect(self.updatexy)
		#self.exponentialRebinOrder.valueChanged.connect(self.updatexy)

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

		
	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "PDFgetX3 GUI"))
		#self.gudrunFormat.setText(_translate("MainWindow", "gudrun format"))
		#self.pdfgetxFormat.setText(_translate("MainWindow", "pdfgetx format"))
		self.fileLabel.setText(_translate("MainWindow", "file"))
		self.bkgFileLabel.setText(_translate("MainWindow", "background\nfile"))
		self.bkgscaleLabel.setText(_translate("MainWindow", "background\nscale"))
		self.bkgscaleLabel.adjustSize()
		self.rpolyLabel.setText(_translate("MainWindow", "rpoly"))
		self.QminLabel.setText(_translate("MainWindow", "Qmin"))
		self.QmaxLabel.setText(_translate("MainWindow", "Qmax"))
		self.qmaxinstLabel.setText(_translate("MainWindow", "Qmax inst"))
		
		self.filename.setText(_translate('MainWindow',"exampleFiles/LaB6_0p4mm_011_av10_monitor.xye"))
		self.bkgfilename.setText(_translate('MainWindow',"exampleFiles/0p4mm_capillary_018_av17_monitor.xye"))
		self.fileListLabel.setText(_translate("MainWindow", "File list"))		
		self.compositionBox.setText(_translate("MainWindow", "LaB6"))
		self.wavelengthBox.setText(_translate("MainWindow", "0.270793"))
		self.compositionLabel.setText(_translate("MainWindow", "composition"))
		self.bkgfilebutton.setText(_translate("MainWindow", "..."))
		self.removeButton.setText(_translate("MainWindow", "remove from list"))
		self.iqCheckBox.setText(_translate("MainWindow", "I(Q)"))
		self.sqCheckBox.setText(_translate("MainWindow", "S(Q)"))
		self.fqCheckBox.setText(_translate("MainWindow", "F(Q)"))
		self.saveButton.setText(_translate("MainWindow", "Save"))
		self.plotLabel.setText(_translate("MainWindow", "Plot"))
		self.grCheckBox.setText(_translate("MainWindow", "G(r)"))
		self.fileButton.setText(_translate("MainWindow", "..."))
		self.fileButton.setShortcut(_translate("MainWindow", "Ctrl+O"))
		self.QButton.setText(_translate("MainWindow", "Q (Å\u207B\u00B9)"))
		self.twothetaButton.setText(_translate("MainWindow", "2theta (°)"))
		self.wavelengthLabel.setText(_translate("MainWindow", "wavelength"))
		self.plotButton.setText(_translate("MainWindow", "Plot"))
		self.inputFormatLabel.setText(_translate("MainWindow", "Input format"))
		self.menuFile.setTitle(_translate("MainWindow", "File"))
		self.actionOpen.setText(_translate("MainWindow", "Open"))
		self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
		self.rminLabel.setText(_translate("MainWindow", "rmin (Å)"))
		self.rmaxLablel.setText(_translate("MainWindow", "rmax (Å)"))
		self.rstepLabel.setText(_translate("MainWindow", "rstep (Å)"))

	def startWorker(self):
		self.plotted = False
		if self.running:
			plt.close()
			self.thread.stop()
		
		inputfile=self.filename.text()
		x,y = np.loadtxt(inputfile,comments = '#', unpack = True, usecols=(0,1))
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
		qmin = qmin, qmax = qmax, qmaxinst = qmaxinst, rpoly = rpoly, rmin = rmin, rmax = rmax, rstep = rstep, wavelength = wavelength, x = xrebin,
		y = yrebin)
		plt.ion()
		self.thread.start()
		self.thread.outputs.connect(self.plotUpdate)


	def plotUpdate(self,outputs: list):
		self.qi,self.iq,self.bkg,self.q,self.sq,self.fq,self.r, self.gr = outputs
		plotDct = {'I(Q)':[self.qi,self.iq,'Q (Å$^{-1}$)',self.plotlist[0]],
					'S(Q)': [self.q,self.sq,'Q (Å$^{-1}$)',self.plotlist[1]],
					'F(Q)': [self.q,self.fq,'Q (Å$^{-1}$)',self.plotlist[2]],
					'G(r)': [self.r,self.gr,'r (Å)',self.plotlist[3]]}
		if not self.plotted:	
			self.q0 = self.q
			self.sq0 = self.sq
			self.fq0 = self.fq
			self.gr0 = self.gr
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
					self.ax[plotno].set_xlabel('Q (Å$^{-1}$)')
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
					self.ax[plotno].set_xlabel('Q (Å$^{-1}$)')
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
					self.ax[plotno].set_xlabel('Q (Å$^{-1}$)')
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
					self.ax[plotno].plot(self.r,self.gr,linewidth = linethickness)
					self.ax[plotno].set_xlabel('r (Å)')
					self.ax[plotno].set_ylabel('G(r)')
					
					if holdAxes:
						self.ax[plotno].set_xlim(*xlims['gr'])
						self.ax[plotno].set_ylim(*ylims['gr'])
					else:
						self.ax[plotno].set_xlim(self.r[0],self.r[-1])	
					self.ax[plotno].xaxis.set_label_coords(0.5,-0.08)			
				plotno += 1

		plt.subplots_adjust(top = 0.99, bottom = 0.07, right = 0.99, left = 0.07, 
            hspace = 0.2, wspace = 0)
		plt.show()
		self.plotted = True
		plt.pause(0.01)

		self.centralwidget.activateWindow()

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
		
		pdffunctions.writeOutput(file=self.filename.text(),bkgfile=self.bkgfilename.text(),bkgscale=self.bkgscalebox.value(),
		composition = self.compositionBox.text(),qmin=self.qminbox.value(),qmax=self.qmaxbox.value(),qmaxinst=self.qmaxinstbox.value(),
		rpoly=self.rpolybox.value(),dataformat = self.dataformat, rmin = self.rminBox.value(), rmax = self.rmaxBox.value(),
		rstep = self.rstepBox.value(),wavelength = float(self.wavelengthBox.text()),iqcheck = self.iqcheck, sqcheck = self.sqcheck, 
		fqcheck = self.fqcheck, grcheck = self.grcheck)
		
		
		if len(self.plotlist[self.plotlist == True])==0:
			print('no outputs selected to plot')
			return
	
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

	def write_iq_file(self):
		if self.iqcheck:
			basename = os.path.splitext(self.filename.text())[0]
			outfile = f'{basename}.iq'
			iqsub = self.iq-self.bkg
			print(f'writing {outfile}')
			np.savetxt(outfile,np.array([self.qi,iqsub]).transpose())
			if self.twothetaButton.isChecked():
				outfilexy = f'{basename}_bkgsub.xy'
				print(f'writing {outfilexy}')
				twotheta = 2*np.arcsin(float(self.wavelengthBox.text())*self.qi/(4*np.pi))*180/np.pi
				np.savetxt(outfilexy,np.array([twotheta,iqsub]).transpose())
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

			x,y = np.loadtxt(self.filename.text(),unpack=True,usecols=(0,1),comments='#')
			self.thread.x, self.thread.y = self.qRebin(x,y)
			newbkgfile = self.updatebkgfile()
			self.thread.bkgfile = newbkgfile
			self.thread.repeat = True

	def updatebkgfile(self):
		bkgfile = self.bkgfilename.text()
		if not self.noRebin.isChecked():
			xback, yback = np.loadtxt(bkgfile,comments = '#', unpack = True, usecols = (0,1))
			xbrebin,ybrebin = self.qRebin(xback,yback)
			if not os.path.exists('tmp/'):
				os.makedirs('tmp/')
			tmpbkgfile = 'tmp/tmp_bkg.xy'
			np.savetxt(tmpbkgfile,np.array([xbrebin,ybrebin]).transpose(),fmt = '%.6f')
			return tmpbkgfile
		else:
			return bkgfile
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

if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())

