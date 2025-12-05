s = "(]"

check = []
i= (len(s)-2) #4,5
while i >= 0:
    if s[i]=='[' and s[i+1]==']':
        check.append(True)
    elif s[i]=='(' and s[i+1]==')':
        check.append(True)
    elif s[i]=='{' and s[i+1]=='}':
        check.append(True)
    else:
        check.append(False)
    i -=2
        
print(all(check))

             