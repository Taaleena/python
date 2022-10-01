import pandas as pd

print ()
kab_date = {
    'ID': ['0', '1', '2', '3', '4', '5'],
    'Ryad': ['uchitel', '1', '2', '3', '4', '5'],
    'Parta': ['0', '2', '1', '3', '1', '2'],
}

kd = pd.DateFrame (date = kab_date)

with open ('kabinet.csv', 'a') as cl:
    cl.write (f'{kd}')
    cl.write ('\n')

print (kd)