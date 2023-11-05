def insertSort(list):
    for i in range(1, len(list)):
        temp = list[i]

        for j in range(i - 1, -1, -1):
            if list[j] > temp:
                list[j + 1], list[j] = list[j], list[j + 1]
                list[j] = temp
