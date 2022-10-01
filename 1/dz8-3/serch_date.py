from read_date import read_date 
from print_date import print_date

def serch_date (word, date):
    if len (date) > 0:
        lst = []
        for item in date:
            if word in item:
                lst.append (item)
            if lst == []:
                return None
            else:
                return lst
    else:
        return None