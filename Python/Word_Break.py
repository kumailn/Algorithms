def wordBreak(s, dict):
    checklist = [False] * (len(s) + 1)
    checklist[len(s)] = True
    for i in range(len(s))[::-1]:
        for j in range(i,len(s)):
            if s[i:j+1] in dict and checklist[j+1]==True:
                checklist[i]=True
    return checklist[0]

print(wordBreak("cars", ["car","ca","rs"]))