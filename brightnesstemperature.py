import numpy as np
import math
import pylab
import matplotlib.pyplot as plt
import matplotlib
from scipy.interpolate import spline

data1 = np.loadtxt('Tb_median.dat')
z1=np.array(data1[:,0])
Tb1=np.array(data1[:,1])
z1new=np.linspace(np.amin(z1),np.amax(z1),10000)

data2 = np.loadtxt('Tb_fragos.dat')
z2=np.array(data2[:,0])
Tb2=np.array(data2[:,1])
z2new=np.linspace(np.amin(z2),np.amax(z2),10000)

data3 = np.loadtxt('Tb_unabsorbed.dat')
z3=np.array(data3[:,0])
Tb3=np.array(data3[:,1])
z3new=np.linspace(np.amin(z3),np.amax(z3),10000)

data4 = np.loadtxt('Tb_low.dat')
z4=np.array(data4[:,0])
Tb4=np.array(data4[:,1])
z4new=np.linspace(np.amin(z4),np.amax(z4),10000)

data5 = np.loadtxt('Tb_up.dat')
z5=np.array(data5[:,0])
Tb5=np.array(data5[:,1])
z5new=np.linspace(np.amin(z5),np.amax(z5),10000)

Tb1new=spline(z1, Tb1,z1new)
Tb2new=spline(z2, Tb2,z2new)
Tb3new=spline(z3, Tb3,z3new)
Tb4new=spline(z4, Tb4,z4new)
Tb5new=spline(z5, Tb5,z5new)


fig1=plt.figure(dpi=72,figsize=(35.0, 30.0))
ax1= fig1.add_subplot(111)
plt.plot(z1new,Tb1new,linewidth=10, color='blue', linestyle = '-',label=r'${\rm Simulation}$')
plt.plot(z2new,Tb2new,linewidth=10, color='red', linestyle = '-',label=r'${\rm Absorbed\, SED\,Fragos\,et\,al.\,2013}$')
plt.plot(z3new,Tb3new,linewidth=10, color='green', linestyle = '-',label=r'${\rm Unabsorbed\, SED\,et\,al.\,2013}$')
ax1.set_xlim(6,25)
plt.fill_between(z4new, Tb4new, Tb5new, color='grey', alpha='0.3')
ax1.xaxis.set_label_text(r'${\rm z}$', fontsize = 90, color='black')
ax1.yaxis.set_label_text(r'${\rm \overline{\delta T_b}\,(mK)}$', fontsize = 90, color='black')
ax1.tick_params('both', labelsize=70, length=40, width=3, which='major')
ax1.tick_params('both', length=25, width=1, which='minor')
ax1.set_yticks([-150,-125,-100,-75,-50,-25,0,25,50])
ax1.set_xticks([6,10,15,20,25])
ax1.get_yaxis().get_major_formatter()
plt.legend(fancybox=True, shadow=True, fontsize=55,loc='upper right')
plt.title(r'${\rm T_{vir}=5\times 10^5 K}$',fontsize=90,y=1.02)
plt.savefig('Tvir5e5.pdf')

