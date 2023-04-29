def outofbaseten(innum, outbase):
    """
    values:
        innum: integer: the number to be converted
        outbase: the base that innum is to be converted into
    output: list of integers: innum converted into a number in base outbase, in the form (1st digit, 2nd digit,etc)

    takes an integer in base 10, and converts it into abitrary base outbase by finding the number of digits the output will have(the magnitude), and starting with the largest digit in the output, calculating the value of the digit, adding it to a running list, and then substracting it from the value of the number to be converted.
    """
    if not isinstance(innum, int):
        if innum.isinteger() is False:
            raise ValueError("outofbaseten() only works with integer input")
    
    if innum == 0:
        return [0]

    import math
    magnitude = math.floor(math.log(innum)/math.log(outbase))
    worknum = innum
    out = []
    for i in range(magnitude + 1):
        digitsize = outbase ** (magnitude - i)
        digit = math.floor(worknum/digitsize)
        out.append(digit)
        worknum = worknum - digit * digitsize
    return out

def intobaseten(innum, inbase):
    """
    values:
        innum: list of integers: number to be converted into base 10 in the form (1st digit, 2nd digit,etc)
        inbase: the base that innum is in
    output: interger: the value of innum as an integer

    calculates the value of innum as an python integer by summing the value of each digit, which is found by multiplying the digtit's value by its magnitude
    """
    value = 0
    length = len(innum)
    for count, digit in enumerate(innum):
        magnutude = inbase ^ (length - count)
        value += magnutude * digit
    return value


def baseconvert(innum, inbase, outbase):
    """
    values:
    innum: list of integers: the number to be converted. each item in the list represents a digit
    inbase: ineger: the numerical base that innum is in
    outbase: integer: the numerical base that the function will output

    for now the function only works with inbase = 10
    ill do the other bit later
    """
    if inbase == 0:
        raise ValueError('base 0 is not possible')
    if inbase == 1:
        if innum == [0]:
            return [0]
        else:
            raise ValueError('non-bijective base 1 can only represent 0')

    index = 0
    for i in innum:
        index += 1
        if int(i) > inbase:
            raise ValueError('the digit at position'+str(index)+'is greater than the base')

    innum_string_representation = ''
    for i in innum:
        innum_string_representation += str(i)
    inint = int(innum_string_representation)
    return outofbaseten(inint,outbase)
