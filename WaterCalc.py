mu, e, bd, cr, rr, ctc, muc, dt = '','','','','','','',''  # assigns the variable of '' to each test

print('Welcome to the Water Treatment Calculator!')

mu_list = 'mu for Makeup'
e_list = 'e for Evaporation'
bd_list = 'bd for Blowdown'
cr_list = 'cr for Cycles of Concentration'
rr_list = 'rr for Recirculation Rate'
ctc_list = 'ctc for Cooling Tower Conductivity'
muc_list = 'muc for Makeup Water Conductivity'
dt_list = 'dt for Delta T'

def test_list():
    # this lists what tests have NOT been run
    if mu == '':
        print(mu_list)

    if e == '':
        print(e_list)

    if bd == '':
        print(bd_list)

    if cr == '':
        print(cr_list)

    if rr == '':
        print(rr_list)

    if ctc == '':
        print(ctc_list)

    if muc == '':
        print(muc_list)

    if dt == '':
        print(dt_list)

def tests_not_run():
    print('''\nPlease type in the shortcut for any of the following
    cooling tower system information that you may have:''' + '\n' )
    test_list()
    print('\n' + 'Type done if you are finished. ')

tests_not_run()

def has_more_data():
    # ask if user has more data to enter
    # returns true or false
    print('Do you have any more data you would like to enter? Y/N')
    while True:
        yn= input()
        if yn == 'y':
            print('Thank you. Please enter in another test.')
            tests_not_run()
            return True
        elif yn == 'n':
            print('Tests will now be run' + '\n')
            return False
        else:
            print('Sorry; try again!')
            continue

def get_number():
    # stores data as different variables
    while True:
        try:
            data = float(input())
            print('Thanks!')
            return data
        except ValueError:
            print("Please enter an actual number.")


while True:

    test = input() # write in 'mu' or 'e' or 'bd'. Depends on what info you have

    if test in ('mu', 'e', 'bd', 'cr', 'rr', 'ctc', 'muc', 'dt'):

        if test == 'mu':
            print ('What is the cooling tower makeup gpm?: ')
            mu = get_number()
            if not has_more_data():
                break

        elif test == 'e':
            print ('What is the cooling tower evaporation rate in gpm?: ')
            e = get_number()
            if not has_more_data():
                break

        elif test == 'bd':
            print ('What is the cooling tower blowdown in gpm?: ')
            bd = get_number()
            if not has_more_data():
                break

        elif test == 'cr':
            print ('How many cycles is the cooling tower running at?: ')
            cr = get_number()
            if not has_more_data():
                break

        elif test == 'rr':
            print ('What is the recirculation rate in gpm?: ')
            rr = get_number()
            if not has_more_data():
                break

        elif test == 'ctc':
            print ('What is the cooling tower conductivity?: ')
            ctc = get_number()
            if not has_more_data():
                break

        elif test == 'muc':
            print ('What is the makeup water conductivity?: ')
            muc = get_number()
            if not has_more_data():
                break

        elif test == 'dt':
            print ('What is the delta T in F across the cooling tower?: ')
            dt = get_number()
            if not has_more_data():
                break

    elif test == 'done':
            print('Thank you!')
            break

    else:
        print('Please enter a valid shortcut: ')
        continue


# the following runs the calculations
while True:

    if e != '' and rr != '' and cr !='':
        if mu == '' :
            mu = (e * rr) / (cr - 1)

    elif cr != '' and bd != '':
        if mu == '' :
            mu = cr * bd

    elif mu != '' and bd != '':
        if cr == '' :
            cr = mu / bd

    elif ctc != '' and muc != '':
        if cr == '' :
            cr = ctc / muc

    elif e != '' and bd != '':
        if cr == '' :
            cr = (e + bd) / bd

    elif mu != '' and bd != '':
        if e == '' :
            e = mu - bd

    elif cr != '' and bd != '':
        if e == '' :
            e = (cr * bd) - bd

    elif dt != '' and r != '':
        if e == '' :
            e = dt * rr * .00085

    elif e != '' and cr != '':
        if bd == '' :
            bd = e / (cr - 1)

    elif mu != '' and e != '':
        if bd == '' :
            bd = mu - e

    elif mu != '' and cr != '':
        if bd == '' :
            bd = mu / cr

    break

#the following prints the results:


print('The cooling tower makeup rate is ' + str(format(mu, '.2f')))

print('The cooling tower makeup rate is ' + str(format(mu, '.2f')))

print('The cooling tower cycles are at ' + str(format(cr, '.2f')))

print('The cooling tower cycles are at ' + str(format(cr, '.2f')))

print('The cooling tower cycles are at ' + str(format(cr, '.2f')))

print('The evaporation rate is ' + str(format(e, '.2f')))

print('The evaporation rate is ' + str(format(e, '.2f')))

print('The evaporation rate is ' + str(format(e, '.2f')))

print('The cooling tower blowdown is ' + str(format(bd, '.2f')))

print('The cooling tower blowdown is ' + str(format(bd, '.2f')))

print('The cooling tower blowdown is ' + str(format(bd, '.2f')))

# To Do:
    #1 Have list of calculations run itself over multiple times
    #2 Print out of user inputs with list of calculated variables below
    #3 Add more calculations
    #4 Combine with KIVY

    # ALSO
        #Upload to GITHUB


# total list of calculations so far
    #completed
 # MU = (E * RR) / (CR - 1)
 # MU = CR * BD
 # CR = MU / BD
 # CR = CTC / MUC
 # CR = (E + BD) / BD
 # E = MU - BD
 # E = (CR * BD) - BD
 # E = DT * RR * .00085
 # BD = E / (CR - 1)
 # BD = MU - E
 # BD = MU / CR
        # not completed


print('The End')
