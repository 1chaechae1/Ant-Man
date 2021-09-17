"""
name={1234:'김아산',1235:'박천안',1236:'이서울'}
print(name)
addr=dict(a1='서울',a2='대전',a3='천안')
print(addr)


a={"name":"임채현","phone":"01012345678","age":24}
print(a)
print(a["name"])
print(a.get('phone'))
print(a.keys())
print(a.values())


contact={"Lastname":"임", "Firstname":"채현", "Company":"대학교"}
for key, value in contact.items():
    print(key, ":", value)
"""

items = {"커피음료": 7, "펜": 3, "종이컵": 2, "우유": 1, "콜라": 4, "책": 5}
name = input("물건의 이름을 입력하시오: ")
print("재고: ", items[name])
