def slices(string, d):
    if d> len(string):
        raise ValueError
    elif d==0:
        raise ValueError
    else:
        slices = []
        for indx, elem in enumerate(string):
            if len(string) - indx >= d:
                curr_slice = []
                curr_indx = indx
                while len(curr_slice) < d:
                    curr_slice.append(int(string[curr_indx]))
                    curr_indx += 1
                slices.append(curr_slice)
    return slices