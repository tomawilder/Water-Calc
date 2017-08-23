import pdb

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
'dt': 'delta T',
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
    elif test == "done":
        break

#prints out user inputs
print('\nUser inputs are as follows:')
for user_input in values_dic:
    listed_values = values_dic[user_input]
    if listed_values:
        test_result = values_dic[user_input]
        result_list = [test_result]
        test_name = inputs_dic[user_input]
        print('The %s is %s.' % (test_name, int(test_result)))



print('\nCalculations are as follows:')



# the following runs the calculations
