def score_sort(array):
    n = len(array)
    for end in range(1,n):
        for current in range(end, 0, -1):
            if array[current-1][1] > array[current][1]:
                array[current-1], array[current] = array[current], array[current-1]
    return array

score_array = [['James', 40], ['Mason', 70], ['Thiago', 80], ['Kai', 60], ['Trevoh',5]]

print('정렬 전 --> ' , score_array)
score_array = score_sort(score_array)
print('정렬 후 --> ', score_array)

print('스코어별 조편성')
for i in range(len(score_array)//2):
    print(score_array[i][0], ':', score_array[len(score_array)-1-i][0])

