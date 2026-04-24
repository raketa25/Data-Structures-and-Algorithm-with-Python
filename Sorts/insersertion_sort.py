"""
This code implements the insertion sort algorithm, which is a simple sorting algorithm that builds the final sorted array one item at a time. It works by repeatedly taking the next unsorted item and inserting it into the correct position in the already sorted part of the array. The algorithm has an average and worst-case time complexity of O(n^2), but it performs well on small or partially sorted lists.

The insertion sort algorithm is efficient for small data sets and is often used as a building block in more complex sorting algorithms, such as Timsort. It is also an in-place sorting algorithm, meaning it does not require additional space for another array, making it memory efficient.
"""


def insertion_sort(myList):

    for i in range(1, len(myList)):
        temp = myList[i]
        j = i - 1            # keep track of the index of the last sorted element

        while temp < myList[j] and j > -1:
            myList[j + 1] = myList[j]
            myList[j] = temp
            j -= 1

    return myList




if __name__ == "__main__":
    myList = [5, 8, 2, 9, 1, 7, 5, 6]
    sortedList = insertion_sort(myList)
    print("Sorted List:", sortedList)