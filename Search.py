import random


def bin_search(ary, f_data) :
    start = 0
    end = len(ary) - 1

    while start <= end:
        mid = (start + end) // 2
        if f_data == ary[mid]:
            return mid
        elif f_data > ary[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return -1


data_array = ['펩시', '코카콜라', '맥콜', '삼다수', '솔의눈', '하이네켄', '비타오백']
sell_array = [random.choice(data_array) for _ in range(20)]


print('오늘 판매된 전체 물건(중복O, 정렬X): ', sell_array)
sell_array.sort()
print('오늘 판매된 전체 물건(중복O, 정렬O): ', sell_array)
sell_product = list(set(sell_array))
print('오늘 판매된 물품 종류(중복x): ', sell_product)

sell_list = []
for product in sell_product:
    cnt = 0
    pos = 0
    while pos != -1:
        pos = bin_search(sell_array, product)
        if pos != -1 :
            cnt += 1
            del(sell_array[pos])
    sell_list.append((product, cnt))

print()
print("결산 결과 ==>", sell_list)
