n=int(input('enter the number_'))
b=0
while n!=0:
	a=n%10
	n//=10
	b=b*10 +a
print(b, 'is the reverse of the number entered')
	