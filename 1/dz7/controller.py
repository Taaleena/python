
from import_data import import_data
from export_data import export_data
from print_data import print_data
from search_data import search_data

def greeting ():
    print ("Privet")

def input_date ():
    last_name = input ("print familia: ")
    first_name = input ("print name: ")
    phone_num = input ("print telefon: ")
    note = input ("print comment: ")
    return [last_name, first_name, phone_num, note]

def choice_raz ():
    raz = input ("print razdelitel: ")
    if raz == "":
        raz = None
    return raz

def choice_todo ():
    print ("what do you do?: \n\
    1 - export; \n\
    2 - import; \n\
    3 - search.")
    ch = input ("print nomer: ")
    if ch == "1":
        date = export_date ()
        print_date (date)
    elif ch == "2":
        raz = choice_raz ()
        print_date (date)
    else:
        word = input ("print date for search: ")
        date = export_date ()
        item = search_date (word, date)
        if item != None:
            print ("Familia".center(15), "Imya".center(15), "Tel".center(15), "comment".center(20))
            print ("-" * 85)
            print (item[0].center(15), item[1].center(15), item[2].center(15), item[3].center(20))
        else:
            print ("date is not")