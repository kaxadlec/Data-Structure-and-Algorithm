memos = [None for _ in range(100)]  # 전역리스트, memos 공간 None으로 채워넣음
memos[0], memos[1]= 0, 1    # memos.append 안 쓰는 이유는 0번방, 1번방에 숫자 넣어야하기 때문


def fibo_memo_recu(n):
    """
    재귀함수에 Memorization(DP) 을 사용한 피보나치 수열 처리 함수
    :param n: 
    :return: 
    """
    global memos

    if n <= 1:
        return memos[n]
    if memos[n] is not None:    # 전역 메모리 memos에, 이전에 계산 결과 값이 존재하면
        return memos[n]

    memos[n] = fibo_memo_recu(n-2) + fibo_recu(n-1)     # 처음 방문하는 n이면
    return memos[n]

def fibo_memo(n):
    """
    Memorization(DP) 을 사용한 피보나치 수열 처리 함수
    :param n:
    :return:
    """
    memo = [0, 1]  # memo의 초기값 0, 1
    if n <= 1:
        return memo[n]
    else:
        for i in range(2, n+1):
            memo.append(memo[i-1] + memo[i-2])
        return memo[n]


def fibo_recu(n):
    global count_recursion

    """
    재귀함수를 이용한 피보나치 수열 처리
    :param n:
    :return:
    """
    if n<= 1:
        return n
    else:
        return fibo_recu(n - 1) + fibo_recu(n - 2)


def fibo_iter(n):
    """
    반복문을 사용한 피보나치 수열 처리 함수
    :param n:
    :return:
    """
    r = list()
    p1, p2 = 1, 1
    for _ in range(n):
        r.append(p1)
        p1, p2 = p2, p1 + p2
    return r[-1]


print("Fibonacci used memo-recu: 0 1", end=' ')
for i in range(2,10):
    print(fibo_memo_recu(i), end=' ')
print()

print("Fibonacci used memorization: 0 1", end=' ')
for i in range(2,10):
    print(fibo_memo(i), end=' ')
print()

print("Fibonacci used Recursion:  0 1", end=' ')
for i in range(2,10):
    print(fibo_recu(i), end=' ')
print()

print("Fibonacci used loop: 0 1", end=' ')
for i in range(2,10):
    print(fibo_iter(i), end=' ')
print()

