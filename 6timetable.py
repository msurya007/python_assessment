import random
def timetable(n):
    a = []
    b = []
    for i in range(n):
        r = random.sample(range(0,n),n)
        a.append(r)
    for i in range(n):
        c = input("Enter data : ")
        b.append(c)
    for i in range(5):
        print("Day-",i+1,end=" ")
        for j in range(5):
            c = a[i][j]
            print(b[c],end=" ")
        print("\n")
n = int(input())
timetable(n)