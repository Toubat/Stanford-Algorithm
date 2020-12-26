# assignment 2


def countSplitInv(arr_left, arr_right, n):
    # arrA is a sorted array
    arrA, inv = [], 0
    i, j = 0, 0
    while i < len(arr_left) and j < len(arr_right):
        if arr_left[i] <= arr_right[j]:
            arrA.append(arr_left[i])
            i += 1
        else:
            arrA.append(arr_right[j])
            j += 1
            inv += len(arr_left) - i

    if i == len(arr_left) and j < len(arr_right):
        arrA += arr_right[j:]
    elif j == len(arr_right) and i < len(arr_left):
        arrA += arr_left[i:]

    return arrA, inv


def sortCountInv(arrA):
    # base case
    n = len(arrA)
    if n == 1:
        return arrA, 0
    else:
        arrB, x = sortCountInv(arrA[: n // 2])
        arrC, y = sortCountInv(arrA[n // 2:])
        arrD, z = countSplitInv(arrB, arrC, n)

    return arrD, x + y + z


def isSorted(arr):
    i = 0
    while i < len(arr) - 1:
        if arr[i] > arr[i+1]:
            return False
        i += 1
    return True


def main():
    file = open("assign2_input.txt", 'r')
    lst = []
    while True:
        line = file.readline()
        if not line:
            break
        lst.append(int(line))
    arr, inv = sortCountInv(lst)
    print(isSorted(arr))
    print(inv)

    return 0


main()