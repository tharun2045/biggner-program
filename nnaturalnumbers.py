nu = int(raw_input())
if nu < 0:
   print("Enter a positive number")
else:
   sum = 0
   while(nu > 0):
       sum += nu
       nu -= 1
   print(sum)
