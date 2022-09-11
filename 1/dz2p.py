
#1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

#float_num = input('input float number: ')
#sum = 0
#for i in float_num:
#    if i != '.':
#        sum += int(i)
#print(sum)


#2.  Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

#n = 5
#factorial = 1
#print()
#for i in range(1, n+1):
#    factorial *= i
#    print(factorial, end=' ')
	
	
#3. Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

#n = int(input('Give me number: ')) 

#print()
#def sequence(n):

#   return[round((1 + 1 / x)**x, 2) for x in range (1, n + 1)]   
        
#print(sequence(n))
#print()
#print(round(sum(sequence(n))))
#print()

#4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

#from random import randint

#with open('333.txt', 'w') as data:
#    data.write('0\n')
#    data.write('2\n')
#    data.write('3\n')
#    data.write('7\n')
#    data.write('6\n')

#def get_numbers(n):
#    return [randint(-n/2, n) for i in range(-n, n + 1)]
#
#def get_data_from_file(path):
#    data = open(path, 'r')
#    dlist = [int(line.strip()) for line in data]
#    data.close()
#    return dlist
#
#def get_mult(numbers, datalist):
#    mult = 1
#    for i in datalist:
#        mult *= numbers[i]
#    return mult

#path = '333.txt'
#n = 10 
#datalist = get_data_from_file(path)
#numbers = get_numbers(n)
#print()
#print(numbers)
#print()
#print(datalist)
#print()
#print(get_mult(numbers, datalist))
#print()

#5. Реализуйте алгоритм перемешивания списка

#list = ['Mrak', 6.616, 2546, 'moon']
#print()
#print(list) 
#import random
#random.shuffle(list)
#print()
#print('result', list) 
#print()