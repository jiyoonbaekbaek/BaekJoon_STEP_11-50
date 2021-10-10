import sys
input=sys.stdin.readline

class FindMax:
    def read(self):
        self.n=int(input())
        self.numb=list(map(int,input().split()))
    
    def solve(self):
        self.dp=[]
        for i in range(self.n):
            cur=[]
            if i==0:
                cur.append(self.numb[0])
                self.dp.append(cur)
            else:
                cur.append(max(self.dp[i-1])+self.numb[i])
                cur.append(self.numb[i])
                self.dp.append(cur)
        ans=float("-inf")
        for cand in self.dp:
            cur_cand=max(cand)
            if cur_cand>ans:
                ans=cur_cand
        print(ans)
       
        
fm=FindMax()
fm.read()
fm.solve()
