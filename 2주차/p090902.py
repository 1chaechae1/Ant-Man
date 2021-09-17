L=[1,2,3,4,5]
print(type(L))
L.append(10)
print(type(L))
print(L)

print(L[3:5])#끝번호-1
L.reverse()
print(L)


s={1,2,3}
print(type(s))
print(s)
s.add(4)
print(s)
s.add(2)
print(s)


t=(1,2,3,4,5)
print(type(t))
print(t)
print(t.index(3))

a=3
b=7
a,b = b,a
print(a,b)

d = {1:10, 2:20, 3:30}
print(type(d))
print(d)

print(d[1])
print(d.keys())
print(d.values())
print('\a')

num1 = 3
num2 = 5
print("%d + %d = %d " % (num1 ,num2 , num1+num2))
