lo,up=map(int,input().strip().split())
for k in range(lo+1,up):
   if k > 1:
       for i in range(2,k):
           if (k % i) == 0:
               break
       else:
    
        print(k ,end=" ")
