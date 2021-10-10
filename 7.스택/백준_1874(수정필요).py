import sys
input=sys.stdin.readline
class Series:
    def read(self):
        self.n=int(input())
        self.info=[int(input()) for _ in range(self.n)]
    def solve(self):
        ans=[]
        start=1
        stack=[]
        for i in range(len(self.info)):
            while True: 
                if start<=self.info[i]: #다음 숫자가 목표 숫자 이하임 -> 넣어야 함 !
                    stack.append(start)
                    global cur
                    ans.append('+')
                    start+=1 #다음에 스택에 쌓일 숫자 
                if len(stack)>0 and stack[-1]>=self.info[i]: #현재 스택 중에 찾아야 함 
                    for_ch=stack[-1]
                    del stack[-1]
                    ans.append('-')
                    if for_ch==self.info[i]:
                        break
                else: 
                    try:
                        if stack[-1]<self.info[i] and start>self.info[i]: #값을 만들 수 없음 !
                            print('NO',end='\n')
                            return
                    except:
                        if len(stack)==0 and start>self.info[i]:
                            print('NO',end='\n')
                            return
        for an in ans:
            print(an,end='\n')            
series=Series()
series.read()
series.solve()    
