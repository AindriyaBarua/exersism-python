def rotate(text,key):
    for i in range(0,len(text)):
        ch=text[i]
        if ch.isalpha():
            change=(ord(ch)+key)
            if (change <=90 and ch.isupper()) or (change<=122 and ch.islower()):
                text=text.replace(text[i],str(change))
            elif ch.islower():
                text=text.replace(text[i],str(65+change-90))
            elif ch.islower():
                text=text.replace(text[i],str(97+change-122))
    return text