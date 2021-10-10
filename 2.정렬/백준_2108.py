import sys
import math
input=sys.stdin.readline

class Statistics:
    def read(self):
        self.n=int(input())
        self.c=[0]*8001 # -4000 ~ -1 , 0 , 1 ~ 4000
        self.min=float("inf")
        self.max=float("-inf")
        self.sum=0
        self.mid=0
        for _ in range(self.n):
            a=int(input())
            self.c[a+4000]+=1 #-4000 이 0번 인덱스에 들어가야 함 !
            if a<self.min:
                self.min=a
            if a>self.max:
                self.max=a
            self.sum+=a
        self.c=self.c[self.min+4000:self.max+4000+1]
        print(round(self.sum/self.n),end='\n')
        
        for i in range(len(self.c)):
            if self.c[i]!=0:
                self.mid+=self.c[i]
                if self.mid>=(self.n//2)+1:
                    print(self.min+i,end='\n')
                    break
                    
        M=max(self.c)
        if self.c.count(M)==1:
            print(self.c.index(M)+self.min,end='\n')
        else:
            f=self.c.index(M)
            self.c[f]=0 
            print(self.c.index(M)+self.min,end='\n')
            
        print(self.max-self.min,end='\n')
        
sta=Statistics()
sta.read()
