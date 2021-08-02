import sys

n, r, c = map(int, sys.stdin.readline().split())

sqr = 2 ** n

def search(y , x, size): 
    for i in range(y, y+size): 
        for j in range(x, x+size): 
            if size != 2:
                search(y, x, size//2)
                search(y,(x+((size//2)*(size//2))),size//2)
                search((y+((size//2)*(size//2)*2)),x,size//2)
                search((y+((size//2)*(size//2)*3)),(x+size//2),size//2)
                return