"""
Homework #8 I/O
"""
import os.path
from os import path

FileName = input()


# This function creates a new file.
def NewFile():
	NewFile = open(FileName, 'w')
	text = input("Please enter the text: \n")
	NewFile.write(text)
	NewFile.close()

# This function checks is entered file exists. 
def isFileExist():
	if path.exists(FileName):
		return True
	else:
		return False

# This function reads file
def readFile():
	file = open(FileName)
	print(file.read())
	file.close()


# This function overwrites the file
def writeFile():
	file = open(FileName, 'w')
	text = input()
	file.write(text)
	file.close()


# This function appends file
def appendFile():
	file = open(FileName, 'a')
	text = input()
	file.write('\n')
	file.write(text)
	file.close()


# This function replaces certain line
def replaceLine():
	lineNum = int(input('Line:\n'))
	text = input('Text:\n')
	with open(FileName) as file:
		readLines = file.readlines()
		file.close()
	with open('NewFile.txt', 'w') as file:
		for i, line in enumerate(readLines, 1):
			if i == lineNum:
				file.writelines(text)
				file.writelines('\n')
			else:
				file.writelines(line)
		file.close()


# Main function
def main():
	if not isFileExist():
		NewFile()
	elif isFileExist():
		text = input('Enter A if you want read this file''\n'
					'Enter B if you want write this file' '\n'
					'Enter C if you want append this file''\n'
					'Enter D if you want to change specific line''\n')
		if text == 'A':
			readFile()
		if text == 'B':
			writeFile()
		if text == 'C':
			appendFile()
		if text == 'D':
			replaceLine()


main()
