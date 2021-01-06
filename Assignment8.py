# Assignment 8

# Worst: O(n^2) time | O(n) space
# Average: O(nlogn) time | O(n) space
def twoSumInRange(lst, left_bound, right_bound):
    hash_table = {}
    num_targets = 0
    lst.sort()
    i, j = 0, len(lst) - 1
    while i < j:
        # if two number sum is not in range, increment or decrement pointers
        if lst[i] + lst[j] < left_bound:
            i += 1
        elif lst[i] + lst[j] > right_bound:
            j -= 1
        else:
            # if two number sum in range, then fix position j, increment pointer i to find all pairs of distinct numbers
            # in that range until lst[i] + lst[j] is not in range
            idx = i
            while idx < len(lst) and inRange(lst[idx] + lst[j], left_bound, right_bound):
                if lst[idx] != lst[j] and lst[idx] + lst[j] not in hash_table:
                    hash_table[lst[idx] + lst[j]] = True
                    num_targets += 1
                idx += 1
            # when finished an iteration, decrement j by 1 to find new set of pairs
            j -= 1

    return num_targets


def inRange(num, left, right):
    return left <= num <= right


def init_input(lst, path):
    file = open(path, 'r')
    while True:
        num = file.readline()
        if not num:
            break
        lst.append(int(num))

    return 0


def main():
    lst = []
    init_input(lst, 'assign8_input.txt')
    num_targets = twoSumInRange(lst, -10000, 10000)
    print(f'Number of target value t formed by distinct value such that x + y = t is: {num_targets}')

    return 0


if __name__ == '__main__':
    main()