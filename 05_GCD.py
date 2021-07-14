# 두 자연수 a, b의 최대공약수 구하는 알고리즘

# input: 두 자연수
# output: 최대공약수(GCD)


# 내 풀이
def Gcd(a, b):
    common_div = min(a, b)
    while True:
        if a % common_div == 0 & b % common_div == 0:
            return common_div
        else: common_div -= 1

print(Gcd(1, 5))
print(Gcd(3, 6))


# 책 풀이
def gcd(a, b):
    i = min(a, b)
    while True:
        