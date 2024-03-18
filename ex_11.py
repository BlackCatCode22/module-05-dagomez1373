#ex 1
import re

example = " From example098@my.scccd.edu Sun Mar 17"
words = example.split()
emal = words[1]
pieces = emal.split('@')
print(pieces[0])

#ex 2

import re
hand = open('mbox-short.txt')
numlist = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+), line')
    if len(stuff) != 1 : continue
    num = float(stuff[0])
    numlist.append(num)
print('Maximum:', max(numlist))


