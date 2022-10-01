def write_date (date, name):
    with open (name, 'a+') as file:
        file.write (''.join (map (str, date)))
        file.write (f'\n')

def count_date (name):
    with open (name, 'r') as file:
        date = file.read ()
    return date.count ('\n')