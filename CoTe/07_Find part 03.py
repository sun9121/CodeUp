# 가게의 부품 개수 파악
n = int(input())
# 가게에 있는 물품을 리스트로 받기
list_shop = list(map(int, input().split()))
list_shop.sort()
# 손님의 구매 개수 파악
m = int(input())
# 손님의 구매 목록 리스트로 받기
list_cstm = list(map(int, input().split()))

def binary_search(target, array, start, end):
    if start > end:
        # print('start : ', start)
        return None
    mid = (start + end) // 2
    # print(mid)
    if array[mid] == target:
        # print(f'mid:{mid}')
        # print(target)
        # print(array[mid])
        return mid + 1
    elif array[mid] < target:
        return binary_search(target, array, mid+1, end)
    else:
        return binary_search(target, array, start, mid-1)

for i in list_cstm:
    # print(f'i:{i}')
    result = binary_search(i, list_shop, 0, n-1)
    # print(result)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')

