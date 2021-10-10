import sys
input=sys.stdin.readline
from collections import deque 

class Calculate:
    def read(self):
        self.n=int(input())
        self.numb=list(map(int,input().split()))
        op=list(map(int,input().split()))
        self.Op=[]
        for i in range(len(op)):
            if op[i]>0:
                self.Op.extend([str(i)]*op[i])
        self.cal=deque([self.numb[0],self.numb[1]])
    
    def rule(self,x,a,b):
       if x=='0':
           return a+b
       elif x=='1':
           return a-b
       elif x=='2':
           return a*b
       else:
           if a<0 and b>0:
               return (abs(a)//b)*-1
           else:
               return a//b 
    
    def solve(self):
        op_n=self.n-1
        ans=[]
        for i in range(4): # +,-,x,/
            if str(i) in self.Op:
                search_queue=deque([str(i)])
                while search_queue:
                    person=search_queue.popleft()
                    if len(person)-(op_n-1)==op_n:
                        x=person.split()
                        for i in range(len(x)):
                            a=self.cal.popleft()
                            b=self.cal.popleft()
                            r=self.rule(x[i],a,b)
                            if i==len(x)-1:
                                ans.append(r)
                                self.cal+=[self.numb[0],self.numb[1]]
                                break
                            self.cal+=[r]
                            self.cal+=[self.numb[i+2]]
                    
                    else:
                        root=person
                        tmp=[]
                        use=self.Op.copy()
                        for it in root.split():
                            use.remove(it)
                        for item in use:
                            if root+' '+item not in tmp:
                                tmp.append(str(root)+' '+str(item))
                        search_queue+=tmp
                    
        print(max(ans))
        print(min(ans))            
         
c=Calculate()
c.read()
c.solve()        
