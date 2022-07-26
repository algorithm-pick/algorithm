def solution(bridge_length, weight, truck_weights):
    answer = 0
    current = [0] * bridge_length
    current_sum = 0
    while True:
        answer += 1
        current_sum -= current.pop(0)
        if not truck_weights:
            current.append(0)
        else:
            if current_sum + truck_weights[0] <= weight:
                temp = truck_weights.pop(0)
                current.append(temp)
                current_sum += temp
            else:
                current.append(0)
        if current_sum == 0:
            break
    return answer

print(solution(2, 10, [7,4,5,6]))