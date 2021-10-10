import sys
import copy
input=sys.stdin.readline

class Stair:
    def read(self):
        self.n=int(input())
        self.info=[int(input()) for _ in range(self.n)]
        
    def solve(self):
        ways=[]
        for i in range(self.n):
            cur=self.info[i]
            box=[]
            if i==0:
                p_a=[0,cur]
                p_b=[0,cur]
                box.append(p_a)
                box.append(p_b)
                ways.append(box)
            elif i==1:
                p_a=copy.deepcopy(ways[i-1][1])
                p_a.append(cur)
                p_b=[0,cur]
                box.append(p_a)
                box.append(p_b)
                ways.append(box)
            else:
                p_a=copy.deepcopy(ways[i-1][1])
                p_a.append(cur)
                s1=ways[i-2][0]
                s2=ways[i-2][1]
                if sum(s1)>sum(s2):
                    p_b=copy.deepcopy(s1)
                else:
                    p_b=copy.deepcopy(s2)
                p_b.append(cur)
                box.append(p_a)
                box.append(p_b)
                ways.append(box)
          
        
        s1=sum(ways[-1][0])
        s2=sum(ways[-1][1])
        print(max(s1,s2))

st=Stair()
st.read()
st.solve()
