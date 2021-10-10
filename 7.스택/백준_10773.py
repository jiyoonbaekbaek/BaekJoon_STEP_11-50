import sys
input=sys.stdin.readline

class JM:
    def solve(self):
        self.n=int(input())
        self.stack=[]
        for _ in range(self.n):
            new=int(input())
            if new!=0:
                self.stack.append(new)
            else:
                del self.stack[-1]
        print(sum(self.stack)) 
jm=JM()
jm.solve()
