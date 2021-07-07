# 팩토리얼 (1부터 n까지의 곱) 구하기

# input: n
# output: 1 * 2 * 3 * ... * n (n!)


# 내 풀이
def cal_fac(n):
    if n == 0:
        val = 1
    else:
        val = 1
        for i in range(1, n+1):
            val *= i
    return val

print(cal_fac(0))
print(cal_fac(5))
print(cal_fac(10))


# 책 풀이
def fact(n):
    f = 1
    for i in range(1, n + 1):
        f = f * i
    return f

print(fact(1))
print(fact(5))
print(fact(10))