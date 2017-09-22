def rotate(text,key):
    new=''
    for i in range(0,len(text)):
        ch=text[i]
        if ch.isalpha():
            change=(ord(ch)+key)
            if ch.isupper():
                if change >90:
                    change= 66+change-90-2
            elif (ch.islower()):
                if change>122:
                    change= 96+change-122
            new=new+chr(change)
        else:
            new=new+ch
    return new