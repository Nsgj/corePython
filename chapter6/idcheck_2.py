__author__ = 'gary'
import string
import keyword
alphas = string.letters + '_'
nums = string.digits
keyw = keyword.kwlist
print 'Welcome to the Identifier Checker v1.0\nTestees must be at least 2 chars long.'

myInput = raw_input('Identifier to test ')


if(len(myInput)>0):
    if (myInput[0] not in alphas) or (myInput in keyw):
        print '''invalid:first symbol must be alphasbetic'''
    elif(len(myInput) == 1):
        if(myInput  in keyw):
            print 'invalid input'
        else:
            print 'valid number'
    else:    
        for i in myInput[1:]:
            if i not in (alphas + nums):
                print '''invalid input'''
        else:
            print 'okay as an identifier'
""" yes i check it out """
