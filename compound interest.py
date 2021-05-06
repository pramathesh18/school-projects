from time import sleep as zz

#calculate SI & CI

zz(1)
print()
print()
print()
print('                    》instructions《')
print()
print()

zz(2)
print('enter 0 to find amount for simple interest')
print('enter 1 to find amount for compound interest')
zz(2)
print()
i = int(input('enter your choice_'))

if i == 0:
	p	=int(input('initial principal balance_'))
	r	=int(input('interest rate_'))
	t = int(input('time period_'))
	print(p+((p*r*t)/100))

elif i == 1:
	p	=int(input('initial principal balance_'))
	r	=int(input('interest rate_'))

	n	=int(input('number of times interest applied per time period'))

	t	=int(input('number of time periods elapsed_'))
	a=(p*(1+(r/n))**(t))
	print(a)
	
		
			
else :
	print('the choice you have entered is wrong.Please recheck')	
	
	
	
	
	