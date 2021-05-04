def Avg(listNums):
    length = len(listNums)
    total = 0
    if length > 0:
        for i in range(len(listNums)):
            if type(listNums[i]) == str:
                raise TypeError("String in list")
            else:
                total += listNums[i]
    else:
        raise IndexError("List is empty")
    avg = (total / length)
    return avg







