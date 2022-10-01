def print_date (date, search = False):
    if len (date) > 0:
        print ('ID'.center (5), 'Imya'.center (20), 'Familia'.center (20), 'Klass'.center (5), 'Status'.center (10), \
            'Ryad'.center (5), 'Parta'.center (5))
        print ()

        if not search:
            del date [0]
        for item in date:
            print (item [0].center (5), item [1].center (5), item [2].center (5), item [3].center (5), item [4].center (5), \
                item [4].center (5), item [6].center (5))
    else:
        print ('pusto')