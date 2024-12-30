def maxmin(list_of_integers):
    two_integers = []
    list_of_integers = sorted(list_of_integers)
    for i in range(len(list_of_integers)):
        two_integers.append(list_of_integers[0])
        two_integers.append(list_of_integers[-1])
        return two_integers


integers = [0, 5, 2, 9, 12, -100]
print(maxmin(integers))
