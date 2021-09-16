import sys
# 1. 재귀함수로 구현
def binary_search(array, target, start, end):
    if start > end:
        return None
    middle = (start + end) // 2
    if array[middle] == target:
        return middle + 1
    elif array[middle] < target:
        return binary_search(array, target, middle+1, end)
    else:
        return binary_search(array, target, start, middle-1)

    n, target = list(map(int, input().split()))
    array = list(map(int, input().split()))

    result = binary_search(array, target, 0, n-1)
    if result == None:
        print("존재하는 원소가 없습니다!")
    else:
        print(result)
