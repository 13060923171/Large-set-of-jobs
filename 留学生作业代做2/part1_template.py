import numpy as np
import pandas as pd
def classify_prices(discount):
	price_classification = [] # Change/remove this line
	for d in discount:
		if float(d) <= 0:
			category = 'no_discount'
			price_classification.append(category)
		elif 0 <= float(d) <= 0.1:
			category = 'discounted'
			price_classification.append(category)
		elif 0.1 <= float(d) <= 0.2:
			category = 'good_deal'
			price_classification.append(category)
		else:
			category = 'buy_now'
			price_classification.append(category)
	# Please, introduce your answer here
	return price_classification

def calculate_discount(current, reference):
	list_discount = []
	for i in range(len(current)):
		c = current[i]
		r = reference[i]
		discount = (r - c)/r
		list_discount.append(discount)

	return list_discount

def read_files(current_price_filename, reference_price_filename):
	with open(current_price_filename,encoding='utf-8')as f:
		data = np.loadtxt(f,delimiter=',')

	with open(reference_price_filename, encoding='utf-8')as f:
		data1 = np.loadtxt(f, delimiter=',')

	current = np.array(data,dtype=np.int)  # Change/remove this line
	reference = np.array(data1,dtype=np.int)  # Change/remove this line
	# Please, introduce your answer here

	return current, reference

def check_output(current, reference, discount, price_classification):
	# Do not modify this function, it is provided only for you to check your answer
	n_prices = len(discount)
	print('----------------------------------------------')
	print('P', 'current', 'ref', 'discount', 'classification', sep='\t')
	print('----------------------------------------------')
	for i in range(n_prices):
		print(i, current[i],
			  reference[i],
			  str(np.round(discount[i], 2)) + '%',
			  price_classification[i], sep='\t')

if __name__ == '__main__':
	current_price_filename = 'data/current_prices_example.csv' # You can change this value for testing
	reference_price_filename = 'data/reference_prices_example.csv' # You can change this value for testing

	# The lines below are provided to run your code in a similar order as
	# will be done during marking and to help you check your answer.
	current, reference = read_files(current_price_filename, reference_price_filename)
	discount = calculate_discount(current, reference)
	price_classification = classify_prices(discount)

	# You can use the function below to check your answer only
	# Please comment it for your submission
	check_output(current, reference, discount, price_classification)
