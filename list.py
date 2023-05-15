# 순서를 가지는 객체의 집합

# 지하철 칸별로 10명, 20명, 30명 
subway1 = 10
subway2 = 20
subway3 = 30

subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "박명수"] # ['유재석', '조세호', '박명수']
print(subway)

print(subway.index("조세호")) # 1

subway.append("하하") # ['유재석', '조세호', '박명수', '하하']
print(subway)

subway.insert(1, "정형돈") # ['유재석', '정형돈', '조세호', '박명수', '하하']
print(subway) 

# print(subway.pop()) # 하하
# print(subway) # ['유재석', '정형돈', '조세호', '박명수']

# print(subway.pop()) # 박명수
# print(subway) # ['유재석', '정형돈', '조세호']

# print(subway.pop()) # 조세호
# print(subway) # ['유재석', '정형돈']

subway.append("유재석") 
print(subway) # ['유재석', '정형돈', '조세호', '박명수', '하하', '유재석']
print(subway.count("유재석")) # 2

num_list = [5,2,4,3,1]
num_list.sort()
print(num_list) # [1, 2, 3, 4, 5]
num_list.reverse()
print(num_list) # [5, 4, 3, 2, 1]
# num_list.clear()
# print(num_list) # []

mix_list = ["조세호", 20, True]
print(mix_list)

num_list.extend(mix_list)
print(num_list) # [5, 4, 3, 2, 1, '조세호', 20, True]