import sys
input=sys.stdin.readline

class Uc:
    def read(self):
        self.info=list(map(int,input().split()))
        self.info=sorted(self.info)
        self.a=self.info[0]
        self.b=self.info[1]
    def solve(self):
        r=self.info[1]%self.info[0]
        self.info[1]=self.info[0]
        self.info[0]=r
        while r>0:
            r=self.info[1]%self.info[0]
            self.info[1]=self.info[0]
            self.info[0]=r
        print(self.info[1])
        print((self.info[1])*(self.a//self.info[1])*(self.b//self.info[1]))
            
uc=Uc()
uc.read()
uc.solve()
