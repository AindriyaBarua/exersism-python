def is_pangram(string):
    s_string=string.lower()
    ls=[]
    for s in s_string:
        if s.isalpha():
                c=ord(s)
                if ls.count(c)==0:
                    ls.append(c)
    if len(ls)==26:
        return True
    return False






