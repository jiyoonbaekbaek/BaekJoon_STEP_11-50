import sys
input=sys.stdin.readline

class Real:
    def read(self):
        self.n=int(input())
        self.info=list(map(int,input().split()))
    def solve(self):
        self.info=sorted(self.info)
        if len(self.info)==1:
            print(self.info[0]**2)
            return
        print(self.info[0]*self.info[-1])
           
r=Real()
r.read()
r.solve()
