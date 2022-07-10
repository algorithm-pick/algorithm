from collections import defaultdict

def solution(genres, plays):
    answer = []
    genres_dict = defaultdict(list)
    genres_sum = defaultdict(int)
    for i in range(len(genres)):
        genres_sum[genres[i]] += plays[i]
        genres_dict[genres[i]].append([plays[i], i])
    genres_sum = sorted(genres_sum.items(), key=lambda x: x[1], reverse=True)
    for i in genres_sum:
        genres_dict[i[0]].sort(key=lambda x: (-x[0], x[1]))
        answer.append(genres_dict[i[0]][0][1])
        if len(genres_dict[i[0]]) >= 2:
            answer.append(genres_dict[i[0]][1][1])
    return answer

print(solution(["classic", "Newage", "pop", "classic", "classic", "pop", "Newage"], [500, 1700, 600, 150, 800, 2500, 1500]))