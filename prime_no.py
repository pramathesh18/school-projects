"""
Write a program to enter a number and check if it is prime or not
"""

p = int(input('enter the no._'))
t=0
for i in range(2,p):
	if p%i == 0:
		print("the entered no. is not a prime no.")
		t+=1
		break
		
if t == 0:
	print('entered no is a prime number')
	