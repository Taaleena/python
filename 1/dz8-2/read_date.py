def read_date ():
    lst_stud = []
    with open ('students.csv', 'r') as file:
        for line in file:
            temp = line.strip ().split (';')
            lst_stud.append (temp)
        print (lst_stud)
    
    lst_kab = []
    with open ('kabinet.csv', 'r') as file:
        for line in file:
            temp = line.strip ().split (';')
            lst_kab.append (temp)
        print (lst_kab)

    lst = []
    for i in range (len (lst_stud)):
        lst.append ([lst_stud[i][0], lst_stud [i][1], lst_stud[i][2], lst_stud[i][3], lst_stud[i][4], \
            lst_kab [i][0], lst_kab [i][0]])
    return lst