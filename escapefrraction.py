
import numpy as np
import h5py
from astropy.table import Table

index=[]
indexpop3=[]
stellar_mass=[]
column_density=[]
stellar_masspop3=[]
column_densitypop3=[]
escape_fraction=[]
	
with h5py.File('poutput_0052_fesc_halos.h5','r') as hf1:
	for i in range(len(hf1.keys())):
		gp1 = hf1.get('Halo%08d'%(i))
		mass1=gp1.get('Mstar_pop2')
		mass1=np.array(mass1)
		mass2=np.array(gp1.get('Mstar_pop3'))
		total=mass1+mass2
		if total>0:
			index.append(i)
			stellar_mass.append(total)

index=np.array(index)
stellar_mass=np.array(stellar_mass)


with h5py.File('poutput_0052_fesc_halos.h5','r') as hf:
	for x in range((len(index))):
		column_galaxy=[]
		escape_fraction_galaxy=[]
		gp1 = hf.get('Halo%08d'%(index[x])+'/Pop2_Stars')
		for y in range(len(gp1.keys())):
			gp2=gp1.get('star%08d'%(y))
			column_star=np.array(gp2.get('NHI'))
			escape_fraction_star=np.exp(-column_star*1.13954390e-23)
		#	average_column_star=np.sum(column_star)/len(column_star)
			average_escape_fraction_star=np.sum(escape_fraction_star)/len(escape_fraction_star)
			print len(escape_fraction_star)
			escape_fraction_galaxy.append(average_escape_fraction_star)
		#	column_galaxy.append(average_column_star)
		gp3 = hf.get('Halo%08d'%(index[x])+'/Pop3_Stars')
		for z in range(len(gp3.keys())):
			gp4=gp3.get('star%08d'%(z))
			column_starpop3=np.array(gp4.get('NHI'))
			escape_fraction_starpop3=np.exp(-column_starpop3*1.13954390e-23)
			average_escape_fraction_starpop3=np.sum(escape_fraction_starpop3)/len(escape_fraction_starpop3)
			average_column_starpop3=np.sum(column_starpop3)/len(column_starpop3)
		#	escape_fraction_galaxy.append(average_escape_fraction_star)
			escape_fraction_galaxy.append(average_escape_fraction_starpop3)


		#column_galaxy=np.array(column_galaxy)
		#column_galaxy_average=np.sum(column_galaxy)/len(column_galaxy)
		#column_density.append(column_galaxy_average)
		escape_fraction_galaxy=np.array(escape_fraction_galaxy)
		escape_fraction_galaxy_average=np.sum(escape_fraction_galaxy)/len(escape_fraction_galaxy)
		escape_fraction.append(escape_fraction_galaxy_average)

#column_density=np.array(column_density)
escape_fraction=np.array(escape_fraction)

f4 = open('escape8.dat','w' )
for j in range(len(escape_fraction)):
	f4.write(str(stellar_mass[j]) + " " + str(escape_fraction[j]) + "\n")
f4.close()
