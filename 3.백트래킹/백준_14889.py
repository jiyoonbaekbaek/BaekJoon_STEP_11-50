import sys
input=sys.stdin.readline
import itertools 
import copy

class Soccer:
    def read(self):
        self.n=int(input())
        self.info=[]
        for _ in range(self.n):
            a=input().split()
            a=list(map(int,a))
            self.info.append(a)
        
    def solve(self):
        Min=float("inf")
        tm=self.n//2    #team member 
        u=[i for i in range(1,self.n)]
        s1=itertools.combinations(u,tm-1)
        s1=list(map(list,s1))
        for pairs in s1: # ex. i=0, pairs=[1,2] -> [0,1,2] 가 team 
            s_a=0
            s_b=0 
            pairs.append(0)
            info=copy.deepcopy(self.info)
            c=[]
            for p1 in pairs:
                for p2 in pairs:
                    if p1!=p2:
                        s_a+=self.info[p1][p2]
                        if p1 not in c:
                            info[p1]=[0]*self.n
                            for i in range(self.n):
                                info[i][p1]=0
                        if p2 not in c:
                            info[p2]=[0]*self.n
                            for i in range(self.n):
                                info[i][p2]=0
    
                        c.append(p1)
                        c.append(p2)
            for left in info:
                s_b+=sum(left)
            t=abs(s_a-s_b)
            if t<Min:
                Min=t 
      
            
        print(Min)           
         
s=Soccer()
s.read()
s.solve()      
