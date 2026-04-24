def find_max_min(myList):
    if len(myList) == 0:
        return None, None

    max_val = myList[0]
    min_val = myList[0]

    for num in myList:
        if num > max_val:
            max_val = num
        elif num < min_val:
            min_val = num

    results = (max_val, min_val)

    return results


if __name__ == "__main__":
    print( find_max_min([5, 3, 8, 1, 6, 9]) )


    """
        EXPECTED OUTPUT:
        ----------------
        (9, 1)
        
    """
