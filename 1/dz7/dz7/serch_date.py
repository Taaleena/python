from export_date import export_date
from print_date import print_date

def serch_date (word, date):
    if len (date) > 0:
        for item in date:
            if word in item:
                return item
    else:
        return None