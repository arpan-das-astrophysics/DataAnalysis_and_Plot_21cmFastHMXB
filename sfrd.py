import numpy as np
import math
import pylab
import matplotlib.pyplot as plt
import matplotlib

data1 = np.loadtxt('sfrd_tvir5e4.dat')
z1=np.array(data1[:,0])
sfrd1=np.array(data1[:,1])

data2 = np.loadtxt('sfrd_tvir5e5.dat')
z2=np.array(data2[:,0])
sfrd2=np.array(data2[:,1])

constant=7.9e+27

data3 = np.loadtxt('mlim-15.dat')
z3m=np.array(data3[:,1])
z3l=np.array(data3[:,0])
z3h=np.array(data3[:,2])
rho3m=np.array(data3[:,4])
rho3l=np.array(data3[:,3])
rho3h=np.array(data3[:,5])
sfrd3m=np.power(10,rho3m)/constant
sfrd3l=np.power(10,rho3l)/constant
sfrd3h=np.power(10,rho3h)/constant

data4 = np.loadtxt('mlim-10.dat')
z4m=np.array(data4[:,1])
z4l=np.array(data4[:,0])
z4h=np.array(data4[:,2])
rho4m=np.array(data4[:,4])
rho4l=np.array(data4[:,3])
rho4h=np.array(data4[:,5])
sfrd4m=np.power(10,rho4m)/constant
sfrd4l=np.power(10,rho4l)/constant
sfrd4h=np.power(10,rho4h)/constant

data5 = np.loadtxt('mlim-17.dat')
z5m=np.array(data5[:,1])
z5l=np.array(data5[:,0])
z5h=np.array(data5[:,2])
rho5m=np.array(data5[:,4])
rho5l=np.array(data5[:,3])
rho5h=np.array(data5[:,5])
sfrd5m=np.power(10,rho5m)/constant
sfrd5l=np.power(10,rho5l)/constant
sfrd5h=np.power(10,rho5h)/constant

fig1=plt.figure(dpi=72,figsize=(35.5, 31.0))
ax1= fig1.add_subplot(111)

plt.plot(z1,sfrd1,linewidth=12, color='green', linestyle = '-',label=r'${\rm T_{vir}^{min}=5\times 10^4K}$')
plt.plot(z2,sfrd2,linewidth=12, color='blue', linestyle = '-',label=r'${\rm T_{vir}^{min}=5\times 10^5K}$')
plt.errorbar(z4m, sfrd4m, xerr=[z4m-z4l,z4h-z4m],yerr=[sfrd4m-sfrd4l,sfrd4h-sfrd4m], color='red',fmt='o',markersize=15,elinewidth=3,label=r'${\rm M_{UV}^{min}=-10\,(Bouwens\, et\, al\, 2015)}$')
plt.errorbar(z3m, sfrd3m, xerr=[z3m-z3l,z3h-z3m],yerr=[sfrd3m-sfrd3l,sfrd3h-sfrd3m], color='darkorange',fmt='o',markersize=15,elinewidth=3,label=r'${\rm M_{UV}^{min}=-15\,(Bouwens\, et\, al\, 2015)}$')
plt.errorbar(z5m, sfrd5m, xerr=[z5m-z5l,z5h-z5m],yerr=[sfrd5m-sfrd5l,sfrd5h-sfrd5m], color='purple',fmt='o',markersize=15,elinewidth=3,label=r'${\rm M_{UV}^{min}=-17\,(Bouwens\, et\, al\, 2015)}$')

#plt.plot(z3,sfrd3,'o', color='blue',markersize='20', label=)
#plt.plot(z4,sfrd4,'o', color='cyan',markersize='20', label=r'${\rm m_{lim<-10}(Bouwens\, et\, al\, 2015)}$')
ax1.set_xlim(5,25)
ax1.set_ylim(1.e-6,1.e+1)
plt.yscale('log', nonposy='clip')
ax1.xaxis.set_label_text(r'${\rm z}$', fontsize = 120, color='black')
ax1.yaxis.set_label_text(r'${\rm SFRD(M_\odot yr^{-1} cMpc^{-3})}$', fontsize = 120, color='black')
ax1.tick_params('both', labelsize=90, length=40, width=3, which='major',pad=20)
ax1.tick_params('both', length=25, width=1, which='minor')
plt.legend(fancybox=True, shadow=True, fontsize=65,loc='upper right')
plt.tight_layout()
plt.savefig('sfrd.pdf')

