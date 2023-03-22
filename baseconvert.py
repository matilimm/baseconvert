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
        if i > inbase:
            raise ValueError('the digit at position'+str(index)+'is greater than the base')

    innum_string_representation = ''
    for i in innum:
        innum_string_representation += str(i)
    inint = int(innum_string_representation)
    return inint

#TODO github
#TODO code for conversion to abritrary base

print(baseconvert(10,10,10))