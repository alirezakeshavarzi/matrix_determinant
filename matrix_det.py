n = int(input('Enter a size of matrix : '))
b = [[None] * n] *n
print('This is b : ', b)

for i in range(n):
    for j in range(n):
        b[i][j] = int(input())

print(b)