def selectionSort(list):
    index = 0
    for i in range(len(list)):
        index = i
        for j in range(i + 1, len(list)):
            if list[index] > list[j]:
                index = j
                list[i], list[index] = list[index], list[i]
