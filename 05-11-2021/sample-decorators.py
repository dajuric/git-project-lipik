from typing import *
import functools

def splitString(function):
    @functools.wraps(function)
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string

    return wrapper

def toUpper(function):
    @functools.wraps(function)
    def wrapper():
        result = function()
        result = result.upper()
        return result

    return wrapper

@splitString
@toUpper
def returnString():
    return "Moja je noga bolesna"

print(returnString())