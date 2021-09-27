def gcd(a,b):
    while(b != 0):
        r = a%b
        a=b
        b=r
    return a

a=int(input('숫자를 입력 '))
b=int(input('숫자를 입력 '))
print("최대 공약수는 %d" %(gcd(a,b)))
