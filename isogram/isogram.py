'''def is_isogram(string):
    l=list(string)
    flag=0
    for i in range(0,l.length):
        for k in range(0,l.length):
            if l[i]==l[k]:
                flag=1
    if flag==0:
        return True
    else:
        return False
        '''


def is_isogram(string):
    lower_string = string.lower()

    for s in lower_string:
        if s.isalpha():
            if lower_string.count(s) > 1:
                return False
    return True





