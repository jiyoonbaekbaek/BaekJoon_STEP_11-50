import sys
input=sys.stdin.readline

class VPS:
    def read(self):
        self.info=[]
        while True:
            a=input().rstrip()
            if a=='.':
                break
            self.info.append(a.rstrip())
    def solve(self):
        for i in range(len(self.info)):
            self.info[i]=self.info[i].replace(" ","")
            for lts in self.info[i]:
                if lts not in ['[',']','(',')']:
                    self.info[i]=self.info[i].replace(lts,"")
            stop=float("inf")
            if len(self.info[i])==0:
                print('yes',end='\n')
                continue
            while stop>0:
                self.info[i]=self.info[i].replace('()','P')
                self.info[i]=self.info[i].replace('[]','P')
                stop=self.info[i].count('P')
                self.info[i]=self.info[i].replace('P','')
            if len(self.info[i])==0:
                print('yes',end='\n')
            else:
                print('no',end='\n')
vps=VPS()
vps.read()
vps.solve()
