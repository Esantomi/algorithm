# 재귀 호출(recursion)을 써서 팩토리얼 구하기

# 팩토리얼의 성질: n! = n * (n-1)!

# 2! = 2 * 1!
# 3! = 3 * 2!
# 4! = 4 * 3!


# 풀이
def fact(n):
    if n <= 1:
        return 1
    return n * fact(n-1)

print(fact(1))
print(fact(5))
print(fact(10))


# 생각
# fact(3)을 생각했을 때 ret는 3 * fact(2)이다.
# fact(2)의 ret는 2 * fact(1)이다.
# fact(1)의 ret는 1이다.
# 따라서 fact(2)는 2 * 1 = 2가 되고, fact(3)은 3 * 2 = 6이 된다.