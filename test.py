count_num = 4


def isPrime(num):
    # 절반을 나누면 길이에서 하나적은 인덱스로 보기에 1을 플러스해준다.
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False

    return True


def DFS(num):
    if len(str(num)) == count_num:
        print(num)
    else:
        for i in range(1, 10):
            if i % 2 == 0:
                continue;

            if isPrime(num * 10 + i):
                DFS(num * 10 + i)


DFS(2)
DFS(3)
DFS(5)
DFS(7)