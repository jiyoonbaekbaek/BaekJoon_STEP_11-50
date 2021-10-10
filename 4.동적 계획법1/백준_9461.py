import sys
from collections import deque
input=sys.stdin.readline

class PD:
    def read(self):
       self.n=int(input())
       self.x=[int(input()) for _ in range(self.n)]
       self.pd=deque([1,1,1])
    
    def solve(self):
        ans=[]
        while len(ans)<max(self.x):
            c1=self.pd.popleft()
            ans.append(c1)
            c2=self.pd[0]
            self.pd+=[c1+c2]
        for nb in self.x:
            print(ans[nb-1])

pd=PD()
pd.read()
pd.solve()
