import sys
input=sys.stdin.readline

class Compare:
    def read(self):
        self.info=[]
        self.ind_f=[] 
        self.n=int(input())
        for _ in range(self.n):
            [b,h]=list(map(int,input().split()))
            self.info.append([b,h])
            self.ind_f.append(str(b)+str(h)) #각 사람별 특수한 id 
        self.info.sort(key=lambda x:x[1],reverse=True)



    def solve(self):
        ans=[float("inf")]*self.n
        for i in range(self.n):
            com=self.info[i][0]
            cur=self.info[i][1]
            ind=self.ind_f.index(str(com)+str(cur))
            self.ind_f[ind]=0 #solved 
            count=0
            if i==0:
                ans[ind]=count+1
            else:
                for j in range(i):
                    if self.info[j][1]>cur and self.info[j][0]>com:
                        count+=1
        
                ans[ind]=count+1
            
        
        
        for score in ans:
            print(score,end=' ')
        
        
c=Compare()
c.read()
c.solve()
