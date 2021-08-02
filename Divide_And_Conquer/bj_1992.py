import sys

n = int(sys.stdin.readline().strip())

video = []

for i in range(n):
    video.append(list(map(int,sys.stdin.readline().strip())))

def compression(y , x, size): #그래프의 좌표 값과 그래프의 사이즈를 파라미터로 설정
    for i in range(y, y+size): #2개의 for문을 사용해 (0,0)부터 (n,n)까지 탐색
        for j in range(x, x+size): 
            if video[y][x] != video[i][j]: #만약 (0,0)지점의 그래프 값과 탐색하려는 지점의 그래프 값이 다르면 한 번호로 합칠 수 없기 때문에 상하좌우 재귀함수를 호출
                print("(",end='')
                compression(y, x, size//2)
                compression(y,(x+size//2),size//2)
                compression((y+size//2),x,size//2)
                compression((y+size//2),(x+size//2),size//2)
                print(")",end='')
                return
    print(video[y][x],end='') #다 일치한다면 하나의 숫자로 합쳐서 출력할 수 있으므로 하나만 출력

compression(0,0,n)