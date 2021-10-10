import sys
import copy
input=sys.stdin.readline

class One:
    def read(self):
        self.n=int(input())
    
    def solve(self):
        if self.n==1:
            print(0)
            return
        box=[]
        box.append(self.n-1)
        if self.n%3==0:
            box.append(self.n//3)
        if self.n%2==0:
            box.append(self.n//2)
        c=1
        Min=min(box)
        if Min==1:  #한번의 연산만에 1이 나오는 경우 
            print(c)
            return
        while Min>1:
            f=float("inf")
            s=float("inf")
            t=float("inf")
            f_box=[item-1 for item in box]
            s_box=[item//3 for item in box if item%3==0]
            t_box=[item//2 for item in box if item%2==0]
            box=[]
            f=min(f_box)
            if s_box:
                s=min(s_box)
            if t_box:
                t=min(t_box)
            c+=1
            Min=min(f,s,t)
            box.extend(f_box)
            box.extend(s_box)
            box.extend(t_box)
        print(c)

one=One()
one.read()
one.solve()
