import sys
input=sys.stdin.readline
class Stack:
    def read(self):
        self.n=int(input())
        self.command=[input() for _ in range(self.n)]
    def solve(self):
        stack=[]
        for cm in self.command:
            if cm[:4]=='push':
                stack.append(int(cm[5:]))
            elif cm[:3]=='pop':
                if len(stack)!=0:
                    print(stack.pop(),end='\n')
                else:
                    print(-1,end='\n')
            elif cm[:4]=='size':
                print(len(stack),end='\n')
            elif cm[:5]=='empty':
                if len(stack)==0:
                    print(1,end='\n')
                else:
                    print(0,end='\n')
            elif cm[:3]=='top':
                if len(stack)!=0:
                    print(stack[-1],end='\n')
                else:
                    print(-1,end='\n')

st=Stack()
st.read()
st.solve()
