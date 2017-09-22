def square_of_sum(n):
    sum= 0
    for i in range(1,n+1):
        sum += i
    s1=sum**2
    return s1

def sum_of_squares(n):
    sum= 0
    for i in range(1,n+1):
        sum += (i**2)
    return sum


def difference(n):
    diff=square_of_sum(n)-sum_of_squares(n)
    return diff



