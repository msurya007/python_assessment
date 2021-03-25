def count(s):
  n = 0
  x = []
  while n<len(s)-1:
      c = 1
      while s[n] == s[n+1]:
          n += 1
          c += 1
          if n+1 == len(s):
              break
      if c == 1:
          x.append(str(s[n]))
      else:
          x.append(str(s[n]+str(c)))
      n += 1
  if s[-1] != s[-2]:
      x.append(s[-1])
  c = ''.join(i for i in x)
  print(c)

s = input()
count(s)