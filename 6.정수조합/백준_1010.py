import sys
input=sys.stdin.readline

class BN:
    def read(self):
        self.n=int(input())
        self.info=[]
        for _ in range(self.n):
            self.info.append(list(map(int,input().split())))
    def solve(self):
        for pb in self.info:
            if pb[0]==1:
                print(pb[1],end='\n')
            else:
                row=pb[0]-2
                col=pb[1]-pb[0]+1
                init=[i for i in range(1,col+1)]
                for _ in range(row):
                    new=[0]*len(init)
                    for j in range(col):
                        new[j]=sum(init[:j+1])
                    init=new
                print(sum(init),end='\n')
                
     

bn=BN()
bn.read()
bn.solve()
