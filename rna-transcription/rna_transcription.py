def to_rna(str):
    if len(str)==str.count('G')+str.count('C')+str.count('T')+str.count('A'):
        str=str.replace("G", "c")
        str=str.replace("C", "G")
        str=str.replace("T", "a")
        str=str.replace("A", "U")
        str=str.upper()
    else:
        str=''
    return str

