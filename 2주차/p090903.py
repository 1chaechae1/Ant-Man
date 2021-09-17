#text1 = int(input('숫자입력'))
#print(type(text1))

#if True and False:
#    print("yes")
#else:
#    print("No")

a = 8
b = 11
c=a&b
d=a^b
print(c)
print(d)

a=[1,2,3,4,5]
b = 3 in a
print(b)

#money = int(input('돈을 입력하시오'))
#if money >=1000:
#    print('초코릿을 사자')
#else:
#    print('사탕을 사자')    
#print('끝')

#score = int(input('점수를 입력'))
#if score>=90:
#    print('수')
#elif score>=80:
#    print('우')
#elif score>=70:
#    print('미')
#elif score>=60:
#    print('양')
#else:
#    print('가')

#for i in range(1,11):
#    print(i)

#i = 1
#while(i<=10):
#    print(i)
#    i+=1

#for i in [1,2,3]:
#    for j in [1,2]:
#        print("i= ",i, " j = ",j)

#for i in range(2,10):
#    print("===",i,"단===")
#    for j in range(1,10):
#        print("%d * %d=%d" %(i,j,i*j))
#print()

for i in range(1, 11):
    if i == 5: continue
    print(i)
