# 집합 (set)
# 중복 안됨, 순서 없음
my_set = {1,2,3,3,3}
print(my_set) # {1, 2, 3}

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합(java와 phthon을 모두 할 수 있는 개발자)
print(java & python) # {'유재석'}
print(java.intersection(python)) # {'유재석'}

# 합집합 (java 또는 python 개발자)
print(java | python) # {'양세형', '박명수', '김태호', '유재석'} /  순서는 보장되지 않음
print(java.union(python)) # {'양세형', '박명수', '김태호', '유재석'} /  순서는 보장되지 않음

# 차집합 (java 할 수 있지만 python은 할 줄 모르는 개발자)
print(java - python) # {'양세형', '김태호'}
print(java.difference(python)) # {'양세형', '김태호'}

# pyhton 할 줄아는 사람 추가
python.add("김태호")
print(python) # {'박명수', '김태호', '유재석'}

# java 개발자 감소
java.remove("김태호")
print(java) # {'양세형', '유재석'}