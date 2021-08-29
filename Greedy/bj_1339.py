import sys

n = int(sys.stdin.readline().strip())

words = [] # 단어를 담을 리스트

for i in range(n):
    words.append(sys.stdin.readline().strip())

alphabet_to_num = {}

for word in words:
    cnt = 1 # 만약 단어가 n자리 수 라면 n-1승 부터 시작해야 하므로 초기값을 1로 둔다.
    for i in word:
        if i not in alphabet_to_num: # 알파벳이 딕셔너리에 아직 없는 알파벳이면 자릿수에 맞는 숫자를 곱한 후 새로 추가해준다.
            alphabet_to_num[i] = 10 ** (len(word)-cnt)
        elif i in alphabet_to_num: # 알파벳이 이미 딕셔너리에 있으면 기존 숫자에 현재 자릿수만큼 곱한 뒤 얻은 값을 더해준다.
            alphabet_to_num[i] += 10 ** (len(word)-cnt)
        cnt += 1

number_list = list(sorted(alphabet_to_num.items(),key=lambda x : x[1],reverse=True)) # 딕셔너리의 value 값을 기준으로 내림차순으로 sort를 돌려준다.

result = 0

for i in range(len(number_list)): # 내림차순으로 정렬된 딕셔너리의 value값들을 9 부터 차례대로 곱해준다.
    result += number_list[i][1] * (9-i)

print(result)