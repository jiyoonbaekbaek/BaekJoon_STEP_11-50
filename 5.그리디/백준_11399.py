import sys
input=sys.stdin.readline

class LineUp:
    def read(self):
        self.n=int(input())
        self.info=list(map(int,input().split()))
    def solve(self):
        ans=0
        cur=0
        self.info=sorted(self.info)
        for i in range(self.n,0,-1): #5명이면 weight 은 5 ~ 1 
            ans+=self.info[cur]*i
            cur+=1
        print(ans)

lu=LineUp()
lu.read()
lu.solve()
