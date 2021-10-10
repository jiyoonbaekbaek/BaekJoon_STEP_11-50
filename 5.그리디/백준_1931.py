# python3
import sys
# 포인트 : end 시간이 같을 경우 start가 빠른 애들이 먼저 정렬되어야 함

class Maxmeeting:
    def read(self):
        self.meetn = int(input())
        self.meeting=[]
        self.startonly=[]
        self.endonly=[]
        done=[]
        for i in range(self.meetn):
                [start, end] = list(map(int, sys.stdin.readline().split()))
                self.meeting.append([start,end])
        self.meeting=sorted(self.meeting,key=lambda X:X[0])
        self.meeting = sorted(self.meeting, key=lambda X: X[1])






    def Answer(self):
        count=0
        start=0
        end=0
        for i in range(len(self.meeting)):
            if i==0:
                start=self.meeting[i][0]
                end=self.meeting[i][1]
                count+=1
            else:
                new_start=self.meeting[i][0]
                new_end=self.meeting[i][1]
                if end<=new_start :
                    start=new_start
                    end=new_end
                    count+=1
        return count


    def quicksort(self,array):
        if len(array)<2:
            return array
        else:
            pivot=array[0]
            less=[i for i in array[1:] if i<=pivot]
            greater=[i for i in array[1:] if i>pivot]

            return self.quicksort(less)+[pivot]+self.quicksort(greater)











max = Maxmeeting()
max.read()
print(max.Answer())
