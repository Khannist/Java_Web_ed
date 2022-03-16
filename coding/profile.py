
def profile(name, age, address):
    print("나의 이름은 {0}이고, 나이는 {1}이고, 주소는 {2}입니다.".format(name,age,address))
    
    
    
name = input("이름 = ")
age = int(input("나이 = "))
address = input("주소 = ")

profile(name, age, address)
