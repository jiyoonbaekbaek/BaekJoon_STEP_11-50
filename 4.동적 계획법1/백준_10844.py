import sys
input=sys.stdin.readline

class ES:
    def read(self):
        self.n=int(input())
    
    def solve(self):
        cur=1
        if self.n==cur:
            print(9)
            return
        self.dp=[1,2,2,2,2,2,2,2,2,1] #0,1,2,3,4,5,6,7,8,9
        cur+=1
        while cur<self.n:
            cur+=1
            tmp=[]
            for i in range(10):
                if i==0 or i==9:
                    tmp.append(self.dp[1])
                else:
                    tmp.append(self.dp[i-1]+self.dp[i+1])
            self.dp=tmp
        print(sum(self.dp[1:])%1000000000)
        
es=ES()
es.read()
es.solve()
