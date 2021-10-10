import sys
input=sys.stdin.readline

class RING:
    def read(self):
        self.n=int(input())
        self.info=list(map(int,input().split()))
    def GCD(self,a,b):
        r=float("inf")
        while r>0:
            if a>b:
                r=a%b
                a,b=b,r 
            else:
                r=b%a
                a,b=r,a
        return max(a,b) 
    def solve(self):
        F=self.info[0]
        result=0
        for nb in self.info[1:]:
            result=self.GCD(F,nb)
            print(str(F//result)+'/'+str(nb//result),end='\n')
ring=RING()
ring.read()
ring.solve()
