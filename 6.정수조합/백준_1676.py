import sys
input=sys.stdin.readline
n=int(input())
f_count=0
option=[]
i=0
while 5**i<=n:
    option.append(i)
    i+=1
option=sorted(option,reverse=True)
total=[i for i in range(1,n+1)]
for nb in total:
    for op in option:
        if nb%(5**op)==0:
            f_count+=op
            break
print(f_count)
