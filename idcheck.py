__author__ = 'gary'
import string
alphas = string.letters + '_'
nums = string.digits

print 'Welcome to the Identifier Checker v1.0\nTestees must be at least 2 chars long.'

myInput = raw_input('Identifier to test ')

if(len(myInput)>1):
    if myInput[0] not in alphas:
        print '''invalid:first symbol must be alphasbetic'''
    else:
        for i in myInput[1:]:
            if i not in (alphas + nums):
                print '''invalid input'''
        else:
            print 'okay as an identifier'
""" yes i check it out """