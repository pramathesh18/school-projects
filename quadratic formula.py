
#start

import cmath
print('enter a,b,c if the equation is')
print('ax²+bx+c')

a=int(input('enter no a'))
b=int(input('enter no b'))
c=int(input('enter no c'))

d=b**2 - 4*a*c

if d<=0:
	print('roots are imaginary')
else:
	print('roots are real')
e=cmath.sqrt(d)
print('the roots.are:-')
print((((-b)+e)/2*a),(((-b)-e)/2*a))



#end!!!!
