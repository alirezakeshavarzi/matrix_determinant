# fact with recursive.

def fact_r(n):
    if n==0 or n==1 or n==2 :
        return n
    else:
        return n * fact_r(n-1)


def sum_r(n):
    if n==0 or n==1:
        return n
    else:
        return n + sum_r(n-1)


def multi(a,b):
    m =0
    for i in range(b):
        m += a
    return m

def multi_r(a,b):
    if b==1:
        return a
    else:
        return a * multi_r(a, b-1)


def fibo_r(n):
    if n==0 or n==1:
        return 1
    else:
        return fibo_r(n-2) + fibo_r(n-1)

print('fibo : ', fibo_r(5))


print('mulri_r : ', multi_r(12,3))
