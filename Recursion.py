# 재귀함수로 피보나치 수 구현
def fibo_recu(n):
    if n==0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo_recu(n - 1) + fibo_recu(n - 2)


print("Fibonacci used Recursion:  0 1", end=' ')
for i in range(2,10):
    print(fibo_recu(i), end=' ')
print()


# 반복문으로 피보나치 수 구현
def fibo_iter(n):
    r = list()
    p1, p2 = 1, 1
    for _ in range(n):
        r.append(p1)
        p1, p2 = p2, p1 + p2
    return r[-1]


print("Fibonacci used loop: 0 1", end=' ')
for i in range(2,10):
    print(fibo_iter(i), end=' ')