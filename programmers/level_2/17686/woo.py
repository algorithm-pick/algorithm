def solution(files):
    answer = []
    files_dict = dict()
    for i in files:
        length = len(i)
        files_dict[i] = []
        next1 = 0
        for j in range(length):
            if i[j].isdigit():
                files_dict[i].append(i[:j].lower())
                next1 = j
                break
        next2 = 0
        for k in range(next1, length):
            if k >= (next1 + 5):
                files_dict[i].append(int(i[next1:k]))
                next2 = k
                break
            if not i[k].isdigit():
                files_dict[i].append(int(i[next1:k]))
                next2 = k
                break
        if next2 == 0:
            files_dict[i].append(int(i[next1:]))
            continue
        files_dict[i].append(i[next2:])
    sorted_dict = sorted(files_dict.items(), key=lambda x : (x[1][0], x[1][1]))
    for i in sorted_dict:
        answer.append(i[0])
    return answer

print(solution(["img12", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))