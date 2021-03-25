def uncomman(w1,w2):
    s1 = set(w1)
    s2 = set(w2)
    l = list(s1 & s2)
    s = " "
    for i in w1:
        if i not in l:
            s+=i
    for i in w2:
        if i not in l:
            s+=i
    print(s)

word1 = input()
word2 = input()
uncomman(word1,word2)