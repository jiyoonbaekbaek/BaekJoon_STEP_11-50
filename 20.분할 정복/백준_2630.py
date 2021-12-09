import sys
input=sys.stdin.readline 
sys.setrecursionlimit(10**6)

class CP:
    def read(self):
        self.n=int(input())
        self.paper=[]
        self.init_sum=0
        for _ in range(self.n):
            new=list(map(int,input().split()))
            self.paper.append(new)
            self.init_sum+=sum(new)
        self.w=0
        self.b=0
         
    def solve(self,data):
        _sum=0
        if self.init_sum==0:
            self.w+=1
            return
        elif self.init_sum==self.n**2:
            self.b+=1
            return
        else:
            cur=len(data[0]) 
            for i in range(cur):
                _sum+=sum(data[i])
            if _sum==0:
                self.w+=1
                return
            elif _sum==cur**2:
                self.b+=1
                return
            elif cur>=1:
                new_1=[data[i][:cur//2] for i in range(cur) if i<cur//2]
                new_2=[data[i][cur//2:] for i in range(cur) if i<cur//2]
                new_3=[data[i][:cur//2] for i in range(cur) if i>=cur//2]
                new_4=[data[i][cur//2:] for i in range(cur) if i>=cur//2]
                self.solve(new_1)
                self.solve(new_2)
                self.solve(new_3)
                self.solve(new_4)
        
cp=CP()
cp.read()
cp.solve(cp.paper)
print(cp.w)
print(cp.b)
        
    
