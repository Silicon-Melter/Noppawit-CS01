arr = [0]
while True:
    i = int(input("enter:"))
    arr.append(i)
    if (i == -1):
        break
    s = sum(arr)
    print(s)
    