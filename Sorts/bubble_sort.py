"""
This code implements the bubble sort algorithm, which is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order. The process is repeated until the list is sorted. The algorithm has an average and worst-case time complexity of O(n^2), making it inefficient for large data sets. However, it is easy to understand and implement, making it a popular choice for educational purposes when learning about sorting algorithms.

The bubble sort algorithm is an in-place sorting algorithm, meaning it does not require additional space for another array, making it memory efficient. It is also a stable sorting algorithm, meaning that it preserves the relative order of equal elements. Despite its simplicity, bubble sort is generally not used in practice due to its inefficiency compared to other sorting algorithms like quicksort or mergesort.
"""


def bubble_sort(myList):
    for i in range(len(myList) - 1, 0, -1):
        for j in range(i):
            if myList[j] > myList[j + 1]:
                temp = myList[j]
                myList[j] = myList[j + 1]
                myList[j + 1] = temp
    return myList

if __name__ == "__main__":
    myList = [5, 8, 2, 9, 1, 7, 5, 6]
    sortedList = bubble_sort(myList)
    print("Sorted List:", sortedList)