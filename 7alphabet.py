num = list(map(int,input().split(",")))
alphabet = ""
for i in range(len(num)):
    c = chr(ord('@')+num[i])
    alphabet += c
print(alphabet)