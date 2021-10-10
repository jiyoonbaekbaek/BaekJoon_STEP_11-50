from collections import deque
import sys
input=sys.stdin.readline

class NM:
    def read(self):
       self.N,self.M=map(int,input().split())
       self.st=1
       for i in range(self.N,self.N-self.M,-1):
           self.st*=i
       self.st=self.st//self.N
       
    def BFS(self): #BFS
        use=[str(i) for i in range(1,self.N+1)]
        for i in range(1,self.N+1):
            search_queue=deque()
            search_queue+=[str(i)]
            root=str(i)
            ans=[]
            c=0
            while c<self.st:
                person=search_queue.popleft()
                if len(person)-(self.M-1)==self.M:
                    c+=1
                    print(person)         
                else:
                    root=person 
                    search_queue+=[str(root)+' '+str(item) for item in use if str(item) not in root]
                  
                
                
                
        

nm=NM()
nm.read()
nm.BFS()
