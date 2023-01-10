import random

n = int(input('Enter a number between 1 to 1000 : '))

x = random.randint(1,n)

while True:
    if x==n:
        print('\nfind number :')
        print('x = ', x)
        print('n = ', n)
        break
    elif x < n:
        print('x : ', x)
        x = random.randint(x, n)


