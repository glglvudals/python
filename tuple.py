menu = ("돈까스", "치즈까스") # 값을 추가하거나 변경 불가능, 변수 값을 괄호로 묶은게 튜플
print(menu[0])
print(menu[1])

# menu.add("생선까스") # 'tuple' object has no attribute 'add'

name = "김종국"
age = 20
hobby = "코딩"
print(name, age, hobby) # 김종국 20 코딩

(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age , hobby) # 김종국 20 코딩