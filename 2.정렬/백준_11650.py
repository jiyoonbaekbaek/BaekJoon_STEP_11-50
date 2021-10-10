import sys
input=sys.stdin.readline

class XY:
    def read(self):
        self.n=int(input())
        self.coor=[]
        for _ in range(self.n):
            coor=list(map(int,input().split()))
            self.coor.append(coor)
    
    def solve(self):
        s1=sorted(self.coor,key=lambda x:x[1])
        s2=sorted(s1,key=lambda x:x[0])
        for l in s2:
            for i in range(len(l)):
                if i==0:
                    print(l[i],end=' ')
                else:
                    print(l[i],end='\n')
        
xy=XY()
xy.read()
xy.solve()  
