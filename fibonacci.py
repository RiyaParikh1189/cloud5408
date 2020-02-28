'''
Write a code to print fibonacci series
'''

def fibonacci(number):
    a,b=0,1
    if(number==1):
        print(a)
    else:
        for i in range(number):
            print(a)
            c=a+b
            a,b=b,c

if __name__ == '__main__':
    #steps=int(input("Enter number of steps:"))
    steps=15
    if(steps>=0):
        fibonacci(steps)
