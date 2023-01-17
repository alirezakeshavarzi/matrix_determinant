import os

q = [[int(input('Enter number : ')) for i in range(2) ] for j in range(2)]


for i in range(2):
    for j in range(1,3):
        h = (q[j][i] / q[i][i]) * (-1)
