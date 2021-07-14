# 두 자연수 a, b의 최대공약수 구하는 알고리즘

# input: 두 자연수
# output: 최대공약수(GCD)


# 내 풀이
def Gcd(a, b):
    common_div = min(a, b)
    while True:
        if a % common_div == 0 and b % common_div == 0:
            return common_div
        else: common_div -= 1

print(Gcd(1, 5))
print(Gcd(3, 6))
print(Gcd(60, 24))
print(Gcd(81, 27))


# 책 풀이
def gcd(a, b):
    i = min(a, b)
    while True:
        if a % i == 0 and b % i == 0:
            return i
        i = i - 1

print(gcd(1, 5))  # 1
print(gcd(3, 6))  # 3
print(gcd(60, 24))  # 12
print(gcd(81, 27))  # 27