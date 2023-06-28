import os
import matplotlib.pyplot as plt
import numpy as np
import matplotlib

matplotlib.rcParams.update({'font.size': 12})

from diffpy.pdfgetx.pdfconfig import PDFConfig
from diffpy.pdfgetx.pdfgetter import PDFGetter



def run_pdfgetx3(file: str,bkgfile: str,bkgscale: float,composition: str, qmin: float,qmax: float,qmaxinst: float,rpoly: float,
dataformat: str,rmin: float, rmax: float, rstep: float,wavelength = 0.2, x= None, y= None):
	
	config = PDFConfig(bgscale = bkgscale, qmin = qmin, qmax = qmax, qmaxinst = qmaxinst, dataformat = dataformat, rpoly = rpoly, composition = composition, 
	backgroundfile = bkgfile, rmin = rmin, rmax = rmax, rstep = rstep)
	if dataformat == 'twotheta':
		config.wavelength = wavelength
	pdfcalc = PDFGetter(config = config)
	if type(x) == np.ndarray:
		pdfcalc(x,y)
	else:
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
	
def writeOutput(file: str,bkgfile: str,bkgscale: float,composition: str,qmin: float,qmax: float,qmaxinst: float,rpoly: float,
dataformat: str,rmin: float, rmax: float, rstep: float,wavelength = 0.2, iqcheck = True, sqcheck = True, fqcheck = True, grcheck = True):
	config = PDFConfig(bgscale = bkgscale, qmin = qmin, qmax = qmax, qmaxinst = qmaxinst, dataformat = dataformat, rpoly = rpoly, composition = composition, 
	backgroundfile = bkgfile, rmin = rmin, rmax = rmax, rstep = rstep)
	if dataformat == 'twotheta':
		config.wavelength = wavelength
	pdfcalc = PDFGetter(config = config)
	pdfcalc(filename = file)
	outfile = os.path.splitext(file)[0]
	plotlist = np.array([iqcheck,sqcheck,fqcheck,grcheck])

	for n in range(len(plotlist)):
		if n:
			#if n == 0:
			#	pdfcalc.writeOutput(filename = outfile+'.iq', outputtype = 'iq')
			if n == 1:
				sqfile = f'{outfile}.sq'
				pdfcalc.writeOutput(filename = sqfile, outputtype = 'sq')
				print(f'writing {sqfile}')
			elif n == 2:
				fqfile = f'{outfile}.fq'
				pdfcalc.writeOutput(filename = fqfile, outputtype = 'fq')
				print(f'writing {fqfile}')
			elif n == 3:
				grfile = f'{outfile}.gr'
				pdfcalc.writeOutput(filename = outfile+'.gr', outputtype = 'gr')
				print(f'writing {grfile}')
			
	
	

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
	
