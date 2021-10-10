import sys
input=sys.stdin.readline

class LIS:
    def read(self):
        self.n=int(input())
        self.info=list(map(int,input().split()))
        
    def solve(self):
        self.sum=[]
        self.cur=[]
        for i in range(self.n):
            if i==0:
                self.sum.append(1)
                self.cur.append(self.info[0])
            else:
                    S=0
                    for j in range(len(self.sum)):
                        if self.cur[j]<self.info[i]:
                            if self.sum[j]>S:
                                S=self.sum[j]
                    self.sum.append(S+1)
                    self.cur.append(self.info[i])
                
          
        
        print(max(self.sum))
                    
lis=LIS()
lis.read()
lis.solve()
