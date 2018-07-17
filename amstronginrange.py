lo,up=map(int,input().strip().split())
for j in range(lo, up + 1):
   order = len(str(j))
   sum = 0
   temp = j
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10
   if j == sum:
       print(j,end=" ")
