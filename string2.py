python = "Python is Amazing"
print(python.lower()) # 모든 문자 소문자 출력
print(python.upper()) # 모든 문자 대문자 출력
print(python[0].isupper()) # 첫 문자가 대문자면 TRUE
print(len(python)) # 문자열 단어 수 반환
print(python.replace("Python", "Java")) # Python이라는 단어를 Java로 변경

index = python.index("n")
print(index) #n이라는 단어가 몇 번째있는지
index = python.index("n", index + 1) 
print(index) # 2번째 있는 n 출력

print(python.find("n")) # n 이 몇번째 있는지 출력
print(python.find("Java")) # 원하는 값이 변수에 포함되어 있지 않을 경우에는 -1 반환
#print(python.index("Java")) # python이라는 변수에는 Java가 없기 때문에 에러가 발생
print("hi") # 오류가 발생했기 때문에 hi가 출력되지 않음

print(python.count("n")) # n이 몇개 있는지 출력


