To Do:

- Need new name :/
- Have CalcWriter print out values_dic[result] instead of string
- Add more calculations
- Print calculation results with no repeat of user inputs
- Print calculation result with calculation used
- Combine with KIVY


Total list of calculations so far:
  - E1 = (((ev * cr) / (cr - 1)) - mu)
  - E2 = (cr * bd) - mu
  - E3 = (cc / mc) - cr
  - E4 = ((ev + bd) / bd) - cr
  - E5 = (mu - bd) - ev
  - E6 = (dt * rr * .00085) - ev

Completed:

- Create CalcWriter program; writes out the needed core calculation code. Just input
  calculations set to zero and then copy and copy/paste into WaterCalc.

- Automatically extrapolate variables to all possible variables
    - ex: enter "a = b + c" as formula; automatically figures that:
          - b = a - c
          - c = a - b
    - using Sympy now but takes a long time
