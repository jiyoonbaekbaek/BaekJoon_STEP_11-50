import sys
input=sys.stdin.readline

class IT:
    def read(self):
        self.n=int(input())
        self.tri=[list(map(int,input().split())) for _ in range(self.n)]
        self.dp=[]
    
    def solve(self):
        if self.n==1:
            print(self.tri[0][0]) 
            return
        self.dp.append([self.tri[0][0]])
        for i in range(1,self.n):
            for j in range(len(self.tri[i])):
                if j==0:
                    self.dp.append([self.dp[i-1][0]+self.tri[i][j]])
                elif j==len(self.tri[i])-1:
                    self.dp[i].extend([self.dp[i-1][j-1]+self.tri[i][j]])
                else:
                    s1=self.dp[i-1][j-1]+self.tri[i][j]
                    s2=self.dp[i-1][j]+self.tri[i][j]
                    self.dp[i].extend([max(s1,s2)])
            
        
        last_row=self.dp[self.n-1]
        print(max(last_row))        
        
        
        
        
it=IT()
it.read()
it.solve()
