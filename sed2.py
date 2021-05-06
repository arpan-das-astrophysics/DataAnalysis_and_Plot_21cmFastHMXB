import numpy as np
import math
import pylab
import matplotlib.pyplot as plt
import matplotlib
from scipy import interpolate


kev=np.arange(0.1,10,.01)
SFR=0.0021470217

data1 = np.loadtxt('stat.dat')
mean=np.array(data1[:,1])
up=np.array(data1[:,2])
low=np.array(data1[:,3])


data3=np.loadtxt('/home/arpan/Desktop/John/SED/fragos_absorbed.dat')
energy=np.array(data3[:,0])
sed_absorbed=np.array(data3[:,1])

data4=np.loadtxt('/home/arpan/Desktop/John/SED/fragos_unabsorbed.dat')
sed_unabsorbed=np.array(data4[:,1])

f1=interpolate.interp1d(energy,sed_absorbed)
f2=interpolate.interp1d(energy,sed_unabsorbed)

sed_absorbed_new=f1(kev)/(2.30*kev)/SFR
sed_unabsorbed_new=f2(kev)/(2.30*kev)/SFR

normalisation=math.pow(10,40.46)/1.64271159522e+40

sed_absorbed_final=sed_absorbed_new*normalisation
sed_unabsorbed_final=sed_unabsorbed_new*normalisation
sed_mean=sed_unabsorbed_final*mean
sed_plus_sigma=sed_unabsorbed_final*up
sed_minus_sigma=sed_unabsorbed_final*low

fig1=plt.figure(dpi=72,figsize=(35.5, 31.0))
ax1= fig1.add_subplot(111)
plt.plot(kev,sed_absorbed_final, linewidth=12, color='red', linestyle = '-', label=r'${\rm Absorbed\, SED\, (Fragos\, et\, al. \, 2013)}$')
plt.plot(kev,sed_unabsorbed_final, linewidth=12, color='darkgreen', linestyle = '-', label=r'${\rm Intrinsic\, SED\, (Fragos\, et\, al \,2013)}$')
plt.plot(kev,sed_mean, linewidth=20, color='black', linestyle = '-', label=r'${\rm \langle e^{-tau} \rangle \times Intrinsic\, SED\, (Fragos\, et\, al(2013)) }$')
#plt.plot(kev,sed_plus_sigma, linewidth=3, color='darkgreen', linestyle = '--', label=r'${\rm 68\%\,CL}$')
#plt.plot(kev,sed_minus_sigma, linewidth=3, color='darkgreen', linestyle = '--')
#plt.plot([], [], color='grey', linewidth=10, label=r'${\rm 68\%\, CL }$')

ax1.set_xscale("log")
ax1.set_yscale("log")
ax1.set_ylim(1.e+38,1.e+41)

plt.fill_between(kev, sed_minus_sigma, sed_plus_sigma, color='grey', alpha='0.3')
ax1.set_xlim(0.1,10)
ax1.xaxis.set_label_text(r'${\rm Energy(keV)}$', fontsize = 120, color='black')
ax1.yaxis.set_label_text(r'${\rm L_{HMXB}/SFR(erg\,\,\, s^{-1}\, keV^{-1}\, M_\odot^{-1}\, yr)}$', fontsize = 120, color='black')
ax1.tick_params('both', labelsize=90, length=40, width=3, which='major',pad=40)
ax1.tick_params('both', length=25, width=1, which='minor')
ax1.set_xticks([0.1,1,10])
#ax1.set_yticks([0.001,0.01,0.1,1])
#ax1.get_xaxis().get_major_formatter()
ax1.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax1.get_yaxis().get_major_formatter()
plt.legend(fancybox=True, shadow=True, fontsize=60,loc='lower right')
plt.tight_layout()
plt.savefig('sed.pdf')
