# print("a" + "b")
# print("a", "b")

# 방법 1
print("나는 %d살입니다." % 20) # d는 정수 값만 넣어 줄수 있음
print("나는 %s을 좋아해요." %"파이썬") # s는 string값을 넣겠다는 것임
print("Apple은 %c%c로 시작해요." % ("A", "B")) # 만 글자만 받겠다

print("나는 %s살입니다." % 20)
print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))

# 방법 2
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간")) # 나는 파란색과 빨간색을 좋아해요.
print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간")) # 나는 파란색과 빨간색을 좋아해요.
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간")) # 나는 빨간색과 파란색을 좋아해요.

# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요".format(age = 20, color="빨간")) # 나는 20살이며, 빨간색을 좋아해요
print("나는 {age}살이며, {color}색을 좋아해요".format(color="빨간", age = 20)) # 나는 20살이며, 빨간색을 좋아해요

# 방법 4
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요") # 나는 20살이며, 빨간색을 좋아해요