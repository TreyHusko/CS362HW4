def full(fName, lName):
    if type(fName) != str or type(lName) != str:
        raise TypeError("Name isn't valid string")
    elif len(fName) == 0 or len(lName) == 0:
        raise ValueError("No name input")
    else:
        fullName = fName + " " + lName
    return fullName

