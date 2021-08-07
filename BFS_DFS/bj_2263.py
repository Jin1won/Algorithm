import sys
sys.setrecursionlimit(10**5)

n = int(sys.stdin.readline().strip())
inorder = list(map(int,sys.stdin.readline().split()))
postorder = list(map(int,sys.stdin.readline().split()))

fast = [0]*(n+1) 
for i in range(1, n): #한번에 root에 해당하는 inorder의  i를 찾기 위해서 설정 
    fast[inorder[i]] = i


def preorder(in_s, in_e, po_s, po_e):
    if (in_s>in_e or po_s>po_e):
        return

    root = postorder[po_e]
    print(root, end=" ")

    left_length = fast[root] - in_s
    right_length = in_e - fast[root]
    preorder(in_s, in_s+left_length-1, po_s, po_s+left_length-1) #왼쪽 서브트리 탐색
    preorder(in_e-right_length+1, in_e, po_e-right_length, po_e-1)#오른쪽 서브트리 탐색

preorder(0, n-1, 0, n-1)