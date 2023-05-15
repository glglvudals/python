absent = [2, 5] # 결석
no_book = [7] 
for student in range(1, 11):
    if student in absent:
        continue # 값에 없어도 계속 진행해라
    elif student in no_book:
        print(f"오늘 수업 여기까지. {student}는 교무실로 따라와")
        break # 조건에 충족하게 되면 중지
    print(f"{student}, 책 읽어봐")
    