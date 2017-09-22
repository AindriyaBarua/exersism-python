def detect_anagrams(string, array):
    lisret = []
    list1 = list(array)
    str2="".join(set(string.lower()))
    for ent in list1:
        if len(string) == len(ent) and string.lower() != ent.lower():
           flag=0
           for ch in str2.lower():
               c2=(string.lower().count(ch))
               c1=(ent.lower()).count(ch)
               if(c2!=c1):
                   flag=1
                   break
           if flag==0:
               lisret.append(ent)

    return lisret










