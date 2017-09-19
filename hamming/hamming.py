def distance(test1, test2):
	if len(test1) != len(test2):
        	raise ValueError()

        if test1 == "":
                return 0

        hamming_distance = 0
	for i in range(len(test1)):
		if test1[i] == test2[i]:
                    hamming_distance += 0
                else:
                    hamming_distance += 1
	return hamming_distance

