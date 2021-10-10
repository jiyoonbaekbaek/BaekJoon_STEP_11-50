import sys
input=sys.stdin.readline
sys.setrecursionlimit(10000)

class Sudoku:
    def read(self):
        self.count=[0]*9 #1,2,3,4,5,6,7,8,9
        self.box_i=[]
        self.box=[]
        self.hv=[]
        self.fill=[] #0 위치 
        self.c=0
        n=-3
        for i in range(9):
            new=list(map(int,input().split()))
            for j in range(len(new)):
                if new[j]!=0:
                    self.count[new[j]-1]+=1
                else:
                    self.fill.append(9*i+j)
            self.hv.extend(new)
            if i%3==0:
                n+=3
            for j in range(0,9,3):#0,3,6 
                if i%3==0:
                    self.box.append(new[j:j+3]) 
                    self.box_i.extend([(j//3)+n]*3)
                else:
                    self.box[(j//3)+n].extend(new[j:j+3])  
                    self.box_i.extend([(j//3)+n]*3)     
        self.ln=[]
        for i in range(len(self.count)):
            if self.count[i]<9:
                for _ in range(9-self.count[i]):
                    self.ln.append(i+1)
        self.solve(0)
        
    def solve(self,fz):
        ans=[]
        if len(self.ln)==0 and self.c==0:
            self.c+=1
            for i in range(0,9**2,9):
                for j in range(9):
                    if j<8:
                        print(self.hv[i+j],end=' ')
                    else:
                        print(self.hv[i+j],end='\n')
            return
        
        if self.c==1:
            return #이미 답을 구함 ! 더 이상 재귀 안 돎  
        
        z=self.fill[fz]
        row=z//9
        col=z%9
        bi=self.box_i[z]
        for n in list(set(self.ln)):
            if n not in self.hv[row*9:row*9+9]:
                if n not in self.hv[col:9**2:9]:
                    if n not in self.box[bi]:
                        self.hv[z]=n 
                        self.ln.remove(n)
                        self.box[bi].append(n)
                        self.solve(fz+1)
                        self.hv[z]=0
                        self.ln.append(n)
                        self.box[bi].remove(n)
                            
            
                             
                
  
s=Sudoku()
s.read()
