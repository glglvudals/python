cabinet = {3:"유재석", 100:"김태호"} # {key:value}
print(cabinet[3]) # 유재석
print(cabinet[100]) # 김태호

print(cabinet.get(3)) # 유재석
# print(cabinet[5]) # 5라는 키가 없기 때문에 에러발생하고 프로그램 종료되어 hi 출력 안됨
# print("hi")
print(cabinet.get(5)) # none으로 표시되고 hi까지 출력됨
print("hi")

print(cabinet.get(5, "사용가능")) # 키값이 없을 경우 사용가능 출력
print("hi")

print(3 in cabinet) # True
print(5 in cabinet) # False

cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet) # {'A-3': '김종국', 'B-100': '김태호', 'C-20': '조세호'}

del cabinet["A-3"] 
print(cabinet) # {'B-100': '김태호', 'C-20': '조세호'}
print(cabinet.keys()) # dict_keys(['B-100', 'C-20'])
print(cabinet.values()) # dict_values(['김태호', '조세호'])
print(cabinet.items()) # dict_items([('B-100', '김태호'), ('C-20', '조세호')])

cabinet.clear()
print(cabinet) # {}