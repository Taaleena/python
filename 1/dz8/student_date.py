import pandas as pd

print ()
stud_date = {
    'ID': ['0', '1', '2', '3', '4', '5'],
    'Imya': ['', 'Mariya', 'Viktor', 'Dmitriy', 'Anna', 'Viktoria'],
    'Familia': ['', 'Vaseva', 'Hvorih', 'Losev', 'Lish', 'Letova'],
    'Klass': ['', '9', '10', '8', '10', '9a'],
    'Status': ['', 'hor', 'hor', 'udl', 'otl', 'hor']
}

sd = pd.DateFrame (date = stud_date)

with open ('studens.csv', 'a') as cl:
    cl.write (f'{sd}')
    cl.write ('\n')

print (sd)