def solution(s):
    answer = ""
    word =""
    for i in range(len(s)):
        word +=s[i]
        if word == "0" or word == "zero":
            word=""
            answer += '0'
        if word == "1" or word == "one":
            word=""
            answer += '1'
        if word == "2" or word == "two":
            word=""
            answer += '2'
        if word == "3" or word == "three":
            word=""
            answer += '3'
        if word == "4" or word == "four":
            word=""
            answer += '4'
        if word == "5" or word == "five":
            word=""
            answer += '5'
        if word == "6" or word == "six":
            word=""
            answer += '6'
        if word == "7" or word == "seven":
            word=""
            answer += '7'
        if word == "8" or word == "eight":
            word=""
            answer += '8'
        if word == "9" or word == "nine":
            word=""
            answer += '9'
    return int(answer)