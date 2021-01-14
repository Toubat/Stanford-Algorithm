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

# O(n) time | O(m) space - where n is length of "words" list, m is the length of "given_words" list
def minDistances(words, given_words):
    if not words:
        return float('inf')
    cache = {}
    # bookkeeping parameter
    # key -> string | value -> number of string
    for word in given_words:
        if word in cache:
            cache[word] += 1
        else:
            cache[word] = 1
    slow, fast = 0, -1
    match_count = 0
    min_distance = float('inf')
    while True:
        if match_count < len(cache):
            fast += 1
            current = words[fast]
            if current in cache:
                if cache[current] == 1:
                    match_count += 1
                cache[current] -= 1
        if match_count == len(cache):
            min_distance = min(min_distance, fast - slow)
            current = words[slow]
            if current in cache:
                if cache[current] == 0:
                    match_count -= 1
                cache[current] += 1
            slow += 1
        # terminate condition
        if fast == len(words) - 1 and match_count != len(cache):
            break

    return min_distance


def main():

    testcases = [  # test distance(a, b, c, c)
        ['a', 'b', 'c', 'd', 'a', 'c', 'f'],  # ans -> 4
        ['c', 'a', 'a', 'b', 'b', 'c', 'f'],  # ans -> 5
        ['a', 'd', 'b', 'c', 'a', 'a', 'f'],  # ans -> inf
        ['a', 'c', 'c', 'c', 'b', 'c', 'c'],  # ans -> 4
        ['a', 'e', 'c', 'd', 'b', 'c', 'a'],  # ans -> 4
        [],                                   # ans -> inf
        ['a', 'c', 'd', 'f', 'e', 'r', 'b', 'r', 'e', 'g', 'c', 'y', 'u', 'a', 'b'],  # ans -> 10
        ['e', 'a', 'e', 'e', 'b', 'e', 'e', 'b', 'e', 'e', 'b', 'c', 'c', 'a', 'a']   # ans -> 3
    ]
    ans = [4, 5, float('inf'), 4, 4, float('inf'), 10, 3]

    for i in range(len(testcases)):
        d = minDistances(testcases[i], ['a', 'b', 'c', 'c'])
        print(f"{ans[i]} ---> {d}")
        assert d == ans[i]

    return 0


if __name__ == '__main__':
    main()