# 1부터 n까지의 합 구하기

# input: n
# output: 1부터 n까지의 합

def sum_n(n):
    s = 0
    for i in range(n+1):  # range(시작, 끝, 간격) 중 시작, 간격은 생략 가능
        s += i
    return s

print(sum_n(5))