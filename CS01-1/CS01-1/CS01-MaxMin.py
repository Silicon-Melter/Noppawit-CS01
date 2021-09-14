l = int(input("enter loop: "))
arr = []
for i in range(l):
    num = int(input("enter number: "))
    arr += [num]
print(arr)
arr.sort(reverse=False)
print(arr[0])
len_arr = len(arr)
print(arr[len_arr-1])