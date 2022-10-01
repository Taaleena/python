from read_date import *
from print_date import *
from serch_date import *
from export_date import *

def greeting ():
    print ("Privet")

def start ():
    print ("chto nado? \n\
        1: Dannie uchenikov \n\
        2: Poisk uchenika \n\
        3: Nichego \n\
        4: Noviy uchenik")
    ch = input ("vash vibor: ")

    if ch == '1':
        date = read_date ()
        print_date (date)
        start ()
    
    elif ch == '2':
        info = input ("parametr dlya poiska: ")
        date = read_date ()
        item = serch_date (info, date)
        if item != None:
            print_date (item, True)
        else:
            print ("nichego")
        start ()
    elif ch == '3':
        print ("poka")

    elif ch == '4':
        export_date ()
        start ()

    else:
        print ("escho raz vash vibor: ")
        start ()

