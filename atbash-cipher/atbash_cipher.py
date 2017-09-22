def encode(string):
    new=''
    c=0
    for ch in string:
        if ch.isalpha():
            if ch.isupper():
                new+=chr(90-ord(ch)+65).lower()
                c+=1
            if ch.islower():
                new+=chr(122-ord(ch)+97).lower()
                c+=1
        elif ch.isdigit():
            new+=ch
            c+=1
        if c==5:
            new+=' '
            c=0
    if new.endswith(' '):
        new=new[:-1]
    return new





def decode(string):
    new=''
    for ch in string:
        if ch.isalpha() or ch.isdigit():
            if ch.isupper():
                new+=chr(65+(90-ord(ch))).lower()
            elif ch.islower():
                new+=chr(97+122-(ord(ch))).lower()
            else:
                new+=ch
    return new



