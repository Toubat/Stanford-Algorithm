import numpy as np

def findKClosestElements(arr, target, k):
    if not arr:
        return []
    idx = insertPosition(arr, target)
    i, j = idx - 1, idx
    k_closest = []
    while k > 0 and i >= 0 and j < len(arr):
        if i >= 0 and abs(arr[i] - target) < abs(arr[j] - target):
            k_closest.append(arr[i])
            i -= 1
        elif j < len(arr):
            k_closest.append(arr[j])
            j += 1
        k -= 1
    if k > 0:
        if i >= 0:
            k_closest += arr[max(0, i - k + 1):i+1]
            i -= 1
        elif j < len(arr):
            k_closest += arr[j:j+k]

    return k_closest


def insertPosition(arr, target):
    left, right = 0, len(arr) - 1
    while left + 1 < right:
        mid = left + (right - left) // 2
        if arr[mid] >= target:
            right = mid
        else:
            left = mid + 1
    if arr[left] >= target:
        return left
    elif arr[right] >= target:
        return right
    else:
        return right + 1


def main():
    lst = [0.1994, 0.1994, 0.1993, 0.1993, 0.1992]
    print(np.std(lst))

    return 0


main()

