import random

def randomSelection(arr, left, right, order): # average runtime O(n)
    order -= 1
    if len(arr) == 1:
        return arr[0]
    swap(arr, random.randint(left, right), left)
    pivot = arr[left]
    linearPartition(arr, pivot, left, right)
    idx = arr.index(pivot)
    if order == idx:
        return pivot
    elif order < idx:
        return randomSelection(arr, left, idx - 1, order + 1)
    else:
        return randomSelection(arr, idx + 1, right, order + 1)


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
    # 500 unittests
    lst = list(range(1, 101))
    for i in range(500):
        random.shuffle(lst)
        order = random.randint(1, 100)
        num_in_order = randomSelection(lst, 0, len(lst) - 1, order)
        assert num_in_order == order


if __name__ == '__main__':
    main()