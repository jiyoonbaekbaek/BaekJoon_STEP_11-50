import sys
input=sys.stdin.readline

class FC:
    def read(self):
        self.n=int(input())
        self.x=[int(input()) for _ in range(self.n)]
        self.z=[1,0]
        self.o=[0,1]
    
    def solve(self):
        ans=[]
        m=max(self.x)
        cur=2
        while cur<=m:
            n_z=self.z[cur-2]+self.z[cur-1]
            n_o=self.o[cur-2]+self.o[cur-1]
            self.z.append(n_z)
            self.o.append(n_o)
            cur+=1
        
        for numb in self.x:
            ans.append([self.z[numb],self.o[numb]])

        for a in ans:
            print(a[0],a[1])

fc=FC()
fc.read()
fc.solve()
