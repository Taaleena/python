
def print_date (data):
    if len (date) > 0:
        print ("Familia".center(15), "Imya".center(15), "Tel".center(15), "comment".center(20))
        print ("-" * 85)
        for item in date:
            print (item[0].center(15), item[1].center(15), item[2].center(15), item[3].center(20))
    else:
        print ("nothing") 