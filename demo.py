def minTime(levels, current, sword):
    if current <= sword:
        return levels
    else:
        time_1 = current - 1 + (current - sword) + (levels - sword)
        time_2 = current + levels

        return min(time_1, time_2)


def main():
    T = input()
    for i in range(int(T)):
        case = input()
        levels, current, sword = list(map(int, input().split()))
        time = minTime(levels, current, sword)
        print(f'Case #{i + 1}: {time}')

    return 0


main()

