import sys
from itertools import product
input=sys.stdin.readline

class EF:
    def read(self):
        a=0
        b=0
        c=0
        self.var=[]
        while a!=-1 or b!=-1 or c!=-1:
            a,b,c=map(int,input().split())
            if a!=-1 or b!=-1 or c!=-1:
                self.var.append([a,b,c])
            
    def chart(self):
        self.ch={}
        for it in product([i for i in range(21)],repeat=3):
           (a,b,c)=it
           if a<=0 or b<=0 or c<=0:
               self.ch[(a,b,c)]=1
           elif a<b and b<c:
               self.ch[it]=self.ch[(a,b,c-1)]+\
               self.ch[(a,b-1,c-1)]-self.ch[(a,b-1,c)]
           else:
               self.ch[it]=self.ch[(a-1,b,c)]+\
               self.ch[(a-1,b-1,c)]+self.ch[(a-1,b,c-1)]-\
               self.ch[(a-1,b-1,c-1)]
    
    def solve(self):
        self.chart()
        for tasks in self.var:
            [a,b,c]=tasks
            put=str(a)+','+' '+str(b)+','+' '+str(c)
            if a<=0 or b<=0 or c<=0:
                print('w('+put+')'+' '+'='+' '+str(1),end='\n')
            elif a>20 or b>20 or c>20:
                print('w('+put+')'+' '+'='+' '+str(self.ch[(20,20,20)]),end='\n')
            else:
                print('w('+put+')'+' '+'='+' '+str(self.ch[(a,b,c)]),end='\n')
            
ef=EF()
ef.read()
ef.solve()
