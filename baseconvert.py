def outofbaseten(innum, outbase):
    """
    input:
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
    input:
        innum: list of integers: number to be converted into base 10 in the form (1st digit, 2nd digit,etc)
        inbase: the base that innum is in
    output: interger: the value of innum as an integer

    calculates the value of innum as an python integer by summing the value of each digit, which is found by multiplying the digtit's value by its magnitude
    """
    value = 0
    length = len(innum)
    for count, digit in enumerate(iterable=innum,start=1):
        magnutude = inbase ** (length - count)
        value += magnutude * digit
    return value

def deprettify(innum):
    """
    input:
        innum: string: a number in base between 2 and 64 inclusive writen as a string eg: "15", "7C", or "a+"
    output: list of integers: the same number as innum but in the form of a list of each digit as an integer

    converts numbers writen as strings in arbritrary bases up to 64 into the list form that other functions work on.
    note that this only works with bases up to 64 and expects upper case letters, then lower case letters, then '+' then '/' for digits higher than 9.
    """
    outnum = []
    for i in innum:
        try:
            int(i)
        except ValueError:
            if i == '+':
                outnum.append(62)
            elif i == '/':
                outnum.append(63)
            elif i.isupper() is True:
                outnum.append(ord(i)-55)
            else:
                outnum.append(ord(i)-61)
        else:
            outnum.append(int(i))
    return outnum

def prettify(innum):
    """
    input:
        innnum: list of integers: a number in the form of a list of digits
    output: string: the number innum represented as a string

    converts numbers from the list forn used by other functions in this library into a string. the output will use 0 to 9 for digits with value up to 9, then upper case letters, then lower case letters, then '+', and '/' for 62 and 63.
    """
    outnum = ''
    for i in innum:
        if i < 10:
            outnum += str(i)
        elif i < 36:
            outnum += chr(i+55)
        elif i < 62:
            outnum += chr(i+61)
        elif i == 62:
            outnum += '+'
        elif i == 63:
            outnum += '/'
        else:
            raise ValueError("prettify() only works with numbers in a base no more than 64")
    return outnum

def baseconvert(innum, inbase, outbase):
    """
    input:
        innum: list of integers: the number to be converted. each item in the list represents a digit
        inbase: ineger: the numerical base that innum is in
        outbase: integer: the numerical base that the function will output

    convert a number writen as a list of digits from one arbitrary base to another
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

    inint = intobaseten(innum=innum,inbase=inbase)
    return outofbaseten(inint,outbase)