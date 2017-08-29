print('\nWelcome to the Water Treatment Calculator!')

# These are all the possible values you can provide
# as pairs of `shortcut: name` This is a dictionary/hash table
inputs_dic = {
'mu': 'makeup gpm',
'e': 'evaporation gpm',
'bd': 'blowdown gpm',
'cr': 'cycles of concentration',
'rr': 'recirculation rate gpm',
'ctc': 'cooling tower conductivity in mmhos',
'muc': 'makeup water conductivity in mmhos',
'dt': 'delta T in degrees F',
}

# dictionary, gives the value of None to the following
values_dic = {
  'mu': None,
  'e': None,
  'bd': None,
  'cr': None,
  'rr': None,
  'ctc': None,
  'muc': None,
  'dt': None,
}

#creates a loop
while True:
    for test_shortcut in inputs_dic:
        #True for each 'inputs' dictionary entry that has a value of None
        #False for each 'inputs' dictionary entry that does not have a value of None
        not_entered_yet = values_dic[test_shortcut] is None
        #For each 'inputs' dictionary entry that has value of None...
        if not_entered_yet:
            #list of 'inputs' dictionary that return 'None'
            test_name = inputs_dic[test_shortcut]
            #Reminds the user what values can be entered:
            print('  - Type %s to enter %s' % (test_shortcut, test_name))
    print('  - Type done when finished\n')


    #lets user insert data and stores as 'test' variable. Ends data entry when done is typed
    while True:
        test = input("Type here: ")
        if test in inputs_dic:
            break
        elif test == "done":
            break
        else:
            print("Please enter one of the menu options.")

    #If input is in 'inputs' dictionary...
    if test in inputs_dic:
        #variable = inputs dictionary list?
        value_name = inputs_dic[test]
        print('\nWhat is the %s?' % value_name)
        #checks to make sure entry is a number. returns to menu if R/r
        while True:
            try:
                entry = input("Please enter a result or type \"R\" to return to the menu. ")
                if entry == 'r' or entry == 'R':
                    break
                entry = float(entry)
                values_dic[test] = entry
                print('\nThanks!\n')
                break
            except ValueError:
                continue
            break
    elif test == "done" or test == "Done":
        break

#prints out user inputs
print('\nUser inputs are as follows:')
for user_input in values_dic:
    listed_values = values_dic[user_input]
    if listed_values:
        test_result = values_dic[user_input]
        test_name = inputs_dic[user_input]
        print('The %s is %s.' % (test_name, format(test_result, '.2f')))

# calculation section
print('\nCalculations are as follows:')

#converts dictionary to variables. easier to type out/read
mu = values_dic['mu']
e = values_dic['e']
bd = values_dic['bd']
cr = values_dic['cr']
rr = values_dic['rr']
ctc = values_dic['ctc']
muc = values_dic['muc']
dt = values_dic['dt']


while True:

    if e is not None and rr is not None and cr is not None and mu is None:
        mu = ((e * rr) / (cr - 1))
        continue

    elif cr is not None and bd is not None and mu is None:
        mu = (cr * bd) #same as line 112 and line 140
        continue

    elif ctc is not None and muc is not None and cr is None:
        cr = (ctc / muc)
        continue

    elif mu is not None and bd is not None and cr is None:
        cr = (mu / bd) #same as line 104 and line 140
        continue

    elif e is not None and bd is not None and cr is None:
        cr = ((e + bd) / bd) # same as line 124
        continue

    elif mu is not None and bd is not None and e is None:
        e = (mu - bd) # same as line 136
        continue

    elif cr is not None and bd is not None and e is None:
        e = ((cr * bd) - bd) # same as line 116
        continue

    elif dt is not None and rr is not None and e is None:
        e = (dt * rr * .00085)
        continue

    elif e is not None and cr is not None and bd is None:
        bd = (e / (cr - 1))
        continue

    elif mu is not None and e is not None and bd is None:
        bd = (mu - e) # same as line 120
        continue

    elif mu is not None and cr is not None and bd is None:
        bd = (mu / cr) # same as line 112 and line 104
        continue

    break

#converts strings back to dictionary
values_dic['mu'] = mu
values_dic['e'] = e
values_dic['bd'] = bd
values_dic['cr'] = cr
values_dic['rr'] = rr
values_dic['ctc'] = ctc
values_dic['muc'] = muc
values_dic['dt'] = dt


for user_input in values_dic:
    listed_values = values_dic[user_input]
    if listed_values:
        test_result = values_dic[user_input]
        test_name = inputs_dic[user_input]
        print('The %s is %s.' % (test_name, format(test_result, '.2f')))
