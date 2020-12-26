import random

def randomSelection(arr, order): # average runtime O(n)
    if len(arr) == 1:
        return arr[0]
    idx = random.randint(0, len(arr) - 1)
    pivot = arr[idx]
    linearPartition(arr, pivot, 0, len(arr) - 1)
    if order - 1 == idx:
        return pivot
    elif order - 1 > idx:
        return randomSelection(arr[:idx], order)
    else:
        return randomSelection(arr[idx+1:], order - idx - 1)


def deterministicSelection(arr, order): # average runtime O(n)
    pass

def linearPartition(array, pivot, left, right):
    i = left + 1
    for j in range(left + 1, right + 1):
        if array[j] < pivot:
            swap(array, i, j)
            i += 1
    swap(array, left, i - 1)

    return i - 1

def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

    return 0

def main():
    lst = [3, 8, 2, 5, 1, 4, 7, 6]
    num = randomSelection(lst, 1)
    print(num)


if __name__ == '__main__':
    main()