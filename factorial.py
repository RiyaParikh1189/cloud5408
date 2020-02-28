'''
Write a code to print factorial of given number.
'''

def findFactorial(num):
    if num<=0:
        return 1
    else:
        return num*findFactorial(num-1)

if __name__ == '__main__':
    number = int(input('Enter number to find factorial:'))
    if(number<0):
        print('Factorial of negative number does not exist.')
    else:
        print('factorial of {} = {}'.format(number,findFactorial(number)))





