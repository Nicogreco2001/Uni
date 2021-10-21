def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return
    else:
        fibo = 0 + 1
        n_2, n_1 = 1, 1
        for value in range(3,n+1):
            fibo = n_2 + n_1
            n_2 = n_1
            n_1 = fibo
        return fibo

print((fibo(int((input())))))
