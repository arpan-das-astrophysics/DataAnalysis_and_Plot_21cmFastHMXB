import numpy as np
import math
import pylab
import matplotlib.pyplot as plt
import matplotlib
from scipy import interpolate

SFR=0.0021470217
kev=np.arange(0.1,3,.01)
hertz=kev*2.417990504024e+17
normalisation1=4.27155616953e+40/4.72353131958e+40
normalisation2=4.27155616953e+40/4.56354870246e+40
normalisation3=4.27155616953e+40/4.23506386999e+40
powerlaw1=np.power(kev,-0.8)*math.pow(10,40.4)
powerlaw2=np.power(kev,-0.95)*math.pow(10,40.4)
powerlaw3=np.power(kev,-1.5)*math.pow(10,40.4)

for i in range(len(kev)):
	if kev[i]<0.59:
		powerlaw1[i]=0
	else:
		powerlaw1[i]=powerlaw1[i]

for i in range(len(kev)):
	if kev[i]<0.49:
		powerlaw2[i]=0
	else:
		powerlaw2[i]=powerlaw2[i]

for i in range(len(kev)):
	if kev[i]<0.49:
		powerlaw3[i]=0
	else:
		powerlaw3[i]=powerlaw3[i]


data1 = np.loadtxt('stat.dat')
mean=np.array(data1[:,1])
up=np.array(data1[:,2])
low=np.array(data1[:,3])
energy1=np.array(data1[:,0])

data3=np.loadtxt('/home/arpan/Desktop/John/SED/fragos_absorbed.dat')
energy=np.array(data3[:,0])
sed_absorbed=np.array(data3[:,1])


data4=np.loadtxt('/home/arpan/Desktop/John/SED/fragos_unabsorbed.dat')
sed_unabsorbed=np.array(data4[:,1])

f1=interpolate.interp1d(energy,sed_absorbed)
f2=interpolate.interp1d(energy,sed_unabsorbed)
f3=interpolate.interp1d(energy1,mean)

sed_absorbed_new=f1(kev)/(2.30*kev)/SFR
sed_unabsorbed_new=f2(kev)/(2.30*kev)/SFR
mean_new=f3(kev)

normalisation=math.pow(10,40.46)/1.64271159522e+40

sed_unabsorbed_final=sed_unabsorbed_new*normalisation
sed_mean=sed_unabsorbed_final*mean_new

print np.trapz(sed_mean,kev)
print np.trapz(powerlaw1,kev)
print np.trapz(powerlaw2,kev)
print np.trapz(powerlaw3,kev)


fig1=plt.figure(dpi=72,figsize=(35.5, 31.0))
ax1= fig1.add_subplot(111)
plt.plot(kev,sed_mean, linewidth=7, color='black', linestyle = '-', label=r'${\rm Simulation}$')
plt.plot(kev,powerlaw1, linewidth=7, color='darkgreen', linestyle = '-', label=r'${\rm Powerlaw(\alpha=-0.8)}$')
plt.plot(kev,powerlaw2, linewidth=7, color='darkblue', linestyle = '-', label=r'${\rm Powerlaw(\alpha=-0.95)}$')
plt.plot(kev,powerlaw3, linewidth=7, color='darkred', linestyle = '-', label=r'${\rm Powerlaw(\alpha=-1.5)}$')

ax1.set_xscale("log")
ax1.set_yscale("log")
ax1.set_ylim(1.e+38,1.e+41)

ax1.set_xlim(0.1,10)
ax1.xaxis.set_label_text(r'${\rm Energy(keV)}$', fontsize = 90, color='black')
ax1.yaxis.set_label_text(r'${\rm L_{HMXB}/SFR(erg\,\,\, s^{-1}\, keV^{-1}\, M_\odot^{-1}\, yr)}$', fontsize = 90, color='black')
ax1.tick_params('both', labelsize=70, length=40, width=3, which='major',pad=40)
ax1.tick_params('both', length=25, width=1, which='minor')
ax1.set_xticks([0.1,1,10])
#ax1.set_yticks([0.001,0.01,0.1,1])
#ax1.get_xaxis().get_major_formatter()
ax1.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax1.get_yaxis().get_major_formatter()
plt.legend(fancybox=True, shadow=True, fontsize=50,loc='lower right')
plt.savefig('powerlaw.pdf')
