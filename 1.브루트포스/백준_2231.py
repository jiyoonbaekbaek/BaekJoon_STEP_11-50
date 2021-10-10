def divisionsum(a):
    i=0
    temp=0
    ans=''
    while temp<a:
        temp=10*i
        i+=1
        for x in range(10):
            summ=temp+x
            for j in range(len(str((temp)))):
                summ+=int(str(temp)[j])
            summ+=x
            if summ==a:
                for j in range(len(str(temp))-1):
                    ans+=str(temp/10)[j]
                ans+=str(x)
                print(ans)
                return
    print(0)
    
                        
a=int(input())
divisionsum(a)
