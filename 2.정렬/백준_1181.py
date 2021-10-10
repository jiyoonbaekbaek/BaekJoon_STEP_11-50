import sys
input=sys.stdin.readline

class Dictionary:
    def read(self):
        self.n=int(input())
        self.info={}
        for _ in range(self.n):
            a=str(input().rstrip())
            l=len(a)
            if l not in self.info:
                self.info[l]=[]
                self.info[l].append(a)
            elif a not in self.info[l]:
                self.info[l].append(a)
            
       
    
    def solve(self):
        d=sorted(self.info.items())
        for i in range(len(d)):
            if len(d[i][1])>1:
                d[i][1].sort()
                for item in d[i][1]:
                    print(item,end='\n')
            if len(d[i][1])==1:
                print(d[i][1][0],end='\n')
                
dic=Dictionary()
dic.read()
dic.solve()        
