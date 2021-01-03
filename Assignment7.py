# Assignment 7
from structure_utils import *
import math

def medianMaintenance(lst):
    medians = []
    large_half = MinHeap([])
    small_half = MaxHeap([])
    for num in lst:

        if not len(large_half) and not len(small_half):
            small_half.insert(num, num)
            medians.append(num)
        else:
            if num >= small_half.peek():
                large_half.insert(num, num)
            else:
                small_half.insert(num, num)
            balanceTwoHeaps(large_half, small_half)
            k = math.ceil((len(small_half) + len(large_half)) / 2)
            if len(small_half) == k:
                medians.append(small_half.peek())
            else:
                medians.append(large_half.peek())

    return medians


def balanceTwoHeaps(large_half, small_half):
    if len(large_half) - len(small_half) == 2:
        min_in_large_half = large_half.deleteMin().key
        small_half.insert(min_in_large_half, min_in_large_half)
    elif len(small_half) - len(large_half) == 2:
        max_in_small_half = small_half.deleteMax().key
        large_half.insert(max_in_small_half, max_in_small_half)

    return 0


def initInput(lst, path):
    file = open(path, 'r')
    while True:
        line = file.readline()
        if not line:
            break
        lst.append(int(line))

    return 0


def main():
    lst = []
    initInput(lst, 'assign7_input.txt')
    medians = medianMaintenance(lst)
    print(f'Sum of all medians mod 10000 is: {sum(medians) % 10000}')


if __name__ == '__main__':
    main()