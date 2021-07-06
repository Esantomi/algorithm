# 동명이인 찾기
# n명의 사람 이름 중 같은 이름을 찾아 집합으로 만들어 반환하는 알고리즘

# input: n명의 이름이 든 리스트
# output: 같은 이름이 든 집합


# 내 풀이
def homonym(list):
    s = set()
    for i in range(len(list)-1):  # a[-1]은 비교할 필요가 없음
        if list.count(list[i]) >= 2:
            s.add(list[i])
    return(s)

l = ["Tom", "Jerry", "Mike", "Tom"]
l2 = ["Tom", "Jerry", "Mike", "Tom", "Mike"]
print(homonym(l))
print(homonym(l2))


# Pythonic한 풀이
def homonym_pythonic(l):
    s = set()
    for i in l[:-1]:
        if l.count(i) >= 2:
            s.add(i)
    return s

l = ["Tom", "Jerry", "Mike", "Tom"]
l2 = ["Tom", "Jerry", "Mike", "Tom", "Mike"]
print(homonym_pythonic(l))
print(homonym_pythonic(l2))


# 책 풀이
def find_same_name(a):
    n = len(a)
    result = set()
    for i in range(0, n-1):  # a[-1]은 비교할 필요가 없음
        for j in range(i+1, n):
            if a[i] == a[j]:
                result.add(a[i])
    return result

name = ["Tom", "Jerry", "Mike", "Tom"]
print(find_same_name(name))
name2 = ["Tom", "Jerry", "Mike", "Tom", "Mike"]
print(find_same_name(name2))