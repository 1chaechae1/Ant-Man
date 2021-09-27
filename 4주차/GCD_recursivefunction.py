def gcd(a,b):
    if a%b == 0:
        return b
    else:
        return gcd(b, a%b)

a=int(input('숫자를 입력 '))
b=int(input('숫자를 입력 '))
print("최대 공약수는 ", gcd(a,b))
