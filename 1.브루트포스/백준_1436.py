def doom(a):
    n=666
    numb=1
    while True:
        if a==1:
            print(n)
            return
        n+=1
        if "666" in str(n) :
            numb+=1
            if numb==a:
                print(n)
                return

x=int(input())
doom(x)
