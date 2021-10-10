# python3


def tile(numb):
    fibo=[0,1]
    for i in range(2,numb+2):
            fibo.append((fibo[i-2]+fibo[i-1])%15746)
           

    print(fibo[-1])
