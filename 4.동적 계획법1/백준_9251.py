import sys
input=sys.stdin.readline

class LCS:
    def read(self):
        self.st1=str(input().strip())
        self.st2=str(input().strip())
        self.cell=[]
    
    def solve(self):
        put=0
        put_i=[]
        for x in range(len(self.st2)):
            if self.st1[0] in self.st2[:x+1]:
                put_i.append(1)
            else:
                put_i.append(0)
        for i in range(len(self.st2)):
            row=[]
            for j in range(len(self.st1)):
                if i==0 :
                    if self.st2[0] in self.st1[:j+1]:
                        put=1
                    else:
                        put=0
                    row.append(put)
                elif i>0 and j==0:
                    self.cell=self.cell[:i] #왜 이러는지 모름 ! 
                    row.append(put_i[i])
                elif i>0 and j>0:
                    if self.st2[i]==self.st1[j]:
                        row.append(self.cell[i-1][j-1]+1)
                    else:
                        row.append(max(self.cell[i-1][j],row[j-1]))
            self.cell.append(row)  
        ans=0
        for i in range(len(self.cell)):  
            if max(self.cell[i]) > ans:
                ans=max(self.cell[i])   
        print(ans)

lcs=LCS()
lcs.read()
lcs.solve()
