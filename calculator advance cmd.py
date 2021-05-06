

print('welcome to our customized calculator')

while True:
    nn = (input('press 1 to continue to the calcultor or press any key to terminate. : '))

    if nn == '1':
        print(' \npress 1 for addition\npress 2 for multiplication\npress 3 for substraction\npress 4 for division')

        n1 = int(input('enter your choice : '))

        if n1 == 1:
            print('you have choose to do addition.')
            n2 = int(input(' how many times do you want to add? : '))
            a = 0
            for i in range (n2):
                n3 = int(input(f'enter the number {i+1} : '))
                a = a + n3
            print(f"the addition of the numbers is {a}")

        elif n1 == 2:
            print('you have choose to do multiplication')
            n2 = int(input('how many numbers do you want to do multiplication? : '))
            a = 0
            for i  in range(n2):
                n3 = int(input(f'enter the number {i + 1} : '))
                a = a * n3
                print(f"the multiplication of the numbers is {a}")

        elif n1 == 3:
            print('you have choose to do substraction')
            n2 = int(input("enter the substractent : "))
            n3 = int(input('enter the the to be substracted : '))
            print(f"the result of the substraction is {n2 - n3}")

        elif n1 == 4:
            print('you have choose to do division')
            n2 = int(input('enter the divident : '))
            n3 = int(input('enter the divisor : '))
            print(f'the quotient is {n2/n3}\n integer quotient is {n2//n3}\n remainder is {n2%n3}')


    else:
        print('terminating......')
        break