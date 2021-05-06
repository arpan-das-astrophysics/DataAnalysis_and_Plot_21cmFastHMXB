import numpy as np
import math
import pylab
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.ticker import *
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.colors import Normalize
import h5py
#cm = plt.cm.get_cmap('RdYlBu')
class MidpointNormalize(Normalize):
    def __init__(self, vmin=None, vmax=None, midpoint=None, clip=False):
        self.midpoint = midpoint
        Normalize.__init__(self, vmin, vmax, clip)

    def __call__(self, value, clip=None):
        x, y = [self.vmin, self.midpoint, self.vmax], [0, 0.5, 1]
        return np.ma.masked_array(np.interp(value, x, y))

cmap = LinearSegmentedColormap.from_list('mycmap', ['magenta','blue','cyan','green','orange','red'])

redshift8_index=np.array([0,1,2,3,7,11,12])
redshift10_index=np.array([0,1,5,8,12,15,19])
redshift12_index=np.array([0,2,3,11,25,31])
redshift14_index=np.array([0,4])


NHI_redshift8=[]
NHI_redshift10=[]
NHI_redshift12=[]
NHI_redshift14=[]
opacity_redshift8=[]
opacity_redshift10=[]
opacity_redshift12=[]
opacity_redshift14=[]
sfr=[]

with h5py.File('redshift8.h5','r') as hf8:
	for j in range(len(redshift8_index)):
		gp8 = hf8.get('halo{0}'.format(redshift8_index[j]))
		NHI8= np.array(gp8.get('Column_Density'))
		NHI_redshift8.append(NHI8)
		opacity8= np.array(gp8.get('Opacity'))
		opacity_redshift8.append(opacity8[70])

with h5py.File('redshift10.h5','r') as hf10:
	for k in range(len(redshift10_index)):
		gp10 = hf10.get('halo{0}'.format(redshift10_index[k]))
		NHI10= np.array(gp10.get('Column_Density'))
		NHI_redshift10.append(NHI10)
		opacity10= np.array(gp10.get('Opacity'))
		opacity_redshift10.append(opacity10[70])

with h5py.File('redshift12.h5','r') as hf12:
	for l in range(len(redshift12_index)):
		gp12 = hf12.get('halo{0}'.format(redshift12_index[l]))
		NHI12= np.array(gp12.get('Column_Density'))
		NHI_redshift12.append(NHI12)
		opacity12= np.array(gp12.get('Opacity'))
		opacity_redshift12.append(opacity12[70])

with h5py.File('redshift14.h5','r') as hf14:
	for m in range(len(redshift14_index)):
		gp14 = hf14.get('halo{0}'.format(redshift14_index[m]))
		NHI14= np.array(gp14.get('Column_Density'))
		NHI_redshift14.append(NHI14)
		opacity14= np.array(gp14.get('Opacity'))
		opacity_redshift14.append(opacity14[70])
		

NHI_redshift8=np.array(NHI_redshift8)
NHI_redshift10=np.array(NHI_redshift10)
NHI_redshift12=np.array(NHI_redshift12)
NHI_redshift14=np.array(NHI_redshift14)

opacity_redshift8=np.array(opacity_redshift8)
opacity_redshift10=np.array(opacity_redshift10)
opacity_redshift12=np.array(opacity_redshift12)
opacity_redshift14=np.array(opacity_redshift14)

print opacity_redshift10
print opacity_redshift12
print opacity_redshift14
print opacity_redshift8

stellarmass_redshift8=np.array([3.035e+05,1.177e+05,1.191e+04,3.506e+04,9951,1078,1775])
stellarmass_redshift10=np.array([1080,1.502e+04,3028,7604,1.368e+04,2001,266.1])
stellarmass_redshift12=np.array([2738,1043,115.6,1190,886.3,77.54])
stellarmass_redshift14=np.array([757.3,2815])

halomass_redshift8=np.array([2.464e+08,1.857e+08,7.697e+07,1.244e+08,6.02e+07,3.862e+07,3.961e+07])
halomass_redshift10=np.array([7.846e+07,6.586e+07,3.355e+07,1.92e+07,1.455e+07,1.254e+07,8.026e+06])
halomass_redshift12=np.array([2.461e+07,1.351e+07,1.219e+07,7.812e+06,5.365e+06,4.325e+06])
halomass_redshift14=np.array([4.273e+06,2.28e+06])

sfr_redshift8=np.log10(stellarmass_redshift8/20.e+6)
sfr.append(np.amin(sfr_redshift8))
sfr.append(np.amax(sfr_redshift8))

sfr_redshift10=np.log10(stellarmass_redshift10/20.e+6)
sfr.append(np.amin(sfr_redshift10))
sfr.append(np.amax(sfr_redshift10))

sfr_redshift12=np.log10(stellarmass_redshift12/20.e+6)
sfr.append(np.amin(sfr_redshift12))
sfr.append(np.amax(sfr_redshift12))

sfr_redshift14=np.log10(stellarmass_redshift14/20.e+6)
sfr.append(np.amin(sfr_redshift14))
sfr.append(np.amax(sfr_redshift14))


sfr=np.array(sfr)

fig1=plt.figure(dpi=72)
ax1= fig1.add_subplot(111)
plt.scatter(halomass_redshift8, opacity_redshift8, c=sfr_redshift8, s=500, cmap=cmap, vmin=np.amin(sfr), vmax=np.amax(sfr),marker='o',label=r'${\rm z=7.99}$')
plt.scatter(halomass_redshift10, opacity_redshift10, c=sfr_redshift10, s=500, vmin=np.amin(sfr), vmax=np.amax(sfr), cmap=cmap,marker='^',label=r'${\rm z=9.95}$')
plt.scatter(halomass_redshift12, opacity_redshift12, c=sfr_redshift12, s=500, vmin=np.amin(sfr), vmax=np.amax(sfr), cmap=cmap,marker='*',label=r'${\rm z=12.12}$')
plt.scatter(halomass_redshift14, opacity_redshift14, c=sfr_redshift14, s=500, vmin=np.amin(sfr), vmax=np.amax(sfr), cmap=cmap,marker='D',label=r'${\rm z=14.78}$')

c_bar=plt.colorbar()
c_bar.set_label(r'${\rm log(SFR(M_\odot/yr))}$', fontsize=40, rotation=-90, labelpad=60)
#tick_array = np.linspace(-4.5,-1.8,8)
#c_bar.set_ticks(tick_array)
for t in c_bar.ax.get_yticklabels():
	t.set_fontsize(20)


ax1.set_xscale("log")
#ax1.set_yscale("log")
#ax1.set_ylim(1.e+18,1.e+23)
ax1.set_xlim(1.e+6,1.e+9)
ax1.xaxis.set_label_text(r'${\rm Halo\, Mass(M_\odot)}$', fontsize = 40, color='black')
ax1.yaxis.set_label_text(r'${\rm \langle e^{-\tau}_{1\, kev}\rangle}$', fontsize = 40, color='black')
ax1.tick_params('both', labelsize=25, length=20, width=2, which='major')
ax1.tick_params('both', length=10, width=1, which='minor')
#x1.text(math.pow(10,8.7), math.pow(10,19.3),r'${\rm z=8}$',fontsize=50,color='black',bbox=dict(facecolor='none', edgecolor='black'))
ax1.get_xaxis().get_major_formatter()
leg=ax1.legend(fancybox=True, shadow=True, fontsize=30,loc='lower right',scatterpoints = 1)
for l in leg.legendHandles:
	l.set_color('grey')
plt.show()

