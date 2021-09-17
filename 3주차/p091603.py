#함수 선언
def calArea(pr):
    p_area = 2*3.14+pr
    return p_area

def hap():
    num1 = int(input('정수 입력 '))
    num2 = int(input('정수 입력 '))
    return num1 + num2

def plus(a,b,c):
    return a+b+c

def minus():
    pass #아무것도 실행을 안하겠다.
#######################
"""
ar = 20
a_area = calArea(ar)
print(a_area)


print("임채현님 두 수를 입력하세요")
hap2 = hap()
print("결과: ", hap2)
print("김동영님 두 수를 입력하세요")
hap3 = hap()
print("결과: ", hap3)
"""

a=int(input('정수를 입력 '))
b=int(input('정수를 입력 '))
c=int(input('정수를 입력 '))

sum = plus(a,b,c)
print("합은 ", sum)
