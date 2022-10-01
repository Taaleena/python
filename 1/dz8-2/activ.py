from read_date import read_date

def activ ():
    if not (len (read_date ()) > 0):

        with open ('students.csv', 'a+') as file:
            file.write ('ID; Imya; Familia; Klass; Status \n')

        with open ('kabinet.csv', 'a+') as file:
            file.write ('ID; Ryad; Parta \n')