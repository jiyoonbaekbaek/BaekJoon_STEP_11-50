import sys
input=sys.stdin.readline

class Backpack:
    def read(self):
        [self.i,self.j]=list(map(int,input().split()))
        self.info=[list(map(int,input().split())) for _ in range(self.i)]
        
    def solve(self):
        self.dp=[]
        for I in range(self.i):
            cur=[]
            for J in range(self.j+1):
                if I==0:
                    if self.info[0][0]<=J:
                        cur.append(self.info[0][1])
                    else:
                        cur.append(0)
                else:
                    can1=self.dp[I-1][J]
                    if J-self.info[I][0]>=0: #현재 제한된 용량이 현재 무게의 물건을 담을 수 있는 경우 
                        can2=self.info[I][1]+self.dp[I-1][J-self.info[I][0]]
                    else:
                        can2=0
                    cur.append(max(can1,can2))
            self.dp.append(cur)            
        print(self.dp[-1][-1])               

bp=Backpack()
bp.read()
bp.solve()
