import os
import numpy as np
from diffpy.pdfgetx import PDFConfig, PDFGetter
from diffpy.pdfgetx import __version__ as pgxversion

def versionCheck(version = pgxversion):
	vlist = version.split('.')
	vlist = [int(i) for i in vlist]
	checkVersion = [2,4]
	for i,ic in zip(vlist,checkVersion):
		if i < ic:
			return False
	return True


def run_pdfgetx3(file: str,bkgfile: str,bkgscale: float,composition: str, qmin: float,qmax: float,qmaxinst: float,rpoly: float,
				dataformat: str,rmin: float, rmax: float, rstep: float,wavelength = 0.2, x= None, y= None, 
				terminationfunctions = None):
	if not terminationfunctions:
		terminationfunctions = []
	config = PDFConfig(bgscale = bkgscale, qmin = qmin, qmax = qmax, qmaxinst = qmaxinst, dataformat = dataformat, rpoly = rpoly, 
					composition = composition, backgroundfile = bkgfile, rmin = rmin, rmax = rmax, rstep = rstep)
	if versionCheck(pgxversion):
		config.terminationfunctions = terminationfunctions
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
dataformat: str,rmin: float, rmax: float, rstep: float,wavelength = 0.2, iqcheck = True, sqcheck = True, fqcheck = True, 
grcheck = True, makedirs = True):
	config = PDFConfig(bgscale = bkgscale, qmin = qmin, qmax = qmax, qmaxinst = qmaxinst, dataformat = dataformat, rpoly = rpoly, composition = composition, 
	backgroundfile = bkgfile, rmin = rmin, rmax = rmax, rstep = rstep)
	if dataformat == 'twotheta':
		config.wavelength = wavelength
	pdfcalc = PDFGetter(config = config)
	pdfcalc(filename = file)
	outfile = os.path.splitext(file)[0]
	outfile = os.path.basename(outfile)
	outdir = os.path.dirname(file)
	plotlist = np.array([iqcheck,sqcheck,fqcheck,grcheck])
	if makedirs:
		os.makedirs(f'{outdir}/gr/', exist_ok=True)
		os.makedirs(f'{outdir}/fq/', exist_ok=True)
		os.makedirs(f'{outdir}/sq/', exist_ok=True)
	for n in range(len(plotlist)):
		if n:
			#if n == 0:
			#	pdfcalc.writeOutput(filename = outfile+'.iq', outputtype = 'iq')

			if n == 1:
				sqfile = f'{outdir}/sq/{outfile}.sq'
				pdfcalc.writeOutput(filename = sqfile, outputtype = 'sq')
				print(f'writing {sqfile}')
			elif n == 2:
				fqfile = f'{outdir}/fq/{outfile}.fq'
				pdfcalc.writeOutput(filename = fqfile, outputtype = 'fq')
				print(f'writing {fqfile}')
			elif n == 3:
				grfile = f'{outdir}/gr/{outfile}.gr'
				pdfcalc.writeOutput(filename = grfile, outputtype = 'gr')
				print(f'writing {grfile}')

			
	
	
