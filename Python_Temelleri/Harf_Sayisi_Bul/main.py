cumle = "sadasdkqwlkşsadkkşkcxşlkzkkkdasşdkaksmxözmmcxmmxömxq"
kelime = dict()

for i in cumle:
    if i in kelime:
        kelime[i] +=1
    else:
        kelime[i] = 1
for i,j in kelime.items():
    print(i,":",j)
