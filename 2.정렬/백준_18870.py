import sys
input=sys.stdin.readline

class Compress:
    def read(self):
        self.n=int(input())
        self.coor=list(map(int,input().split()))
    
    def solve(self):
        sort_coor=sorted(list(set(self.coor))) # -10,-9,2,4 / 999 1000
        sort_coor_d={sort_coor[i]:i for i in range(len(sort_coor))}
        for item in self.coor:
            print(sort_coor_d[item],end=' ') 

c=Compress()
c.read()
c.solve()
