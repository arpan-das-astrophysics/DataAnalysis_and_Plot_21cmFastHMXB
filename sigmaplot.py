import numpy as np
import math
import pylab
import matplotlib.pyplot as plt
import matplotlib
from scipy import stats

data1 = np.loadtxt('stat.dat')
mean=np.array(data1[:,1])
up=np.array(data1[:,2])
low=np.array(data1[:,3])

PI=3.14
hplank=6.62606896e-27
NU_over_EV=1.60217646e-12 / hplank
NUIONIZATION=13.60*NU_over_EV
HeI_NUIONIZATION=24.59*NU_over_EV
HeII_NUIONIZATION=(NUIONIZATION*4.0) 

kev = np.arange(0.1,10.0,.01)
pi= 3.14159
h=4.135667662e-18
c=299792458
hertz=2.417990504024e+17*kev

#####################################################
#Define the Hydrogen, Helium and metal cross sections
######################################################
def HI(frequency,result=[]):
	for nu in frequency:
		if (nu < NUIONIZATION):
			result.append(0)	    
		else:
			epsilon = math.sqrt( nu/NUIONIZATION - 1)
			#epsilon =math.sqrt( e/0.0136 - 1)
			result.append((6.3e-18) * math.pow(NUIONIZATION/nu, 4) * math.exp(4-(4*math.atan(epsilon)/epsilon)) / (1-math.exp(-2*PI/epsilon)))
	return result

def HeI(frequency,result=[]):
	for nu in frequency:
		if (nu < HeI_NUIONIZATION):
			result.append(0)
		else:
			x = nu/NU_over_EV/13.61 - 0.4434
			y = math.sqrt(x*x + math.pow(2.136, 2))
			result.append(9.492e-16*((x-1)*(x-1) + 2.039*2.039) * math.pow(y, (0.5 * 3.188 - 5.5))* math.pow(1.0 + math.sqrt(y/1.469), -3.188))

	return result

def metals(energy,result=[]):
	for e in energy:
		if(0.030<= e < 0.100):
			result.append((17.3 + 608.1 * e - 2150.0 * e * e)*math.pow(e,-3)*1.0e-24)
		elif(0.100<= e <.284):
			result.append((34.6 + 267.9 * e- 476.1 * e * e)*math.pow(e,-3)*1.0e-24)
		elif(0.284<= e <0.400):
			result.append((78.1+18.8*e+4.3*e*e)*math.pow(e,-3)*1.0e-24)
		elif(0.400<= e <0.532):
			result.append((71.4+66.8*e-51.4*e*e)*math.pow(e,-3)*1.0e-24)
		elif(0.533<= e <0.707):
			result.append((95.5+145.8*e-61.1*e*e)*math.pow(e,-3)*1.0e-24)
		elif(0.707<= e <0.867):
			result.append((308.9-380.6*e+294.0*e*e)*math.pow(e,-3)*1.0e-24)
		elif(0.867<= e <1.303):
			result.append((120.6+169.3*e-47.7*e*e)*math.pow(e,-3)*1.0e-24)
		elif(1.303<= e <1.840):
			result.append((141.3+146.8*e-31.5*e*e)*math.pow(e,-3)*1.0e-24)
		elif(1.840<= e <2.471):
			result.append((202.7+104.7*e-17.0*e*e)*math.pow(e,-3)*1.0e-24)
		elif(2.471<= e <3.210):
			result.append((342.7+18.7*e)*math.pow(e,-3)*1.0e-24)
		elif(3.210<= e <4.038):
			result.append((352.2+18.7*e)*math.pow(e,-3)*1.0e-24)
		elif(4.038<= e <7.111):
			result.append((433.9 - 2.4*e + 0.75*e*e)*math.pow(e,-3)*1.0e-24)
		elif(7.111<= e <8.331):
			result.append((629.0 + 30.9*e)*math.pow(e,-3)*1.0e-24)
		else:
			result.append((701.2 + 25.2*e)*math.pow(e,-3)*1.0e-24)

	return result

cross_section_HI=np.array(HI(hertz))
cross_section_HeI=np.array(HeI(hertz))
cross_section_metals=np.array(metals(kev))-cross_section_HI-cross_section_HeI/10.0

NH1=math.pow(10,21.4)
tau1=(cross_section_HI+cross_section_HeI/10.0+0.0*cross_section_metals)*NH1
opacity1=np.exp(-tau1)

tau3=(cross_section_HI+cross_section_HeI/10.0+1.0*cross_section_metals)*math.pow(10,20.8)
opacity3=np.exp(-tau3)

NH2=math.pow(10,21)*5
tau2=(cross_section_HI+cross_section_HeI/10.0+cross_section_metals)*NH2
opacity2=np.exp(-tau2)

tau4=(cross_section_HI+cross_section_HeI/10.0+1.0*cross_section_metals)*math.pow(10,21)
opacity4=np.exp(-tau4)


fig1=plt.figure(dpi=72,figsize=(35.5, 31.0))
ax1= fig1.add_subplot(111)
plt.plot(kev,mean, linewidth=20, color='black', linestyle = '-', label=r'${\rm Median}$')
plt.plot([], [], color='grey', linewidth=10, alpha=0.3, label=r'${\rm 68\%\, CL }$')
#plt.plot(kev,opacity1, linewidth=12, color='green', linestyle = '--',dashes=(50,20), label=r'${\rm N_{HI}=10^{21.4}\, cm^{-2},Z=0}$')
plt.plot(kev,opacity3, linewidth=12, color='blue', linestyle = '--', dashes=(50,20),label=r'${\rm N_{HI}=10^{20.8}\, cm^{-2},Z=Z_\odot}$')
plt.plot(kev,opacity4, linewidth=12, color='cyan', linestyle = '--', dashes=(50,20),label=r'${\rm N_{HI}=10^{21}\, cm^{-2},Z=Z_\odot}$')
#plt.plot(kev,opacity2, linewidth=12, color='red', linestyle = '--',dashes=(50,20), label=r'${\rm N_{HI}=5\times 10^{21}\, cm^{-2},Z=Z_\odot}$')
ax1.set_xscale("log")
#ax1.set_yscale("log")
ax1.set_ylim(0,1)

plt.fill_between(kev, up, low, color='grey', alpha='0.3')
ax1.set_xlim(0.1,5)
ax1.xaxis.set_label_text(r'${\rm Energy(keV)}$', fontsize = 120, color='black')
ax1.yaxis.set_label_text(r'${\rm e^{-\tau}}$', fontsize = 120, color='black')
ax1.tick_params('both', labelsize=90, length=40, width=3, which='major',pad=40)
ax1.tick_params('both', length=25, width=1, which='minor')
ax1.set_xticks([0.1,1.0,10])
#ax1.set_yticks([0.001,0.01,0.1,1])
#ax1.get_xaxis().get_major_formatter()
ax1.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax1.get_yaxis().get_major_formatter()
plt.legend(fancybox=True, shadow=True, fontsize=60,loc='lower right')
plt.tight_layout()
plt.savefig('opacity.pdf')


