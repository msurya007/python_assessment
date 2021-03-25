import random
import string

n = input()
str = n[::-1].lower()
s=1
r=''.join(random.choices(string.ascii_uppercase,k=s))
print(r+str)