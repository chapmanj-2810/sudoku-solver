import numpy as np
from itertools import permutations, product

test_case = np.genfromtxt('hard_sudoku.txt', delimiter=',', dtype=int) 
test_solution = np.genfromtxt('hard_sudoku_sol.txt', delimiter=',', dtype=int) 

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
	missing_numbers = [[value]*(9-count) for value,count in zip(values,counts) if value != 0 and count != 0]
	missing_numbers_flatlist = list(iterFlatten(missing_numbers))

	unique_combinations = set(permutations(missing_numbers_flatlist, len(missing_numbers_flatlist)))

	x_ind, y_ind = np.where(puzzle==0)
	indices = np.column_stack([x_ind, y_ind])

	for combo in unique_combinations:

		for val,ind in zip(combo, indices):
			puzzle[ind[0], ind[1]] = val		

		if len(set(puzzle[:,0]))==9 & len(set(puzzle[:,1]))==9 & len(set(puzzle[:,2]))==9 & len(set(puzzle[:,3]))==9 & len(set(puzzle[:,4]))==9 & len(set(puzzle[:,5]))==9 & len(set(puzzle[:,6]))==9 & len(set(puzzle[:,7]))==9 & len(set(puzzle[:,8]))==9 & len(set(puzzle[0,:]))==9 & len(set(puzzle[1,:]))==9 & len(set(puzzle[2,:]))==9  & len(set(puzzle[3,:]))==9 & len(set(puzzle[4,:]))==9 & len(set(puzzle[5,:]))==9 & len(set(puzzle[6,:]))==9 & len(set(puzzle[7,:]))==9  & len(set(puzzle[8,:]))==9:
			if len(set(puzzle[:3,:3].flatten()))==9 & len(set(puzzle[:3,3:6].flatten()))==9 & len(set(puzzle[:3,6:].flatten()))==9 & len(set(puzzle[3:6,:3].flatten()))==9 & len(set(puzzle[3:6,3:6].flatten()))==9 & len(set(puzzle[3:6,6:].flatten()))==9 & len(set(puzzle[6:,:3].flatten()))==9 & len(set(puzzle[6:,3:6].flatten()))==9 & len(set(puzzle[6:,6:].flatten()))==9:
				return(puzzle)
			else:
				continue
		else:
			continue
				
print(sudoku_solver(test_case))
print('The solution found is: {}'.format((sudoku_solver(test_case)==test_solution).all()))