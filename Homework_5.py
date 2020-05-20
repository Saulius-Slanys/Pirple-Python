"""
Homework #5
FizzBuzz
"""


S = 100

def prime (number):											# this function checks is nuber is a prime
	i = 1
	while i <= number:
		if number == 1:										# 1 is not a prime
			break
		elif number % i == 0 and i != 1 and i!= number:		# if number is not a prime, stops next calculations
			break
		elif i == number:									# number is a prime
			number = 'Prime'
			break
		i += 1
	return number


def FizzBuzz (number):
	i = 1
	while i <= number:
		if i %3 == 0 and i %5 == 0:							# number multiples by 3 and 5
				print('FizzBuzz')
		elif i % 3 == 0:									# number multiples by 3
				print('Fizz')
		elif i % 5 == 0:									# number multiples by 5
				print('Buzz')
		else:												# nuber or prime
				print(prime(i))
		i += 1
	

	
FizzBuzz(S)