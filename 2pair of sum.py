def pair(arr,s,l):
    for i in range(l):
        for j in range(i+1,l):
            if arr[i]+arr[j] == s:
                print((arr[i],arr[j]))
                return
    else:
        print("No Pairs found")

arr = list(map(int,input()))
s = 8
l = len(arr)
pair(arr,s,l)