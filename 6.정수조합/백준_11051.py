import sys
input=sys.stdin.readline

class BN:
    def read(self):
        self.info=list(map(int,input().split()))
    def solve(self):
        if self.info[1]==0:
            print(1)
            return
        elif self.info[1]==1:
            print(self.info[0]%10007)
            return
        else:
            row=self.info[1]-2
            col=self.info[0]-self.info[1]+1
            init=[i for i in range(1,col+1)]
            for _ in range(row):
                new=[0]*len(init)
                for j in range(col):
                    new[j]=sum(init[:j+1])%10007
                init=new
            print(sum(init)%10007)
                
     

bn=BN()
bn.read()
bn.solve()
