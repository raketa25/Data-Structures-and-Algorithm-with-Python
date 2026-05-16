from pivot import pivot, swap

def quick_sort_helper(myList, left, right):
    if left < right:
        pivot_index = pivot(myList, left, right)
        quick_sort_helper(myList, left, pivot_index - 1)
        quick_sort_helper(myList, pivot_index + 1, right)
    return myList

def quick_sort(myList):
    result = quick_sort_helper(myList, 0, len(myList) - 1)
    return result

# function to test the quick_sort function
if __name__ == "__main__":
    myList = [4, 6, 1, 7, 3, 2, 5]
    print("The sorted list is:> ", quick_sort(myList))