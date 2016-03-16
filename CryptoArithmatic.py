#/usr/bin/python3

import itertools
import re
import os
import sys


def get_value(word, substitution):
    s = 0
    factor = 1
    for letter in reversed(word):
        s += factor * substitution[letter]
        factor *= 10
    return s


def solve2(equation):
    # split equation in left and right
    left, right = equation.lower().replace(' ', '').split('=')
    # split words in left part
    left = left.split('+')
    # create list of used letters
    letters = set(right)
    for word in left:
        for letter in word:
            letters.add(letter)
    letters = list(letters)
    bigResult = 0
    finalResult = ""
    digits = range(10)
    for perm in itertools.permutations(digits, len(letters)):
        sol = dict(zip(letters, perm))

        if sum(get_value(word, sol) for word in left) == get_value(right, sol):
            #result = print(' + '.join(str(get_value(word, sol)) for word in left) + " = {} (mapping: {})".format(get_value(right, sol), sol))
            if get_value(right, sol) > bigResult:
                bigResult = get_value(right, sol)
                finalResult = ' + '.join(str(get_value(word, sol)) for word in left) + " = {} (mapping: {})".format(get_value(right, sol), sol)
    print("\n Biggest solution is:  ", finalResult)


if __name__ == '__main__':
    inp = ""
    inputString = ""
    while "money" not in inp.lower():
        inp = input(r'enter your input: ')
        inp = re.sub(r'[0-9]','',inp)
        inp = re.sub(r'\$','',inp)
        inp = inp.split('#')[0]
        inp = inp.strip()
        #inp = re.sub(r'#+[0-9,]')
        if len(inputString) <= 0:
            if "money" not in inp.lower():
                inputString = inp
        else:
            if "money" not in inp.lower() :
                inputString += " + " +inp
                #print("Inner value : "+inputString)
    inputString += " = " + inp
    #solve2("SEND + MORE = MONEY")
    print(inputString)
    solve2(inputString)
