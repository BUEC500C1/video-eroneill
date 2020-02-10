# EC500 Hw1
# Copyright 2020  Erin K O'Neill erinkate@bu.edu

# convert arabic numerals to roman 
# now with decimal and too large checks 

import string 


def convertnum(x):
    """convert the integer x into a string representation of x in roman numerals"""
    if x > 3999:
        return('too large')
    if not float(x).is_integer():
        return('not int')
    # first set up our lists 
    roman = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
    arabic = [1000, 500, 100, 50, 10, 5, 1, 0 , 0] 
    # divide thru each value and go down 
    stringrom = ""
    xval = x
    for conval in range(len(roman)):
        nxtlet = xval//arabic[conval]
        # print(nxtlet, " next letter")
        xval = xval%arabic[conval]
        # print(xval, " next xval")
        if xval == 0 and nxtlet ==0:
            break
        if nxtlet == 4:
            stringrom += roman[conval] + roman[conval - 1]
            # print("add 4 type")
        else:
            for i in range(nxtlet):
                stringrom += roman[conval]
                # print("add reg type")
        if conval%2 == 0  and  xval//(arabic[conval] - arabic[conval + 2]) == 1:
            # this is the 9 cases 
            xval = xval - (arabic[conval] - arabic[conval+2])
            stringrom += roman[conval+2] + roman[conval]

            
        # print(stringrom, " current string")
        
    return str(stringrom)

def main():
    print(convertnum(1066) + " should be MLXVI")

if __name__ == '__main__':
    main()

