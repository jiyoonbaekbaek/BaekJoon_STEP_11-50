import sys
input=sys.stdin.readline

class FindOut:
  def read(self):
    self.box=[]
    while True:
      [a,b]=list(map(int,input().split()))
      if a==0 and b==0:
        break      
      else:
        self.box.append([a,b])
  def solve(self):
    for problem in self.box:
      if problem[0]%problem[1]==0:
        print('multiple',end='\n')
      elif problem[1]%problem[0]==0:
        print('factor',end='\n')
      else:
        print('neither',end='\n')
 
 
fo=FindOut()
fo.read()
fo.solve()
