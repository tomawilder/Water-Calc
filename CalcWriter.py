# work this by typing "python3 CalcWriter.py cs.txt"

#import argv module/command line tool
from sys import argv
from sympy import var
from sympy import solve
import re

script, filename = argv
target = open(filename, 'w')
target.truncate()

mu, ev, rr, cr, bd, cc, mc, dt = var('mu, ev, rr, cr, bd, cc, mc, dt')
list1 = [mu, ev, rr, cr, bd, cc, mc, dt]
list3 = ("mu", "ev", "rr", "cr", "bd", "cc", "mc", "dt")

#list of equations set to 0. These can be changed to whatever calculations you want
E1 = (((ev * cr) / (cr - 1)) - mu)
E2 = ((cr * bd) - mu)
E3 = ((cc / mc) - cr)
E4 = (((ev + bd) / bd) - cr)
E5 = ((mu - bd) - ev)
E6 = ((dt * rr * .00085) - ev)

list2 = [E1, E2, E3, E4, E5, E6]
space = "\n"

for solution in list1:
    for equation in list2:
        sols = solve([equation], [solution])
        if sols != []:
            sols = (sols)
            target.write(f"{sols}{space}")

target = open(filename)

#text compiler
for a_line in target:
    resplit = re.split('\W+', a_line[5:-2])
    var_list = []
    for var in list3:
        if var in resplit:
            var_list.append(var)

    print(f"{space}\telif ", end = '')
    for is_not in var_list:
        print(f"{is_not} is not None and ", end = '')
    print(f"{a_line[1:3]} is None:")
    print(f"\t\t{a_line[1:3]} = {a_line[5:-2]}") #issue with editor??
    print("\t\tcontinue")
print("-------")
