t=int(input("Enter number:"))
temp=t
rev=0
while(t>0):
    dig=t%10
    rev=rev*10+dig
    t=t//10
if(temp==rev):
    print("yes")
else:
    print("no")
