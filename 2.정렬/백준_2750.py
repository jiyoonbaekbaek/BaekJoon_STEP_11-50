# python3
import sys
sys.setrecursionlimit(10000)

class Sort:
    def read(self):
        self.n = int(input())
        self.item=[]
        for _ in range(self.n):
                self.item.append(int(input()))

    def answer(self):
        self.item=self.Quicksort(self.item)
        for item in self.item:
            print(item,end='\n')




    def Quicksort(self,array):
        if len(array)<2:
            return array
        else:
            pivot=array[0]
            less=[i for i in array[1:] if i<=pivot]
            greater=[i for i in array[1:] if i>pivot]

            return self.Quicksort(less)+[pivot]+self.Quicksort(greater)











sort = Sort()
sort.read()
sort.answer()
