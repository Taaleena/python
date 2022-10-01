from write_date import count_date

def export_date ():
    lisst = dict ()
    ID = count_date ('students.csv')
    lisst ['id'] = ID
    lisst ['Imya'] = input ("enter imya: ")
    lisst ['Familia'] = input ("enter familia: ")
    lisst ['Klass'] = input ("enter klass: ")
    lisst ['Status'] = input ("enter status: ")
    lisst ['Ryad'] = input ("enter ryad: ")
    lisst ['Parta'] = input ("enter parta: ")

    return lisst

