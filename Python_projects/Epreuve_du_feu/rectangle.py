#Exo 5
import sys

def file_to_list(f1):
	f = open(f1)
	lst = []
	e = ''

	for l in f:
		lst.append(l.replace('\n', ''))

	f.close()

	return lst

def rectangle(f1,f2):
	target = file_to_list(f1)
	grid = file_to_list(f2)
	answer_coord = 0

	for i in range((len(grid) - len(target)) + 1):
		if target[0] in grid[i]:
			answer_coord = grid[i].index(target[0])

		if (target[1] in grid[i + 1]) and (grid[i + 1].index(target[1]) == answer_coord):
			if (target[2] in grid[i + 2]) and (grid[i + 2].index(target[2]) == answer_coord):
				return (answer_coord, i)

	return False

if __name__ == "__main__":
    print(rectangle(sys.argv[1], sys.argv[2]))