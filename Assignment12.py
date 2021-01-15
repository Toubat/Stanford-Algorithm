# Assignment 12
import sys
sys.setrecursionlimit(10000000)

def knapsack(capacity, items):
    cache = [[x for x in range(capacity+1)] for _ in range(len(items)+1)]
    for j in range(capacity+1):
        cache[0][j] = 0
    for idx in range(len(items)):
        value, weight = items[idx]
        i = idx + 1
        for j in range(1, capacity+1):
            if j - weight >= 0:
                cache[i][j] = max(cache[i-1][j], cache[i-1][j-weight] + value)
            else:
                cache[i][j] = cache[i-1][j]

    return cache[len(items)][capacity]


def knapsackRecursive(capacity, items, idx, cache=None):
    if cache is None:
        cache = {}
    if idx == -1:
        return 0
    i = idx + 1
    if str(capacity)+str(':')+str(i) in cache:
        return cache[str(capacity)+str(':')+str(i)]
    value, weight = items[idx]
    if capacity - weight >= 0:
        value_with_item = value + knapsackRecursive(capacity-weight, items, idx-1, cache)
        value_without_item = knapsackRecursive(capacity, items, idx-1, cache)
        cache[str(capacity)+str(':')+str(i)] = max(value_with_item, value_without_item)
    else:
        cache[str(capacity)+str(':')+str(i)] = knapsackRecursive(capacity, items, idx-1, cache)

    return cache[str(capacity)+str(':')+str(i)]


def initInput(lst, path):
    with open(path, 'r') as f:
        capacity, num_items = list(map(int, f.readline().split()))
        while True:
            line = f.readline()
            if not line:
                break
            value, weight = list(map(int, line.split()))
            lst.append((value, weight))

    return capacity, num_items


def main():
    lst = []
    capacity, num_items = initInput(lst, 'assign12_input_1.txt')
    max_value = knapsack(capacity, lst)
    print("Max value is: ", max_value)

    lst = []
    capacity, num_items = initInput(lst, 'assign12_input_2.txt')
    max_value = knapsackRecursive(capacity, lst, len(lst) - 1)
    print("Max value is: ", max_value)

    return 0


if __name__ == '__main__':
    main()