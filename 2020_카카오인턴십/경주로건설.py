from collections import deque
def solution(board):
    direction_x = [1,-1,0,0] #0번째 아래, 1번째 위, 2번째 오른쪽, 3번째 왼쪽
    direction_y=[0,0,1,-1]
    dp = [[1000000000]*(1+len(board)) for _ in range(1+len(board))]
    visited = [[False]*len(board) for _ in range(len(board))]
    queue=deque()
    dp[0][0] = 0
    visited[0][0] = True
    queue.append((0,0,0,visited)) #아래방향      4번째 인자는 직전에 방향을 바꿨는    지 안바꿨는지 표시
    queue.append((0,0,2,visited)) #오른쪽방향
    while queue:
        x,y,d,visited = queue.popleft()
        for i in range(4):
            nx = x + direction_x[i]
            ny = y + direction_y[i]
            if 0 <= nx < len(board) and 0 <= ny < len(board[0]):
                if board[nx][ny] != 1:
                    if d == i: #같은 방향으로 이동하는 경우
                        if dp[nx][ny] >= dp[x][y]+100:
                            dp[nx][ny] = dp[x][y]+100
                            visited[nx][ny] = True
                            queue.append((nx,ny,i,visited))
                    else:
                        if dp[nx][ny] >= dp[x][y]+600:
                            dp[nx][ny] = dp[x][y]+600
                            visited[nx][ny] = True
                            queue.append((nx,ny,i,visited))
    answer = dp[len(board)-1][len(board)-1]
    return answer