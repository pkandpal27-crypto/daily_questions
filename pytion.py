def insertionSort(arr):
    s = len(arr)
    if s <= 1:
        return
    
    # Start from the second element
    for i in range(1, s):
        key = arr[i]
        j = i - 1
        
        # Move elements greater than key one step ahead
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
