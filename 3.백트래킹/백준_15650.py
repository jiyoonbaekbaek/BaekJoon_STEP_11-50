import itertools
import sys
input=sys.stdin.readline

class NM:
    def read(self):
       self.N,self.M=map(int,input().split())
       self.use=''
       for i in range(1,self.N+1):
           self.use+=str(i)
       
    def honey(self): #BFS
        for v in itertools.combinations(self.use,self.M):
            for l in range(len(v)):
                if l==len(v)-1:
                    print(v[l],end='\n')
                else:
                    print(v[l],end=' ')
         
nm=NM()
nm.read()
nm.honey()
