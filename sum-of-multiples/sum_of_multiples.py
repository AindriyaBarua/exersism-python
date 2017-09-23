def sum_of_multiples(n, lis):
    sum=0
    for i in range(0,len(lis)):
        lim=lis[i]*(n//lis[i])
        sum+=lis[i]*(lim*(lim+1))//2
    return sum




