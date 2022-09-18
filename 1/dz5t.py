
#1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

#my_text = 'Напишите поларабв напиабв програбвмму двоцнойз программу, лдазхыабвзцрп удаляющую из \
#    этого абв текста все вабвс слова жызпьваывпабвжзрнт, содерабващие содержащие "абв"'

#def del_some_words(my_text):
#    my_text = list(filter(lambda x: 'абв' not in x, my_text.split()))
#    return " ".join(my_text)

#my_text = del_some_words(my_text)
#print()
#print(my_text)
#print()

#3. Создайте программу для игры в ""Крестики-нолики"".


#board = list(range(1,10))

#def draw_board(board):
#    print ("-" * 13)
#    for i in range(3):
#        print ("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
#        print ("-" * 13)

#def take_input(player_token):
#    valid = False
#    while not valid:
#        player_answer = input("Куда ставим " + player_token+"? ")
#        try:
#            player_answer = int(player_answer)
#        except:
#            print ("Некорректный ввод")
#            continue
#        if player_answer >= 1 and player_answer <= 9:
#            if (str(board[player_answer-1]) not in "XO"):
#                board[player_answer-1] = player_token
#                valid = True
#            else:
#                print ("Тут нет места")
#        else:
#            print ("Некорректный ввод.")

#def check_win(board):
#    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
#    for each in win_coord:
#        if board[each[0]] == board[each[1]] == board[each[2]]:
#            return board[each[0]]
#    return False

#def main(board):
#    counter = 0
#    win = False
#    while not win:
#        draw_board(board)
#        if counter % 2 == 0:
#            take_input("X")
#        else:
#            take_input("O")
#        counter += 1
#        if counter > 4:
#            tmp = check_win(board)
#            if tmp:
#                print (tmp, "выиграл!")
#                win = True
#                break
#        if counter == 9:
#            print ("Ничья!")
#            break
#    draw_board(board)

#main(board)

#4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def write_file(name,st):
    with open(name, 'w') as data:
        data.write(st)

def coding(txt):
    count = 1
    res = ''
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]:
            count += 1
        else:
            res = res + str(count) + txt[i]
            count = 1
    if count > 1 or (txt[len(txt)-2] != txt[-1]):
        res = res + str(count) + txt[-1]
    return res


def decoding(txt):
    number = ''
    res = ''
    for i in range(len(txt)):
        if not txt[i].isalpha():
            number += txt[i]
        else:
            res = res + txt[i] * int(number)
            number = ''
    return res



print()
s = input("Введите текст для кодировки: ")
print()
write_file("file_1.txt", s)
write_file("file_2.txt", coding(s))
print()
print(f"Текст после кодировки: {coding(s)}")
print()
print(f"Текст после дешифровки: {decoding(coding(s))}")
print() 

