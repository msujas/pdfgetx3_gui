from PyQt5 import QtCore
import time
from . import pdffunctions
import diffpy.pdfgetx
import os
from glob import glob

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
			try:
				qi,iq,bkg,q,sq,fq,r, gr = pdffunctions.run_pdfgetx3(file=self.file, bkgfile=self.bkgfile, bkgscale=self.bkgscale,
			composition = self.composition, qmin=self.qmin, qmax=self.qmax, qmaxinst=self.qmaxinst,
			rpoly=self.rpoly,dataformat = self.dataformat, rmin = self.rmin, rmax = self.rmax, 
			rstep = self.rstep,wavelength = self.wavelength, x = self.x, y = self.y)
			except diffpy.pdfgetx.pdfconfig.PDFConfigError as e:
				if 'Unknown chemical' in str(e):
					self.outputs.emit(['invalid composition'])
					return
			self.repeat = False
			self.outputs.emit([qi,iq,bkg,q,sq,fq,r, gr])


			while self.repeat == False:
				time.sleep(0.01)
		return
	def stop(self):
		self.running = False
		
class SaveDirWorker(QtCore.QThread):
	outputs = QtCore.pyqtSignal(bool)
	def __init__(self, filename, bkgfile,bkgscale: float,composition: str,qmin: float,qmax: float,qmaxinst: float,rpoly: float,
dataformat: str,rmin: float, rmax: float, rstep: float,wavelength: float):
		super(SaveDirWorker,self).__init__()
		self.filename = filename
		self.bkgfile = bkgfile
		self.bkgscale = bkgscale
		self.composition = composition
		self.qmin = qmin
		self.qmax = qmax
		self.qmaxinst = qmaxinst
		self.rpoly = rpoly
		self.dataformat = dataformat
		self.rmin = rmin
		self.rmax = rmax
		self.rstep = rstep
		self.wavelength = wavelength
	def run(self):
		directory = os.path.dirname(self.filename)
		extension = os.path.splitext(self.filename)[-1]
		files = glob(f'{directory}/*{extension}')
		os.makedirs(f'{directory}/gr/', exist_ok=True)
		os.makedirs(f'{directory}/fq/', exist_ok=True)
		os.makedirs(f'{directory}/sq/', exist_ok=True)
		self.running = True
		print(f'running in {directory}')
		for file in files:
			if not self.running:
				break
			pdffunctions.writeOutput(file,self.bkgfile, self.bkgscale,self.composition,self.qmin,self.qmax,
							self.qmaxinst,self.rpoly, self.dataformat,self.rmin,self.rmax,self.rstep, self.wavelength, makedirs=False)
		self.outputs.emit(True)
	def stop(self):
		self.running = False