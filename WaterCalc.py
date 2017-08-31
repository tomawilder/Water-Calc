print('\nWelcome to the Water Treatment Calculator!')

# These are all the possible values you can provide
# as pairs of `shortcut: name` This is a dictionary/hash table
inputs_dic = {
'mu': 'makeup gpm',
'ev': 'evaporation gpm',
'bd': 'blowdown gpm',
'cr': 'cycles of concentration',
'rr': 'recirculation rate gpm',
'cc': 'cooling tower conductivity in mmhos',
'mc': 'makeup water conductivity in mmhos',
'dt': 'delta T in degrees F',
}

# dictionary, gives the value of None to the following
values_dic = {
  'mu': None,
  'ev': None,
  'bd': None,
  'cr': None,
  'rr': None,
  'cc': None,
  'mc': None,
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

# Starting here, you have a dictionary with some data
# but not all.
# So you start running some calculation
# Function starts here

#converts dictionary to variables. easier to type out/read
mu = values_dic['mu']
ev = values_dic['ev']
bd = values_dic['bd']
cr = values_dic['cr']
rr = values_dic['rr']
cc = values_dic['cc']
mc = values_dic['mc']
dt = values_dic['dt']

#def calculate():
while True:

    if ev is not None and cr is not None and mu is None:
        mu = cr*ev/(cr - 1)
        continue

    elif cr is not None and bd is not None and mu is None:
        mu = bd*cr
        continue

    elif ev is not None and bd is not None and mu is None:
        mu = bd + ev
        continue

    elif mu is not None and cr is not None and ev is None:
        ev = mu - mu/cr
        continue

    elif cr is not None and bd is not None and ev is None:
        ev = bd*(cr - 1)
        continue

    elif mu is not None and bd is not None and ev is None:
        ev = -bd + mu
        continue

    elif rr is not None and dt is not None and ev is None:
        ev = 0.00085*dt*rr
        continue

    elif ev is not None and dt is not None and rr is None:
        rr = 1176.47058823529*ev/dt
        continue

    elif mu is not None and ev is not None and cr is None:
        cr = -mu/(ev - mu)
        continue

    elif mu is not None and bd is not None and cr is None:
        cr = mu/bd
        continue

    elif cc is not None and mc is not None and cr is None:
        cr = cc/mc
        continue

    elif ev is not None and bd is not None and cr is None:
        cr = (bd + ev)/bd
        continue

    elif mu is not None and cr is not None and bd is None:
        bd = mu/cr
        continue

    elif ev is not None and cr is not None and bd is None:
        bd = ev/(cr - 1)
        continue

    elif mu is not None and ev is not None and bd is None:
        bd = -ev + mu
        continue

    elif cr is not None and mc is not None and cc is None:
        cc = cr*mc
        continue

    elif cr is not None and cc is not None and mc is None:
        mc = cc/cr
        continue

    elif ev is not None and rr is not None and dt is None:
        dt = 1176.47058823529*ev/rr
        continue

    break

#converts strings back to dictionary
values_dic['mu'] = mu
values_dic['ev'] = ev
values_dic['bd'] = bd
values_dic['cr'] = cr
values_dic['rr'] = rr
values_dic['cc'] = cc
values_dic['mc'] = mc
values_dic['dt'] = dt

# Function ends
# by this point , the dictionary contains as many values as possible
#
# could be:
#
# populate_all_values(values_dict)
#

for user_input in values_dic:
    listed_values = values_dic[user_input]
    if listed_values:
        test_result = values_dic[user_input]
        test_name = inputs_dic[user_input]
        print('The %s is %s.' % (test_name, format(test_result, '.2f')))
