"""
Homework #6
Nested Loops
"""

r = 7
c = 13


def table (rows, columns):
	if r > 59 or c > 235 or c % 2 == 0:				# My monitors size
		print('Max rows is 59 and max columns is 235 and columns can not be even number')
		return False

	for row in range(r):
		if row % 2 == 0:
			for column in range(c):
				if column % 2 == 0:
					if column != c - 1:
						print("X", end = "")
					else:
						print("X")
				else:
					print("|", end = "")
		else:
			print("-" * c)
	return True


table(r, c)
