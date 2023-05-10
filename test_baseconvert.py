import baseconvert

def test_16_from_10_to_12():
    """
    test baseconvert() converting 16 from base 10 to base 12
    should get: `[1,4]`
    """
    output = baseconvert.baseconvert(inbase=10,outbase=12,innum="16")
    assert output == [1,4], ("16 was not succsesfully converted from base 10 to base 12, expected `[1,4]`, got `"+str(output)+"`")

def test_large_num_10_to_16():
    """
    test baseconvert converting 12244743 from base 10 to hexidecimal
    should get: [11,10,13,7,0,7]
    """
    output = baseconvert.baseconvert(inbase=10,outbase=16,innum="12244743")
    assert output == [11,10,13,7,0,7], ("12244743 was not succsesfully converted from base 10 to base 16, expected `[11,10,13,7,0,7]`, got `"+str(output)+"`")

def test_base_0():
    """
    attempts to convert 0 from base 10 to base 0
    should throw ValueError
    """
    try: 
        output = baseconvert.baseconvert(inbase=10,outbase=0,innum=0)
    except ValueError:
        ValueErrord = True
    except:
        message = "threw a different error"
    else:
        message = "returned"+str(output)
    assert ValueErrord, "attempting to convert 0 into base 0 from base 10 didn't throw a ValueError, instead it"+message

def test_negative_num():
    """
    test baseconvert with negative innum
    converting -12 from base 10 to base 8
    should get [-1,4]
    """
    output = baseconvert.baseconvert(inbase=10,outbase=8,innum="-12")
    assert output == [-1,4], ("-12 was not successfully converted from base 10 to base 8")

def test_14_from_10_to_8():
    """
    test outofbaseten converting from base 10 to base 8
    should get: [1,6]
    """
    output = baseconvert.outofbaseten(innum=14,outbase=8)
    assert output == [1,6], ("14 was not successfully converted from base 10 to base 8")

def test_large_num_10_to_6():
    """
    test outofbaseten converting 13722656 from base 10 to base 6
    should get: [1,2,1,0,0,4,2,4,5,2]
    """
    output = baseconvert.outofbaseten(innum=13722656,outbase=6)
    assert output == [1,2,1,0,0,4,2,4,5,2], ("13722656 was not successfully converted from base 10 to base 6")

def test_1011_from_2_to_10():
    """
    test intobaseten converting 1011 from base 2 to base 10
    should get: [1,1]
    """
    output = baseconvert.intobaseten(innum=1011,inbase=2)
    assert output == [1,1], ("1011 was not successfully converted from base 2 to base 10")

def test_large_num_from_14_to_10():
    """
    test intobaseten converting 23651722 from base 14 to base 10
    should get: [2,3,6,8,3,8,7,8,6]
    """
    output = baseconvert.intobaseten(innum=23651722,inbase=14)
    assert output == [2,3,6,8,3,8,7,8,6], ("23651722 was not successfully converted from base 14 to base 10")

def test_deprettify_9D():
    """
    test deprettify deprettifying '9D'
    should get [9,13]
    """
    output = baseconvert.deprettify(innum='9D')
    assert output == [9,13], ("9D was not successfully deprettified")

def test_deprettify_large_num():
    """
    test deprettify deprettifying 'Aa1+F/'
    should get [10,36,1,62,15,63]
    """
    output = baseconvert.deprettify(innum='Aa1+F/')
    assert output == [10,36,1,62,15,63], ("Aa1+F/ was not successfully deprettified")

def test_prettify_num():
    """
    test prettify prettifying [7,38,2]
    should get '7c2'
    """
    output = baseconvert.prettify(innum=[7,38,2])
    assert output == '7c2', ("[7,38,2] was not successfully prettified")

def test_prettify_large_num():
    """
    test prettify prettifying [2,13,12,15,7,2,8,9]
    should get '2DCF7289'
    """
    output = baseconvert.prettify(innum=[2,13,12,15,7,2,8,9])
    assert output == '2DCF7289', ("[2,13,12,15,7,2,8,9] was not successfully prettified")


### run tests
test_16_from_10_to_12()
test_large_num_10_to_16()
test_negative_num()
test_14_from_10_to_8()
test_large_num_10_to_6()
test_1011_from_2_to_10()
test_large_num_from_14_to_10()
test_deprettify_9D()
test_deprettify_large_num()
test_prettify_num()
test_prettify_large_num()