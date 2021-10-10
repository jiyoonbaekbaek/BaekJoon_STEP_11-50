# python3
import sys
sys.setrecursionlimit(10**6)

class Sort:
    def read(self):
        self.n = int(input())
        self.item=[]
        for _ in range(self.n):
                self.item.append(int(sys.stdin.readline()))

    def answer(self):
        for item in sorted(self.item):
            print(item,end='\n')




    




sort = Sort()
sort.read()
sort.answer()
