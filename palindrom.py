N=int(input(""))

Rev=0
Rem=0
temp=N
while(N>0):
   
  Rem=N%10
  Rev=(Rev*10)+Rem
  N=N//10
    
if(temp==Rev):
  print("yes")
else:
  print("no")
