from export_date import export_date
from write_date import write_date

def export_date2 ():
    lisst = export_date ()

    write_date ([lisst.get ('ID'), lisst.get ('Imya'), lisst.get ('Familia'), lisst.get ('Klass'), lisst.get ('Status')], 'students.csv')

    write_date ([lisst ('ID'), lisst ('Ryad'), lisst ('Parta')], 'kabinet.csv')
