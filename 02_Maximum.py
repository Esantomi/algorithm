# 최댓값 찾기
# 주어진 숫자 n개 중 가장 큰 숫자를 찾는 알고리즘

# input: 숫자 리스트
# output: 최댓값


# 내 풀이
def maximum(list):
    val = 0
    for i in range(len(list)-1):
        if list[i] > val:
            val = list[i]
        else: pass
    return val

l = [17, 92, 18, 33, 58, 7, 33, 42]
print(maximum(l))


# 책 풀이
def find_max(a):
    n = len(a)
    max_v = a[0]
    for i in range(1, n):
        if a[i] > max_v:
            max_v = a[i]
    return max_v

v = [17, 92, 18, 33, 58, 7, 33, 42]
print(find_max(v))