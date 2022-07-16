from itertools import product


def solution(word):
    dictionary = []
    for i in range(1, 6):
        for j in product(["A", "E", "I", "O", "U"], repeat=i):
            dictionary.append("".join(list(j)))

    dictionary.sort()
    return dictionary.index(word) + 1
