#1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

#list = [5, 2, 7, 9, 1]
#print(sum(list[1::2]))



#2.  Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.


#list = [3, 4, 5, 6]
#result_list = []
#for i in range((len(list)+1)//2):
#    result_list.append(list[i]*list[len(list)-1-i])
#print()
#print(result_list)
#print()




#3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.


#list = [1.1, 2.2, 3.4, 4, 5.8]
#min = 1
#max = 0
#for i in list:
#    if (i - int(i)) <= min:
#        min = i - int(i)
#    if (i - int(i)) >= max:
#        max = i - int(i)  
#print()
#print(max-min)
#print()




#4. Напишите программу, которая будет преобразовывать десятичное число в двоичное

#s = ""
#n = 9
#while n != 0:
#    s = str(n%2) + s
#    n //=2
#print()
#print(s)
#print()



#5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

#n = 5

#def get_fibonacci(n):
#    fibo_nums = []
#    a, b = 1, 1
#    for i in range(n-1):
#        fibo_nums.append(a)
#        a, b = b, a + b
#    a, b = 0, 1
#    for i in range (n):
#        fibo_nums.insert(0, a)
#        a, b = b, a - b
#    return fibo_nums

#fibo_nums = get_fibonacci(n)
#print()
#print(get_fibonacci(n))
#print()
#print(fibo_nums.index(0))
#print()
