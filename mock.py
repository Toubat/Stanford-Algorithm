import pdb

def findShortestDistance(words, word1, word2):
    if not words:
        return float('inf')
    if word1 == word2:
        return findShortestDistanceOfSingleWord(words, word1)
    p1, p2 = 0, 0
    shortestSoFar = float('inf')
    while p1 < len(words) and p2 < len(words):
        if words[p1] != word1:
            p1 += 1
        if words[p2] != word2:
            p2 += 1
        if p1 < len(words) and p2 < len(words) and words[p1] == word1 and words[p2] == word2:
            d = abs(p1 - p2)
            shortestSoFar = min(d, shortestSoFar)
            # increment pointer with lowest index by 1
            if p1 < p2:
                p1 += 1
            elif p1 > p2:
                p2 += 1

    return shortestSoFar

def findShortestDistanceOfSingleWord(words, word):
    p1, p2 = None, None
    shortestSoFar = float('inf')
    for i in range(len(words)):
        if words[i] == word:
            if p2 is None:
                p2 = i
            else:
                p1 = p2
                p2 = i
                shortestSoFar = min(abs(p2 - p1), shortestSoFar)

    return shortestSoFar


def main():

    testcases = [
        ['a', 'b', 'c', 'd', 'a', 'd', 'f'],  # ans -> 1
        ['a', 'a', 'a', 'b', 'b', 'c', 'f'],  # ans -> 1
        ['a', 'd', 'b', 'c', 'a', 'a', 'f'],  # ans -> 2
        ['a', 'c', 'c', 'c', 'c', 'c', 'c'],  # ans -> inf
        ['a', 'e', 'c', 'd', 'b', 'r', 'a'],  # ans -> 2
        [], # ans -> inf
        ['a', 'c', 'd', 'f', 'e', 'r', 'b'],   # ans -> 6
        ['e', 'a', 'e', 'e', 'b', 'e', 'e', 'b', 'e', 'e', 'b', 'c', 'c', 'a', 'a']  # ans -> 3
    ]
    ans = [1, 1, 2, float('inf'), 2, float('inf'), 6, 3]
    ans2 = [4, 1, 1, float('inf'), 6, float('inf'), float('inf'), 1]
    for i in range(len(testcases)):
        d = findShortestDistance(testcases[i], 'a', 'b')
        print(f"{ans[i]} ---> {d}")
        assert d == ans[i]


    return 0


if __name__ == '__main__':
    main()