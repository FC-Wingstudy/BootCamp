def factorial(n):
    # 이상태로 돌리면 스택 오버플로가 발생한
    # 탈출 조건
    if n <= 1:
        return 1
    return factorial(n-1) * n


if __name__ == '__main__':
    n = 3
    res = factorial(n)
    print('The factorial of {} is {}'.format(n, res))