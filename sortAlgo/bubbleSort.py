def bubbleSort(list):
    index = len(list) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(index):
            if list[i] > list[i + 1]:
                sorted = False
                # print("前面的list[i]:" + i + "/ " + list[i])
                list[i], list[i + 1] = list[i + 1], list[i]
                # print("后面的list[i]:" + i + "/ " + list[i])
        index = index - 1
