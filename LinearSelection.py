import random
from Assignment3 import *

def randomSelection(arr, left, right, order):  # average runtime O(n)
    if len(arr) == 1:
        return arr[0]
    swap(arr, random.randint(left, right), left)
    pivot = arr[left]
    linearPartition(arr, pivot, left, right)
    idx = arr.index(pivot)
    if order - 1 == idx:
        return pivot
    elif order - 1< idx:
        return randomSelection(arr, left, idx - 1, order)
    else:
        return randomSelection(arr, idx + 1, right, order)


def deterministicSelection(arr, left, right, order):  # average runtime O(n)
    if len(arr) == 1:
        return arr[0]
    # divide array into subarrays of size 5, and sort each of them; pick median of each subarray
    mid_arr = divideSortPickMedians(arr, left, right, 5)
    pivot = deterministicSelection(mid_arr, 0, len(mid_arr) - 1, len(mid_arr) // 2)
    idx = arr.index(pivot)
    swap(arr, idx, left)
    pivot = arr[left]
    linearPartition(arr, pivot, left, right)
    idx = arr.index(pivot)
    if order - 1 == idx:
        return pivot
    elif order - 1 < idx:
        return deterministicSelection(arr, left, idx - 1, order)
    else:
        return deterministicSelection(arr, idx + 1, right, order)


def divideSortPickMedians(arr, left_idx, right_idx, size):
    left, right = left_idx, left_idx + size - 1
    mid_arr = []
    while True:
        if right <= right_idx:
            quicksort(arr, left, right, 'middle')
            mid_arr.append(arr[(right + left) // 2])
        elif right > right_idx >= left:
            quicksort(arr, left, right_idx, 'middle')
            mid_arr.append(arr[(left + right_idx) // 2])
            break
        elif right > right_idx and left > right_idx:
            break
        left = right + 1
        right += size

    return mid_arr


def main():
    # 500 Unit-Tests
    lst = list(range(1, 101))
    for i in range(500):
        random.shuffle(lst)
        order = random.randint(1, 100)
        num_in_order = randomSelection(lst[:], 0, len(lst) - 1, order)
        assert num_in_order == order
        num_in_order = deterministicSelection(lst[:], 0, len(lst) - 1, order)
        assert num_in_order == order


if __name__ == '__main__':
    main()