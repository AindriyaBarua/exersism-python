def encode(str1):
    if not str1:
        return ''
    else:
        ch1 = str1[0]
        c = 1
        res = ''
        for i in range(1,len(str1)):
            if str1[i] == ch1:
                c += 1
            else:
                if c == 1:
                    res = res + ch1
                else:
                    res = res + str(c) + ch1
                    c = 1
            ch1 = str1[i]
        if c == 1:
            res = res + ch1
        else:
            res = res + str(c) + ch1
        return res
def decode(str2):
    if not str2:
        return ""
    else:
        res=''
        mul=0
        for i in range(0,len(str2)):
            if str2[i].isdigit():
                mul = mul*10+int(str2[i])
            else:
                if i==0:
                    mul=1
                res += mul*str2[i]
                if i!=len(str2)-1 and not str2[i+1].isdigit():
                    res = res+str2[i+1]
                    i += 1
                mul=0
    return res

        #char = text[1]
        #quantity = text[0]
        #return char * int(quantity) + decode(text[2:])





