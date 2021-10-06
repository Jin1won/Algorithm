def solution(gems):
    le = [[0,0] for _ in range(len(gems))] #i번째부터 모든 보석을 포함하는 가장 짧은 길이와 끝 인덱스 저장
    max_len = 0
    for i in range(len(gems)):
        l = [gems[i]]
        cnt = 1
        le[i][0] = cnt
        le[i][1] = i
        for j in range(i+1,len(gems)):
            if gems[j] not in l:
                l.append(gems[j])
                cnt += 1
                le[i][0] = cnt
                le[i][1] = j
        max_len = max(max_len,cnt)
    start = 1
    end = len(gems)
    for i in range(len(le)):
        if le[i][0] == max_len:
            if end-start > le[i][1]-i:
                start = i+1
                end = le[i][1]+1
    answer = [start,end]
    return answer

print(solution(["XYZ", "XYZ", "XYZ"]))