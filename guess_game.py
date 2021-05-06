from random import randint as ran
n = ran(20,50)
#print (n)
print("Game starts now. \nYou have to guess the correct no. \nYou"" have only 9 chances")

for i in range (9):
	a = int ( input ('enter the no._\n'))
	
	if a==n:
		print('your guess is right \n you have taken', (i+1), 'guesse to win \ncongrats')
		break
		
	elif a>n:
		print('the winning number is lesser than your guess\ntry again \nOnly', (8-i),'Guesses is left now')
		
		
	else :
			print('the winning number is greater than your guess \ntry again \nOnly', (8-i),'Guesses is left now')
	if i==8:
		print('Game over\nthe no. was 18')
		
	