from collections import defaultdict
import sys
input=sys.stdin.readline

class FK:
    def solve(self):
        n=int(input())
        ANS=[]
        for _ in range(n):
            closet=defaultdict(int)
            ans=1
            mn=int(input())
            for _ in range(mn):
                new=input().split()
                closet[new[1]]+=1
            for codi in list(closet.values()):
                ans*=codi+1
            ans-=1
            ANS.append(ans)
        for nb in ANS:
            print(nb,end='\n')
fk=FK()
fk.solve()
