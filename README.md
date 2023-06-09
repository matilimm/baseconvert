# baseconvert
This is a library for python that will convert integers between abitrary natural number bases.

## Tutorial
in this tutorial we will convert a integer from dozenal to base64 using baseconvert.

say we have a dozenal integer, written as a string, eg: `"123BA9"`. baseconvert requires a number to be expressed as a list of integer digits. so we can't do anything until we take our number into this form. to do this we use `deprettify`:
```python
import baseconvert
number_as_string = "123BA9"
number_as_list = baseconvert.deprettify(number_as_string)
```
at this stage, the value of `number_as_list` will be `[1, 2, 3, 11, 10, 9]`. notice that the letters have been interpreted to have numerical values corresponding to their position in the alphabet. the `deprettify` and `prettify` functions will work with digit values greater than 9 being 1st the upper case letters A-Z, then lower case a-z, then +, then /. fix this aside \
Once we have our number as a list, we can convert it to a different base.
```python
number_in_base_64 = baseconvert.baseconvert(innum=number_as_list,inbase=12,outbase=64)
```
this will give `[13, 38, 45, 12]`.\
and we can write that as a string.
```python
final_number = baseconvert.prettify(number_in_base_64)
```
which will give:
```
'DcjC'
```

## How-to guides
### Convert a number from an arbitrary base to a python integer
Convert a number $n$, represented as a string in base $b$, into string format, then into a python integer.
```python
import baseconvert
n = '123'
b = 15
n_as_list = baseconvert.deprettify(n)
n_as_int = baseconvert.intobaseten(innum=n_as_string, inbase=b)
```
This gives:
```
258
```
### Convert a python integer into a number writen in an arbitrary base
Write a number $n$, represented as a python integer in an arbitrary base $b$.
```python
import baseconvert
n = 123
b = 16
n_as_list = baseconvert.outofbaseten(innum=n,outbase=b)
n_as_string = baseconvert.prettify(n_as_list)
```
This gives:
```
7B
```
### Convert a number between large bases using list notation
Convert a number $n$, represent as a list of individual digits from large base $b1$ into base $b2$. \
$b1$ and $b2$ can be any size, but string representation in only supported for bases $\le 64$.
```python
import baseconvert
n = [12,84,780,3]
b1 = 5040
b2 = 1000
n_in_b1 = baseconvert.baseconvert(innum=n,inbase=b1,outbase=b2)
```
This gives:
```
[1, 538, 426, 433, 603]
```
note that that is wrong and will be changed

### Write a number as a list of digits
Write a number $n$ that you have as a string as a list of digits. This works with any base up to 64
```python
import baseconvert
n = '13Cd+'
n_as_list = baseconvert.deprettify(n)
```
this gives:
```
[1, 3, 12, 39, 62]
```
## Explanation
We write numbers using a positional base ten (decimal) system. That means that we use ten unique symbols to write numbers, ten being the radix or base of the system. The symbols used are 0 and the digits 1 to 9. We use these to write larger numbers by multiplying each digit by a power of the base, so the right most digit is mustilplied by $10^0$ ie. 1, and then $10^1$, $10^2$, etc. moving left. so a number like 512 can thought of as shorthand for $(5 \times 10^2)+(1 \times 10^1)+(2 \times 10^0)$.\
Simmilarly, you can use any natural number as a radix, some common bases are 2 (binary), 16 (hexadecimal), and 12 (dozenal). So a number in hexadecimal like 6A3 can be read as $(6 \times 16^2)+(10 \times 16^1)+(3 \times 16^0)$.\
For bases larger than 10, digits larger than 9 are writen in a number of ways, the most common is to use the upper case latin letters A-Z, then if higher digits are needed, lower case a-z can be used. This is simmilar to the approach taken by most implemenations of base64, a common radix used for data storage, as a digit of base64 uses exactly 6 bits of memory, and around the upper limit of what can be easily human readable. the digits 0 to 9, along with the upper and lower case latin alphabet compromise 62 symbols, so only two more are needed, usually + and /, to make 64. Actual base64 usually puts the digits 0 to 9 after the upper and lower case letters. baseconvert does not do that.

## Reference

### List of functionallity
The following functions are written in baseconvert:
- `prettify`
- `deprittify`
- `intobaseten`
- `outofbaseten`
- `baseconvert`

### Bibliography

The wikipedia pages for positional notation and radix give a good dicription of how positional number systems work, including discriptions of more non-standard systems such as negative and non-ineger bases, and bijective numerical systems.

