from datetime import datetime as dt
from prav import dict_log


def get_log (res, oper):
    dtime = dt.now ()
    with open ('result.txt', 'a', encoding='utf-8') as file:
        file.write ('{}; операция: {}; результат: {}\n'
                     .format (dtime, oper, res))