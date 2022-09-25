from print_date import print_date
from export_data import export_data

def search_date (word, date):
    if (len (date) > 0):
        for item in date:
            if word in item:
                return item
    else:
        return None