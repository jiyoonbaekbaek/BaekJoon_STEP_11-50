# python3
import sys

class Coin:
    def read(self):
        [self.number,self.goal]=list(map(int,input().split()))
        self.coin=[]
        for _ in range(self.number):
            a=int(input())
            self.coin.append(a)


    def find(self):
        count=0
        self.candidate = [item for item in self.coin if item <= self.goal]
        self.candidate = sorted(self.candidate)
        while self.goal!=0:
            self.now=self.candidate.pop()
            if self.now>self.goal:
                continue
            count+=self.goal // self.now
            self.goal-=(self.goal//self.now) * self.now

        return count


coin=Coin()
coin.read()
print(coin.find())
