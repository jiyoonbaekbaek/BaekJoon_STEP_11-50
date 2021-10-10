import sys
input=sys.stdin.readline

class Electric:
    def read(self):
        self.n=int(input())
        self.info=[]
        for _ in range(self.n):
            new=list(map(int,input().split()))
            self.info.append(new)
        
    def solve(self):
        self.info=sorted(self.info,key=lambda x:x[0])
        self.sum=[]
        self.cur=[]
        for i in range(self.n):
            if i==0:
                self.sum.append(1)
                self.cur.append(self.info[0][1])
            else:
                    S=0
                    for j in range(len(self.sum)):
                        if self.cur[j]<self.info[i][1]:
                            if self.sum[j]>S:
                                S=self.sum[j]
                    self.sum.append(S+1)
                    self.cur.append(self.info[i][1])
            
                
        print(self.n-max(self.sum))
                    
elec=Electric()
elec.read()
elec.solve()
