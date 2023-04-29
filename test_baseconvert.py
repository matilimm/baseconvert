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
    test baseconbert converting 12244743 from base 10 to hexidecimal
    should get: [11,10,13,7,0,7]
    """
    output = baseconvert.baseconvert(inbase=10,outbase=16,innum="12244743")
    assert output == [11,10,13,7,0,7], ("12244743 was not succsesfully converted from base 10 to base 16, expected `[11,10,13,7,0,7]`, got `"+str(output)+"`")

def test_base_0():
    """
    attempts to covert 0 from base 10 to base 0
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


### run tests
test_16_from_10_to_12()
test_large_num_10_to_16()
test_base_0()