import sys
input=sys.stdin.readline

class SOIL:
    def read(self):
        self.city_n=int(input())
        self.distance=list(map(int,input().split()))
        self.price=list(map(int,input().split()))
    def solve(self):
        Min_price=float("inf")
        ans=0
        for i in range(len(self.price)-1):
            if self.price[i]<Min_price:
              Min_price=self.price[i]
            ans+=self.distance[i]*Min_price 
        print(ans)

soil=SOIL()
soil.read()
soil.solve()
