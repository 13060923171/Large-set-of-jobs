import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif']=['SimHei']
def read_vegetable_data(filename):
	df = pd.read_csv(filename)
	# Please, introduce your answer here

	return df

def generate_plot_1(df):
	df = df.dropna()
	df = df.iloc[:, 3:18]
	cabbage_1 = (float(df.iloc[1, 2]) + float(df.iloc[2,2]) + float(df.iloc[3,2])) /3
	cabbage_2 = (float(df.iloc[1, 3]) + float(df.iloc[2, 3]) + float(df.iloc[3, 3])) / 3
	cabbage_3 = (float(df.iloc[1, 4]) + float(df.iloc[2, 4]) + float(df.iloc[3, 4])) / 3
	cabbage_4 = (float(df.iloc[1, 5]) + float(df.iloc[2, 5]) + float(df.iloc[3, 5])) / 3
	cabbage_5 = (float(df.iloc[1, 6]) + float(df.iloc[2, 6]) + float(df.iloc[3, 6])) / 3
	cabbage_6 = (float(df.iloc[1, 7]) + float(df.iloc[2, 7]) + float(df.iloc[3, 7])) / 3
	cabbage_7 = (float(df.iloc[1, 8]) + float(df.iloc[2, 8]) + float(df.iloc[3, 8])) / 3
	cabbage_8 = (float(df.iloc[1, 9]) + float(df.iloc[2, 9]) + float(df.iloc[3, 9])) / 3
	cabbage_9 = (float(df.iloc[1, 10]) + float(df.iloc[2, 10]) + float(df.iloc[3, 10])) / 3
	cabbage_10 = (float(df.iloc[1, 11]) + float(df.iloc[2, 11]) + float(df.iloc[3, 11])) / 3
	cabbage_11 = (float(df.iloc[1, 12]) + float(df.iloc[2, 12]) + float(df.iloc[3, 12])) / 3
	cabbage_12 = (float(df.iloc[1, 13]) + float(df.iloc[2, 13]) + float(df.iloc[3, 13])) / 3
	carrots_1= (float(df.iloc[4, 2]) + float(df.iloc[5,2])) /2
	carrots_2 = (float(df.iloc[4, 3]) + float(df.iloc[5, 3])) / 2
	carrots_3 = (float(df.iloc[4, 4]) + float(df.iloc[5, 4])) / 2
	carrots_4 = (float(df.iloc[4, 5]) + float(df.iloc[5, 5])) / 2
	carrots_5 = (float(df.iloc[4, 6]) + float(df.iloc[5, 6])) / 2
	carrots_6 = (float(df.iloc[4, 7]) + float(df.iloc[5, 7])) / 2
	carrots_7 = (float(df.iloc[4, 8]) + float(df.iloc[5, 8])) / 2
	carrots_8 = (float(df.iloc[4, 9]) + float(df.iloc[5, 9])) / 2
	carrots_9 = (float(df.iloc[4, 10]) + float(df.iloc[5, 10])) / 2
	carrots_10 = (float(df.iloc[4, 11]) + float(df.iloc[5, 11])) / 2
	carrots_11 = (float(df.iloc[4, 12]) + float(df.iloc[5, 12])) / 2
	carrots_12 = (float(df.iloc[4, 13]) + float(df.iloc[5, 13])) / 2
	cauliflower_1 = (float(df.iloc[6, 2]) + float(df.iloc[7,2]) + float(df.iloc[8,2])) /3
	cauliflower_2 = (float(df.iloc[6, 3]) + float(df.iloc[7, 3]) + float(df.iloc[8, 3])) / 3
	cauliflower_3 = (float(df.iloc[6, 4]) + float(df.iloc[7, 4]) + float(df.iloc[8, 4])) / 3
	cauliflower_4 = (float(df.iloc[6, 5]) + float(df.iloc[7, 5]) + float(df.iloc[8, 5])) / 3
	cauliflower_5 = (float(df.iloc[6, 6]) + float(df.iloc[7, 6]) + float(df.iloc[8, 6])) / 3
	cauliflower_6 = (float(df.iloc[6, 7]) + float(df.iloc[7, 7]) + float(df.iloc[8, 7])) / 3
	cauliflower_7 = (float(df.iloc[6, 8]) + float(df.iloc[7, 8]) + float(df.iloc[8, 8])) / 3
	cauliflower_8 = (float(df.iloc[6, 9]) + float(df.iloc[7, 9]) + float(df.iloc[8, 9])) / 3
	cauliflower_9 = (float(df.iloc[6, 10]) + float(df.iloc[7, 10]) + float(df.iloc[8, 10])) / 3
	cauliflower_10 = (float(df.iloc[6, 11]) + float(df.iloc[7, 11]) + float(df.iloc[8, 11])) / 3
	cauliflower_11 = (float(df.iloc[6, 12]) + float(df.iloc[7, 12]) + float(df.iloc[8, 12])) / 3
	cauliflower_12 = (float(df.iloc[6, 13]) + float(df.iloc[7, 13]) + float(df.iloc[8, 13])) / 3
	lettuce_1 = (float(df.iloc[9, 2]) + float(df.iloc[10,2]) + float(df.iloc[11,2])+ float(df.iloc[12,2])+ float(df.iloc[13,2])+ float(df.iloc[14,2])) /6
	lettuce_2 = (float(df.iloc[9, 3]) + float(df.iloc[10, 3]) + float(df.iloc[11, 3]) + float(df.iloc[12, 3]) + float(
		df.iloc[13, 3]) + float(df.iloc[14, 3])) / 6
	lettuce_3 = (float(df.iloc[9, 4]) + float(df.iloc[10, 4]) + float(df.iloc[11, 4]) + float(df.iloc[12, 4]) + float(
		df.iloc[13, 4]) + float(df.iloc[14, 4])) / 6
	lettuce_4 = (float(df.iloc[9, 5]) + float(df.iloc[10, 5]) + float(df.iloc[11, 5]) + float(df.iloc[12, 5]) + float(
		df.iloc[13, 5]) + float(df.iloc[14, 5])) / 6
	lettuce_5 = (float(df.iloc[9, 6]) + float(df.iloc[10, 6]) + float(df.iloc[11, 6]) + float(df.iloc[12, 6]) + float(
		df.iloc[13, 6]) + float(df.iloc[14, 6])) / 6
	lettuce_6 = (float(df.iloc[9, 7]) + float(df.iloc[10, 7]) + float(df.iloc[11, 7]) + float(df.iloc[12, 7]) + float(
		df.iloc[13, 7]) + float(df.iloc[14, 7])) / 6
	lettuce_7 = (float(df.iloc[9, 8]) + float(df.iloc[10, 8]) + float(df.iloc[11, 8]) + float(df.iloc[12, 8]) + float(
		df.iloc[13, 8]) + float(df.iloc[14, 8])) / 6
	lettuce_8 = (float(df.iloc[9, 9]) + float(df.iloc[10, 9]) + float(df.iloc[11, 9]) + float(df.iloc[12, 9]) + float(
		df.iloc[13, 9]) + float(df.iloc[14, 9])) / 6
	lettuce_9 = (float(df.iloc[9, 10]) + float(df.iloc[10, 10]) + float(df.iloc[11, 10]) + float(df.iloc[12, 10]) + float(
		df.iloc[13, 10]) + float(df.iloc[14, 10])) / 6
	lettuce_10 = (float(df.iloc[9, 11]) + float(df.iloc[10, 11]) + float(df.iloc[11, 11]) + float(df.iloc[12, 11]) + float(
		df.iloc[13, 11]) + float(df.iloc[14, 11])) / 6
	lettuce_11 = (float(df.iloc[9, 12]) + float(df.iloc[10, 12]) + float(df.iloc[11, 12]) + float(df.iloc[12, 12]) + float(
		df.iloc[13, 12]) + float(df.iloc[14, 12])) / 6
	lettuce_12 = (float(df.iloc[9, 13]) + float(df.iloc[10, 13]) + float(df.iloc[11, 13]) + float(df.iloc[12, 13]) + float(
		df.iloc[13, 13]) + float(df.iloc[14, 13])) / 6

	spinach_1 = (float(df.iloc[15, 2]) + float(df.iloc[16,2])) /2
	spinach_2 = (float(df.iloc[15, 3]) + float(df.iloc[16, 3])) / 2
	spinach_3 = (float(df.iloc[15, 4]) + float(df.iloc[16, 4])) / 2
	spinach_4 = (float(df.iloc[15, 5]) + float(df.iloc[16, 5])) / 2
	spinach_5 = (float(df.iloc[15, 6]) + float(df.iloc[16, 6])) / 2
	spinach_6 = (float(df.iloc[15, 7]) + float(df.iloc[16, 7])) / 2
	spinach_7 = (float(df.iloc[15, 8]) + float(df.iloc[16, 8])) / 2
	spinach_8 = (float(df.iloc[15, 9]) + float(df.iloc[16, 9])) / 2
	spinach_9 = (float(df.iloc[15, 10]) + float(df.iloc[16, 10])) / 2
	spinach_10 = (float(df.iloc[15, 11]) + float(df.iloc[16, 11])) / 2
	spinach_11 = (float(df.iloc[15, 12]) + float(df.iloc[16, 12])) / 2
	spinach_12 = (float(df.iloc[15, 13]) + float(df.iloc[16, 13])) / 2
	potatoes_1 = (float(df.iloc[17, 2]) + float(df.iloc[18,2])) /2
	potatoes_2 = (float(df.iloc[17, 3]) + float(df.iloc[18, 3])) / 2
	potatoes_3 = (float(df.iloc[17, 4]) + float(df.iloc[18, 4])) / 2
	potatoes_4 = (float(df.iloc[17, 5]) + float(df.iloc[18, 5])) / 2
	potatoes_5 = (float(df.iloc[17, 6]) + float(df.iloc[18, 6])) / 2
	potatoes_6 = (float(df.iloc[17, 7]) + float(df.iloc[18, 7])) / 2
	potatoes_7 = (float(df.iloc[17, 8]) + float(df.iloc[18, 8])) / 2
	potatoes_8 = (float(df.iloc[17, 9]) + float(df.iloc[18, 9])) / 2
	potatoes_9 = (float(df.iloc[17, 10]) + float(df.iloc[18, 10])) / 2
	potatoes_10 = (float(df.iloc[17, 11]) + float(df.iloc[18, 11])) / 2
	potatoes_11 = (float(df.iloc[17, 12]) + float(df.iloc[18, 12])) / 2
	potatoes_12 = (float(df.iloc[17, 13]) + float(df.iloc[18, 13])) / 2
	sweet_potatoes_1 = (float(df.iloc[19, 2]) + float(df.iloc[20,2])) /2
	sweet_potatoes_2 = (float(df.iloc[19, 3]) + float(df.iloc[20, 3])) / 2
	sweet_potatoes_3 = (float(df.iloc[19, 4]) + float(df.iloc[20, 4])) / 2
	sweet_potatoes_4 = (float(df.iloc[19, 5]) + float(df.iloc[20, 5])) / 2
	sweet_potatoes_5 = (float(df.iloc[19, 6]) + float(df.iloc[20, 6])) / 2
	sweet_potatoes_6 = (float(df.iloc[19, 7]) + float(df.iloc[20, 7])) / 2
	sweet_potatoes_7 = (float(df.iloc[19, 8]) + float(df.iloc[20, 8])) / 2
	sweet_potatoes_8 = (float(df.iloc[19, 9]) + float(df.iloc[20, 9])) / 2
	sweet_potatoes_9 = (float(df.iloc[19, 10]) + float(df.iloc[20, 10])) / 2
	sweet_potatoes_10 = (float(df.iloc[19, 11]) + float(df.iloc[20, 11])) / 2
	sweet_potatoes_11 = (float(df.iloc[19, 12]) + float(df.iloc[20, 12])) / 2
	sweet_potatoes_12 = (float(df.iloc[19, 13]) + float(df.iloc[20, 13])) / 2
	sum_cabbage = [cabbage_1,cabbage_2,cabbage_3,cabbage_4,cabbage_5,cabbage_6,cabbage_7,cabbage_8,cabbage_9,cabbage_10,cabbage_11,cabbage_12]
	sum_carrots = [carrots_1,carrots_2,carrots_3,carrots_4,carrots_5,carrots_6,carrots_7,carrots_8,carrots_9,carrots_10,carrots_11,carrots_12]
	sum_cauliflower = [cauliflower_1,cauliflower_2, cauliflower_3, cauliflower_4, cauliflower_5, cauliflower_6, cauliflower_7, cauliflower_8, cauliflower_9, cauliflower_10,cauliflower_11, cauliflower_12]
	sum_lettuce = [lettuce_1,lettuce_2,lettuce_3,lettuce_4,lettuce_5,lettuce_6,lettuce_7,lettuce_8,lettuce_9,lettuce_10,lettuce_11,lettuce_12]
	sum_spinach = [spinach_1,spinach_2,spinach_3,spinach_4,spinach_5,spinach_6,spinach_7,spinach_8,spinach_9,spinach_10,spinach_11,spinach_12]
	sum_potatoes = [potatoes_1,potatoes_2,potatoes_3,potatoes_4,potatoes_5,potatoes_6,potatoes_7,potatoes_8,potatoes_9,potatoes_10,potatoes_11,potatoes_12]
	sum_sweet_potatoes = [sweet_potatoes_1,sweet_potatoes_2,sweet_potatoes_3,sweet_potatoes_4,sweet_potatoes_5,sweet_potatoes_6,sweet_potatoes_7,sweet_potatoes_8,sweet_potatoes_9,sweet_potatoes_10,sweet_potatoes_11,sweet_potatoes_12]
	x = np.arange(12)
	x_data = ['{}月'.format(i) for i in range(1, 13)]
	bar_width = 0.1
	plt.bar(x, sum_cabbage, bar_width, label='cabbage', color="IndianRed", align="center", alpha=0.5)
	plt.bar(x + bar_width, sum_carrots, bar_width, label='carrots', color="HotPink", align="center", alpha=0.5)
	plt.bar(x + bar_width+ bar_width, sum_cauliflower, bar_width, label='cauliflower', color="Orange", align="center", alpha=0.5)
	plt.bar(x + bar_width+ bar_width+ bar_width, sum_lettuce, bar_width, label='lettuce', color="Yellow", align="center", alpha=0.5)
	plt.bar(x + bar_width+ bar_width+ bar_width+ bar_width, sum_spinach, bar_width, label='spinach', color="DarkKhaki", align="center", alpha=0.5)
	plt.bar(x + bar_width+ bar_width+ bar_width+ bar_width+ bar_width, sum_potatoes, bar_width, label='potatoes', color="Orchid", align="center", alpha=0.5)
	plt.bar(x + bar_width+ bar_width+ bar_width+ bar_width+ bar_width+ bar_width, sum_sweet_potatoes, bar_width, label='weet_potatoes', color="Red", align="center", alpha=0.5)
	plt.xticks(x + bar_width / 2, x_data)
	plt.legend()
	plt.show()
	# Code to generate Plot 1 (show or save to file)

	# Please, introduce your answer here
	
	print('Plot 1 not completed yet.') # Remove this line when completed.

def generate_plot_2(df, vegetable):
	df = df.iloc[19:27,3:18]
	df = df.dropna()
	conv_1 = (float(df.iloc[0, 2]) + float(df.iloc[2,2]) + float(df.iloc[3,2]) + float(df.iloc[5,2])) / 4
	conv_2 = (float(df.iloc[0, 3]) + float(df.iloc[2, 3]) + float(df.iloc[3, 3]) + float(df.iloc[5, 3])) / 4
	conv_3 = (float(df.iloc[0, 4]) + float(df.iloc[2, 4]) + float(df.iloc[3, 4]) + float(df.iloc[5, 4])) / 4
	conv_4 = (float(df.iloc[0, 5]) + float(df.iloc[2, 5]) + float(df.iloc[3, 5]) + float(df.iloc[5, 5])) / 4
	conv_5 = (float(df.iloc[0, 6]) + float(df.iloc[2, 6]) + float(df.iloc[3, 6]) + float(df.iloc[5, 6])) / 4
	conv_6 = (float(df.iloc[0, 7]) + float(df.iloc[2, 7]) + float(df.iloc[3, 7]) + float(df.iloc[5, 7])) / 4
	conv_7 = (float(df.iloc[0, 8]) + float(df.iloc[2, 8]) + float(df.iloc[3, 8]) + float(df.iloc[5, 8])) / 4
	conv_8 = (float(df.iloc[0, 9]) + float(df.iloc[2, 9]) + float(df.iloc[3, 9]) + float(df.iloc[5, 9])) / 4
	conv_9 = (float(df.iloc[0, 10]) + float(df.iloc[2,10]) + float(df.iloc[3, 10]) + float(df.iloc[5, 10])) / 4
	conv_10 = (float(df.iloc[0, 11]) + float(df.iloc[2, 11]) + float(df.iloc[3, 11]) + float(df.iloc[5, 11])) / 4
	conv_11 = (float(df.iloc[0, 12]) + float(df.iloc[2, 12]) + float(df.iloc[3, 12]) + float(df.iloc[5, 12])) / 4
	conv_12 = (float(df.iloc[0, 13]) + float(df.iloc[2, 13]) + float(df.iloc[3, 13]) + float(df.iloc[5, 13])) / 4
	org_1 = (float(df.iloc[1,2]) + float(df.iloc[4,2])) / 2
	org_2 = (float(df.iloc[1, 3]) + float(df.iloc[4, 3])) / 2
	org_3 = (float(df.iloc[1, 4]) + float(df.iloc[4, 4])) / 2
	org_4 = (float(df.iloc[1, 5]) + float(df.iloc[4, 5])) / 2
	org_5 = (float(df.iloc[1, 6]) + float(df.iloc[4, 6])) / 2
	org_6 = (float(df.iloc[1, 7]) + float(df.iloc[4, 7])) / 2
	org_7 = (float(df.iloc[1, 8]) + float(df.iloc[4, 8])) / 2
	org_8 = (float(df.iloc[1, 9]) + float(df.iloc[4, 9])) / 2
	org_9 = (float(df.iloc[1, 10]) + float(df.iloc[4, 10])) / 2
	org_10 = (float(df.iloc[1, 11]) + float(df.iloc[4, 11])) / 2
	org_11 = (float(df.iloc[1, 12]) + float(df.iloc[4, 12])) / 2
	org_12 = (float(df.iloc[1, 13]) + float(df.iloc[4, 13])) / 2
	x = np.arange(12)
	sum_org = [org_1,org_2,org_3,org_4,org_5,org_6,org_7,org_8,org_9,org_10,org_11,org_12]
	sum_conv = [conv_1,conv_2,conv_3,conv_4,conv_5,conv_6,conv_7,conv_8,conv_9,conv_10,conv_11,conv_12]
	x_data = ['{}月'.format(i) for i in range(1,13)]
	bar_width = 0.35
	plt.bar(x, sum_org,bar_width,label='org',color="red",align="center",alpha=0.5)
	plt.bar(x+bar_width,sum_conv,bar_width,label='conv',color="blue",align="center",alpha=0.5)
	plt.xticks(x+bar_width/2, x_data)
	plt.legend()
	plt.show()
	# Code to generate Plot 2 (show or save to file)
	
	# Please, introduce your answer here
	
	print('Plot 2 not completed yet.') # Remove this line when completed.


def find_cheapest_month(df, vegetable, organic=None):
	cheapest_month = 'Not completed yet'  # Change/remove this line
	df = df.loc[1:50,[' Wholesale vegetable prices, organic and conventional, monthly and annual, 2013','Unnamed: 3','Unnamed: 5','Unnamed: 6','Unnamed: 7','Unnamed: 8','Unnamed: 9','Unnamed: 10','Unnamed: 11','Unnamed: 12','Unnamed: 13','Unnamed: 14','Unnamed: 15','Unnamed: 16']]
	df = df.dropna()
	list_name = [str(n) for n in df[' Wholesale vegetable prices, organic and conventional, monthly and annual, 2013']]
	list_Organic_Conventional = [str(i) for i in df['Unnamed: 3']]
	jan_13 = [float(j) for j in df['Unnamed: 5']]
	feb_13 = [float(j) for j in df['Unnamed: 6']]
	mar_13 = [float(j) for j in df['Unnamed: 7']]
	apr_13 = [float(j) for j in df['Unnamed: 8']]
	may_13 = [float(j) for j in df['Unnamed: 9']]
	jun_13 = [float(j) for j in df['Unnamed: 10']]
	jul_13 = [float(j) for j in df['Unnamed: 11']]
	aug_13 = [float(j) for j in df['Unnamed: 12']]
	sep_13 = [float(j) for j in df['Unnamed: 13']]
	oct_13 = [float(j) for j in df['Unnamed: 14']]
	nov_13 = [float(j) for j in df['Unnamed: 15']]
	dec_13 = [float(j) for j in df['Unnamed: 16']]
	sum_list_sum = []
	for i in range(len(list_name)):
		if vegetable in list_name[i]:
			if organic == True and list_Organic_Conventional[i] == 'Org':
				sum_list = [jan_13[i],feb_13[i],feb_13[i],mar_13[i],apr_13[i],may_13[i],jun_13[i],jul_13[i],aug_13[i],sep_13[i],oct_13[i],nov_13[i],dec_13[i]]
				sum_list_sum.append(sum_list)
			elif organic == False and list_Organic_Conventional[i] == 'Conv':
				sum_list = [jan_13[i],feb_13[i],feb_13[i],mar_13[i],apr_13[i],may_13[i],jun_13[i],jul_13[i],aug_13[i],sep_13[i],oct_13[i],nov_13[i],dec_13[i]]
				sum_list_sum.append(sum_list)
	min1 = min(sum_list_sum)
	number = min1.index(min(min1))
	if int(number) == 0:
		return 'Jan-13'
	elif int(number) == 1:
		return 'Feb-13'
	elif int(number) == 2:
		return 'Mar-13'
	elif int(number) == 3:
		return 'Apr-13'
	elif int(number) == 4:
		return 'May-13'
	elif int(number) == 5:
		return 'Jun-13'
	elif int(number) == 6:
		return 'Jul-13'
	elif int(number) == 7:
		return 'Aug-13'
	elif int(number) == 8:
		return 'Sep-13'
	elif int(number) == 9:
		return 'Oct-13'
	elif int(number) == 10:
		return 'Nov-13'
	elif int(number) == 11:
		return 'Dec-13'


	# Please, introduce your answer here
	





if __name__ == '__main__':
	''' You might modify the values of
	these variables to try different aspects
	of your code. You might also want to try
	different files that have the same format
	but different numbers for the prices.
	Running this file should produce all the
	outputs you need, two plots and the desired value'''

	filename = 'data/Vegetables.csv' # You can change this value for testing

	# Parameters for plot 2
	vegetable_for_plot_2 = 'Lettuce' # You can change this value for testing

	# Parameters for finding the cheapest month:
	vegetable_for_cheapest_month = 'Carrots' # You can change this value for testing
	organic_for_cheapest_month = False # You can change this value for testing


	# The code below is for your reference, so you can visualise your answer
	df = read_vegetable_data(filename)

	# Generate plots:
	generate_plot_1(df)
	generate_plot_2(df, vegetable_for_plot_2)

	# Cheapest month info:
	cheapest_month = find_cheapest_month(df, 
										 'Carrots',
										False,)

	print('For', vegetable_for_cheapest_month, 
		  '(organic =', organic_for_cheapest_month,
		  ') the cheapest month was:', cheapest_month)
