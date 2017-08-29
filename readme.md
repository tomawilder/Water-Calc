To Do:

- Convert calculations to formats:
        - Given A = B + C:
        - if A is none and B is not none and C is not None:
              run calculation

        ?      or

        - Given A = B + C:

        - try (B + C):
            Except:
              pass
            if True:
              A = B + C

- Automatically extrapolate variables to all possible variables
    - ex: enter "a = b + c" as formula; automatically figures that:
          - b = a - c
          - c = a - b
    - using Sympy now but takes way too long ~ 15 seconds
- Print calculation results with no repeat of user inputs
- Print calculation result with calculation used
- Combine with KIVY
- Add more calculations

Total list of calculations so far:
  - E1 = (((e * rr) / (cr - 1)) - mu)
  - E2 = (cr * bd) - mu
  - E3 = (ctc / muc) - cr
  - E4 = ((e + bd) / bd) - cr
  - E5 = (mu - bd) - e
  - E6 = (dt * rr * .00085) - e
