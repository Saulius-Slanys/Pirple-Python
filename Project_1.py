"""
Project #1
Game Conect 4
"""

ROW = 7
COL = 6

def drawField(field):
	for row in range(11):
		if row % 2 == 0:
			practicalRow = int(row / 2)
			for column in range(13):
				if column % 2 == 0:
					practicalColumn = int(column / 2)
					if column != 12:
						print(field[practicalColumn][practicalRow], end = '')
					else:
						print(field[practicalColumn][practicalRow])
				else:
					print('|', end = '')
		else:
			print('-------------')


diagonalRightList = []
# This function is modified Nikita Tiwari code https://www.geeksforgeeks.org/zigzag-or-diagonal-traversal-of-matrix/
def diagonalRight(matrix):
	lineList = []
	# There will be ROW+COL-1 lines in the output 
	for line in range(4, 10) : 
		# Get column index of the fifth element 
		# in this line of output. The index is 4 
		# for first ROW lines witch has 4 elements and 10 for 
		# last line.
		start_col = max(0, line - ROW) 
  
		# Get count of elements in this line. 
		# The count of elements is equal to 
		# minimum of line number, COL-start_col and ROW  
		count = min(line, (COL - start_col)) 
  
		# Append players list  
		for j in range(0, count) :
			lineList.append((matrix[min(ROW, line) - j - 1][start_col + j]))
		diagonalRightList.append(lineList)
		lineList = []
    
diagonalLeftList = []
# This function is modified Nikita Tiwari code https://www.geeksforgeeks.org/zigzag-or-diagonal-traversal-of-matrix/
def diagonalLeft(matrix):
	lineList = []
	# There will be ROW+COL-1 lines in the output 
	for line in range(4, 10) : 
		# Get column index of the fifth element 
		# in this line of output. The index is 4 
		# for first ROW lines witch has 4 elements and 10 for 
		# last line.
		start_col = max(0, line - ROW) 
  
		# Get count of elements in this line. 
		# The count of elements is equal to 
		# minimum of line number, COL-start_col and ROW  
		count = min(line, (COL - start_col)) 
  
		# Append players list  
		for j in range(0, count) :
			lineList.append((matrix[max(0, (ROW - line)) + j][start_col + j]))
		diagonalLeftList.append(lineList)
		lineList = []


def checkHorizontal(Win):			#This function checks if player conected 4 in row
	for i in range(6):
		piece = 0
		for j in range(7):
			if currentField[j][i] == Win:
				piece += 1
				if piece == 4:
					return True
			elif currentField[j][i] != Win:
				piece = 0

def checkVertical(Win):				#This function checks if player conected 4 in column
	for i in range(6, -1, -1):
		piece = 0
		column = currentField[i]
		for j in range(5, -1, -1):
			if column[j] == ' ':
				break
			if column[j] == Win:
				piece += 1
				if piece == 4:
					return True
			elif column[j] != Win:
				piece = 0


def checkDiagonalRight(Win):
	for i in range(len(diagonalRightList)):
		piece = 0
		for j in range(len(diagonalRightList[i])):
			if diagonalRightList[i][j] == Win:
				piece += 1
				if piece == 4:
					return True
			elif diagonalRightList[i][j] != Win:
				piece = 0


def checkDiagonalLeft(Win):
	for i in range(len(diagonalLeftList)):
		piece = 0
		for j in range(len(diagonalLeftList[i])):
			if diagonalLeftList[i][j] == Win:
				piece += 1
				if piece == 4:
					return True
			elif diagonalLeftList[i][j] != Win:
				piece = 0


Player = 1
currentField = [[' ', ' ', ' ', ' ', ' ', ' '],
		[' ', ' ', ' ', ' ', ' ', ' '],
		[' ', ' ', ' ', ' ', ' ', ' '],
		[' ', ' ', ' ', ' ', ' ', ' '],
		[' ', ' ', ' ', ' ', ' ', ' '],
		[' ', ' ', ' ', ' ', ' ', ' '],
		[' ', ' ', ' ', ' ', ' ', ' ']]
drawField(currentField)

#print(diagonalRight)


while(True):
	print('Players turn:', Player)
	MoveColumn = int(input('Please enter the column\n')) - 1	#Replaces 0-th column with first column
	if MoveColumn > 6:											#Out of board
		print('Out of game board')
		print('Retray')
		pass
	elif Player == 1:
		# Make move for first player
		for row in range(5, -1, -1):
			if currentField[MoveColumn][row] == ' ':
				currentField[MoveColumn][row] = 'X' #u'\u2B24' I can not figure out how to use colorfull unicode symbols on Python 3.8.0 Shell on Windows 10
				Player = 2
				break
			elif currentField[MoveColumn][0] != ' ':	#Returns move to first player if column is full
				print('This column is full')
				print('Choose other column')
				player = 1
				break
		diagonalRight(currentField)
		diagonalLeft(currentField)				
		# Checks if player won
		if checkVertical('X'):
			drawField(currentField)
			print('Won player: 1')
			break
		if checkHorizontal('X'):
			drawField(currentField)
			print('Won player: 1')
			break
		if checkDiagonalRight('X'):
			drawField(currentField)
			print('Won player: 1')
			break
		if checkDiagonalLeft('X'):
			drawField(currentField)
			print('Won player: 1')
			break
		diagonalRightList = []
		diagonalLeftList = []
		
	else:
		# Make move for second player
		for row in range(5, -1, -1):
			if currentField[MoveColumn][row] == ' ':
				currentField[MoveColumn][row] = 'O' #u'\u2B58' I can not figure out how to use colorfull unicode symbols on Python 3.8.0 Shell on Windows 10
				Player = 1
				break
			elif currentField[MoveColumn][0] != ' ':	#Returns move to second player if column is full
				print('This column is full')
				print('Choose other column')
				player = 2
				break
		diagonalRight(currentField)
		diagonalLeft(currentField)
		# Checks if player won
		if checkVertical('O'):
			drawField(currentField)
			print('Won player: 2')
			break
		if checkHorizontal('O'):
			drawField(currentField)
			print('Won player: 2')
			break
		if checkDiagonalRight('O'):
			drawField(currentField)
			print('Won player: 2')
			break
		if checkDiagonalLeft('O'):
			drawField(currentField)
			print('Won player: 2')
			break
		diagonalRightList = []
		diagonalLeftList = []
	drawField(currentField)
