import numpy as np
import matplotlib.pyplot as plt
import os
def linear(r,rho):
    return 4*np.pi*r*rho

direc = r'C:\Users\kenneth1a\Documents\PDF\July2021\LaB6_capillaries\gr\SA_off/'
os.chdir(direc)
grfile = 'LaB6_0p7mm_021_av20_monitor.gr'
r,G = np.loadtxt(grfile,skiprows=  26, unpack = True)
1
rrange = np.arange(0,20,1)
fig,ax = plt.subplots()
print('enter nothing to exit')
print('enter "save" to save file')
minindex = np.abs(r-1).argmin()
r2 = r[minindex:]
G2 = G[minindex:]
rho = 0.0975
scale = 1
fit = linear(rrange,rho)
while True:
    ax.cla()
    Gscale = G*scale
    Gscale2 = G2*scale
    gr = Gscale2/linear(r2,rho) + 1
    ax.plot(r,Gscale)
    ax.plot(rrange,-1*fit)
    ax.plot(r2,gr)
    ax.plot(r,np.ones(len(r)),'--')
    ax.plot(r,np.zeros(len(r)),'--')
    ax.set_xlabel('r (Å)')
    ax.set_ylabel('G(r)')
    ax.set_xlim(r[0],r[-1])
    plt.show(block=False)
    plt.pause(0.1)
    scaleinput = input('input scale:')
    if scaleinput == '':
        break
    elif scaleinput == 'save':
        print('saving')
        np.savetxt(grfile.replace('.gr','.sgr'),np.array([r2,gr]).transpose(),fmt = '%.6f',header = f'rho = {rho}\nr(Å) g(r)')
        np.savetxt(grfile.replace('.gr','_scaled.gr'),np.array([r,Gscale]).transpose(),fmt = '%.6f',header = 'r(Å) G(r)')
        
    try:
        scale = float(scaleinput)
    except ValueError:
        print('enter number')