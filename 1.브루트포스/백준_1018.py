import sys
input=sys.stdin.readline

class Chess:
    def read(self):
        self.h,self.w=map(int,input().split())
        self.info=[]
        for _ in range(self.h):
            self.info.append(str(input()).rstrip())
        self.op=[]
    
    def solve(self):
        if self.w>8:
            wid=self.w-8
        else: #width는 최소 8
            wid=0
        if self.h>8:
            hei=self.h-8
        else: #height은 최소 8 
            hei=0
        for x in range(wid+1):
            check=''
            switch_1=0
            switch_2=0
            cur_1='WB'*4 #random default
            cur_2='BW'*4
            for j in range(hei+1): #한번에 8개씩
                count=0
                while count<8:
                    check+=self.info[j+count][x:x+8]
                    count+=1
                if count==8: #0~7, 1~8, 2~9
                    for i in range(0,len(check),8):
                        for q in range(8):
                            if check[i+q]!=cur_1[q]:
                                switch_1+=1
                            if check[i+q]!=cur_2[q]:
                                switch_2+=1
                        cur_1,cur_2=cur_2,cur_1
                    self.op.append(min(switch_1,switch_2))
                    switch_1=0
                    switch_2=0
                    check=''
        
        print(min(self.op))

chess=Chess()
chess.read()
chess.solve()
