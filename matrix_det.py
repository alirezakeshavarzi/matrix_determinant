
n = int(input('Enter number : '))
mat = [[int(input('Enter number : ')) for i in range(n) ] for j in range(n)] # getting matrix.


for i in range(1,n):
    for j in range(n):

        h = (mat[i][j] / mat[j][j]) * (-1)

        for k in range(n):

            h *= mat[j][k]
            mat[i][k] += h

det = mat[0][0]
for i in range(1,n):
    det *= mat[i][i]

print()
print('determinant : ', det)
