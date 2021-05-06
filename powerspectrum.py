import numpy as np
import math
import pylab
import matplotlib.pyplot as plt
from scipy.interpolate import spline
import matplotlib

data1 = np.loadtxt('ps_fragos_0.1.dat')
redshift_fragos=np.array(data1[:,0])
power_fragos=np.array(data1[:,3])
#f1=interp1d(redshift_fragos, power_fragos)
redshift_fragos_new=np.linspace(np.amin(redshift_fragos),np.amax(redshift_fragos),10000)

data2 = np.loadtxt('ps_median_0.1.dat')
redshift_median=np.array(data2[:,0])
power_median=np.array(data2[:,3])
#f2=interp1d(redshift_median, power_median)
redshift_median_new=np.linspace(np.amin(redshift_median),np.amax(redshift_median),10000)

data3 = np.loadtxt('ps_unabsorbed_0.1.dat')
redshift_unabsorbed=np.array(data3[:,0])
power_unabsorbed=np.array(data3[:,3])
#f3=interp1d(redshift_unabsorbed, power_unabsorbed)
redshift_unabsorbed_new=np.linspace(np.amin(redshift_unabsorbed),np.amax(redshift_unabsorbed),10000)

data4 = np.loadtxt('ps_low_0.1.dat')
redshift_low=np.array(data4[:,0])
power_low=np.array(data4[:,3])
redshift_low_new=np.linspace(np.amin(redshift_low),np.amax(redshift_low),10000)

data5 = np.loadtxt('ps_up_0.1.dat')
redshift_high=np.array(data5[:,0])
power_high=np.array(data5[:,3])
redshift_high_new=np.linspace(np.amin(redshift_high),np.amax(redshift_high),10000)

data6 = np.loadtxt('powerlaw.dat')
redshift_power=np.array(data6[:,0])
power_power=np.array(data6[:,3])
redshift_power_new=np.linspace(np.amin(redshift_power),np.amax(redshift_power),10000)

power_fragos_new=spline(redshift_fragos, power_fragos,redshift_fragos_new)
power_median_new=spline(redshift_median, power_median,redshift_median_new)
power_unabsorbed_new=spline(redshift_unabsorbed, power_unabsorbed,redshift_unabsorbed_new)
power_low_new=spline(redshift_low, power_low,redshift_low_new)
power_high_new=spline(redshift_high, power_high,redshift_high_new)
power_power_new=spline(redshift_power, power_power,redshift_power_new)

fig1=plt.figure(dpi=72,figsize=(35.5, 31.0))
ax1= fig1.add_subplot(111)

plt.plot(redshift_unabsorbed_new,np.power(10,power_unabsorbed_new),linewidth=10, color='darkgreen', linestyle = '-',label=r'${\rm Unbsorbed\, SED\, (Fragos\,et\,al.\,2013)}$')
plt.plot(redshift_median_new,np.power(10,power_median_new),linewidth=15, color='black', linestyle = '-',label=r'${\rm Fiducial\, SED}$')
plt.plot(redshift_fragos_new,np.power(10,power_fragos_new),linewidth=10, color='red', linestyle = '-',label=r'${\rm Absorbed\, SED\, (Fragos\,et\,al.\,2013)}$')
plt.plot(redshift_power_new,np.power(10,power_power_new),linewidth=10,alpha=0.5, color='blue', linestyle = '-',label=r'${\rm Truncated\, power\, law}$')
#plt.plot(redshift_low_new,np.power(10,power_low_new),linewidth=10, color='black', linestyle = '--')
#plt.plot(redshift_high_new,np.power(10,power_high_new),linewidth=10, color='black', linestyle = '--')


ax1.set_xlim(6,20)
ax1.set_ylim(1.e-1,1.e+3)
ax1.set_yscale("log")
ax1.xaxis.set_label_text(r'${\rm z}$', fontsize = 120, color='black')
ax1.yaxis.set_label_text(r'${\rm \overline{\delta T_b}^2\Delta_{21}^2[mK^2]}$', fontsize = 120, color='black')
ax1.tick_params('both', labelsize=70, length=40, width=3, which='major',pad=20)
ax1.tick_params('both', length=25, width=1, which='minor')
plt.title(r'${\rm k=0.1\, Mpc^{-1},\, T_{vir}=5\times 10^4 K}$',fontsize=90,y=1.02)
plt.legend(fancybox=True, shadow=True, fontsize=65,loc='lower right')
plt.tight_layout()
plt.savefig('1Tvir5e4.pdf')
