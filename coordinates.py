import numpy as np
import h5py

pop2index=[]
pop3index=[]
with h5py.File('output_0052_anyl.h5','r') as hf:
	gp = hf.get('Halo000012')
	mass1=np.array(gp.get('pop2_mass'))
	mass2=np.array(gp.get('pop3_mass'))
	x_pop2=np.array(gp.get('pop2_position_x'))
	y_pop2=np.array(gp.get('pop2_position_y'))
	z_pop2=np.array(gp.get('pop2_position_z'))
	x_pop3=np.array(gp.get('pop3_position_x'))
	y_pop3=np.array(gp.get('pop3_position_y'))
	z_pop3=np.array(gp.get('pop3_position_z'))			


pop2mass_output=[]
pop3mass_output=[]
with h5py.File('poutput_0052_fesc_halos.h5','r') as hf1:
	gp1=hf1.get('Halo00000012/Pop2_Stars/')
	gp2=hf1.get('Halo00000012/Pop3_Stars/')
	for y in range(len(gp1.keys())):
		gp3=gp1.get('star%08d'%(y))
		mass3=np.array(gp3.get('mass'))
		pop2mass_output.append(mass3)
	for z in range(len(gp1.keys())):
		gp4=gp2.get('star%08d'%(z))
		mass4=np.array(gp3.get('mass'))
		pop3mass_output.append(mass4)

pop2mass_output=np.array(pop2mass_output)
pop3mass_output=np.array(pop3mass_output)


for k in range(len(pop2mass_output)):
	for l in range(len(mass1)):
		if pop2mass_output[k]==mass1[l]:
			pop2index.append(l)

pop2index=np.array(pop2index)

for u in range(len(pop3mass_output)):
	for v in range(len(mass2)):
		if pop3mass_output[u]==mass2[v]:
			pop3index.append(v)

pop3index=np.array(pop3index)
X_final=[]
Y_final=[]
Z_final=[]

for n in range(len(pop2index)):
	X_final.append(x_pop2[pop2index[n]])
	Y_final.append(y_pop2[pop2index[n]])
	Z_final.append(z_pop2[pop2index[n]])


for m in range(len(pop3index)):
	X_final.append(x_pop3[pop3index[m]])
	Y_final.append(y_pop3[pop3index[m]])
	Z_final.append(z_pop3[pop3index[m]])	

X_final=np.array(X_final)
Y_final=np.array(Y_final)
Z_final=np.array(Z_final)
f4 = open('halo12.dat','w' )
for a in range(len(X_final)):
	f4.write(str(X_final[a]) + " " + str(Y_final[a]) +  " " + str(Z_final[a]) +"\n")
f4.close()

