jumin = "990120-1234567"

print("성별 : " + jumin[7]) # 1
print("연 : " + jumin[0:2]) # 99
print("월 : " + jumin[2:4]) # 01
print("일 : " + jumin[4:6]) # 20

print("생년월일 : " + jumin[0:6]) # 990120
print("뒤 7자리 : " + jumin[7:]) #1234567 7부터 끝까지
print("뒤 7자리 (뒤에서부터) : " + jumin[-7:] ) # 맨 뒤에서 7번쨰부터 끝까지