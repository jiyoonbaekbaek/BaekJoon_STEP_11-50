import sys 
input=sys.stdin.readline

class UC:
    def read(self):
        self.n=int(input())
        self.info=[]
        self.clue=[]
        c=0
        for i in range(self.n):
            a=int(input())
            self.info.append(a)
            if i>0:
                c=self.info[i-1]
                self.clue.append(abs(a-c))
    def gcd(self,a,b):
        r=float("inf")
        while r>0:
            if b>a:
                r=b%a
                b,a=a,r
            else:
                r=a%b
                b,a=r,b 
        return max(a,b)
    def solve(self):
        GCD=self.clue[0]
        ans=[]
        for i in range(len(self.clue)):
            GCD=self.gcd(GCD,self.clue[i])
        for i in range(1,int(GCD**(1/2))+1):
            if GCD%i==0:
                ans.append(i)
                if (i**2)!=GCD:
                    ans.append(GCD//i)
        ans.sort()
        for item in ans:
            if item>1:
                print(item,end=' ')

uc=UC()
uc.read()
uc.solve()
