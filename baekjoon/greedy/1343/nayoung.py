def solution():
    board = input().split('.')
    answer = ''
    a = 'AAAA'
    b = 'BB'
    for i in range(len(board)):
        temp = ''
        c1, c2 = divmod(len(board[i]), 4)
        temp += (a * c1)
        if c2 == 0:
            if i != len(board) - 1:
                temp += '.'
            answer += temp
            continue
        c3, c4 = divmod(c2, 2)
        temp += (b * c3)
        if c4 != 0:
            print(-1)
            return
        if i != len(board) - 1:
            temp += '.'
        answer += temp
    print(answer)

solution()