# print the remainder of the first n numbers when divided by 3.

n = int(input("Enter number: "))
num = 3
rem = 0
for i in range(1, n+1):
  rem = i % num
  print("num"+"="+str(i)+":"+"rem"+":"+str(rem))