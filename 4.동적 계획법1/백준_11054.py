import sys
input=sys.stdin.readline

class Bitonic:
    def read(self):
        self.n=int(input())
        self.info=list(map(int,input().split()))
        self.info2=list(reversed(self.info))
        
    def solve(self):
        self.sum_1=[]
        self.cur_1=[]
        self.sum_2=[]
        self.cur_2=[]  
        for i in range(self.n):
            if i==0:
                self.sum_1.append(1)
                self.cur_1.append(self.info[0])
                self.sum_2.append(1)
                self.cur_2.append(self.info2[0])
            else:
                S_1=0
                S_2=0
                for j in range(len(self.sum_1)):
                    if self.cur_1[j]<self.info[i]:
                        if self.sum_1[j]>S_1:
                            S_1=self.sum_1[j]
                    if self.cur_2[j]<self.info2[i]:
                        if self.sum_2[j]>S_2:
                            S_2=self.sum_2[j]
                self.sum_1.append(S_1+1)
                self.cur_1.append(self.info[i])
                self.sum_2.append(S_2+1)
                self.cur_2.append(self.info2[i])
            
        for i in range(len(self.sum_1)):
                ind=self.n-1-i
                self.sum_1[i]+=self.sum_2[ind]
                self.sum_1[i]-=1
        print(max(self.sum_1))
        
bt=Bitonic()
bt.read()
bt.solve() 
