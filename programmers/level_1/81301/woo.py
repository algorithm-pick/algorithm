def solution(s):
    answer = ""
    while len(s) != 0:
        if s[0] == "0" or s[0] == "1" or s[0] == "2" or s[0] == "3" or s[0] == "4" or s[0] == "5" or s[0] == "6" or s[0] == "7" or s[0] == "8" or s[0] == "9":
            answer += s[0]
            s = s[1:len(s)]
        elif s[0:4] == "zero":
            answer += "0"
            s = s[4:len(s)]
        elif s[0:3] == "one":
            answer += "1"
            s = s[3:len(s)]
        elif s[0:3] == "two":
            answer += "2"
            s = s[3:len(s)]
        elif s[0:5] == "three":
            answer += "3"
            s = s[5:len(s)]
        elif s[0:4] == "four":
            answer += "4"
            s = s[4:len(s)]
        elif s[0:4] == "five":
            answer += "5"
            s = s[4:len(s)]
        elif s[0:3] == "six":
            answer += "6"
            s = s[3:len(s)]
        elif s[0:5] == "seven":
            answer += "7"
            s = s[5:len(s)]
        elif s[0:5] == "eight":
            answer += "8"
            s = s[5:len(s)]
        elif s[0:4] == "nine":
            answer += "9"
            s = s[4:len(s)]
    return int(answer)

print(solution("one4seveneight"))