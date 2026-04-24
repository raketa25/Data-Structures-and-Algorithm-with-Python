"""
This code implements the selection sort algorithm, which is a simple sorting algorithm that repeatedly finds the minimum element from the unsorted part of the array and places it at the beginning. The algorithm has an average and worst-case time complexity of O(n^2), making it inefficient for large data sets. However, it is easy to understand and implement, making it a popular choice for educational purposes when learning about sorting algorithms.

The selection sort algorithm is an in-place sorting algorithm, meaning it does not require additional space for another array, making it memory efficient. It is also a stable sorting algorithm, meaning that it preserves the relative order of equal elements. Despite its simplicity, selection sort is generally not used in practice due to its inefficiency compared to other sorting algorithms like quicksort or mergesort.
"""


def selection_sort(myList):
    for i in range(len(myList) - 1):
        min_index = i
        for j in range(i + 1, len(myList)):
            if myList[j] < myList[min_index]:
                min_index = j
        if min_index != i:
            temp = myList[i]
            myList[i] = myList[min_index]
            myList[min_index] = temp

    return myList
            
    


if __name__ == "__main__":
    myList = [5, 8, 2, 9, 1, 7, 5, 6]
    sortedList = selection_sort(myList)
    print("Sorted List:", sortedList)