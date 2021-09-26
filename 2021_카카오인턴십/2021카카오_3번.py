def solution(n, k, cmd):
    table = []
    for i in range(n):
        table.append(i)
    index = k #테이블 포인터
    r = [] #삭제된 값의 인덱스 넘버 저장할 리스트
    for i in cmd:
        if i[0] == 'U':
            index -= int(i[2:])
        elif i[0] == 'D':
            index += int(i[2:])
        elif i[0] == 'C':
            if index == len(table)-1:
                r.append(table.pop())
                index -= 1
            else:
                r.append(table.pop(index))
        elif i[0] == 'Z':
            d = r.pop()
            table.append(d)
            table.sort()
            if d <= table[index]:
                index += 1
    answer=''
    for i in range(n):
        if i in table:
            answer += 'O'
        else:
            answer += 'X'
    return answer

print(solution(8,2,	["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))