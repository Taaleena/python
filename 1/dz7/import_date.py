
def import_date (date, raz = None):
    with open ("phone. csv", "a+") as file:
        if raz == None:
            for i in date:
                file.write (f"{i}\n")
            file.write (f"\n")
        else:
            file.write (raz.join(date))
            file.write (f"\n")