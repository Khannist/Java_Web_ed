
#나무찍기
#WHILE_1.PY

treeHIT=0 # 나무 찍은 횟수
while treeHIT<10 : # 나무를 찍은 횟수가 10보다 작은 동안 반복
                   # treeHIT <10 조건에 만족할때만 아래로 내려감,
                   # 그렇지 않으면 while문을 탈출한다
    treeHIT +=1
    print("나무를 %d번 찍었습니다." % treeHIT)
    if treeHIT ==10:
        print("나무가 넘어갑니다.")


a=100
while a <300:
    a +=1
    print("a에 %d를 더했습니다." %a)
    if a == 300:
        print("a가 300이 되었습니다.")