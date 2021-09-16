import sys
# 순차 탐색 구현
def sequential_search(n, target, array):
    for i in range(n):
        if array[i] == target:
            return i+1 # 인덱스가 아닌 '몇'번째 데이터인지 변환

array = [i for i in range(10, 30, 2)]
n = len(array)
target = 14

res = sequential_search(n, target, array)
print(f"{target} 데이터는 array의 {res}번째에 존재!")
