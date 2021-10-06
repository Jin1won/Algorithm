def solution(numbers, hand):
    answer = ''
    previous_position_L = [[-3,0]]
    previous_position_R = [[-3,2]]
    for number in numbers:
        if number % 3 == 1:
            answer += 'L'
            if number == 1:
                previous_position_L.append([0,0])
            elif number == 4:
                previous_position_L.append([-1,0])
            else:
                previous_position_L.append([-2,0])
        elif number % 3 == 0 and number != 0:
            answer += 'R'
            if number == 3:
                previous_position_R.append([0,2])
            elif number == 6:
                previous_position_R.append([-1,2])
            else:
                previous_position_R.append([-2,2])
        elif number % 3 == 2 or number == 0:
            lx,ly = previous_position_L[-1]
            rx,ry = previous_position_R[-1]
            if number == 2:
                l_length = abs(lx-0)+abs(ly-1)
                r_length = abs(rx-0)+abs(ry-1)
                if l_length < r_length:
                    answer += 'L'
                    previous_position_L.append([0,1])
                elif r_length < l_length:
                    answer += 'R'
                    previous_position_R.append([0,1])
                else:
                    if hand == 'left':
                        answer += 'L'
                        previous_position_L.append([0,1])
                    else:
                        answer += 'R'
                        previous_position_R.append([0,1])
            elif number == 5:
                l_length = abs(lx+1)+abs(ly-1)
                r_length = abs(rx+1)+abs(ry-1)
                if l_length < r_length:
                    answer += 'L'
                    previous_position_L.append([-1,1])
                elif r_length < l_length:
                    answer += 'R'
                    previous_position_R.append([-1,1])
                else:
                    if hand == 'left':
                        answer += 'L'
                        previous_position_L.append([-1,1])
                    else:
                        answer += 'R'
                        previous_position_R.append([-1,1])
            elif number == 8:
                l_length = abs(lx+2)+abs(ly-1)
                r_length = abs(rx+2)+abs(ry-1)
                if l_length < r_length:
                    answer += 'L'
                    previous_position_L.append([-2,1])
                elif r_length < l_length:
                    answer += 'R'
                    previous_position_R.append([-2,1])
                else:
                    if hand == 'left':
                        answer += 'L'
                        previous_position_L.append([-2,1])
                    else:
                        answer += 'R'
                        previous_position_R.append([-2,1])
            else:
                l_length = abs(lx+3)+abs(ly-1)
                r_length = abs(rx+3)+abs(ry-1)
                if l_length < r_length:
                    answer += 'L'
                    previous_position_L.append([-3,1])
                elif r_length < l_length:
                    answer += 'R'
                    previous_position_R.append([-3,1])
                else:
                    if hand == 'left':
                        answer += 'L'
                        previous_position_L.append([-3,1])
                    else:
                        answer += 'R'
                        previous_position_R.append([-3,1])
    return answer