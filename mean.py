import numpy as np
import math
import pylab
import matplotlib.pyplot as plt
import matplotlib
import h5py


redshift8_index=np.array([0,1,2,3,7,11,12])
redshift10_index=np.array([0,1,5,8,12,15,19])
redshift12_index=np.array([0,2,3,11,25,31])
redshift14_index=np.array([0,4])

stellarmass_redshift8=np.array([3.035e+05,1.177e+05,1.191e+04,3.506e+04,9951,1078,1775])
stellarmass_redshift10=np.array([1080,1.502e+04,3028,7604,1.368e+04,2001,266.1])
stellarmass_redshift12=np.array([2738,1043,115.6,1190,886.3,77.54])
stellarmass_redshift14=np.array([757.3,2815])

sfr_redshift8=stellarmass_redshift8/20.e+6
sfr_redshift10=stellarmass_redshift10/20.e+6
sfr_redshift12=stellarmass_redshift12/20.e+6
sfr_redshift14=stellarmass_redshift14/20.e+6



numerator=[]
denomenator=[]



with h5py.File('/home/dasarpan007/Desktop/John/Mean/z8.h5','r') as hf8:
	for j in range(len(redshift8_index)):
		gp8 = hf8.get('halo{0}'.format(redshift8_index[j]))
		opacity8= np.array(gp8.get('opacity_los'))

		for k in range(len(opacity8)):
			numerator.append(opacity8[k]*sfr_redshift8[j])
			denomenator.append(sfr_redshift8[j])

with h5py.File('/home/dasarpan007/Desktop/John/Mean/z10.h5','r') as hf10:
	for x in range(len(redshift10_index)):
		gp10 = hf10.get('halo{0}'.format(redshift10_index[x]))
		opacity10= np.array(gp10.get('opacity_los'))
		for y in range(len(opacity10)):
			numerator.append(opacity10[y]*sfr_redshift10[x])
			denomenator.append(sfr_redshift10[x])
			
with h5py.File('/home/dasarpan007/Desktop/John/Mean/z12.h5','r') as hf12:
	for a in range(len(redshift12_index)):
		gp12 = hf12.get('halo{0}'.format(redshift12_index[a]))
		opacity12= np.array(gp12.get('opacity_los'))
		for b in range(len(opacity12)):
			numerator.append(opacity12[b]*sfr_redshift12[a])
			denomenator.append(sfr_redshift12[a])

with h5py.File('/home/dasarpan007/Desktop/John/Mean/z14.h5','r') as hf14:
	for n in range(len(redshift14_index)):
		gp14 = hf14.get('halo{0}'.format(redshift14_index[n]))
		opacity14= np.array(gp14.get('opacity_los'))
		for m in range(len(opacity14)):
			numerator.append(opacity14[m]*sfr_redshift14[n])
			denomenator.append(sfr_redshift14[n])

				


numerator=np.array(numerator)
denomenator=np.array(denomenator)

kev=np.arange(0.1,10,.01)

for p in range(39,40):
	print p
	data=[]
	for q in range(len(numerator)):
		data.append(numerator[q][p])
	data=np.array(data)
	bins=np.linspace(0,1,1000)
	#histogram=np.histogram(data,bins=bins,weights=denomenator)
	#hist=histogram[0]/np.sum(denomenator)
	fig1=plt.figure(dpi=72)
	ax1= fig1.add_subplot(111)

