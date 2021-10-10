import sys
input=sys.stdin.readline

class UC:
    def read(self):
        self.n=int(input())
        self.info=[list(map(int,input().split())) for _ in range(self.n)]
    def solve(self):
        for pb in self.info:
            r=float("inf")
            pb=sorted(pb)
            a=pb[0]
            b=pb[1]
            while r>0:
                r=pb[1]%pb[0]
                pb[1]=pb[0]
                pb[0]=r
            print((pb[1])*(a//pb[1])*(b//pb[1]),end='\n')
uc=UC()
uc.read()
uc.solve()
