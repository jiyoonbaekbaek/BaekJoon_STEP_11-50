import sys
input=sys.stdin.readline

class Bracket:
    def read(self):
        self.box=input()
        self.cal=self.box.split('-')
    def solve(self):
        ans=0
        try:
            self.cal=self.box.split('-')
        except: #'-' 가 하나도 없음 !
            try: 
                self.cal=self.box.split('+')
                self.cal=list(map(int,self.cal))
                print(sum(self.cal))
                return
            except: #숫자 한개 
                print(int(self.cal[0]))
                return 
        for i in range(len(self.cal)):
            if i==0: #아직 최초의 - 가 나오기 전 
                if len(self.cal[0])==1:
                    ans+=int(self.cal[0][0])
                else:
                    cur_s=self.cal[0].split('+')
                    cur_s=list(map(int,cur_s))
                    ans+=sum(cur_s)
            else: #최초의 -가 등장한 후 
                if len(self.cal[i])==1:
                    ans-=int(self.cal[i][0])
                else:
                    cur_m=self.cal[i].split('+')
                    cur_m=list(map(int,cur_m))
                    ans-=sum(cur_m)
        print(ans)    
            
bc=Bracket()
bc.read()
bc.solve()
