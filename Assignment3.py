# Assignment 3

def quicksort(array, left, right, policy):
    if right <= left:
        return 0
    else:
        numCompare = right - left
        pivot = choosePivot(array, left, right, policy)
        idx = linearPartition(array, pivot, left, right)
        leftCompare = quicksort(array, left, idx - 1, policy)
        rightCompare = quicksort(array,  idx + 1, right, policy)

    return numCompare + leftCompare + rightCompare


def choosePivot(array, left, right, policy):
    if policy == 'first':
        return array[left]
    elif policy == 'final':
        swap(array, left, right)
        return array[left]
    elif policy == 'middle':
        idx = findMedian(array, left, right)
        swap(array, left, idx)
        return array[left]


def findMedian(array, left, right):
    mid_idx = (right + left) // 2
    middle = array[mid_idx]
    
    if array[left] <= middle <= array[right] or array[right] <= middle <= array[left]:
        return mid_idx
    elif middle <= array[left] <= array[right] or array[right] <= array[left] <= middle:
        return left
    elif array[left] <= array[right] <= middle or middle <= array[right] <= array[left]:
        return right
    else:
        print(f"{array[left]}, {middle}, {array[right]}")
        return None


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


def isSorted(arr):
    i = 0
    while i < len(arr) - 1:
        if arr[i] > arr[i+1]:
            return False
        i += 1
    return True


def main():
    file = open("assign3_input.txt", 'r')
    lst = []
    
    while True:
        num = file.readline()
        if not num:
            break
        lst.append(int(num))

    polices = ['first', 'final', 'middle']
    for policy in polices:
        numCompare = quicksort(lst[:], 0, len(lst) - 1, policy)
        print(f"Total number of comparisons under choosing '{policy}' policy is : {numCompare}")

    return 0


if __name__ == '__main__':
    main()