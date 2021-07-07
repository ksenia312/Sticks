from pygame.locals import *
from func import *

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    if count > 0:

        message('Количество палок: ' + str(count), (0, 0, 0))
        kol(count)
        k += 1
        if k == 1 and count // 3 == 0:

            message('Мой ход', (0, 150, 0))
            co += 1

            message('Беру' + str(count % 3), (0, 150, 0))
            comp(count % 3, co)
            count = count - count % 3
            kol(count)

        else:
            message('Ваш ход', (0, 0, 150))
            a = int(input())
            igr += 1
            message('Вы взяли ' + str(a), (0, 0, 150))
            if a >= 2 and count == 1:
                k -= 1
                igr -= 1
                print('сейчас вы можете ввести только 1')
                message('сейчас вы можете ввести только 1', (0, 0, 150))
            elif a == 1 or a == 2:
                count -= a
                igrok(a, igr)
                kol(count)

                if count <= 0:
                    message('Вы выиграли!', (0, 0, 150))
                    continue

                message('Мой ход', (0, 150, 0))
                co += 1
                if count == 1 or count == 2:

                    message('Беру ' + str(count), (0, 150, 0))
                    count = 0
                    kol(count)

                    message('Я выиграл!', (0, 150, 0))
                    continue
                elif a == 1:

                    message('Беру ' + str(2), (0, 150, 0))
                    count -= 2
                    kol(count)
                    comp(2, co)
                else:

                    message('Беру ' + str(1), (0, 150, 0))
                    count -= 1
                    kol(count)
                    comp(1, co)

                if count <= 0:
                    message('Я выиграл!', (0, 150, 0))
            else:
                k -= 1
                igr -= 1
                print('введите целое число от 1 до 2')
                message('Введите целое число от 1 до 2', (0, 0, 150))