import subprocess, os
import matplotlib.pyplot as plt
import numpy as np
import matplotlib

matplotlib.rcParams.update({'font.size': 12})
from diffpy.pdfgetx.version import __version__

# some convenience imports
from diffpy.pdfgetx.pdfconfig import PDFConfig, loadPDFConfig
from diffpy.pdfgetx.pdfgetter import PDFGetter
from diffpy.pdfgetx.transformation import Transformation
from diffpy.pdfgetx.functs import loaddata, findfiles

# TODO - replace with  `loadData = loaddata` for version 3.0
from diffpy.pdfgetx.functs import loadData

def run_pdfgetx3(file: str,bkgfile: str,bkgscale: float,composition: str, qmin: float,qmax: float,qmaxinst: float,rpoly: float,
dataformat: str,rmin: float, rmax: float, rstep: float,wavelength = 0.2):
	config = PDFConfig(bgscale = bkgscale, qmin = qmin, qmax = qmax, qmaxinst = qmaxinst, dataformat = dataformat, rpoly = rpoly, composition = composition, 
	backgroundfile = bkgfile, rmin = rmin, rmax = rmax, rstep = rstep)
	if dataformat == 'twotheta':
		config.wavelength = wavelength
	pdfcalc = PDFGetter(config = config)
	pdfcalc(filename = file)
	r = pdfcalc.gr[0]
	gr = pdfcalc.gr[1]
	fq = pdfcalc.fq[1]
	sq = pdfcalc.sq[1]
	q = pdfcalc.sq[0]
	iq = pdfcalc.iq[1]
	qi = pdfcalc.iq[0]
	iqorig = pdfcalc.results[2][1]
	bkg = iqorig-iq
	return qi,iqorig,bkg,q, sq, fq, r, gr
	
def writeOutput(file,bkgfile,bkgscale,composition,qmin,qmax,qmaxinst,rpoly,dataformat,rmin, rmax, rstep,wavelength = 0.2,
iqcheck = True, sqcheck = True, fqcheck = True, grcheck = True):
	config = PDFConfig(bgscale = bkgscale, qmin = qmin, qmax = qmax, qmaxinst = qmaxinst, dataformat = dataformat, rpoly = rpoly, composition = composition, 
	backgroundfile = bkgfile, rmin = rmin, rmax = rmax, rstep = rstep)
	if dataformat == 'twotheta':
		config.wavelength = wavelength
	pdfcalc = PDFGetter(config = config)
	pdfcalc(filename = file)
	outfile = os.path.splitext(file)[0]
	plotlist = np.array([iqcheck,sqcheck,fqcheck,grcheck])
	outputtypestring = ''
	for n in range(len(plotlist)):
		if n:
			if n == 1:
				pdfcalc.writeOutput(filename = outfile+'.sq', outputtype = 'sq')
			elif n == 2:
				pdfcalc.writeOutput(filename = outfile+'.fq', outputtype = 'fq')
			elif n == 3:
				pdfcalc.writeOutput(filename = outfile+'.gr', outputtype = 'gr')
			
	
	

def plotOutput(fig,ax,qi,iq,bkg,q,sq,fq,rgr,iqcheck = True, sqcheck = True, fqcheck = True, grcheck = True):

	plotlist = np.array([iqcheck,sqcheck,fqcheck,grcheck])

	
	noplots = len(plotlist[plotlist==True])
	
	plotno = 0
	for c,plot in enumerate(plotlist):
		if plot:
			if c == 0:

				ax[plotno].plot(qi,iq,label = 'total scattering')

				ax[plotno].plot(qi,bkg,label = 'background')
				ax[plotno].set_xlabel('Q (Å$^{-1}$)')
				ax[plotno].set_ylabel('Intensity')
				ax[plotno].legend()
			elif c == 1:

				ax[plotno].plot(q,sq)
				ax[plotno].set_xlabel('Q (Å$^{-1}$)')
				ax[plotno].set_ylabel('S(Q)')
			elif c == 2:

				ax[plotno].plot(q,fq)
				ax[plotno].set_xlabel('Q (Å$^{-1}$)')
				ax[plotno].set_ylabel('F(Q)')
			elif c == 3:

				r,g = rgr[0],rgr[1]
				ax[plotno].plot(r,g)
				ax[plotno].set_xlabel('r (Å)')
				ax[plotno].set_ylabel('G(r)')				
			plotno += 1

	plt.show(block = False)
	
