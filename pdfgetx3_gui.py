# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'guilayout.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os
import pdffunctions
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
matplotlib.rcParams.update({'font.size': 12})



class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(702, 657)
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		
		self.filename = QtWidgets.QLineEdit(self.centralwidget)
		self.filename.setGeometry(QtCore.QRect(20, 10, 220, 22))
		self.filename.setObjectName("filename")
		self.bkgfilename = QtWidgets.QLineEdit(self.centralwidget)
		self.bkgfilename.setGeometry(QtCore.QRect(20, 40, 220, 22))
		self.bkgfilename.setObjectName("bkgfilename")
		
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
		self.wavelengthLabel.setGeometry(QtCore.QRect(180, 110, 81, 16))
		self.wavelengthLabel.setObjectName("wavelengthLabel")

		self.outputFormatGroup = QtWidgets.QButtonGroup(self.centralwidget)
		
		#self.gudrunFormat = QtWidgets.QRadioButton(self.centralwidget)
		#self.gudrunFormat.setGeometry(QtCore.QRect(480, 80, 121, 20))
		#self.gudrunFormat.setObjectName("gudrunFormat")
		#self.pdfgetxFormat = QtWidgets.QRadioButton(self.centralwidget)
		#self.pdfgetxFormat.setGeometry(QtCore.QRect(350, 80, 121, 20))
		#self.pdfgetxFormat.setChecked(True)
		#self.pdfgetxFormat.setObjectName("pdfgetxFormat")
		#
		#self.outputFormatGroup.addButton(self.gudrunFormat)
		#self.outputFormatGroup.addButton(self.pdfgetxFormat)
		

		
		self.bkgscalebox = QtWidgets.QDoubleSpinBox(self.centralwidget)
		self.bkgscalebox.setGeometry(QtCore.QRect(371, 190, 61, 22))
		self.bkgscalebox.setProperty("value", 1)
		self.bkgscalebox.setObjectName("bkgscalebox")
		self.bkgscalebox.setDecimals(1)
		self.bkgscalebox.setSingleStep(0.1)
		
		self.qminbox = QtWidgets.QDoubleSpinBox(self.centralwidget)
		self.qminbox.setGeometry(QtCore.QRect(371, 230, 61, 22))
		self.qminbox.setProperty("value", 1)
		self.qminbox.setObjectName("qminbox")
		self.qminbox.setDecimals(1)
		self.qminbox.setSingleStep(0.1)
		
		self.qmaxbox = QtWidgets.QDoubleSpinBox(self.centralwidget)
		self.qmaxbox.setGeometry(QtCore.QRect(371, 270, 61, 22))
		self.qmaxbox.setProperty("value", 23)
		self.qmaxbox.setObjectName("qmaxbox")
		self.qmaxbox.setDecimals(1)
		self.qmaxbox.setSingleStep(0.1)
		
		self.rpolybox = QtWidgets.QDoubleSpinBox(self.centralwidget)
		self.rpolybox.setGeometry(QtCore.QRect(371, 340, 61, 21))
		self.rpolybox.setMaximum(5)
		self.rpolybox.setProperty("value", 1)
		self.rpolybox.setObjectName("rpolybox")
		self.rpolybox.setSingleStep(0.1)
		self.rpolybox.setDecimals(1)
		
		self.qmaxinstbox = QtWidgets.QDoubleSpinBox(self.centralwidget)
		self.qmaxinstbox.setGeometry(QtCore.QRect(371, 310, 61, 21))
		self.qmaxinstbox.setProperty("value", 23)
		self.qmaxinstbox.setObjectName("qmaxinstbox")
		self.qmaxinstbox.setDecimals(1)
		self.qmaxinstbox.setSingleStep(0.1)
		
		self.fileLabel = QtWidgets.QLabel(self.centralwidget)
		self.fileLabel.setGeometry(QtCore.QRect(300, 10, 55, 16))
		self.fileLabel.setObjectName("fileLabel")
		self.bkgFileLabel = QtWidgets.QLabel(self.centralwidget)
		self.bkgFileLabel.setGeometry(QtCore.QRect(300, 40, 101, 31))
		self.bkgFileLabel.setObjectName("bkgFileLabel")
		self.bkgscaleLabel = QtWidgets.QLabel(self.centralwidget)
		self.bkgscaleLabel.setGeometry(QtCore.QRect(450, 190, 121, 16))
		self.bkgscaleLabel.setObjectName("bkgscaleLabel")
		self.rpolyLabel = QtWidgets.QLabel(self.centralwidget)
		self.rpolyLabel.setGeometry(QtCore.QRect(450, 340, 81, 16))
		self.rpolyLabel.setObjectName("rpolyLabel")
		self.QminLabel = QtWidgets.QLabel(self.centralwidget)
		self.QminLabel.setGeometry(QtCore.QRect(450, 230, 71, 16))
		self.QminLabel.setObjectName("QminLabel")
		self.QmaxLabel = QtWidgets.QLabel(self.centralwidget)
		self.QmaxLabel.setGeometry(QtCore.QRect(450, 270, 71, 16))
		self.QmaxLabel.setObjectName("QmaxLabel")
		

		
		self.qmaxinstLabel = QtWidgets.QLabel(self.centralwidget)
		self.qmaxinstLabel.setGeometry(QtCore.QRect(450, 310, 81, 16))
		self.qmaxinstLabel.setObjectName("qmaxinstLabel")
		self.filelistBox = QtWidgets.QComboBox(self.centralwidget)
		self.filelistBox.setGeometry(QtCore.QRect(20, 150, 201, 22))
		self.filelistBox.setObjectName("filelistBox")
		self.fileListLabel = QtWidgets.QLabel(self.centralwidget)
		self.fileListLabel.setGeometry(QtCore.QRect(230, 150, 55, 16))
		self.fileListLabel.setObjectName("fileListLabel")
		
		self.removeButton = QtWidgets.QPushButton(self.centralwidget)
		self.removeButton.setGeometry(QtCore.QRect(220, 180, 111, 28))
		self.removeButton.setObjectName("removeButton")

		self.bkgfilebutton = QtWidgets.QPushButton(self.centralwidget)
		self.bkgfilebutton.setGeometry(QtCore.QRect(250, 40, 41, 28))
		self.bkgfilebutton.setObjectName("bkgfilebutton")
		self.iqCheckBox = QtWidgets.QCheckBox(self.centralwidget)
		self.iqCheckBox.setGeometry(QtCore.QRect(330, 130, 81, 20))
		self.iqCheckBox.setObjectName("iqCheckBox")
		self.sqCheckBox = QtWidgets.QCheckBox(self.centralwidget)
		self.sqCheckBox.setGeometry(QtCore.QRect(420, 130, 81, 20))
		self.sqCheckBox.setObjectName("sqCheckBox")
		self.fqCheckBox = QtWidgets.QCheckBox(self.centralwidget)
		self.fqCheckBox.setGeometry(QtCore.QRect(520, 130, 81, 20))
		self.fqCheckBox.setObjectName("fqCheckBox")
		self.saveButton = QtWidgets.QPushButton(self.centralwidget)
		self.saveButton.setGeometry(QtCore.QRect(410, 470, 93, 28))
		self.saveButton.setObjectName("saveButton")
		self.plotLabel = QtWidgets.QLabel(self.centralwidget)
		self.plotLabel.setGeometry(QtCore.QRect(430, 110, 41, 16))
		self.plotLabel.setObjectName("plotLabel")
		self.grCheckBox = QtWidgets.QCheckBox(self.centralwidget)
		self.grCheckBox.setGeometry(QtCore.QRect(590, 130, 81, 20))
		self.grCheckBox.setObjectName("grCheckBox")
		self.fileButton = QtWidgets.QPushButton(self.centralwidget)
		self.fileButton.setGeometry(QtCore.QRect(250, 10, 41, 28))
		self.fileButton.setObjectName("fileButton")
		self.rminBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
		self.rminBox.setGeometry(QtCore.QRect(120, 290, 62, 22))
		self.rminBox.setMinimum(0.01)
		self.rminBox.setMaximum(100.0)
		self.rminBox.setSingleStep(0.1)
		self.rminBox.setProperty("value", 0.5)
		self.rminBox.setObjectName("rminBox")
		self.rmaxBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
		self.rmaxBox.setGeometry(QtCore.QRect(120, 330, 62, 22))
		self.rmaxBox.setMinimum(3.0)
		self.rmaxBox.setMaximum(10000.0)
		self.rmaxBox.setProperty("value", 30.0)
		self.rmaxBox.setObjectName("rmaxBox")
		self.rstepBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
		self.rstepBox.setGeometry(QtCore.QRect(120, 370, 62, 22))
		self.rstepBox.setDecimals(3)
		self.rstepBox.setMinimum(0.005)
		self.rstepBox.setMaximum(1.0)
		self.rstepBox.setSingleStep(0.01)
		self.rstepBox.setProperty("value", 0.01)
		self.rstepBox.setObjectName("rstepBox")
		self.rminLabel = QtWidgets.QLabel(self.centralwidget)
		self.rminLabel.setGeometry(QtCore.QRect(200, 290, 55, 16))
		self.rminLabel.setObjectName("rminLabel")
		self.rmaxLablel = QtWidgets.QLabel(self.centralwidget)
		self.rmaxLablel.setGeometry(QtCore.QRect(200, 330, 55, 16))
		self.rmaxLablel.setObjectName("rmaxLablel")
		self.rstepLabel = QtWidgets.QLabel(self.centralwidget)
		self.rstepLabel.setGeometry(QtCore.QRect(200, 370, 55, 16))
		self.rstepLabel.setObjectName("rstepLabel")
		
		self.inputFormatGroup = QtWidgets.QButtonGroup(self.centralwidget)
		
		self.QButton = QtWidgets.QRadioButton(self.centralwidget)
		self.QButton.setGeometry(QtCore.QRect(400, 30, 121, 20))
		self.QButton.setChecked(True)
		self.QButton.setObjectName("QButton")
		self.twothetaButton = QtWidgets.QRadioButton(self.centralwidget)
		self.twothetaButton.setGeometry(QtCore.QRect(470, 30, 121, 20))
		self.twothetaButton.setObjectName("twothetaButton")
		
		self.inputFormatGroup.addButton(self.QButton)
		self.inputFormatGroup.addButton(self.twothetaButton)
		

		self.plotButton = QtWidgets.QPushButton(self.centralwidget)
		self.plotButton.setGeometry(QtCore.QRect(310, 470, 93, 28))
		self.plotButton.setObjectName("plotButton")
		#self.updatePlotButton = QtWidgets.QPushButton(self.centralwidget)
		#self.updatePlotButton.setGeometry(QtCore.QRect(310, 500, 93, 28))
		#self.updatePlotButton.setObjectName("updatePlotButton")
		
		self.inputFormatLabel = QtWidgets.QLabel(self.centralwidget)
		self.inputFormatLabel.setGeometry(QtCore.QRect(420, 10, 81, 16))
		self.inputFormatLabel.setObjectName("inputFormatLabel")
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
		self.inputfile = None
		self.dataformat = None
		self.plotlist = []

		
		self.actionOpen.triggered.connect(self.open_file)
		self.fileButton.clicked.connect(self.open_file)
		self.bkgfilebutton.clicked.connect(self.open_bkgfile)
		self.removeButton.clicked.connect(self.removeFile)

		self.plotButton.clicked.connect(self.run)
		self.fileList = []
		self.filelistBox.currentTextChanged.connect(self.changeFile)
		
		#self.updatePlotButton.clicked.connect(self.plotUpdate)
		self.rminBox.valueChanged.connect(self.plotUpdate)
		self.rmaxBox.valueChanged.connect(self.plotUpdate)
		self.rstepBox.valueChanged.connect(self.plotUpdate)
		self.compositionBox.textChanged.connect(self.plotUpdate)
		self.qminbox.valueChanged.connect(self.plotUpdate)
		self.qmaxbox.valueChanged.connect(self.plotUpdate)
		self.qmaxinstbox.valueChanged.connect(self.plotUpdate)
		self.rpolybox.valueChanged.connect(self.plotUpdate)
		
	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		#self.gudrunFormat.setText(_translate("MainWindow", "gudrun format"))
		#self.pdfgetxFormat.setText(_translate("MainWindow", "pdfgetx format"))
		self.fileLabel.setText(_translate("MainWindow", "file"))
		self.bkgFileLabel.setText(_translate("MainWindow", "background\nfile"))
		self.bkgscaleLabel.setText(_translate("MainWindow", "background scale"))
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
		self.bkgfilebutton.setText(_translate("MainWindow", "file"))
		self.removeButton.setText(_translate("MainWindow", "remove from list"))
		self.iqCheckBox.setText(_translate("MainWindow", "I(Q)"))
		self.sqCheckBox.setText(_translate("MainWindow", "S(Q)"))
		self.fqCheckBox.setText(_translate("MainWindow", "F(Q)"))
		self.saveButton.setText(_translate("MainWindow", "Save"))
		self.plotLabel.setText(_translate("MainWindow", "Plot"))
		self.grCheckBox.setText(_translate("MainWindow", "G(r)"))
		self.fileButton.setText(_translate("MainWindow", "file"))
		self.fileButton.setShortcut(_translate("MainWindow", "Ctrl+O"))
		self.QButton.setText(_translate("MainWindow", "Q"))
		self.twothetaButton.setText(_translate("MainWindow", "2theta"))
		self.wavelengthLabel.setText(_translate("MainWindow", "wavelength"))
		self.plotButton.setText(_translate("MainWindow", "Plot"))
		#self.updatePlotButton.setText(_translate("MainWindow", "update plot"))
		self.inputFormatLabel.setText(_translate("MainWindow", "Input format"))
		self.menuFile.setTitle(_translate("MainWindow", "File"))
		self.actionOpen.setText(_translate("MainWindow", "Open"))
		self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
		self.rminLabel.setText(_translate("MainWindow", "rmin (Å)"))
		self.rmaxLablel.setText(_translate("MainWindow", "rmax (Å)"))
		self.rstepLabel.setText(_translate("MainWindow", "rstep (Å)"))
		
	def open_file(self):
		filter = "data file (*.txt *.dat *.xy *.xye *.csv)"
		dialog = QtWidgets.QFileDialog.getOpenFileName(caption = 'select data file',
		filter = filter)

		basefilename = os.path.basename(dialog[0])
		
		
		self.filename.setText(dialog[0])
		self.fileList.append(dialog[0])
		self.filelistBox.addItem('')
		self.filelistBox.setItemText(self.filelistBox.count()-1,basefilename)
		self.filelistBox.setCurrentIndex(self.filelistBox.count()-1)
	def changeFile(self):
		fileindex = self.filelistBox.currentIndex()
		newfile = self.fileList[fileindex]
		self.filename.setText(newfile)
	def removeFile(self):
		if len(self.fileList) != 0:
			fileindex = self.filelistBox.currentIndex()
			self.filelistBox.removeItem(fileindex)
			self.fileList.pop(fileindex)
			self.changeFile()
		else:
			return
		
	def open_bkgfile(self):
		#dialog.setFileMode(QtWidgets.QFileDialog.AnyFile)
		filter = "data file (*.txt *.dat *.xy *.xye *.csv)"
		dialog = QtWidgets.QFileDialog.getOpenFileName(caption = 'select data file',
		filter = filter)

		basefilename = os.path.basename(dialog[0])
		self.bkgfilename.setText(dialog[0])



	def run(self):
		

		iqcheck = self.iqCheckBox.isChecked()
		sqcheck = self.sqCheckBox.isChecked()
		fqcheck = self.fqCheckBox.isChecked()
		grcheck = self.grCheckBox.isChecked()
		
		self.plotlist = np.array([iqcheck,sqcheck,fqcheck,grcheck])
		
		if len(self.plotlist[self.plotlist == True])==0:
			print('no outputs selected to plot')
			return
		
		self.noplots = len(self.plotlist[self.plotlist==True])
		self.fig,self.ax = plt.subplots(self.noplots,1,dpi = 150)

		if self.QButton.isChecked():
			self.dataformat = 'QA'
		elif self.twothetaButton.isChecked():
			self.dataformat = 'twotheta'
		self.inputfile = self.filename.text()
		print('calculating')

		self.plotUpdate()
		




	def plotUpdate(self):

		qi,iq,bkg,q,sq,fq,rgr = pdffunctions.run_pdfgetx3(file=self.inputfile,bkgfile=self.bkgfilename.text(),bkgscale=float(self.bkgscalebox.text()),
		composition = self.compositionBox.text(),qmin=float(self.qminbox.text()),qmax=float(self.qmaxbox.text()),qmaxinst=float(self.qmaxinstbox.text()),
		rpoly=float(self.rpolybox.text()),dataformat = self.dataformat, rmin = float(self.rminBox.text()), rmax = float(self.rmaxBox.text()), 
		rstep = float(self.rstepBox.text()))
		r,g = rgr[0],rgr[1]

		for n in range(self.noplots):
			self.ax[n].cla()

		plotno = 0

		for c,plot in enumerate(self.plotlist):
			if plot:
				if c == 0:

					self.ax[plotno].plot(qi,iq,label = 'total scattering')
					self.ax[plotno].plot(qi,bkg,label = 'background')
					self.ax[plotno].set_xlabel('Q (Å$^{-1}$)')
					self.ax[plotno].set_ylabel('Intensity')
					self.ax[plotno].legend()
				elif c == 1:
					self.ax[plotno].plot(q,sq)
					self.ax[plotno].set_xlabel('Q (Å$^{-1}$)')
					self.ax[plotno].set_ylabel('S(Q)')
				elif c == 2:
					self.ax[plotno].plot(q,fq)
					self.ax[plotno].set_xlabel('Q (Å$^{-1}$)')
					self.ax[plotno].set_ylabel('F(Q)')
				elif c == 3:
					self.ax[plotno].plot(r,g)
					self.ax[plotno].set_xlabel('r (Å)')
					self.ax[plotno].set_ylabel('G(r)')				
				plotno += 1
		
		plt.show(block = False)
		plt.pause(0.01)


		
		
if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())

