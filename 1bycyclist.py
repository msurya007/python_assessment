pi = 3.14
d = 7
r = d/2
t = 0
n=int(input("Enter No.of Rounds : "))
for i in range(0,n):
    c = 2*pi*r
    t += c
print("%.2f Kms travelled." %t )