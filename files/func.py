import pygame

screen = pygame.display.set_mode((1000, 800))
clock = pygame.time.Clock()


def print_text(font, text, color, coordinates):
    screen.blit(font.render(text, True, color), coordinates)


def make_font(size):
    return pygame.font.Font(None, size)


def start():
    pygame.display.set_caption('Игра в палки')
    pygame.init()
    pygame.font.init()
    screen.fill(pygame.Color('white'))

    f1, f2 = make_font(40), make_font(36)

    print_text(f1, 'Играем в игру', (180, 0, 0), (10, 50))
    print_text(f2, 'Есть суммарное количество палок. Вы и компьютер по очереди убираете', (0, 0, 0), (10, 90))
    print_text(f2, 'от 1 до 2-х палок. Тот, кто сделает последний ход, выиграет.', (0, 0, 0), (10, 120))
    print_text(f2, 'Введите количество палок.', (0, 0, 0), (10, 150))
    pygame.display.update()

    co, igr, k = 0, 0, 0

    count = int(input('Количество палок: '))

    print_text(f1, 'Компьютер', (0, 0, 0), (200, 200))
    print_text(f1, 'Игрок', (0, 0, 0), (600, 200))
    d = 'Изначально: ' + str(count)
    print_text(f1, d, (180, 0, 0), (550, 30))
    print_text(f2, 'Строка сообщений: ', (0, 0, 0), (10, 700))

    pygame.display.update()

    return co, igr, f1, f2, d, k, count


co, igr, f1, f2, d, k, count = start()


def kol(count):
    clock.tick(1)
    d = 'Сейчас: ' + str(count)
    pygame.draw.rect(
        screen,
        pygame.Color('white'),
        pygame.Rect(800, 30, 900, 50)
    )
    screen.blit(f1.render(d, True, (180, 0, 0)), (800, 30))
    pygame.display.update()


def comp(col, num):
    screen.blit(f2.render(str(col), True, (0, 0, 0)), (250, 200 + 50 * num))
    pygame.display.update()


def igrok(col, num):
    screen.blit(f2.render(str(col), True, (0, 0, 0)), (630, 200 + 50 * num))
    pygame.display.update()


def message(text, color):
    clock.tick(1)
    pygame.draw.rect(
        screen,
        pygame.Color('white'),
        pygame.Rect(260, 700, 460, 900)
    )
    screen.blit(f2.render(text, True, color), (260, 700))
    pygame.display.update()
