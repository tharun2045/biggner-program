lo,up=map(int,raw_input().strip().split())
for j in range(lo+1 , up ):
   order = len(str(j))
   sum = 0
   temp = j
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10
   if j == sum:
       print j,
