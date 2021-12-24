# Dice rolling
import numpy as np
from random import choice

def dice_probabilities(n_dice, replications):
	D6 =Die()
	result = []
	dice_values = []
	dice_probabilities = []
	face_times = []
	for i in range(replications):
		result.append(D6.compute_add(n_dice))
	for i in range(int(n_dice)*1,(int(n_dice)*6+1)):
		face_times.append(result.count(i))
		dice_values.append(i)
	for f in face_times:
		d = float(int(f) / int(replications))
		dice_probabilities.append(d)

	# dice_values = np.zeros(1) # Change/remove this line
	# dice_probabilities = np.zeros(1)  # Change/remove this line

	# Please, introduce your answer here

	return dice_values, dice_probabilities

class Die():
	def __init__(self,size=6):
		self.size = size
	def compute_add(self,times=2):
		if times <= 0:
			return 0
		else:
			faces = []
			result = 0
			for i in range(1,self.size+1):
				faces.append(i)
			for i in range(times):
				ones_result = choice(faces)
				result += ones_result
			return result

if __name__ == '__main__':
	n_dice = 2  # You can change this value for testing
	replications = 1000000  # You can change this value for testing


	# The code below is for your reference, so you can visualise your answer	
	dv, dp = dice_probabilities(n_dice, replications)

	n = len(dv)
	print('Rolling', n_dice, 'dice has', n, 'possible outcomes:')
	print('With', replications, 'replications, the estimated probabilities are:')
	print('Outcome', 'Prob:', sep='\t')
	for i in range(n):
		print(dv[i], '', np.round(dp[i], 8), sep='\t')
