









def main():
    file = open("assign4_input.txt", 'r')
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