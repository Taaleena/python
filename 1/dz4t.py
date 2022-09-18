
#1. Вычислить число c заданной точностью d

#a = 3
#b = 11
#num = a/b
#print()
#print(round (num,9))
#print()


#2.Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

#num = int(input("Введите число: "))
#i = 2 
#lst = []
#chi = num
#while i <= num:
#    if num % i == 0:
#        lst.append(i)
#        num //= i
#        i = 2
#    else:
#        i += 1
#print(f"Простые множители числа {chi} приведены в списке: {lst}")

#3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

#list = [4, 5, 9 ,12, 4, 6, 6, 12, 21]
#print()
#print(f"Исходный список: {list}")
#print()
#new_list = []
#[new_list.append(i) for i in list if i not in new_list]
#print()
#print(f"неповторяющиеся элементы: {new_list}")
#print()

#4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

#from calendar import c
#import os
#os.system("cls")
#from random import randint
#import itertools

#k = int(input('Задайте натуральную степень k: '))

#list = list([randint(0, 101) for i in range(k+1)]) 
#if list[0] == 0: 
#    list[0] = randint(1, 101)
#print(list)

#def get_polynomial(k, list): 
#    str1 = ['*x**']*(k-1) + ['*x']
#    polynomial = [[a, b, c] for a, b, c  in itertools.zip_longest(list, str1, range(k, 1, -1), fillvalue = '') if a !=0]
#    print(polynomial)
#    for x in polynomial:
#        x.append(' + ') 
#    polynomial = list2(itertools.chain(*polynomial)) 
#    print(polynomial)
#    polynomial[-1] = ' = 0' 
#    return "".join(map(str, polynomial)).replace(' 1*x',' x') 

#list2 = get_polynomial(k, list)
#print(list2)

#with open('33_Polynomial.txt', 'w') as data:
#    data.write(list2)
#with open('33_Polynomial2.txt', 'w') as data:
#    data.write(list2)
	
#5. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.


import random


def write_file(name,st):
    with open(name, 'w') as data:
        data.write(st)

def rnd():
    return random.randint(0,101)

def create_mn(k):
    lst = [rnd() for i in range(k+1)]
    return lst
    
def create_str(sp):
    lst= sp[::-1]
    wr = ''
    if len(lst) < 1:
        wr = 'x = 0'
    else:
        for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
                wr += f'{lst[i]}x^{len(lst)-i-1}'
                if lst[i+1] != 0 or lst[i+2] != 0:
                    wr += ' + '
            elif i == len(lst) - 2 and lst[i] != 0:
                wr += f'{lst[i]}x'
                if lst[i+1] != 0 or lst[i+2] != 0:
                    wr += ' + '
            elif i == len(lst) - 1 and lst[i] != 0:
                wr += f'{lst[i]} = 0'
            elif i == len(lst) - 1 and lst[i] == 0:
                wr += ' = 0'
    return wr


def sq_mn(k):
    if 'x^' in k:
        i = k.find('^')
        num = int(k[i+1:])
    elif ('x' in k) and ('^' not in k):
        num = 1
    else:
        num = -1
    return num


def k_mn(k):
    if 'x' in k:
        i = k.find('x')
        num = int(k[:i])
    return num


def calc_mn(st):
    st = st[0].replace(' ', '').split('=')
    st = st[0].split('+')
    lst = []
    l = len(st)
    k = 0
    if sq_mn(st[-1]) == -1:
        lst.append(int(st[-1]))
        l -= 1
        k = 1
    i = 1 
    ii = l-1 
    while ii >= 0:
        if sq_mn(st[ii]) != -1 and sq_mn(st[ii]) == i:
            lst.append(k_mn(st[ii]))
            ii -= 1
            i += 1
        else:
            lst.append(0)
            i += 1
        
    return lst
    



print()
k1 = int(input("Введите натуральную степень для первого файла k = "))
print()
k2 = int(input("Введите натуральную степень для второго файла k = "))
print()
koef1 = create_mn(k1)
koef2 = create_mn(k2)
write_file("file34_1.txt", create_str(koef1))
write_file("file34_2.txt", create_str(koef2))



with open('file34_1.txt', 'r') as data:
    st1 = data.readlines()
with open('file34_2.txt', 'r') as data:
    st2 = data.readlines()
print()
print(f"Первый многочлен {st1}")
print()
print(f"Второй многочлен {st2}")
print()
lst1 = calc_mn(st1)
lst2 = calc_mn(st2)
ll = len(lst1)
if len(lst1) > len(lst2):
    ll = len(lst2)
lst_new = [lst1[i] + lst2[i] for i in range(ll)]
if len(lst1) > len(lst2):
    mm = len(lst1)
    for i in range(ll,mm):
        lst_new.append(lst1[i])
else:
    mm = len(lst2)
    for i in range(ll,mm):
        lst_new.append(lst2[i])
write_file("file34_res.txt", create_str(lst_new))
with open('file34_res.txt', 'r') as data:
    st3 = data.readlines()
print()
print(f"Итоговый многочлен {st3}")
print()