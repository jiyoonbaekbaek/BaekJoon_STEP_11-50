import sys
input=sys.stdin.readline

class Age:
    def read(self):
        self.n=int(input())
        self.info={}
        for _ in range(self.n):
            a,n=map(str,input().split())
            l=int(a)
            if l not in self.info:
                self.info[l]=[]
                self.info[l].append(n)
            elif a not in self.info[l]:
                self.info[l].append(n)
        
    def solve(self):
        d=sorted(self.info.items())
        for i in range(len(d)):
            for item in d[i][1]:
                print(d[i][0],end=' ')
                print(item,end='\n')

age=Age()
age.read()
age.solve()
