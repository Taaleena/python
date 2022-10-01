import kabinet_date as kab
import student_date as stu

def option ():
    print ("Privet")
    ch = int (input ("chto nado? \n\
        1: Poisk ID po familii \n\
        2: Klass i mesto uchenika \n\
        3: Nichego \n\
        ?: "))
    if ch == 1:
        ser = str (input ("familia?: "))
        if ser in stu.stud_date ['Familia']:
            index = stu.stud_date ['Familia'].index (ser)
            print (f'{stu.stud_date ['ID'][index]}, {stu.stud_date ['Imya'][index]}, {stu.stud_date ['Familia'][index]}, {stu.stud_date ['Klass'][index]}, {stu.stud_date ['Status'][index]}')
            print ('\n Chto-to escho? Y or No:')
            num = input ()
            if num == 'y':
                option ()
            exit ()
    elif ch == 2:
        cla = input ("ID student: ")
        if cla in kab.kab_date ['ID']:
            index = kab.kab_date ['ID'].index (cla)
            print (f'{kab.kab_date ['Ryad'][index]}, {kab.kab_date ['Parta'][index]}')
            print ('\n Chto-to escho? Y or No:')
            num = input ()
            if num == 'y':
                option ()
            exit ()
    else:
        print ("Povtorite")
    exit ()    

option ()


