a,b=map(int,input().split())
for i in range(a+1,b):
  sum=0
  num=i
  while(num>0):
    x=num%10
    num=num//10
    y=x**3
    sum=sum+y
  if(i==sum):
    print(sum,end=' ')
