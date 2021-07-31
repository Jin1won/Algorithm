import sys

n = int(sys.stdin.readline().strip())

def S(idx, size, stage):
    if (stage == 0):
        if (n == idx): 
            return 'm'
        return

    S(idx, (size - stage - 3) // 2, stage - 1)
    if ((idx + (size - stage - 3) // 2) == n): 
        return 'm'
    S(idx + ((size - stage - 3) // 2) + stage + 3, (size - stage - 3) / 2, stage - 1)


size, stage = 3, 0
while (n > size):
    stage +=1 
    size = size * 2 + stage + 3;

if S(1, size, stage) == None:
    print('o')
else:
    print('m')

#느려서 시간초과...