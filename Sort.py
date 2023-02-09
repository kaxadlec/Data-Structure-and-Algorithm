import random
import time

def quick_sort(array, start, end):
    if end <= start:
        return
    low = start
    high = end

    pivot = array[(low + high) // 2]
    while low <= high:
        while array[low] < pivot:
            low = low + 1
        while array[high] > pivot:
            high = high - 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
            low, high = low + 1, high -1

    mid = low

    quick_sort(array, start, mid -1)
    quick_sort(array, mid, end)

def sort(array):
    quick_sort(array, 0, len(array) -1)


data_array = [1000, 10000, 12000, 15000]

for data in data_array:
    temp_array = [random.randint(10000, 99999) for _ in range(data)]
    quick_array = temp_array[:]

    print("데이터 수: ", data)
    start = time.time()
    sort(quick_array)
    end = time.time()
    print(f'퀵 정렬 --> {end-start} 초')
    print()