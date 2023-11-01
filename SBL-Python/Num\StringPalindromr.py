def palindrome_num(num):

     temp = num
     reverse = 0
     while temp > 0:
       remainder = temp % 10
       reverse = (reverse * 10) + remainder
       temp = temp // 10
     if num == reverse:
      print('Number is Palindrome')
     else:
      print("Number is not Palindrome")

def palindrome_string(str):

    if str == str[::-1]:
        print('String is Palindrome')
    else :
        print('String is not Palindrome')

print('Menu Driven program')
while True:
    print('\n Main menu')
    print('1. Palindrome of a number')
    print('2. Palindrome of a string')
    print('3. Exit')
    choice = int(input('Enter your choice: '))

    if choice == 1:
        num = int(input('Enter a number: '))
        palindrome_num(num)
    elif choice == 2:
        str = input('Enter a string: ')
        palindrome_string(str)
    elif choice == 3:
        break
    else :
        print('Wrong choice')
