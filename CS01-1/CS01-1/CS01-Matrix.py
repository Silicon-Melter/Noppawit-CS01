import numpy as np


m=int (input("m "))
n=int (input("n "))


print ("enter 1st arr")
array=[[int(input()) for i in range(m)] for j in range(n)]
narr = np.asarray(array)

print ("enter 2nd arr")
add=[[int(input()) for i in range(m)] for j in range(n)]
narr = np.asarray(add)

narry = np.asarray(array)
narrynp = narry.reshape(int(m),n)
na = narr.reshape(int(n),m)
ans=np.add(narrynp,na)
print(ans)
