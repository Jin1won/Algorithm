def solution(expression):
    num = ''
    array = []
    for char in expression:
        if char not in '+-*':
            num += char
        else:
            array.append(int(num))
            array.append(char)
            num = ''
    array.append(int(num))
    cases = [['+','-','*'],['+','*','-'],['-','+','*'],['-','*','+'],['*','+','-'],['*','-','+']]
    
    sum = []
    for case in cases:
        temp = array[:]
        for operator in case:
            i=0
            while operator in temp:
                if temp[i] == operator:
                    if temp[i] == "+":
                        temp[i-1]=int(temp[i-1])+int(temp[i+1])
                        temp.pop(i+1)
                        temp.pop(i)
                    elif temp[i] == "-":
                        temp[i-1]=int(temp[i-1])-int(temp[i+1])
                        temp.pop(i+1)
                        temp.pop(i)
                    elif temp[i] == "*":
                        temp[i-1]=int(temp[i-1])*int(temp[i+1])
                        temp.pop(i+1)
                        temp.pop(i)
                else:
                    i += 1
        sum.append(abs(temp[0]))
    answer = max(sum)
    return answer

print(solution("50*6-3*2"))