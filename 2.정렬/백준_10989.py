# Counting 정렬 
import sys
input=sys.stdin.readline
sys.setrecursionlimit(10000)

class Sort:
    def readandans(self):
        self.n=int(input())
        self.ca=[0]*10001    # 0 ~ 10000 
        self.Max=0
        for _ in range(self.n):
                a=int(input())
                self.ca[a]+=1
                if a>self.Max:
                    self.Max=a
        for i in range(len(self.ca)):
            if self.ca[i]==0:
                continue #해당 숫자 i 는 정렬 항목에 없음 
            else:
                for _ in range(self.ca[i]):
                    print(i,end='\n')





sort = Sort()
sort.readandans()
