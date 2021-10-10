def inside(x):
    s=[]
    for i in range(len(x)):
        s.append(x[i])
    s=sorted(s,reverse=True)
    for item in s:
        print(item,end='')
        
a=str(input())
inside(a)
