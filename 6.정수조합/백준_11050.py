import sys
input=sys.stdin.readline

class BN:
    def read(self):
        self.info=list(map(int,input().split()))
    def solve(self):
        nm=1
        dm=1
        m=0
        for _ in range(self.info[1]):
            nm*=self.info[0]-m
            dm*=self.info[1]-m
            m+=1 
        print(int(nm/dm))

bn=BN()
bn.read()
bn.solve()
