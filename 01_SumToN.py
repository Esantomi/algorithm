# 1부터 n까지의 합 구하기
# input: n
# output: 1부터 n까지의 합

def sum_n(n):
    s = 0
    for i in range(n+1):  # range(시작, 끝, 간격) 중 시작, 간격은 생략 가능
        s += i
    return s

print(sum_n(5))
print(sum_n(1001))


# 다른 알고리즘으로 구하기
# Gauss Summation, n(n+1)/2

def sum_gauss(n):
    return (n*(n+1))//2  # 정수 나눗셈 (소수점 자리 없게끔)

print(sum_gauss(5))
print(sum_gauss(1001))

# O(n)인 sum_n 알고리즘보다 O(1)인 sum_guass 알고리즘이 더 빠르다.
# 0(n)은 입력 크기와 계산 시간이 대체로 비례한다는 특징을 갖는다.