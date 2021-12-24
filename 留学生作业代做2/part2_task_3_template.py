import numpy as np
import pandas as pd
import random
def read_data(file_patients, file_centres):
	df = pd.read_csv(file_patients).loc[:,['patient_id','x_coord','y_coord','eligible']]
	df1 = pd.read_csv(file_centres).loc[:,['centre_id','x_coord','y_coord','capacity']]
	patients = np.array(df)  # Change/remove this line
	centres = np.array(df1) # Change/remove this line

	# Please, introduce your answer here

	return patients, centres

def euclidean_distance(x1, y1, x2, y2):
	d = ((x1-x2)**2 + (y1-y2)**2) ** float(1/2)


	# Please, introduce your answer here

	return d

def allocation(patients, centres, days):
	eligible = [e for e in patients[:,3]]
	patient_id = [p for p in patients[:,0]]
	x_coord = [x for x in patients[:,1]]
	y_coord = [y for y in patients[:,2]]
	centre_id = [c for c in centres[:,0]]
	x_coord1 = [x for x in centres[:,1]]
	y_coord1 = [y for y in centres[:,2]]
	capacity = [c for c in centres[:,3]]
	e = []
	sum_usage = []
	number_0 = 0
	number_1 = 0
	number_2 = 0
	number_3 = 0
	for i in range(len(eligible)):
		if eligible[i] == 1:
			a = random.randint(0,3)
			b = random.randint(0,int(days-1))
			if a == 0:
				d = euclidean_distance(x_coord[i],y_coord[i],x_coord1[0],y_coord1[0])
				c = [patient_id[i], a, b, d]
				e.append(c)
				number_0 += 1
			if a == 1:
				d = euclidean_distance(x_coord[i],y_coord[i],x_coord1[1],y_coord1[1])
				c = [patient_id[i], a, b, d]
				e.append(c)
				number_1 += 1
			if a == 2:
				d = euclidean_distance(x_coord[i],y_coord[i],x_coord1[2],y_coord1[2])
				c = [patient_id[i], a, b, d]
				e.append(c)
				number_2 += 1
			if a == 3:
				d = euclidean_distance(x_coord[i],y_coord[i],x_coord1[3],y_coord1[3])
				c = [patient_id[i], a, b, d]
				e.append(c)
				number_3 += 1
	for i in range(days):
		l = random.randint(0,int(days-1))
		if l == 0:
			f = [number_0,0]
			g = [number_1,0]
			h = [number_2,0]
			j = [number_3,0]
			sum_usage.append(f)
			sum_usage.append(g)
			sum_usage.append(h)
			sum_usage.append(j)
		if l == 1:
			f = [number_0,1]
			g = [number_1,1]
			h = [number_2,1]
			j = [number_3,1]
			sum_usage.append(f)
			sum_usage.append(g)
			sum_usage.append(h)
			sum_usage.append(j)
		if l == 2:
			f = [number_0,2]
			g = [number_1,2]
			h = [number_2,2]
			j = [number_3,2]
			sum_usage.append(f)
			sum_usage.append(g)
			sum_usage.append(h)
			sum_usage.append(j)


	centre_usage = np.array(sum_usage)  # Change/remove this line

	patient_allocation = np.array(e)  # Change/remove this line
	total_distance = sum(patient_allocation[:,3])  # Change/remove this line


	# Please, introduce your answer here

	return patient_allocation, centre_usage, total_distance


if __name__ == '__main__':
	file_patients = 'data/t3_patients_example.csv'  # You can change this value for testing
	file_centres = 'data/t3_centres_example.csv'  # You can change this value for testing
	days = 3  # You can change this value for testing


	# The code below is for your reference, so you can visualise your answer
	patients, centres = read_data(file_patients, file_centres)
	patient_allocation, centre_usage, total_distance = allocation(patients, centres, days)
	print('Centre usage matrix:')
	print(centre_usage)

	print('Patient allocation matrix:')
	print(patient_allocation)

	print('Total allocation distance:', total_distance)