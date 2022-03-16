# from cmd import PROMPT


# prompt = """
# 1.add
# 2.del
# 3.list
# 4.quit

# enter number: """

# number = 0
# while number!=4:
#     print(prompt)
#     number = int(input()) # input()임의의 수 키보드 입력
    
    
score = int(input("점수를 입력하세요?>> "))

if score >=90 :
    print("학점은 A학점 입니다.")
elif score >=80 :
    print("학점은 B학점 입니다.")
elif score >=70 :
    print("학점은 C학점 입니다.")
elif score >=60 :
    print("학점은 D학점 입니다.") 
elif score <60:
    print("학점은 F학점 입니다.")
        
    
