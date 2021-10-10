import sys
import copy
input=sys.stdin.readline

class Wine:
    def read(self):
        self.n=int(input())
        self.info=[int(input()) for _ in range(self.n)]
    
    def solve(self): 
        self.dp=[]
        for i in range(self.n):
            cur=[]
            if i==0:
                cur.append(0)
                cur.append(self.info[i])
                self.dp.append(cur)
            elif i==1:
                cur.append(self.dp[-1][1]+self.info[i])
                cur.append(self.info[i])
                self.dp.append(cur)
            elif i>=5-1:
                cur.append(self.dp[-1][1]+self.info[i])
                op=copy.deepcopy(self.dp[-2])
                op.append(self.dp[-3][0])
                cur.append(max(op)+self.info[i])
                self.dp.append(cur)
            else:
                cur.append(self.dp[-1][1]+self.info[i])
                cur.append(max(self.dp[-2])+self.info[i])
                self.dp.append(cur)
        if self.n>1:
            cand1=max(self.dp[-2])
            cand2=max(self.dp[-1])
            ans=max(cand1,cand2)
        else:
            ans=max(self.dp[-1])
        print(ans)

wine=Wine()
wine.read()
wine.solve()
