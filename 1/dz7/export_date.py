
def export_date ():
    with open ("phone.csv", "r") as file:
        date = []
        p = []
        for line in file:
            if "," in line:
                temp = line.strip ().split (",")
                date.append (temp)
            elif ";" in line:
                temp = line.strip ().split (";")
                date.append (temp)
            elif line != " ":
                if line != "\n":
                    p.append (line.strip ())
                else: 
                    date.append (p)
                    p = []
    return date
