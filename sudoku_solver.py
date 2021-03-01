import numpy as np
from itertools import permutations

test_case = np.genfromtxt('sudoku_test.csv', delimiter=',', dtype=int) 
test_solution = np.genfromtxt('sudoku_sols.csv', delimiter=',', dtype=int) 

def iterFlatten(root):
	'''iterFlatten takes a nested list input and yields a flattened list where every element contained within the nested list
	is listed one after the other, having removed the nested structure. E.g. [0,[[1,2,3],4],5,6] ---> [0,1,2,3,4,5,6]'''
	if isinstance(root, (list, tuple)):
		for element in root:
			for e in iterFlatten(element):
				yield e
	else:
		yield root

def sudoku_solver(puzzle):

	values, counts = np.unique(puzzle, return_counts=True) #The different values found within the grid and their frequencies.
	missing_numbers = [] #Empty list for the numbers missing from the grid.

	for i in range(len(values)):
		inter_list = [values[i]] * (9-counts[i]) #Generates list of the numbers missing from the grid.
		missing_numbers.append(inter_list)

	missing_numbers = list(iterFlatten(missing_numbers)) #Removes the nested lists to create one list containing all of the missing numbers.
	generator = [j for j in missing_numbers if j>0] #Get rid of zeros which are placer numbers.
	combinations = [] #Empty list to place the different combinations.

	for subset in permutations(generator):
		if list(subset) not in combinations: #Check to see if the combination is already present.
			combinations.append(list(subset))

	for combo in combinations:

		for (ind_x, ind_y), value in np.ndenumerate(puzzle):

			column = puzzle[:, ind_y] #All of the values in the same column as the value.
			row = puzzle[ind_x, :] #All of the values in the same row as the value.

			if value == 0:
				value = combo[number]

	return(test_solution)

print(sudoku_solver(test_case).all() == test_solution.all()) #Check to see if the calculated grid is the same as the solution.