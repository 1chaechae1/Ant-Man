"""
num=[1,2,3]
print(num)
print(type(num))
print(num[0])
print(num[1])
print(num[2])


num=[1,2,3,4,5,6,7,8,9,10]
print(num[3:6])#시작번호:끝번호 -> 시작번호 ~ 끝번호-1
print(num[3:])
print(num[:6])
print(num[1:9:3])
print(num[0:9:2])
print(num[::-1])


num=[1,2,3]
#num[1:2] = ["a","b","c"]
num[1] = ["a","b","c"]
print(num)


black_pink = ["jisoo", "jennie", "lisa", "rose"]
print("jennie" in black_pink)
print("psy" in black_pink)


fruits = []
name = input("좋아하는 과일 이름을 입력하시오: ")
fruits.append(name)
name = input("좋아하는 과일 이름을 입력하시오: ")
fruits.append(name)
name = input("좋아하는 과일 이름을 입력하시오: ")
fruits.append(name)


name = input("과일의 이름을 입력하세요: ")
if name in fruits:
    print("이 과일은 당신이 좋아하는 과일입니다.")
else:
    print("이 과일은 당신이 좋아하는 과일이 아닙니다.")


s = "Python is strong"
print(s[0])
print(s[-6:])
print(s[:6])
print(s[7:9])

"""

