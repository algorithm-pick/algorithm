import itertools

def solution(word):
    sets = ['A', 'E', 'I', 'O', 'U']
    arr = [('A'), ('E'), ('I'), ('O'), ('U')]
    arr += list(itertools.product(sets, repeat = 2))
    arr += list(itertools.product(sets, repeat = 3))
    arr += list(itertools.product(sets, repeat = 4))
    arr += list(itertools.product(sets, repeat = 5))
    for i in range(len(arr)):
        arr[i] = ''.join(arr[i])
    arr.sort()
    return arr.index(word) + 1

print(solution("AAAAE", 6))