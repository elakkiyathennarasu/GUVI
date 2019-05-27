x,y=map(int,input().split())
x=x+1
for i in range(x,y):
  if(i>1):
    for j in range(2,i):
      if((i%j)==0):
        break
    else:
      print(i, end=" ")
