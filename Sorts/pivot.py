def swap(myList, index1, index2):
    temp = myList[index1]
    myList[index1] = myList[index2]
    myList[index2] = temp


def pivot(myList, pivot_index, end_index):
    swap_index = pivot_index

    for i in range(pivot_index + 1, end_index + 1):
        if myList[i] < myList[pivot_index]:
            swap_index = += 1
            swap(myList, swap_index, i)
    swap(myList, pivot_index, swap_index)
    return swap_index


# Test case
if __name__ = "__main__":
    myList = [4, 6, 1, 7, 3, 2, 5]
    print("The sorted list is:> ", pivot(myList, 0, 6))
    print('\n')
    print(myList)