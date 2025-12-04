s = "LVIII"
s=list(s)
"""I can be placed before V (5) and X (10) to make 4 and 9. IV=4
X can be placed before L (50) and C (100) to make 40 and 90. XL=40
C can be placed before D (500) and M (1000) to make 400 and 900.CM=900
"""
mapper={
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
result=[]
for num in s:
    for i,j in mapper.items():
        try:
            x=s[s.index(num)+1]
            if num=='I' and x=='V':
                result.append(4)
                s.pop(s.index(x))
                break
            elif num=='I' and x=='X':
                result.append(9)
                s.pop(s.index(x))
                break
            elif num=='X' and x=='L':
                result.append(40)
                s.pop(s.index(x))
                break
            elif num=='X' and x=='C':
                result.append(90)
                s.pop(s.index(x))
                break
            elif num=='C' and x=='D':
                result.append(400)
                s.pop(s.index(x))
                break
            elif num=='C' and x=='M':
                result.append(900)
                s.pop(s.index(x))
                break     
        except:
            pass
        if num == i:
            result.append(j)
            break
print(sum(result))