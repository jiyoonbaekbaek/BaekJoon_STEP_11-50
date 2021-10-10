import sys
input=sys.stdin.readline

class VPS:
    def read(self):
        self.n=int(input())
        self.info=[input().rstrip() for _ in range(self.n)]
    def solve(self):
        for i in range(len(self.info)):
            #print(i)
            stop=float("inf")
            while stop>0:
                self.info[i]=self.info[i].replace('()','P')
                #print(self.info[i])
                stop=self.info[i].count('P')
                self.info[i]=self.info[i].replace('P','')
                #print(self.info[i])
            #print(self.info[i],end=' final\n')
            if len(self.info[i])==0:
                print('YES',end='\n')
            else:
                print('NO',end='\n')
vps=VPS()
vps.read()
vps.solve()
