# 리스트에 숫자 n개가 있을 때 가장 큰 값이 있는 index를 반환하는 알고리즘

# 내 풀이
def max_idx(list):
    max_val = 0
    max_idx = 0
    for i in range(len(list)-1):
        if list[i] > max_val:
            max_val = list[i]
            max_idx = i
    return max_idx

l = [17, 92, 18, 33, 58, 7, 33, 42]
l2 = [284, 12, 95, 22, 850, 1024, 88, 9, 499]
print(max_idx(l))
print(max_idx(l2))


# 책 풀이
def find_max_idx(a):
    n = len(a)
    max_idx = 0
    for i in range(1, n):
        if a[i] > a[max_idx]:
            max_idx = i
    return max_idx

v = [17, 92, 18, 33, 58, 7, 33, 42]
print(find_max_idx(v))