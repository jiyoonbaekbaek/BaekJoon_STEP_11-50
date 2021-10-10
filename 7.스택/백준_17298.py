from collections import deque

n=int(input())
seq=list(map(int,input().split()))
oks=[-1]*n
stack=[]          
for i in range(n):
    while stack and stack[-1][0] < seq[i]:
          tmp,idx=stack[-1] #제일 위 
          del stack[-1]
          oks[idx]=seq[i]
    stack.append([seq[i],i])
print(*oks)
