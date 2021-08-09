import sys
sys.setrecursionlimit(10**5)

preorder = []
count = 0
while count <= 10000:
    try:
        temp = int(input())
    except:
        break
    preorder.append(temp)
    count += 1

def postorder(start, end):
    if start > end:
        return

    br = end + 1 # 루트 보다 큰 지점의 인덱스 번호 담을 변수

    for i in range(start + 1, end + 1):  # 루트 보다 큰 지점은 오른쪽 서브 트리 작은 지점은 왼쪽 서브트리
        if preorder[start] < preorder[i]:
            br = i
            break

    postorder(start+1,br-1)#왼쪽 서브트리 탐색
    postorder(br, end)#오른쪽 서브트리 탐색
    print(preorder[start])

postorder(0, len(preorder)-1)