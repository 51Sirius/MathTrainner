import os
import pygame as pg
import random as rand
import webbrowser as web
import pyperclip
import time
import sys

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"


def shifr(shifr):
    "Unshifr code"
    return result


def unshifr(shifr):
    "Shifering code"
    return result


def rand_num(numb):
    "add salt"
    return result


def rand_shifr(sett):
    result = ''
    vi = rand.randint(1, 2)
    if vi == 1:
        for i in range(len(sett)):
            amount = rand.randint(10, 200)
            for j in range(amount):
                result += rand_num(rand.randint(1, 50))
            result += unshifr(sett[i])
    else:
        for i in range(len(sett)):
            result += unshifr(sett[i])
            amount = rand.randint(10, 200)
            for h in range(amount):
                result += rand_num(rand.randint(1, 50))
    return result


def input_settings():
    setup_file = open('bd/sett.dat', 'r')
    size_display = int(shifr(setup_file.readline()))
    score = shifr(setup_file.readline())
    theme = int(shifr(setup_file.readline()))
    ex_1 = int(shifr(setup_file.readline()))
    ex_2 = int(shifr(setup_file.readline()))
    rec = int(shifr(setup_file.readline()))
    setup_file.close()
    return size_display, score, theme, ex_1, ex_2, rec


def output_settings():
    setup_file = open('bd/sett.dat', 'w')
    setup_file.write(rand_shifr(str(SIZE)) + '\n')
    setup_file.write(rand_shifr(str(SCORE)) + '\n')
    setup_file.write(rand_shifr(str(THEME)) + '\n')
    setup_file.write(rand_shifr(str(EX_1)) + '\n')
    setup_file.write(rand_shifr(str(EX_2)) + '\n')
    setup_file.write(rand_shifr(str(RECORD)) + '\n')
    setup_file.close()
    lg = open('bd/lg.dat', 'w')
    lg.write(str(LANG))
    lg.close
    sys.exit()


def size_upload(size):
    if size == 1:
        SIZE = (800, 600)
    elif size == 2:
        SIZE = (1000, 700)
    elif size == 3:
        SIZE = (1200, 900)
    return SIZE


def theme_upload(theme):
    if theme == 1:
        COLOR_DISPLAY = (28, 8, 161)
        COLOR_BUTTON_1 = (255, 210, 0)
        MAIN_COLOR_FONT = (199, 24, 24)
        COLOR_BUTTON_2 = (166, 136, 0)
        COLOR_BUTTON_SETUP_1 = (92, 92, 91)
        COLOR_BUTTON_SETUP_2 = (66, 66, 66)
        COLOR_EXIT_DRAW_1 = (66, 66, 66)
        COLOR_EXIT_DRAW_2 = (105, 105, 105)
        COLOR_VERSION_SCORE = (12, 247, 236)
        ACTIVE_COLOR = (0, 51, 255)
        ANTI_VERSION_SCORE_COLOR = (255, 255, 255)
        COLOR_SETUP_MENU_1 = (71, 60, 60)
        COLOR_ENTRY_TEXT = (21, 17, 36)
        MAIN_FONT_COLOR_MENU_1 = (0, 0, 0)
        FIRST_FIGURA = (255, 0, 0)
        SECOND_FIGURE = (0, 255, 0)
        THRE_FIGURE = (0, 0, 255)
    elif theme == 2:
        COLOR_DISPLAY = (50, 50, 50)
        COLOR_BUTTON_1 = (92, 92, 91)
        MAIN_COLOR_FONT = (199, 24, 24)
        COLOR_BUTTON_2 = (66, 66, 66)
        COLOR_BUTTON_SETUP_1 = (92, 92, 91)
        COLOR_BUTTON_SETUP_2 = (66, 66, 66)
        COLOR_EXIT_DRAW_1 = (66, 66, 66)
        COLOR_EXIT_DRAW_2 = (105, 105, 105)
        COLOR_VERSION_SCORE = (12, 247, 236)
        ACTIVE_COLOR = (0, 51, 255)
        ANTI_VERSION_SCORE_COLOR = (255, 255, 255)
        COLOR_SETUP_MENU_1 = (71, 60, 60)
        COLOR_ENTRY_TEXT = (21, 17, 36)
        MAIN_FONT_COLOR_MENU_1 = (0, 0, 0)
        FIRST_FIGURA = (50, 50, 50)
        SECOND_FIGURE = (50, 50, 50)
        THRE_FIGURE = (50, 50, 50)
    elif theme == 3:
        COLOR_DISPLAY = (232, 232, 232)
        COLOR_BUTTON_1 = (141, 145, 214)
        MAIN_COLOR_FONT = (199, 24, 24)
        COLOR_BUTTON_2 = (66, 66, 66)
        COLOR_BUTTON_SETUP_1 = (141, 145, 214)
        COLOR_BUTTON_SETUP_2 = (66, 66, 66)
        COLOR_EXIT_DRAW_1 = (66, 66, 66)
        COLOR_EXIT_DRAW_2 = (105, 105, 105)
        COLOR_VERSION_SCORE = (12, 247, 236)
        ACTIVE_COLOR = (0, 51, 255)
        ANTI_VERSION_SCORE_COLOR = (29, 30, 41)
        COLOR_SETUP_MENU_1 = (71, 60, 60)
        COLOR_ENTRY_TEXT = (21, 17, 36)
        MAIN_FONT_COLOR_MENU_1 = (0, 0, 0)
        FIRST_FIGURA = (232, 232, 232)
        SECOND_FIGURE = (232, 232, 232)
        THRE_FIGURE = (232, 232, 232)
    return COLOR_DISPLAY, COLOR_BUTTON_1, MAIN_COLOR_FONT, COLOR_BUTTON_2, COLOR_BUTTON_SETUP_1, COLOR_BUTTON_SETUP_2, \
           COLOR_EXIT_DRAW_1, COLOR_EXIT_DRAW_2, COLOR_VERSION_SCORE, ACTIVE_COLOR, ANTI_VERSION_SCORE_COLOR, COLOR_SETUP_MENU_1, \
           COLOR_ENTRY_TEXT, COLOR_SETUP_MENU_1, MAIN_FONT_COLOR_MENU_1, FIRST_FIGURA, SECOND_FIGURE, THRE_FIGURE


SIZE, SCORE, THEME, EX_1, EX_2, RECORD = input_settings()
SCORE = int(SCORE)
COLOR_DISPLAY, COLOR_BUTTON_1, MAIN_COLOR_FONT, COLOR_BUTTON_2, COLOR_BUTTON_SETUP_1, COLOR_BUTTON_SETUP_2, \
COLOR_EXIT_DRAW_1, COLOR_EXIT_DRAW_2, COLOR_VERSION_SCORE, ACTIVE_COLOR, ANTI_VERSION_SCORE_COLOR, COLOR_SETUP_MENU_1, \
COLOR_ENTRY_TEXT, COLOR_SETUP_MENU_1, MAIN_FONT_COLOR_MENU_1, FIRST_FIGURE_COLOR, SECOND_FIGURE_COLOR, THRE_FIGURE_COLOR = theme_upload(
    THEME)
__SIZE = size_upload(SIZE)
BLACK_COLOR = (0, 0, 0)
WHITE_COLOR = (255, 255, 255)
display = pg.display.set_mode(__SIZE)
pg.init()
pg.display.set_caption('Math Trainer')
icon = pg.image.load('image\main_icon.png')
pg.display.set_icon(icon)
lg = open('bd/lg.dat', 'r')
LANG = int(lg.readline())
lg.close()
Exit = False


class New_button:
    def __init__(self, x, y, weight, height, message=None, font_color=(0, 0, 0), font_size=30,
                 font_type='/shrift/play_manu.otf', active_color=None,
                 actived_color=None, message_x=None, message_y=None, second_color=None,
                 sukam=4):
        self.x = x
        self.y = y
        self.weight = weight
        self.height = height
        self.ms_x = message_x
        self.ms_y = message_y
        self.font_color = font_color
        self.message = message
        self.active_color = active_color
        self.sukam = sukam
        self.font_type = font_type
        self.action = False
        self.actived_color = MAIN_COLOR_FONT
        self.font_size = font_size

    def draw(self, color, second_color):
        self.color = color
        self.second_color = second_color
        if pg.mouse.get_pressed()[0] == 1:
            pg.time.wait(50)
        mouse = pg.mouse.get_pos()
        click = pg.mouse.get_pressed()
        if self.x < mouse[0] < self.x + self.weight and self.y < mouse[1] < self.y + self.height:
            if click[0] == 1 and self.x < mouse[0] < self.x + self.weight and self.y < mouse[1] < self.y + self.height:
                if self.sukam <= 6:
                    rect_2 = (self.x, self.y, self.weight, self.height)
                    rect_1 = (self.x - self.sukam, self.y - self.sukam, self.weight + self.sukam * 2,
                              self.height + self.sukam * 2)
                    ellipse_1 = pg.draw.rect(display, self.second_color, rect_1)
                    el = pg.draw.rect(display, self.color, rect_2)
                    text_but = Font(self.ms_x, self.ms_y, self.actived_color, self.font_size,
                                    message=self.message)
                    text_but.draw_text()
                    self.sukam += 2
                else:
                    rect_1 = (self.x - self.sukam, self.y - self.sukam, self.weight + self.sukam * 2,
                              self.height + self.sukam * 2)
                    rect_2 = (self.x, self.y, self.weight, self.height)
                    el = pg.draw.rect(display, self.second_color, rect_1)
                    ellipse_2 = pg.draw.rect(display, self.color, rect_2)
                    text_but = Font(self.ms_x, self.ms_y, self.actived_color, self.font_size,
                                    message=self.message)
                    text_but.draw_text()
                self.action = True
            else:
                if self.sukam <= 6:
                    rect_1 = (self.x - self.sukam, self.y - self.sukam, self.weight + self.sukam * 2,
                              self.height + self.sukam * 2)
                    rect_2 = (self.x, self.y, self.weight, self.height)
                    ellipse_2 = pg.draw.rect(display, self.color, rect_2)
                    text_but = Font(self.ms_x, self.ms_y, self.active_color, self.font_size,
                                    message=self.message)
                    text_but.draw_text()
                    self.sukam += 4
                else:
                    rect_2 = (self.x, self.y, self.weight, self.height)
                    rect_1 = (self.x - self.sukam, self.y - self.sukam, self.weight + self.sukam * 2,
                              self.height + self.sukam * 2)
                    el = pg.draw.rect(display, self.second_color, rect_1)
                    ellipse_2 = pg.draw.rect(display, self.color, rect_2)

                    text_but = Font(self.ms_x, self.ms_y, self.active_color, self.font_size,
                                    message=self.message)

                    text_but.draw_text()
                self.action = False
        else:
            rect_1 = (self.x, self.y, self.weight, self.height)
            ellipse_1 = pg.draw.rect(display, self.color, rect_1)
            text_but = Font(self.ms_x, self.ms_y, self.font_color, self.font_size, message=self.message)
            text_but.draw_text()
            self.action = False
        return self.action


def main_menu_rus():
    show_menu = True
    while show_menu:
        event = pg.event.poll()
        if event.type == pg.QUIT:
            output_settings()
        display.fill(COLOR_DISPLAY)
        x_main_text = int(__SIZE[0] / 2 - int((170 / 800) * __SIZE[0]))
        font = int(__SIZE[1] / (600 / 30))
        main_text_1 = Font(x_main_text, int(__SIZE[1] / 24), MAIN_COLOR_FONT, message='Математический', font_size=font)
        main_text_2 = Font(int(__SIZE[0] / 2 - int((100 / 800) * __SIZE[0])),
                           int(__SIZE[1] / 24) + int(__SIZE[1] / (600 / 30)), MAIN_COLOR_FONT, message='треннажер',
                           font_size=font)
        version_text = Font(int(__SIZE[0] - 234), int(__SIZE[1] / 1.03), COLOR_VERSION_SCORE,
                            message='Бета версия: 0.0.5', \
                            font_size=20)
        button_play = Button(int(__SIZE[0] / 2 - (__SIZE[0] / 8)), int(__SIZE[1] / 6.4), int(__SIZE[0] / 4),
                             int(__SIZE[1] / 12), COLOR_BUTTON_1, 'Играть',
                             font_type='/shrift/play_menu.otf', active_color=ACTIVE_COLOR,
                             actived_color=MAIN_COLOR_FONT,
                             font_size=int(__SIZE[1] / 24),
                             message_x=int(__SIZE[0] / 2 - (50 / 800) * __SIZE[0]),
                             message_y=int(__SIZE[1] / 6.4 + int(__SIZE[1] / (80 / 1.2))), second_color=COLOR_BUTTON_2)
        button_level = Button(int(__SIZE[0] / 2 - (__SIZE[0] / 8)), int(__SIZE[1] / 3.55555556), int(__SIZE[0] / 4),
                              int(__SIZE[1] / 12),
                              COLOR_BUTTON_1, 'Уровни', font_size=int(__SIZE[1] / 24),
                              font_type='/shrift/play_menu.otf', active_color=ACTIVE_COLOR,
                              actived_color=MAIN_COLOR_FONT,
                              message_x=int(__SIZE[0] / 2 - (50 / 800) * __SIZE[0]),
                              message_y=int(__SIZE[1] / 3.5555555556 + int(__SIZE[1] / (80 / 1.2))),
                              second_color=COLOR_BUTTON_2)
        button_achivment = Button(int(__SIZE[0] / 2 - (__SIZE[0] / 8)), int(__SIZE[1] / (800 / 325)),
                                  int(__SIZE[0] / 4), int(__SIZE[1] / 12),
                                  COLOR_BUTTON_1, 'Достижения', font_size=int(__SIZE[1] / 32),
                                  font_type='/shrift/play_menu.otf', active_color=ACTIVE_COLOR,
                                  actived_color=MAIN_COLOR_FONT,
                                  message_x=int(__SIZE[0] / 2 - (68 / 800) * __SIZE[0]),
                                  message_y=int(__SIZE[1] / (800 / 325) + int(__SIZE[1] / (80 / 1.2))),
                                  second_color=COLOR_BUTTON_2)
        button_anygames = Button(int(__SIZE[0] / 2 - (__SIZE[0] / 8)), int(__SIZE[1] / (800 / 425)), int(__SIZE[0] / 4),
                                 int(__SIZE[1] / 12), COLOR_BUTTON_1,
                                 'Другое', font_size=int(__SIZE[1] / 28),
                                 font_type='/shrift/play_menu.otf', active_color=ACTIVE_COLOR,
                                 actived_color=MAIN_COLOR_FONT,
                                 message_x=int(__SIZE[0] / 2 - (44 / 800) * __SIZE[0]),
                                 message_y=int(__SIZE[1] / (800 / 425) + int(__SIZE[1] / (80 / 1.2))),
                                 second_color=COLOR_BUTTON_2)
        button_help = Button(0, 0, int(__SIZE[0] / (800 / 75)), int(__SIZE[1] / (600 / 75)), COLOR_BUTTON_SETUP_1, 'П',
                             BLACK_COLOR,
                             font_type='shrift/play_menu.otf', active_color=MAIN_COLOR_FONT,
                             actived_color=COLOR_BUTTON_2,
                             message_x=int(__SIZE[0] / (800 / 75) / 2 - int((24 / 800) * __SIZE[0])),
                             message_y=int(__SIZE[1] / 0.8 / 80), second_color=COLOR_BUTTON_SETUP_2,
                             font_size=int(__SIZE[1] / 10))
        button_setup = Button(int(__SIZE[0] / (800 / 725)), 0, int(__SIZE[0] / (800 / 75)), int(__SIZE[1] / (600 / 75)),
                              COLOR_BUTTON_SETUP_1,
                              message='Н', font_color=BLACK_COLOR, font_type='shrift/play_menu.otf',
                              active_color=MAIN_COLOR_FONT,
                              actived_color=COLOR_BUTTON_2,
                              message_x=int(__SIZE[0] - (__SIZE[0] / (800 / 75) / 2) - int((1 / 33) * __SIZE[0])),
                              message_y=int(__SIZE[1] / 0.8 / 80),
                              second_color=COLOR_BUTTON_SETUP_2, font_size=int(__SIZE[1] / 10))
        button_setup.draw()
        button_help.draw()
        button_achivment.draw()
        button_anygames.draw()
        button_level.draw()
        draw_triangle([0, __SIZE[1]], [int(__SIZE[0] / (800 / 200)), __SIZE[1]],
                      [int(__SIZE[0] / (800 / 100)), int(__SIZE[1] / (600 / 400))], 'k', color=FIRST_FIGURE_COLOR)
        draw_circle([int(__SIZE[0] / (800 / 100)), int(__SIZE[1] / (600 / 360))], int(__SIZE[0] / (800 / 50)),
                    THRE_FIGURE_COLOR)
        button_play.draw()
        version_text.draw_text()
        main_text_1.draw_text()
        main_text_2.draw_text()
        pg.display.update()
        if button_play.action:
            pg.time.wait(50)
            start_play_rus()
        elif button_setup.action:
            pg.time.wait(50)
            setup_menu_start_rus()
        elif button_level.action:
            pg.time.wait(50)
            start_level_rus()
        elif button_achivment.action:
            pg.time.wait(50)
            achivment_rus()
        elif button_help.action:
            pg.time.wait(50)
            help_rus()
        elif button_anygames.action:
            pg.time.wait(50)
            any_game_menu_rus()
        if Exit:
            show_menu = False


def help_rus():
    h = 0
    k = 0
    ready1 = True
    ready2 = True
    show_menu_help = True
    font_vk = Font(int(__SIZE[0] / (800 / 100)), int(__SIZE[1] / (600 / 225)), COLOR_VERSION_SCORE,
                   int(__SIZE[1] / (600 / 20)),
                   message='Нажмите сюда чтобы посетить наш Vk')
    font_ds = Font(int(__SIZE[0] / (800 / 100)), int(__SIZE[1] / (600 / 350)), COLOR_VERSION_SCORE,
                   int(__SIZE[1] / (600 / 20)),
                   message='Нажмите сюда чтобы посетить наш Discord')
    main_text_font = Font(int(__SIZE[0] / (800 / 330)), int(__SIZE[1] / (600 / 20)), MAIN_COLOR_FONT,
                          int(__SIZE[1] / (600 / 40)),
                          message='Помощь')
    while show_menu_help:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                output_settings()
            if event.type == pg.VIDEOEXPOSE:
                ready1 = False
                ready2 = False
            elif event.type != pg.VIDEOEXPOSE:
                ready1 = True
                ready2 = True
        display.fill(COLOR_DISPLAY)
        ready1 = draw_vk(int(__SIZE[0] / (800 / 628)), int(__SIZE[1] / (600 / 206)), int(__SIZE[0] / (800 / 50)),
                         int(__SIZE[0] / (800 / 50)), ready1)
        ready2 = draw_dis(int(__SIZE[0] / (800 / 695)), int(__SIZE[1] / (600 / 332)), int(__SIZE[0] / (800 / 50)),
                          int(__SIZE[0] / (800 / 50)), ready2)
        font_ds.draw_text()
        font_vk.draw_text()
        get_code_rus()
        main_text_font.draw_text()
        show_menu_help = draw_exit(show_menu_help)
        pg.display.update()
        pg.time.wait(150)


def achivment_rus():
    show_menu_achivment = True
    if SCORE >= 0 and SCORE < 500:
        rank = pg.image.load('image/iron.png')
        rank_name = 'железо'
    elif SCORE >= 500 and SCORE < 1000:
        rank = pg.image.load('image/bronze.png')
        rank_name = 'бронза'
    elif SCORE >= 1000 and SCORE < 2000:
        rank = pg.image.load('image/silver.png')
        rank_name = 'серебро'
    elif SCORE >= 2000 and SCORE < 3000:
        rank = pg.image.load('image/gold.png')
        rank_name = 'золото'
    elif SCORE >= 3000 and SCORE < 5000:
        rank = pg.image.load('image/platium.png')
        rank_name = 'платина'
    elif SCORE >= 5000 and SCORE < 10000:
        rank = pg.image.load('image/diamond.png')
        rank_name = 'алмаз'
    elif SCORE >= 10000 and SCORE < 20000:
        rank = pg.image.load('image/master.png')
        rank_name = 'мастер'
    elif SCORE >= 20000 and SCORE < 100000:
        rank = pg.image.load('image/gr_master.png')
        rank_name = 'гранд-мастер'
    elif SCORE >= 100000:
        rank = pg.image.load('image/legend.png')
        rank_name = 'Легенда'
    elif SCORE == 666:
        rank = pg.image.load('image/belaz.png')
    else:
        rank_name = 'новобранец'
    text_1 = Font(int(__SIZE[0] / (800 / 280)), int(__SIZE[1] / (600 / 400)), COLOR_VERSION_SCORE,
                  int(__SIZE[1] / (600 / 34)),
                  message=f'Ваш ранк - {rank_name}', font_type='shrift/math_prem.otf')
    text_2 = Font(int(__SIZE[0] / 2 - __SIZE[0] / (600 / 100)), int(__SIZE[1] / (600 / 440)), COLOR_VERSION_SCORE,
                  int(__SIZE[1] / (600 / 30)), message=f'Ваши счет - {SCORE}', font_type='shrift/math_prem.otf')
    while show_menu_achivment:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                output_settings()
        display.fill(COLOR_DISPLAY)
        rank_rect = rank.get_rect(center=(int(__SIZE[0] / 2), int(__SIZE[1] / 2 - __SIZE[1] / (600 / 100))))
        text_1.draw_text()
        text_2.draw_text()
        display.blit(rank, rank_rect)
        show_menu_achivment = draw_exit(show_menu_achivment)
        pg.display.update()


def start_play_rus():
    h = 0
    button_go = False
    global SCORE
    draw_ok = False
    draw_notok = False
    valid = True
    show_play = True
    need_input = False
    input_text = ''
    score = SCORE
    okey = True
    need_generaite = True
    button_answer = Button_rect(int(__SIZE[0] / (800 / 250)), int(__SIZE[1] / (800 / 650)),
                                int(__SIZE[0] / (800 / 300)),
                                int(__SIZE[1] / (800 / 60)), COLOR_BUTTON_1, 'Ответить', (0, 0, 0),
                                int(__SIZE[1] / (600 / 30)),
                                'shrift\math_prem1.ttf', (0, 0, 0), (0, 0, 0), int(__SIZE[0] / (800 / 330)),
                                int(__SIZE[1] / (800 / 660)), COLOR_BUTTON_2)
    examp = Example(__SIZE)
    while show_play:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                output_settings()
            if need_input and event.type == pg.KEYDOWN:
                if event.unicode == '1' or event.unicode == '2' or event.unicode == '3' or event.unicode == '4' or event.unicode == '5' \
                        or event.unicode == '6' or event.unicode == '7' or event.unicode == '8' or event.unicode == '9' or event.unicode == '0' \
                        or event.unicode == '.' or event.unicode == '-' or event.unicode == ',':
                    valid = True
                else:
                    valid = False
                if len(input_text) >= 20:
                    okey = False
                if event.key == pg.K_BACKSPACE:
                    input_text = input_text[0:-1]
                    okey = True
                    valid = True
                elif okey and valid:
                    if event.unicode == ',':
                        event.unicode = '.'
                    input_text += event.unicode
                if event.key == pg.K_RETURN and input_text != '':
                    valid = True
                    if examp.bool_pr(input_text):
                        examp.gen_ex()
                        input_text = ''
                        draw_ok = True
                        draw_time_ok = 1
                        SCORE += examp.score
                        score += examp.score
                        draw_notok = False
                    else:
                        draw_notok = True
                        draw_time_nok = 1
                    button_go = False
        if need_generaite:
            examp.gen_ex()
        error_1 = Font(int(__SIZE[0] / (800 / 560)), int(__SIZE[1] / (800 / 520)) + int(__SIZE[1] / (800 / 15)),
                       font_size=int(__SIZE[1] / (600 / 14)), font_color=(255, 0, 0), message='Ошибка: длинный ответ')
        error_2 = Font(int(__SIZE[0] / (800 / 560)), int(__SIZE[1] / (800 / 520)) + int(__SIZE[1] / (800 / 15)),
                       font_size=int(__SIZE[1] / (600 / 14)), font_color=(255, 0, 0),
                       message='Ошибка: Неверный формат данных')
        entry_otvet = Entry_text(ANTI_VERSION_SCORE_COLOR, ACTIVE_COLOR, COLOR_ENTRY_TEXT, input_text,
                                 int(__SIZE[1] / (600 / 24)),
                                 'shrift\\math_prem1.ttf', int(__SIZE[0] / (800 / 250)), int(__SIZE[1] / (800 / 500)),
                                 int(__SIZE[0] / (800 / 300)),
                                 int(__SIZE[1] / (800 / 60)), ACTIVE_COLOR, need_input, int(__SIZE[0] / (800 / 260)),
                                 int(__SIZE[1] / (800 / 500)) + int(__SIZE[1] / (800 / 15)))
        if input_text == '':
            entry_otvet.text = 'Ответ введите ответ сюда'
        display.fill(COLOR_DISPLAY)
        examp.draw()
        button_answer.draw()
        entry_otvet.draw()
        show_play = draw_exit(show_play)
        score_font = Font(int(__SIZE[0] - (len(str(score)) + 5) * 25), 20, COLOR_VERSION_SCORE,
                          int(__SIZE[1] / (600 / 28)), message=f'Очки: {score}')
        score_font.draw_text()
        if not okey:
            error_1.draw_text()
        if not valid:
            error_2.draw_text()
        if draw_ok and draw_time_ok <= 1000 and okey and valid:
            draw_okay(int(__SIZE[0] / (800 / 600)), int(__SIZE[1] / (800 / 520)) + int(__SIZE[1] / (800 / 15)),
                      int(__SIZE[0] / (800 / 40)))
            draw_time_ok += 1
        if draw_notok and draw_time_nok <= 1000 and okey and valid:
            draw_no_okay(int(__SIZE[0] / (800 / 600)), int(__SIZE[1] / (800 / 520)) + int(__SIZE[1] / (800 / 15)),
                         int(__SIZE[0] / (800 / 40)))
            draw_time_nok += 1
        pg.display.update()
        need_input = entry_otvet.need_input
        if button_answer.action:
            need_input = True
            if h == 2:
                if input_text != '':
                    valid = True
                    if examp.bool_pr(input_text):
                        examp.gen_ex()
                        input_text = ''
                        draw_ok = True
                        draw_time_ok = 1
                        SCORE += examp.score
                        score += examp.score
                        draw_notok = False
                    else:
                        draw_notok = True
                        draw_time_nok = 1
            else:
                h += 1
        need_generaite = False
        pg.time.wait(1)


def setup_menu_start_rus():
    global Exit
    button_display = Button_rect(int(__SIZE[0] / 2 - (__SIZE[0] / 4)), int(__SIZE[1] / (800 / 175)), int(__SIZE[0] / 2),
                                 int(__SIZE[1] / 12), COLOR_SETUP_MENU_1, 'Экран',
                                 font_type='/shrift/play_menu.otf', active_color=MAIN_COLOR_FONT,
                                 actived_color=MAIN_COLOR_FONT,
                                 font_size=int(__SIZE[1] / 24),
                                 message_x=int(__SIZE[0] / 2 - (50 / 800) * __SIZE[0]),
                                 message_y=int(__SIZE[1] / (800 / 190)), second_color=COLOR_BUTTON_2)
    button_theme = Button_rect(int(__SIZE[0] / 2 - (__SIZE[0] / 4)), int(__SIZE[1] / (800 / 375)), int(__SIZE[0] / 2),
                               int(__SIZE[1] / 12), COLOR_SETUP_MENU_1, 'Тема',
                               font_type='/shrift/play_menu.otf', active_color=MAIN_COLOR_FONT,
                               actived_color=MAIN_COLOR_FONT,
                               font_size=int(__SIZE[1] / 24),
                               message_x=int(__SIZE[0] / 2 - (40 / 800) * __SIZE[0]),
                               message_y=int(__SIZE[1] / (800 / 390)),
                               second_color=COLOR_BUTTON_2)
    button_lang = Button_rect(int(__SIZE[0] / 2 - (__SIZE[0] / 4)), int(__SIZE[1] / (800 / 575)), int(__SIZE[0] / 2),
                              int(__SIZE[1] / 12), COLOR_SETUP_MENU_1, 'Язык',
                              font_type='/shrift/play_menu.otf', active_color=MAIN_COLOR_FONT,
                              actived_color=MAIN_COLOR_FONT,
                              font_size=int(__SIZE[1] / 24),
                              message_x=int(__SIZE[0] / 2 - (44 / 800) * __SIZE[0]),
                              message_y=int(__SIZE[1] / (800 / 590)),
                              second_color=COLOR_BUTTON_2)
    main_sett_font = Font(int(__SIZE[0] / 2 - __SIZE[0] / (800 / 120)), int(__SIZE[1] / (800 / 40)),
                          message='Настройки', font_size=int(__SIZE[1] / (800 / 50)), font_color=MAIN_COLOR_FONT)
    show_menu_setup = True
    while show_menu_setup:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                output_settings()
        display.fill(COLOR_DISPLAY)
        show_menu_setup = draw_exit(show_menu_setup)
        button_display.draw()
        button_lang.draw()
        button_theme.draw()
        main_sett_font.draw_text()
        pg.display.update()
        if button_theme.action:
            menu_theme_settings_rus()
        elif button_lang.action:
            setup_lang_rus()
        elif button_display.action:
            menu_display_settings_rus()
    Exit = True


def setup_lang_rus():
    global LANG
    show_menu_lang_setup = True
    ok_1 = False
    ok_2 = False
    if LANG == 1:
        ok_1 = True
    elif LANG == 2:
        ok_2 = True
    okey_1 = Window_ok(int(__SIZE[0] / 2 - (__SIZE[0] / 4)) + int(__SIZE[0] / 2) - int(__SIZE[0] / (800 / 50)),
                       int(__SIZE[1] / (800 / 175)), int(__SIZE[0] / (800 / 50)), int(__SIZE[1] / (600 / 50)),
                       ANTI_VERSION_SCORE_COLOR,
                       ACTIVE_COLOR, COLOR_VERSION_SCORE, ACTIVE_COLOR, COLOR_VERSION_SCORE, ok_1, 5)
    okey_2 = Window_ok(int(__SIZE[0] / 2 - (__SIZE[0] / 4)) + int(__SIZE[0] / 2) - int(__SIZE[0] / (800 / 50)),
                       int(__SIZE[1] / (800 / 375)), int(__SIZE[0] / (800 / 50)), int(__SIZE[1] / (600 / 50)),
                       ANTI_VERSION_SCORE_COLOR,
                       ACTIVE_COLOR, COLOR_VERSION_SCORE, ACTIVE_COLOR, COLOR_VERSION_SCORE, ok_2, 5)
    button_eng = Button_rect(int(__SIZE[0] / 2 - (__SIZE[0] / 4)), int(__SIZE[1] / (800 / 175)),
                             int(__SIZE[0] / 2),
                             int(__SIZE[1] / 12), COLOR_SETUP_MENU_1, 'Английский',
                             font_type='/shrift/play_menu.otf', active_color=MAIN_COLOR_FONT,
                             actived_color=MAIN_COLOR_FONT,
                             font_size=int(__SIZE[1] / 24),
                             message_x=int(__SIZE[0] / 2 - (200 / 800) * __SIZE[0]),
                             message_y=int(__SIZE[1] / (800 / 190)),
                             second_color=COLOR_BUTTON_2)
    button_rus = Button_rect(int(__SIZE[0] / 2 - (__SIZE[0] / 4)), int(__SIZE[1] / (800 / 375)), int(__SIZE[0] / 2),
                             int(__SIZE[1] / 12), COLOR_SETUP_MENU_1, 'Русский',
                             font_type='/shrift/play_menu.otf', active_color=MAIN_COLOR_FONT,
                             actived_color=MAIN_COLOR_FONT,
                             font_size=int(__SIZE[1] / 24),
                             message_x=int(__SIZE[0] / 2 - (200 / 800) * __SIZE[0]),
                             message_y=int(__SIZE[1] / (800 / 390)),
                             second_color=COLOR_BUTTON_2)
    main_sett_font = Font(int(__SIZE[0] / 2 - __SIZE[0] / (800 / 100)), int(__SIZE[1] / (800 / 40)),
                          message='Язык',
                          font_size=int(__SIZE[1] / (800 / 50)), font_color=MAIN_COLOR_FONT)
    while show_menu_lang_setup:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                output_settings()
        display.fill(COLOR_DISPLAY)
        show_menu_lang_setup = draw_exit(show_menu_lang_setup)
        button_eng.draw()
        button_rus.draw()
        okey_1.draw()
        okey_2.draw()
        main_sett_font.draw_text()
        if okey_1.action:
            LANG = 1
            okey_2.ok = False
        elif okey_2.action:
            LANG = 2
            okey_1.ok = False
        pg.display.update()
        okey_1.action = False
        okey_2.action = False


def start_level_rus():
    global EX_1
    button_5_class = Button_rect(int(__SIZE[0] / 2 - (__SIZE[0] / 4)), int(__SIZE[1] / (800 / 175)), int(__SIZE[0] / 2),
                                 int(__SIZE[1] / 12), COLOR_SETUP_MENU_1, '5 класс',
                                 font_type='/shrift/play_menu.otf', active_color=MAIN_COLOR_FONT,
                                 actived_color=MAIN_COLOR_FONT,
                                 font_size=int(__SIZE[1] / 24),
                                 message_x=int(__SIZE[0] / 2 - (60 / 800) * __SIZE[0]),
                                 message_y=int(__SIZE[1] / (800 / 190)), second_color=COLOR_BUTTON_2)
    button_6_class = Button_rect(int(__SIZE[0] / 2 - (__SIZE[0] / 4)), int(__SIZE[1] / (800 / 375)), int(__SIZE[0] / 2),
                                 int(__SIZE[1] / 12), COLOR_SETUP_MENU_1, '6 класс',
                                 font_type='/shrift/play_menu.otf', active_color=MAIN_COLOR_FONT,
                                 actived_color=MAIN_COLOR_FONT,
                                 font_size=int(__SIZE[1] / 24),
                                 message_x=int(__SIZE[0] / 2 - (50 / 800) * __SIZE[0]),
                                 message_y=int(__SIZE[1] / (800 / 390)),
                                 second_color=COLOR_BUTTON_2)
    button_7_class = Button_rect(int(__SIZE[0] / 2 - (__SIZE[0] / 4)), int(__SIZE[1] / (800 / 575)), int(__SIZE[0] / 2),
                                 int(__SIZE[1] / 12), COLOR_SETUP_MENU_1, '7 класс',
                                 font_type='/shrift/play_menu.otf', active_color=MAIN_COLOR_FONT,
                                 actived_color=MAIN_COLOR_FONT,
                                 font_size=int(__SIZE[1] / 24),
                                 message_x=int(__SIZE[0] / 2 - (50 / 800) * __SIZE[0]),
                                 message_y=int(__SIZE[1] / (800 / 590)),
                                 second_color=COLOR_BUTTON_2)
    main_sett_font = Font(int(__SIZE[0] / 2 - __SIZE[0] / (800 / 220)), int(__SIZE[1] / (800 / 40)),
                          message='Выберите ваш класс',
                          font_size=int(__SIZE[1] / (800 / 50)), font_color=MAIN_COLOR_FONT)
    show_menu_level = True
    while show_menu_level:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                output_settings()
        display.fill(COLOR_DISPLAY)
        show_menu_level = draw_exit(show_menu_level)
        button_5_class.draw()
        button_6_class.draw()
        main_sett_font.draw_text()
        pg.display.update()
        if button_5_class.action:
            EX_1 = 5
            menu_level_class_rus()
        elif button_6_class.action:
            EX_1 = 6
            menu_level_class_rus()


def menu_level_class_rus():
    global EX_2
    show_menu_setup_five_class = True
    ok_1 = False
    ok_2 = False
    ok_3 = False
    if EX_2 == 1:
        ok_1 = True
    elif EX_2 == 2:
        ok_2 = True
    elif EX_2 == 3:
        ok_3 = True
    okey_1 = Window_ok(int(__SIZE[0] / 2 - (__SIZE[0] / 4)) + int(__SIZE[0] / 2) - int(__SIZE[0] / (800 / 50)),
                       int(__SIZE[1] / (800 / 175)), int(__SIZE[0] / (800 / 50)), int(__SIZE[1] / (600 / 50)),
                       ANTI_VERSION_SCORE_COLOR,
                       ACTIVE_COLOR, COLOR_VERSION_SCORE, ACTIVE_COLOR, COLOR_VERSION_SCORE, ok_1, 5)
    okey_2 = Window_ok(int(__SIZE[0] / 2 - (__SIZE[0] / 4)) + int(__SIZE[0] / 2) - int(__SIZE[0] / (800 / 50)),
                       int(__SIZE[1] / (800 / 375)), int(__SIZE[0] / (800 / 50)), int(__SIZE[1] / (600 / 50)),
                       ANTI_VERSION_SCORE_COLOR,
                       ACTIVE_COLOR, COLOR_VERSION_SCORE, ACTIVE_COLOR, COLOR_VERSION_SCORE, ok_2, 5)
    okey_3 = Window_ok(int(__SIZE[0] / 2 - (__SIZE[0] / 4)) + int(__SIZE[0] / 2) - int(__SIZE[0] / (800 / 50)),
                       int(__SIZE[1] / (800 / 575)), int(__SIZE[0] / (800 / 50)), int(__SIZE[1] / (600 / 50)),
                       ANTI_VERSION_SCORE_COLOR,
                       ACTIVE_COLOR, COLOR_VERSION_SCORE, ACTIVE_COLOR, COLOR_VERSION_SCORE, ok_3, 5)
    button_easy = Button_rect(int(__SIZE[0] / 2 - (__SIZE[0] / 4)), int(__SIZE[1] / (800 / 175)),
                              int(__SIZE[0] / 2),
                              int(__SIZE[1] / 12), COLOR_SETUP_MENU_1, 'Легкий',
                              font_type='/shrift/play_menu.otf', active_color=MAIN_COLOR_FONT,
                              actived_color=MAIN_COLOR_FONT,
                              font_size=int(__SIZE[1] / 24),
                              message_x=int(__SIZE[0] / 2 - (200 / 800) * __SIZE[0]),
                              message_y=int(__SIZE[1] / (800 / 190)),
                              second_color=COLOR_BUTTON_2)
    button_medium = Button_rect(int(__SIZE[0] / 2 - (__SIZE[0] / 4)), int(__SIZE[1] / (800 / 375)), int(__SIZE[0] / 2),
                                int(__SIZE[1] / 12), COLOR_SETUP_MENU_1, 'Средний',
                                font_type='/shrift/play_menu.otf', active_color=MAIN_COLOR_FONT,
                                actived_color=MAIN_COLOR_FONT,
                                font_size=int(__SIZE[1] / 24),
                                message_x=int(__SIZE[0] / 2 - (200 / 800) * __SIZE[0]),
                                message_y=int(__SIZE[1] / (800 / 390)),
                                second_color=COLOR_BUTTON_2)
    button_hard = Button_rect(int(__SIZE[0] / 2 - (__SIZE[0] / 4)), int(__SIZE[1] / (800 / 575)), int(__SIZE[0] / 2),
                              int(__SIZE[1] / 12), COLOR_SETUP_MENU_1, 'Сложный',
                              font_type='/shrift/play_menu.otf', active_color=MAIN_COLOR_FONT,
                              actived_color=MAIN_COLOR_FONT,
                              font_size=int(__SIZE[1] / 24),
                              message_x=int(__SIZE[0] / 2 - (200 / 800) * __SIZE[0]),
                              message_y=int(__SIZE[1] / (800 / 590)),
                              second_color=COLOR_BUTTON_2)
    main_sett_font_level = Font(int(__SIZE[0] / 2 - __SIZE[0] / (800 / 200)), int(__SIZE[1] / (800 / 40)),
                                message='Выберите сложность',
                                font_size=int(__SIZE[1] / (800 / 50)), font_color=MAIN_COLOR_FONT)
    while show_menu_setup_five_class:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                output_settings()
        display.fill(COLOR_DISPLAY)
        show_menu_setup_five_class = draw_exit(show_menu_setup_five_class)
        main_sett_font_level.draw_text()
        button_easy.draw()
        okey_1.draw()
        button_medium.draw()
        okey_2.draw()
        button_hard.draw()
        okey_3.draw()
        pg.display.update()
        theme_upload(THEME)
        if okey_2.action:
            okey_1.ok = False
            okey_3.ok = False
            EX_2 = 2
        elif okey_3.action:
            okey_1.ok = False
            okey_2.ok = False
            EX_2 = 3
        elif okey_1.action:
            okey_2.ok = False
            okey_3.ok = False
            EX_2 = 1
        okey_1.action = False
        okey_2.action = False
        okey_3.action = False


def menu_theme_settings_rus():
    global THEME
    show_menu_setup_theme = True
    ok_1 = False
    ok_2 = False
    ok_3 = False
    if THEME == 1:
        ok_1 = True
    elif THEME == 2:
        ok_2 = True
    elif THEME == 3:
        ok_3 = True
    okey_1 = Window_ok(int(__SIZE[0] / 2 - (__SIZE[0] / 4)) + int(__SIZE[0] / 2) - int(__SIZE[0] / (800 / 50)),
                       int(__SIZE[1] / (800 / 175)), int(__SIZE[0] / (800 / 50)), int(__SIZE[1] / (600 / 50)),
                       ANTI_VERSION_SCORE_COLOR,
                       ACTIVE_COLOR, COLOR_VERSION_SCORE, ACTIVE_COLOR, COLOR_VERSION_SCORE, ok_1, 5)
    okey_2 = Window_ok(int(__SIZE[0] / 2 - (__SIZE[0] / 4)) + int(__SIZE[0] / 2) - int(__SIZE[0] / (800 / 50)),
                       int(__SIZE[1] / (800 / 375)), int(__SIZE[0] / (800 / 50)), int(__SIZE[1] / (600 / 50)),
                       ANTI_VERSION_SCORE_COLOR,
                       ACTIVE_COLOR, COLOR_VERSION_SCORE, ACTIVE_COLOR, COLOR_VERSION_SCORE, ok_2, 5)
    okey_3 = Window_ok(int(__SIZE[0] / 2 - (__SIZE[0] / 4)) + int(__SIZE[0] / 2) - int(__SIZE[0] / (800 / 50)),
                       int(__SIZE[1] / (800 / 575)), int(__SIZE[0] / (800 / 50)), int(__SIZE[1] / (600 / 50)),
                       ANTI_VERSION_SCORE_COLOR,
                       ACTIVE_COLOR, COLOR_VERSION_SCORE, ACTIVE_COLOR, COLOR_VERSION_SCORE, ok_3, 5)
    button_standart = Button_rect(int(__SIZE[0] / 2 - (__SIZE[0] / 4)), int(__SIZE[1] / (800 / 175)),
                                  int(__SIZE[0] / 2),
                                  int(__SIZE[1] / 12), COLOR_SETUP_MENU_1, 'Стандартная',
                                  font_type='/shrift/play_menu.otf', active_color=MAIN_COLOR_FONT,
                                  actived_color=MAIN_COLOR_FONT,
                                  font_size=int(__SIZE[1] / 24),
                                  message_x=int(__SIZE[0] / 2 - (200 / 800) * __SIZE[0]),
                                  message_y=int(__SIZE[1] / (800 / 190)),
                                  second_color=COLOR_BUTTON_2)
    button_dracula = Button_rect(int(__SIZE[0] / 2 - (__SIZE[0] / 4)), int(__SIZE[1] / (800 / 375)), int(__SIZE[0] / 2),
                                 int(__SIZE[1] / 12), COLOR_SETUP_MENU_1, 'Дракула',
                                 font_type='/shrift/play_menu.otf', active_color=MAIN_COLOR_FONT,
                                 actived_color=MAIN_COLOR_FONT,
                                 font_size=int(__SIZE[1] / 24),
                                 message_x=int(__SIZE[0] / 2 - (200 / 800) * __SIZE[0]),
                                 message_y=int(__SIZE[1] / (800 / 390)),
                                 second_color=COLOR_BUTTON_2)
    button_white = Button_rect(int(__SIZE[0] / 2 - (__SIZE[0] / 4)), int(__SIZE[1] / (800 / 575)), int(__SIZE[0] / 2),
                               int(__SIZE[1] / 12), COLOR_SETUP_MENU_1, 'Светлая',
                               font_type='/shrift/play_menu.otf', active_color=MAIN_COLOR_FONT,
                               actived_color=MAIN_COLOR_FONT,
                               font_size=int(__SIZE[1] / 24),
                               message_x=int(__SIZE[0] / 2 - (200 / 800) * __SIZE[0]),
                               message_y=int(__SIZE[1] / (800 / 590)),
                               second_color=COLOR_BUTTON_2)
    main_sett_font_theme = Font(int(__SIZE[0] / 2 - __SIZE[0] / (800 / 80)), int(__SIZE[1] / (800 / 40)),
                                message='Тема',
                                font_size=int(__SIZE[1] / (800 / 50)), font_color=MAIN_COLOR_FONT)
    while show_menu_setup_theme:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                output_settings()
        display.fill(COLOR_DISPLAY)
        show_menu_setup_theme = draw_exit(show_menu_setup_theme)
        main_sett_font_theme.draw_text()
        button_standart.draw()
        okey_1.draw()
        button_white.draw()
        okey_3.draw()
        button_dracula.draw()
        okey_2.draw()
        pg.display.update()
        theme_upload(THEME)
        if okey_2.action:
            okey_1.ok = False
            okey_3.ok = False
            THEME = 2
        elif okey_3.action:
            okey_1.ok = False
            okey_2.ok = False
            THEME = 3
        elif okey_1.action:
            okey_2.ok = False
            okey_3.ok = False
            THEME = 1
        okey_1.action = False
        okey_2.action = False
        okey_3.action = False


def menu_display_settings_rus():
    global SIZE
    show_menu_setup_display = True
    ok_1 = False
    ok_2 = False
    ok_3 = False
    if SIZE == 1:
        ok_1 = True
    elif SIZE == 2:
        ok_2 = True
    elif SIZE == 3:
        ok_3 = True
    okey_1 = Window_ok(int(__SIZE[0] / 2 - (__SIZE[0] / 4)) + int(__SIZE[0] / 2) - int(__SIZE[0] / (800 / 50)),
                       int(__SIZE[1] / (800 / 175)), int(__SIZE[0] / (800 / 50)), int(__SIZE[1] / (600 / 50)),
                       ANTI_VERSION_SCORE_COLOR,
                       ACTIVE_COLOR, COLOR_VERSION_SCORE, ACTIVE_COLOR, COLOR_VERSION_SCORE, ok_1, 5)
    okey_2 = Window_ok(int(__SIZE[0] / 2 - (__SIZE[0] / 4)) + int(__SIZE[0] / 2) - int(__SIZE[0] / (800 / 50)),
                       int(__SIZE[1] / (800 / 375)), int(__SIZE[0] / (800 / 50)), int(__SIZE[1] / (600 / 50)),
                       ANTI_VERSION_SCORE_COLOR,
                       ACTIVE_COLOR, COLOR_VERSION_SCORE, ACTIVE_COLOR, COLOR_VERSION_SCORE, ok_2, 5)
    okey_3 = Window_ok(int(__SIZE[0] / 2 - (__SIZE[0] / 4)) + int(__SIZE[0] / 2) - int(__SIZE[0] / (800 / 50)),
                       int(__SIZE[1] / (800 / 575)), int(__SIZE[0] / (800 / 50)), int(__SIZE[1] / (600 / 50)),
                       ANTI_VERSION_SCORE_COLOR,
                       ACTIVE_COLOR, COLOR_VERSION_SCORE, ACTIVE_COLOR, COLOR_VERSION_SCORE, ok_3, 5)
    button_800_600 = Button_rect(int(__SIZE[0] / 2 - (__SIZE[0] / 4)), int(__SIZE[1] / (800 / 175)),
                                 int(__SIZE[0] / 2),
                                 int(__SIZE[1] / 12), COLOR_SETUP_MENU_1, '800 X 600',
                                 font_type='/shrift/play_menu.otf', active_color=MAIN_COLOR_FONT,
                                 actived_color=MAIN_COLOR_FONT,
                                 font_size=int(__SIZE[1] / 24),
                                 message_x=int(__SIZE[0] / 2 - (200 / 800) * __SIZE[0]),
                                 message_y=int(__SIZE[1] / (800 / 190)),
                                 second_color=COLOR_BUTTON_2)
    button_1000_800 = Button_rect(int(__SIZE[0] / 2 - (__SIZE[0] / 4)), int(__SIZE[1] / (800 / 375)),
                                  int(__SIZE[0] / 2),
                                  int(__SIZE[1] / 12), COLOR_SETUP_MENU_1, '1000 X 700',
                                  font_type='/shrift/play_menu.otf', active_color=MAIN_COLOR_FONT,
                                  actived_color=MAIN_COLOR_FONT,
                                  font_size=int(__SIZE[1] / 24),
                                  message_x=int(__SIZE[0] / 2 - (200 / 800) * __SIZE[0]),
                                  message_y=int(__SIZE[1] / (800 / 390)),
                                  second_color=COLOR_BUTTON_2)
    button_1200_900 = Button_rect(int(__SIZE[0] / 2 - (__SIZE[0] / 4)), int(__SIZE[1] / (800 / 575)),
                                  int(__SIZE[0] / 2),
                                  int(__SIZE[1] / 12), COLOR_SETUP_MENU_1, '1200 X 900',
                                  font_type='/shrift/play_menu.otf', active_color=MAIN_COLOR_FONT,
                                  actived_color=MAIN_COLOR_FONT,
                                  font_size=int(__SIZE[1] / 24),
                                  message_x=int(__SIZE[0] / 2 - (200 / 800) * __SIZE[0]),
                                  message_y=int(__SIZE[1] / (800 / 590)),
                                  second_color=COLOR_BUTTON_2)
    main_sett_font_display = Font(int(__SIZE[0] / 2 - __SIZE[0] / (800 / 100)), int(__SIZE[1] / (800 / 40)),
                                  message='Экран',
                                  font_size=int(__SIZE[1] / (800 / 50)), font_color=MAIN_COLOR_FONT)
    while show_menu_setup_display:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                output_settings()
        display.fill(COLOR_DISPLAY)
        main_sett_font_display.draw_text()
        show_menu_setup_display = draw_exit(show_menu_setup_display)
        button_800_600.draw()
        okey_1.draw()
        button_1000_800.draw()
        okey_2.draw()
        button_1200_900.draw()
        okey_3.draw()
        if okey_2.action:
            okey_1.ok = False
            okey_3.ok = False
            SIZE = 2
        elif okey_3.action:
            okey_1.ok = False
            okey_2.ok = False
            SIZE = 3
        elif okey_1.action:
            okey_2.ok = False
            okey_3.ok = False
            SIZE = 1
        okey_1.action = False
        okey_2.action = False
        okey_3.action = False
        pg.display.update()


def any_game_menu_rus():
    show_menu_any_game = True
    text = Font(int(__SIZE[0] / (800 / 315)), int(__SIZE[1] / (600 / 40)), MAIN_COLOR_FONT, int(__SIZE[1] / (600 / 40)),
                message='Другое')
    yes_or_no = Button_rect(int(__SIZE[0] / 2 - (__SIZE[0] / 4)), int(__SIZE[1] / (600 / 300)),
                            int(__SIZE[0] / (800 / 400)),
                            int(__SIZE[1] / 12), COLOR_SETUP_MENU_1, 'Правда ложь',
                            font_type='/shrift/play_menu.otf', active_color=MAIN_COLOR_FONT,
                            actived_color=MAIN_COLOR_FONT,
                            font_size=int(__SIZE[1] / 24),
                            message_x=int(int(__SIZE[0] / 2 - (__SIZE[0] / 4) + (__SIZE[0] / (800 / 95)))),
                            message_y=int(__SIZE[1] / (600 / 315)),
                            second_color=COLOR_BUTTON_2)
    while show_menu_any_game:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                output_settings()
        display.fill(COLOR_DISPLAY)
        show_menu_any_game = draw_exit(show_menu_any_game)
        text.draw_text()
        yes_or_no.draw()
        if yes_or_no.action:
            pg.time.wait(50)
            yes_or_no_rus()
        pg.display.update()


def yes_or_no_rus():
    s = 40
    d = 60
    color_list = [0, 0, 200]
    color_list_2 = [0, 0, 100]
    color_list_3 = [0, 0, 100]
    flag = 1
    show_menu_y_r = True
    h = 0
    play_button = New_button(int(__SIZE[0] / (800 / 250)), int(__SIZE[1] / (600 / 300)), int(__SIZE[0] / (800 / 300)),
                             int(__SIZE[1] / (600 / 80)), 'Играть', (0, 0, 0), int(__SIZE[1] / (600 / 36)),
                             active_color=ACTIVE_COLOR,
                             message_x=int(__SIZE[0] / (800 / 320)), message_y=int(__SIZE[1] / (600 / 320)),
                             sukam=int(__SIZE[0] / (800 / 10)))
    rule_button = New_button(int(__SIZE[0] / (800 / 250)), int(__SIZE[1] / (600 / 450)), int(__SIZE[0] / (800 / 300)),
                             int(__SIZE[1] / (600 / 80)), 'Правила', (0, 0, 0), int(__SIZE[1] / (600 / 36)),
                             active_color=ACTIVE_COLOR,
                             message_x=int(__SIZE[0] / (800 / 347)),
                             message_y=int(__SIZE[1] / (600 / 470)), sukam=int(__SIZE[0] / (800 / 10)))
    main_text = Font(int(__SIZE[0] / (800 / 213)), int(__SIZE[1] / (600 / 100)), font_size=int(__SIZE[1] / (600 / 46)),
                     message='Правда ложь')
    while show_menu_y_r:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                output_settings()
        display.fill(tuple(color_list))
        show_menu_y_r = draw_exit(show_menu_y_r)
        play_button.draw(tuple(color_list_2), tuple(color_list_3))
        main_text.font_color = tuple(color_list_3)
        main_text.draw_text()
        pg.display.update()
        if flag == 10:
            color_list = new_color(color_list, 200)
            if color_list[0] > s:
                color_list_2[0] = color_list[0] - s
                if color_list[0] > d:
                    color_list_3[0] = color_list[0] - d
                else:
                    color_list_3[0] = color_list_2[0]
            else:
                color_list_2[0] = 0
                color_list_3[0] = 0
            if color_list[1] > s:
                color_list_2[1] = color_list[1] - s
                if color_list[1] > d:
                    color_list_3[1] = color_list[1] - d
            else:
                color_list_2[1] = 0
                color_list_3[1] = 0
            if color_list[2] > s:
                color_list_2[2] = color_list[2] - s
                if color_list[1] > d:
                    color_list_3[1] = color_list[1] - d
            else:
                color_list_2[2] = 0
                color_list_3[2] = 0
            flag = 0
        flag += 1
        if play_button.action:
            h += 1
            if h == 4:
                pg.time.wait(50)
                true_or_false_play_rus()
                h = 0
        elif rule_button.action:
            pass


def true_or_false_play_rus():
    global RECORD
    colot_display = (15, 0, 176)
    show_pley_menu = True
    flag = 1
    record = RECORD
    while show_pley_menu:
        start_play_T_F_r()
        score = playing_start_T_F_r()
        retry = retry_rus()
        if score > RECORD:
            RECORD = score
        if not retry:
            break


def start_play_T_F_r():
    flag = 1
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                output_settings()
        display.fill((15, 0, 176))
        flag += 1
        if flag > 1 and flag < 1000:
            font = Font(int(__SIZE[0] / (800 / 200)), int(__SIZE[1] / (600 / 200)), (0, 251, 255),
                        int(__SIZE[1] / (600 / 50)), message='Начинаем ...')
            font.draw_text()
        elif flag > 1000 and flag < 1700:
            font = Font(int(__SIZE[0] / (800 / 350)), int(__SIZE[1] / (600 / 220)), (0, 251, 255),
                        int(__SIZE[1] / (600 / 120)), message='3')
            font.draw_text()
        elif flag > 1700 and flag < 2400:
            font = Font(int(__SIZE[0] / (800 / 350)), int(__SIZE[1] / (600 / 220)), (0, 251, 255),
                        int(__SIZE[1] / (600 / 120)), message='2')
            font.draw_text()
        elif flag > 2400 and flag < 3100:
            font = Font(int(__SIZE[0] / (800 / 350)), int(__SIZE[1] / (600 / 220)), (0, 251, 255),
                        int(__SIZE[1] / (600 / 120)), message='1')
            font.draw_text()
        elif flag > 3100 and flag < 4000:
            font = Font(int(__SIZE[0] / (800 / 220)), int(__SIZE[1] / (600 / 200)), (0, 251, 255),
                        int(__SIZE[1] / (600 / 80)), message='Старт!!!')
            font.draw_text()
        pg.display.update()
        if flag == 4000:
            break


def playing_start_T_F_r():
    score = 0
    show_menu_y_r = True
    flag = 1500
    n = 1500
    button_true = Button_rect(int(__SIZE[0] / 2 - (__SIZE[0] / 3)), int(__SIZE[1] / (800 / 400)), int(__SIZE[0] / 4),
                              int(__SIZE[1] / 6), (255, 206, 0), 'Правда',
                              font_type='/shrift/play_menu.otf', active_color=MAIN_COLOR_FONT,
                              actived_color=MAIN_COLOR_FONT,
                              font_size=int(__SIZE[1] / (600 / 32)),
                              message_x=int(int(__SIZE[0] / 2 - (__SIZE[0] / 3) + __SIZE[0] / (800 / 20))),
                              message_y=int(__SIZE[1] / (800 / 440)), second_color=(255, 164, 0))
    button_false = Button_rect(int(__SIZE[0] / 2 + (__SIZE[0] / 3) - __SIZE[0] / 4), int(__SIZE[1] / (800 / 400)),
                               int(__SIZE[0] / 4),
                               int(__SIZE[1] / 6), (255, 206, 0), 'Ложь',
                               font_type='/shrift/play_menu.otf', active_color=MAIN_COLOR_FONT,
                               actived_color=MAIN_COLOR_FONT,
                               font_size=int(__SIZE[1] / (600 / 32)),
                               message_x=int(
                                   int(__SIZE[0] / 2 + (__SIZE[0] / 3) - __SIZE[0] / 4 + __SIZE[0] / (800 / 45))),
                               message_y=int(__SIZE[1] / (800 / 440)), second_color=(255, 164, 0))
    score_txt = Font(int(__SIZE[0] / (800 / 600)), int(__SIZE[1] / (600 / 10)), message=f'Счёт: {score}',
                     font_size=int(__SIZE[1] / (600 / 26)), font_color=COLOR_VERSION_SCORE)
    reccord_txt = Font(int(__SIZE[0] / (800 / 15)), int(__SIZE[1] / (600 / 10)), message=f'Рекорд: {RECORD}',
                       font_size=int(__SIZE[1] / (600 / 26)), font_color=COLOR_VERSION_SCORE)
    yes = False
    t, ex = generate()
    ex.font_size = int(__SIZE[1] / (600 / 46))
    ex.font_color = COLOR_VERSION_SCORE
    while show_menu_y_r:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                output_settings()
        display.fill((15, 0, 176))
        pg.draw.line(display, (0, 255, 0), [0, 590], [int(__SIZE[0] * flag / n), 590], int(__SIZE[1] / (600 / 14)))
        score_txt.draw_text()
        reccord_txt.draw_text()
        button_true.draw()
        button_false.draw()
        ex.draw_text()
        pg.display.update()
        flag -= 1
        if button_false.action:
            if not t:
                yes = True
            else:
                yes = False
        elif button_true.action:
            if t:
                yes = True
            else:
                yes = False
        if yes:
            score += 1
            score_txt.message = f'Счёт: {score}'
            n = 1500 - score * 10
            flag = n
            t, ex = generate()
            ex.font_size = int(__SIZE[1] / (600 / 40))
            ex.font_color = COLOR_VERSION_SCORE
            yes = False
            pg.time.wait(150)
        elif flag == 1 or ((button_true.action or button_false.action) and not yes):
            break
    return score


def retry_rus():
    show_menu_retry = True
    okey = True
    go = False
    h = 0
    button_yes = Button_rect(int(__SIZE[0] / 2 - (__SIZE[0] / 3)), int(__SIZE[1] / (800 / 300)), int(__SIZE[0] / 4),
                             int(__SIZE[1] / 6), (255, 206, 0), 'Да',
                             font_type='/shrift/play_menu.otf', active_color=MAIN_COLOR_FONT,
                             actived_color=MAIN_COLOR_FONT,
                             font_size=int(__SIZE[1] / (600 / 32)),
                             message_x=int(int(__SIZE[0] / 2 - (__SIZE[0] / 3) + __SIZE[0] / (800 / 45))),
                             message_y=int(__SIZE[1] / (800 / 340)), second_color=(255, 164, 0))
    button_not = Button_rect(int(__SIZE[0] / 2 + (__SIZE[0] / 3) - __SIZE[0] / 4), int(__SIZE[1] / (800 / 300)),
                             int(__SIZE[0] / 4),
                             int(__SIZE[1] / 6), (255, 206, 0), 'Нет',
                             font_type='/shrift/play_menu.otf', active_color=MAIN_COLOR_FONT,
                             actived_color=MAIN_COLOR_FONT,
                             font_size=int(__SIZE[1] / (600 / 32)),
                             message_x=int(
                                 int(__SIZE[0] / 2 + (__SIZE[0] / 3) - __SIZE[0] / 4 + __SIZE[0] / (800 / 45))),
                             message_y=int(__SIZE[1] / (800 / 340)), second_color=(255, 164, 0))
    quest = Font(int(__SIZE[0] / (800 / 150)), int(__SIZE[1] / (600 / 50)), COLOR_VERSION_SCORE,
                 int(__SIZE[1] / (600 / 44)), message='Хотите повторить?')
    while show_menu_retry:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                output_settings()
        display.fill((15, 0, 176))
        button_not.draw()
        button_yes.draw()
        quest.draw_text()
        if button_yes.action and go:
            okey = True
            break
        elif button_not.action and go:
            okey = False
            break
        pg.display.update()
        if h == 10:
            go = True
        elif h < 10:
            h += 1

    return okey


class Button_rect:
    def __init__(self, x, y, weight, height, color_button, message=None, font_color=(0, 0, 0), font_size=30,
                 font_type=None, active_color=None,
                 actived_color=None, message_x=None, message_y=None, second_color=None,
                 sukam=4):  # Инициализируем переменные
        self.x = x
        self.y = y
        self.weight = weight
        self.height = height
        self.message = message
        self.font_color = font_color
        self.font_size = font_size
        self.font_type = font_type
        self.active_color = active_color
        self.actived_color = actived_color
        self.message_x = message_x
        self.message_y = message_y
        self.color = color_button
        self.second_color = second_color
        self.sukam = sukam
        self.action = False

    def draw(self):
        if pg.mouse.get_pressed()[0] == 1:
            pg.time.wait(50)
        mouse = pg.mouse.get_pos()
        click = pg.mouse.get_pressed()
        if self.x < mouse[0] < self.x + self.weight and self.y < mouse[1] < self.y + self.height:
            if click[0] == 1 and self.x < mouse[0] < self.x + self.weight and self.y < mouse[1] < self.y + self.height:
                if self.sukam <= 6:
                    rect_2 = (self.x, self.y, self.weight, self.height)
                    rect_1 = (self.x - self.sukam, self.y - self.sukam, self.weight + self.sukam * 2,
                              self.height + self.sukam * 2)
                    ellipse_1 = pg.draw.rect(display, self.second_color, rect_1)
                    el = pg.draw.rect(display, self.color, rect_2)
                    text_but = Font(self.message_x, self.message_y, self.actived_color, self.font_size,
                                    message=self.message)
                    text_but.draw_text()
                    self.sukam += 2
                else:
                    rect_1 = (self.x - self.sukam, self.y - self.sukam, self.weight + self.sukam * 2,
                              self.height + self.sukam * 2)
                    rect_2 = (self.x, self.y, self.weight, self.height)
                    el = pg.draw.rect(display, self.second_color, rect_1)
                    ellipse_2 = pg.draw.rect(display, self.color, rect_2)
                    text_but = Font(self.message_x, self.message_y, self.actived_color, self.font_size,
                                    message=self.message)
                    text_but.draw_text()
                self.action = True
            else:
                if self.sukam <= 6:
                    rect_1 = (self.x - self.sukam, self.y - self.sukam, self.weight + self.sukam * 2,
                              self.height + self.sukam * 2)
                    rect_2 = (self.x, self.y, self.weight, self.height)
                    ellipse_2 = pg.draw.rect(display, self.color, rect_2)
                    text_but = Font(self.message_x, self.message_y, self.active_color, self.font_size,
                                    message=self.message)
                    text_but.draw_text()
                    self.sukam += 4
                else:
                    rect_2 = (self.x, self.y, self.weight, self.height)
                    rect_1 = (self.x - self.sukam, self.y - self.sukam, self.weight + self.sukam * 2,
                              self.height + self.sukam * 2)
                    el = pg.draw.rect(display, self.second_color, rect_1)
                    ellipse_2 = pg.draw.rect(display, self.color, rect_2)

                    text_but = Font(self.message_x, self.message_y, self.active_color, self.font_size,
                                    message=self.message)

                    text_but.draw_text()
                self.action = False
        else:
            rect_1 = (self.x, self.y, self.weight, self.height)
            ellipse_1 = pg.draw.rect(display, self.color, rect_1)
            text_but = Font(self.message_x, self.message_y, self.font_color, self.font_size, message=self.message)
            text_but.draw_text()
            self.action = False
        return self.action


class Button:
    def __init__(self, x, y, weight, height, color_button, message=None, font_color=(0, 0, 0), font_size=30,
                 font_type=None, active_color=None,
                 actived_color=None, message_x=None, message_y=None, second_color=None, sukam=4):
        self.x = x
        self.y = y
        self.weight = weight
        self.height = height
        self.message = message
        self.font_color = font_color
        self.font_size = font_size
        self.font_type = font_type
        self.active_color = active_color
        self.actived_color = actived_color
        self.message_x = message_x
        self.message_y = message_y
        self.color = color_button
        self.second_color = second_color
        self.sukam = sukam
        self.action = False

    def draw(self):  # Рисуем кнопку
        if pg.mouse.get_pressed()[0] == 1:
            pg.time.wait(50)
        mouse = pg.mouse.get_pos()
        click = pg.mouse.get_pressed()
        if self.x < mouse[0] < self.x + self.weight and self.y < mouse[1] < self.y + self.height:
            if click[0] == 1 and self.x < mouse[0] < self.x + self.weight and self.y < mouse[1] < self.y + self.height:
                if self.sukam <= 40:
                    rect_1 = (self.x + self.sukam, self.y + self.sukam, self.weight + self.sukam,
                              self.height + self.sukam)
                    rect_2 = (self.x, self.y, self.weight, self.height)
                    ellipse_1 = pg.draw.ellipse(display, self.second_color, rect_1)
                    # ellipse_2 = pg.draw.ellipse(display, self.color, rect_2)
                    text_but = Font(self.message_x, self.message_y, self.actived_color, self.font_size,
                                    message=self.message)
                    text_but.draw_text()
                    self.sukam += 2
                else:
                    rect_1 = (self.x + self.sukam, self.y + self.sukam, self.weight + self.sukam,
                              self.height + self.sukam)
                    rect_2 = (self.x, self.y, self.weight, self.height)
                    # ellipse_1 = pg.draw.ellipse(display, self.color, rect_1)
                    ellipse_2 = pg.draw.ellipse(display, self.color, rect_2)
                    text_but = Font(self.message_x, self.message_y, self.actived_color, self.font_size,
                                    message=self.message)
                    text_but.draw_text()
                self.action = True
            else:
                if self.sukam <= 40:
                    rect_1 = (self.x - self.sukam, self.y - self.sukam, self.weight + self.sukam * 2,
                              self.height + self.sukam * 2)
                    rect_2 = (self.x, self.y, self.weight, self.height)
                    ellipse_1 = pg.draw.ellipse(display, self.second_color, rect_1)
                    ellipse_2 = pg.draw.ellipse(display, self.color, rect_2)
                    text_but = Font(self.message_x, self.message_y, self.active_color, self.font_size,
                                    message=self.message)
                    text_but.draw_text()
                    self.sukam += 4
                else:
                    rect_1 = (self.x + self.sukam, self.y + self.sukam, self.weight + self.sukam * 2,
                              self.height + self.sukam * 2)
                    rect_2 = (self.x, self.y, self.weight, self.height)
                    ellipse_1 = pg.draw.ellipse(display, self.color, rect_1)
                    ellipse_2 = pg.draw.ellipse(display, self.second_color, rect_2)
                    text_but = Font(self.message_x, self.message_y, self.active_color, self.font_size,
                                    message=self.message)
                    text_but.draw_text()
                self.action = False
        else:
            rect_1 = (self.x, self.y, self.weight, self.height)
            ellipse_1 = pg.draw.ellipse(display, self.color, rect_1)
            text_but = Font(self.message_x, self.message_y, self.font_color, self.font_size, message=self.message)
            text_but.draw_text()
            self.action = False
        return self.action


class Window_ok:
    def __init__(self, x, y, weight, height, bg_color, line_ac_color, line_non_color, color_ok, color_non_ok, ok, width,
                 act=False):
        self.x = x
        self.y = y
        self.weight = weight
        self.height = height
        self.bg_color = bg_color
        self.line_ac = line_ac_color
        self.line_non = line_non_color
        self.color_ok = color_ok
        self.color_non = color_non_ok
        self.ok = ok
        self.width = width
        self.x_c = int(self.x + self.weight / 2)
        self.y_c = int(self.y + self.height / 2)
        self.action = act

    def draw(self):
        rect_mod = (self.x, self.y, self.weight, self.height)
        rect = pg.draw.rect(display, self.bg_color, rect_mod)
        mouse = pg.mouse.get_pos()
        click = pg.mouse.get_pressed()
        if self.x < mouse[0] < self.x + self.weight and self.y < mouse[1] < self.y + self.height:
            if click[0] == 1 and self.x < mouse[0] < self.x + self.weight and self.y < mouse[1] < self.y + self.height:
                self.ok = True
                self.action = True
            if self.ok:
                line_o = pg.draw.line(display, self.color_ok,
                                      [int(self.x_c - self.weight * (1 / 3)), int(self.y_c - self.height * (1 / 16))],
                                      [int(self.x_c + self.weight * (1 / 16)), int(self.y_c + self.height * (1 / 3))],
                                      self.width)
                line_k = pg.draw.line(display, self.color_ok,
                                      [int(self.x_c + self.weight * (1 / 4.5)),
                                       int(self.y_c - self.height * (1 / 2.5))],
                                      [int(self.x_c + self.weight * (1 / 16)), int(self.y_c + self.height * (1 / 3))],
                                      self.width)
            top_line = pg.draw.line(display, self.line_ac, [self.x, self.y], [self.x + self.weight, self.y])
            top_right = pg.draw.line(display, self.line_ac, [self.x + self.weight, self.y],
                                     [self.x + self.weight, self.y + self.height])
            top_left = pg.draw.line(display, self.line_ac, [self.x, self.y], [self.x, self.y + self.height])
            top_line = pg.draw.line(display, self.line_ac, [self.x, self.y + self.height],
                                    [self.x + self.weight, self.y + self.height])
        else:
            if self.ok:
                line_o = pg.draw.line(display, self.color_non,
                                      [int(self.x_c - self.weight * (1 / 3)), int(self.y_c - self.height * (1 / 16))],
                                      [int(self.x_c + self.weight * (1 / 16)), int(self.y_c + self.height * (1 / 3))],
                                      self.width)
                line_k = pg.draw.line(display, self.color_non,
                                      [int(self.x_c + self.weight * (1 / 4.5)),
                                       int(self.y_c - self.height * (1 / 2.5))],
                                      [int(self.x_c + self.weight * (1 / 16)), int(self.y_c + self.height * (1 / 3))],
                                      self.width)
            top_line = pg.draw.line(display, self.line_non, [self.x, self.y], [self.x + self.weight, self.y])
            top_right = pg.draw.line(display, self.line_non, [self.x + self.weight, self.y],
                                     [self.x + self.weight, self.y + self.height])
            top_left = pg.draw.line(display, self.line_non, [self.x, self.y], [self.x, self.y + self.height])
            top_line = pg.draw.line(display, self.line_non, [self.x, self.y + self.height],
                                    [self.x + self.weight, self.y + self.height])


class Font:  # Класс текста
    def __init__(self, x, y, font_color=(0, 0, 0), font_size=30, font_type='shrift\Main_math.otf',
                 message=None):  # инит переменные текста
        self.x = x
        self.y = y
        self.font_color = font_color
        self.font_type = font_type
        self.font_size = font_size
        self.message = message

    def draw_text(self):
        font_type = pg.font.Font(self.font_type, self.font_size)
        text = font_type.render(self.message, True, self.font_color)
        display.blit(text, (self.x, self.y))


def draw_okay(x, y, radius, color=(0, 255, 0), second_color=(255, 255, 255), width=int(__SIZE[1] / (600 / 10))):
    circle = pg.draw.circle(display, color, (x, y), radius)
    line_1 = pg.draw.line(display, ANTI_VERSION_SCORE_COLOR, [int(x - 1 / 2 * radius), int(y + 1 / 8 * radius)],
                          [int(x - 1 / 8 * radius),
                           int(y + 1 / 1.5 * radius)], width)
    line_2 = pg.draw.line(display, ANTI_VERSION_SCORE_COLOR, [int(x + 1 / 4 * radius), int(y - 1 / 2 * radius)],
                          [int(x - 1 / 8 * radius),
                           int(y + 1 / 1.5 * radius)], width)


def draw_no_okay(x, y, radius, color=(255, 0, 0), second_color=(255, 255, 255), width=int(__SIZE[1] / (600 / 10))):
    circle = pg.draw.circle(display, color, (x, y), radius)
    line_1 = pg.draw.line(display, ANTI_VERSION_SCORE_COLOR, [int(x - (2 / 4) * radius), int(y - (2 / 4) * radius)],
                          [int(x + (2 / 4) * radius), int(y + (2 / 4) * radius)], width)
    line_2 = pg.draw.line(display, ANTI_VERSION_SCORE_COLOR, [int(x + (2 / 4) * radius), int(y - (2 / 4) * radius)],
                          [int(x - (2 / 4) * radius), int(y + (2 / 4) * radius)], width)


def draw_triangle(a, b, c, k, color):
    triangle = pg.draw.polygon(display, color, [a, b, c])


def draw_circle(centre, r, color):
    circle = pg.draw.circle(display, color, centre, r)


def draw_rect(x, y, weight, height, color):
    rect = pg.draw.rect(display, color, (x, y, weight, height))


def draw_exit(cikl):
    h = 2
    if pg.mouse.get_pressed()[0] == 1:
        pg.time.wait(50)
    mouse = pg.mouse.get_pos()
    click = pg.mouse.get_pressed()
    if 20 < mouse[0] < 140 and 20 < mouse[1] < 50:
        if click[0] == 1:
            if h < 10:
                main_line = pg.draw.line(display, COLOR_EXIT_DRAW_1, [20, 40], [140, 40], 6 + h)
                top_line = pg.draw.line(display, COLOR_EXIT_DRAW_1, [20, 40], [60, 20], 6 + h)
                down_line = pg.draw.line(display, COLOR_EXIT_DRAW_1, [20, 40], [60, 60], 6 + h)
                h += 1
            else:
                main_line = pg.draw.line(display, COLOR_EXIT_DRAW_1, [20, 40], [140, 40], 6 + h)
                top_line = pg.draw.line(display, COLOR_EXIT_DRAW_1, [20, 40], [60, 20], 6 + h)
                down_line = pg.draw.line(display, COLOR_EXIT_DRAW_1, [20, 40], [60, 60], 6 + h)
            pg.time.wait(400)
            cikl = False
        else:
            if h < 10:
                main_line = pg.draw.line(display, COLOR_EXIT_DRAW_1, [20, 40], [140, 40], 6 + h)
                top_line = pg.draw.line(display, COLOR_EXIT_DRAW_1, [20, 40], [60, 20], 6 + h)
                down_line = pg.draw.line(display, COLOR_EXIT_DRAW_1, [20, 40], [60, 60], 6 + h)
                main_line_1 = pg.draw.line(display, COLOR_EXIT_DRAW_2, [20, 40], [140, 40], 6)
                top_line_1 = pg.draw.line(display, COLOR_EXIT_DRAW_2, [20, 40], [60, 20], 6)
                down_line_1 = pg.draw.line(display, COLOR_EXIT_DRAW_2, [20, 40], [60, 60], 6)
                h += 1
            else:
                main_line = pg.draw.line(display, COLOR_EXIT_DRAW_1, [20, 40], [140, 40], 6 + h)
                top_line = pg.draw.line(display, COLOR_EXIT_DRAW_1, [20, 40], [60, 20], 6 + h)
                down_line = pg.draw.line(display, COLOR_EXIT_DRAW_1, [20, 40], [60, 60], 6 + h)
                main_line_1 = pg.draw.line(display, COLOR_EXIT_DRAW_2, [20, 40], [140, 40], 6)
                top_line_1 = pg.draw.line(display, COLOR_EXIT_DRAW_2, [20, 40], [60, 20], 6)
                down_line_1 = pg.draw.line(display, COLOR_EXIT_DRAW_2, [20, 40], [60, 60], 6)
    else:
        main_line = pg.draw.line(display, COLOR_EXIT_DRAW_2, [20, 40], [140, 40], 6)
        top_line = pg.draw.line(display, COLOR_EXIT_DRAW_2, [20, 40], [60, 20], 6)
        down_line = pg.draw.line(display, COLOR_EXIT_DRAW_2, [20, 40], [60, 60], 6)
    return cikl


class Entry_text:
    def __init__(self, bg_color, font_color, line_color, text, font_size, font_type, x, y, weight, height,
                 active_line_color, need_input, text_x, text_y):
        self.bg_color = bg_color
        self.font_color = font_color
        self.line_color = line_color
        self.text = text
        self.font_size = font_size
        self.font_type = font_type
        self.x = x
        self.y = y
        self.weight = weight
        self.height = height
        self.active_line_color = active_line_color
        self.need_input = need_input
        self.text_x = text_x
        self.text_y = text_y

    def draw(self):
        click = pg.mouse.get_pressed()
        mouse = pg.mouse.get_pos()
        if click[0] == 1 and self.x < mouse[0] < self.x + self.weight and self.y < mouse[1] < self.y + self.height:
            self.need_input = True
        if click[0] == 1 and not (
                self.x < mouse[0] < self.x + self.weight and self.y < mouse[1] < self.y + self.height):
            self.need_input = False
        rect_1 = (self.x, self.y, self.weight, self.height)
        rect = pg.draw.rect(display, self.bg_color, rect_1)
        if self.need_input:
            left_line = pg.draw.line(display, self.active_line_color, [self.x, self.y], [self.x, self.y + self.height],
                                     6)
            top_line = pg.draw.line(display, self.active_line_color, [self.x, self.y], [self.x + self.weight, self.y],
                                    6)
            down_line = pg.draw.line(display, self.active_line_color, [self.x, self.y + self.height],
                                     [self.x + self.weight, self.y + self.height], 6)
            right_line = pg.draw.line(display, self.active_line_color, [self.x + self.weight, self.y],
                                      [self.x + self.weight,
                                       self.y + self.height], 6)
        else:
            left_line = pg.draw.line(display, self.line_color, [self.x, self.y], [self.x, self.y + self.height], 8)
            top_line = pg.draw.line(display, self.line_color, [self.x, self.y], [self.x + self.weight, self.y], 8)
            down_line = pg.draw.line(display, self.line_color, [self.x, self.y + self.height],
                                     [self.x + self.weight, self.y + self.height], 8)
            right_line = pg.draw.line(display, self.line_color, [self.x + self.weight, self.y],
                                      [self.x + self.weight, self.y + self.height], 8)
        text_font = Font(self.text_x, self.text_y, self.font_color, self.font_size, self.font_type, self.text)
        text_font.draw_text()


class Example:
    def __init__(self, __SIZE, font_type='shrift/ex.otf', font_size=30, font_color=ANTI_VERSION_SCORE_COLOR,
                 result=None, answer=None, vibor=[EX_1, EX_2]):
        self.__SIZE = __SIZE
        self.result = result
        self.answer = answer
        self.font_type = font_type
        self.font_size = int(self.__SIZE[1] / (600 / 40))
        self.font_color = font_color
        self.str_example = None
        self.vibor = vibor
        self.score = 1
        if LANG == 1:
            self.solve = 'Solve the equation :'
        elif LANG == 2:
            self.solve = 'Решите уравнение :'

    def draw(self):
        font_primer = Font(int(self.__SIZE[0] / (800 / 120)), int(self.__SIZE[1] / (800 / 200)),
                           self.font_color, self.font_size, self.font_type, self.str_example)
        font_primer.draw_text()

    def generaite_5_1(self):
        gen_type = rand.randint(1, 2)
        ready = False
        self.score = 1
        # Сложение вычитание нат. чисел
        if gen_type == 1:
            numb_one = rand.randint(10, 50)
            numb_two = rand.randint(10, 50)
            self.result = numb_one + numb_two
            self.str_example = str(numb_one) + ' + ' + str(numb_two) + ' ='
        elif gen_type == 2:
            while not ready:
                numb_one = rand.randint(10, 50)
                numb_two = rand.randint(10, 50)
                if numb_one - numb_two > 0:
                    ready = True
            self.result = numb_one - numb_two
            self.str_example = str(numb_one) + ' - ' + str(numb_two) + ' ='

    def generaite_5_2(self):
        self.score = 3
        gen_type = rand.randint(1, 4)
        ready = False
        # Сложение вычитание нат. чисел
        if gen_type == 1:
            numb_one = rand.randint(50, 200)
            numb_two = rand.randint(50, 200)
            self.result = numb_one + numb_two
            self.str_example = str(numb_one) + ' + ' + str(numb_two) + ' ='
        elif gen_type == 2:
            while not ready:
                numb_one = rand.randint(50, 100)
                numb_two = rand.randint(50, 100)
                if numb_one - numb_two > 0:
                    ready = True
            self.result = numb_one - numb_two
            self.str_example = str(numb_one) + ' - ' + str(numb_two) + ' ='
        elif gen_type == 3:
            numb_one = rand.randint(2, 10)
            numb_two = rand.randint(2, 10)
            self.result = numb_one * numb_two
            self.str_example = str(numb_one) + ' X ' + str(numb_two) + ' ='
        elif gen_type == 4:
            ready = True
            while ready:
                self.result = rand.randint(2, 10)
                numb_one = rand.randint(2, 10)
                numb_two = numb_one * self.result
                her = numb_two % numb_one
                if her == 0:
                    ready = False
            self.str_example = str(numb_two) + ' : ' + str(numb_one) + ' ='

    def generaite_5_3(self):
        self.score = 5
        gen_type = rand.randint(1, 4)
        ready = False
        # Сложение вычитание нат. чисел
        if gen_type == 1:
            numb_one = rand.randint(100, 300)
            numb_two = rand.randint(100, 200)
            self.result = numb_one + numb_two
            self.str_example = str(numb_one) + ' + ' + str(numb_two) + ' ='
        elif gen_type == 2:
            while not ready:
                numb_one = rand.randint(100, 200)
                numb_two = rand.randint(90, 130)
                if numb_one - numb_two > 0:
                    ready = True
            self.result = numb_one - numb_two
            self.str_example = str(numb_one) + ' - ' + str(numb_two) + ' ='
        elif gen_type == 3:
            numb_one = rand.randint(5, 20)
            numb_two = rand.randint(2, 10)
            self.result = numb_one * numb_two
            self.str_example = str(numb_one) + ' X ' + str(numb_two) + ' ='
        elif gen_type == 4:
            ready = True
            while ready:
                self.result = rand.randint(5, 15)
                numb_one = rand.randint(3, 10)
                numb_two = numb_one * self.result
                her = numb_two % numb_one
                if her == 0:
                    ready = False
            self.str_example = str(numb_two) + ' : ' + str(numb_one) + ' ='

    def generate_6_1(self):
        self.score = 1
        gen_type = rand.randint(1, 2)
        if gen_type == 1:
            ready = False
            while not ready:
                numb_one_o = str(rand.randint(1, 10))
                numb_one_t = str(rand.randint(1, 10))
                numb_one = float(numb_one_o + '.' + numb_one_t)
                numb_one_o = str(rand.randint(1, 10))
                numb_one_t = str(rand.randint(1, 10))
                numb_two = float(numb_one_o + '.' + numb_one_t)
                if numb_one + numb_two < 10 and len(str(numb_one + numb_two)) < 10:
                    ready = True
            self.result = numb_one + numb_two
            self.str_example = str(numb_one) + ' + ' + str(numb_two) + ' ='
        elif gen_type == 2:
            ready = False
            while not ready:
                numb_one_o = str(rand.randint(1, 10))
                numb_one_t_1 = str(rand.randint(1, 10))
                numb_one = float(numb_one_o + '.' + numb_one_t_1)
                numb_one_o = str(rand.randint(1, 10))
                numb_one_t = str(rand.randint(1, 10))
                numb_two = float(numb_one_o + '.' + numb_one_t)
                if numb_one - numb_two > 0 and len(str(numb_one - numb_two)) < 10 and float(numb_one_t_1) > float(
                        numb_one_t):
                    ready = True
            self.result = numb_one - numb_two
            self.str_example = str(numb_one) + ' - ' + str(numb_two) + ' ='

    def generaite_6_2(self):
        self.score = 3
        gen_type = rand.randint(1, 2)
        if gen_type == 1:
            ready = False
            while not ready:
                numb_one_o = str(rand.randint(4, 10))
                numb_one_t = str(rand.randint(10, 100))
                numb_one = float(numb_one_o + '.' + numb_one_t)
                numb_one_o = str(rand.randint(2, 10))
                numb_one_t = str(rand.randint(1, 10))
                numb_two = float(numb_one_o + '.' + numb_one_t)
                if numb_one + numb_two < 10 and len(str(numb_one + numb_two)) < 10:
                    ready = True
            self.result = numb_one + numb_two
            self.str_example = str(numb_one) + ' + ' + str(numb_two) + ' ='
        elif gen_type == 2:
            ready = False
            while not ready:
                numb_one_o = str(rand.randint(4, 20))
                numb_one_t_1 = str(rand.randint(1, 10))
                numb_one = float(numb_one_o + '.' + numb_one_t_1)
                numb_one_o = str(rand.randint(2, 10))
                numb_one_t = str(rand.randint(10, 100))
                numb_two = float(numb_one_o + '.' + numb_one_t)
                if numb_one - numb_two > 0 and len(str(numb_one - numb_two)) < 10 and float(numb_one_t_1 * 10) > float(
                        numb_one_t):
                    ready = True
            self.result = numb_one - numb_two
            self.str_example = str(numb_one) + ' - ' + str(numb_two) + ' ='

    def generaite_6_3(self):
        self.score = 5
        gen_type = rand.randint(1, 10)
        if gen_type == 1:
            ready = False
            while not ready:
                numb_one_o = str(rand.randint(10, 30))
                numb_one_t = str(rand.randint(10, 100))
                numb_one = float(numb_one_o + '.' + numb_one_t)
                numb_one_o = str(rand.randint(2, 10))
                numb_one_t_1 = str(rand.randint(100, 1000))
                numb_two = float(numb_one_o + '.' + numb_one_t_1)
                if numb_one + numb_two < 100 and len(str(numb_one + numb_two)) < 1000 and int(numb_one_t) * 10 + int(
                        numb_one_t_1) < 1000:
                    ready = True
            self.result = numb_one + numb_two
            if len(str(self.result)) > 8:
                self.result = float(format(self.result, '.3f'))
            self.str_example = str(numb_one) + ' + ' + str(numb_two) + ' ='
        elif gen_type == 2:
            ready = False
            while not ready:
                numb_one_o = str(rand.randint(10, 30))
                numb_one_t_1 = str(rand.randint(10, 100))
                numb_one = float(numb_one_o + '.' + numb_one_t_1)
                numb_one_o = str(rand.randint(2, 10))
                numb_one_t = str(rand.randint(100, 1000))
                numb_two = float(numb_one_o + '.' + numb_one_t)
                if numb_one - numb_two > 0 and len(str(numb_one - numb_two)) < 1000 and float(
                        numb_one_t_1) / 10 > float(
                    numb_one_t) / 100:
                    ready = True
            self.result = numb_one - numb_two
            if len(str(self.result)) > 5:
                self.result = float(format(self.result, '.3f'))
            self.str_example = str(numb_one) + ' - ' + str(numb_two) + ' ='
        elif gen_type == 3:
            x = rand.randint(1, 10)
            self.result = x
            a = rand.randint(2, 25)
            b = rand.randint(20, 50)
            c = x * a + b
            self.str_example = self.solve + ' ' + str(a) + 'x' + ' + ' + str(b) + ' = ' + str(c)
        elif gen_type == 4:
            x = rand.randint(1, 10)
            self.result = x
            a = rand.randint(2, 25)
            b = rand.randint(20, 50)
            c = x * a - b
            self.str_example = self.solve + ' ' + str(a) + 'x' + ' - ' + str(b) + ' = ' + str(c)
        elif gen_type == 5:
            x = rand.randint(1, 10)
            self.result = x
            a = rand.randint(2, 25)
            b = rand.randint(20, 50)
            c = x * (a * (-1)) + b
            self.str_example = self.solve + ' -' + str(a) + 'x' + ' + ' + str(b) + ' = ' + str(c)
        elif gen_type == 6:
            x = rand.randint(1, 10)
            self.result = x
            a = rand.randint(2, 20)
            b = rand.randint(20, 50)
            c = x * a * (-1) + b * (-1)
            self.str_example = self.solve + ' -' + str(a) + 'x' + ' - ' + str(b) + ' = ' + str(c)
        elif gen_type == 7:
            x = rand.randint(1, 10)
            self.result = x
            a = rand.randint(2, 25)
            b = rand.randint(20, 50)
            c = x * a - b
            self.str_example = self.solve + ' ' + str(a) + 'x' + ' = ' + str(c) + ' + ' + str(b)
        elif gen_type == 8:
            x = rand.randint(1, 10)
            self.result = x
            a = rand.randint(2, 25)
            b = rand.randint(20, 50)
            c = x * a + b
            self.str_example = self.solve + ' ' + str(a) + 'x' + ' = ' + str(c) + ' - ' + str(b)
        elif gen_type == 9:
            x = rand.randint(1, 10)
            self.result = x
            a = rand.randint(2, 15)
            b = rand.randint(20, 40)
            c = x * a * (-1) - b
            self.str_example = self.solve + ' -' + str(a) + 'x' + ' = ' + str(c) + ' + ' + str(b)
        elif gen_type == 10:
            x = rand.randint(1, 10)
            self.result = x
            a = rand.randint(2, 15)
            b = rand.randint(20, 40)
            c = x * a * (-1) + b
            self.str_example = self.solve + ' -' + str(a) + 'x' + ' = ' + str(c) + ' + ' + str(b)

    def bool_pr(self, answer):
        if self.result == float(answer):
            return True
        else:
            return False

    def gen_ex(self):
        self.vibor = [EX_1, EX_2]
        if self.vibor[0] == 5:
            if self.vibor[1] == 1:
                self.generaite_5_1()
            elif self.vibor[1] == 2:
                self.generaite_5_2()
            elif self.vibor[1] == 3:
                self.generaite_5_3()
        elif self.vibor[0] == 6:
            if self.vibor[1] == 1:
                self.generate_6_1()
            elif self.vibor[1] == 2:
                self.generaite_6_2()
            elif self.vibor[1] == 3:
                self.generaite_6_3()


def draw_vk(x, y, weight, height, ready):
    color_1 = (51, 61, 171)
    color_2 = (96, 107, 224)
    color_3 = (223, 224, 242)
    color_4 = (173, 177, 219)
    rect_1 = (x, y, weight, height)
    click = pg.mouse.get_pressed()
    mouse = pg.mouse.get_pos()
    if mouse[0] > x and mouse[0] < x + weight and mouse[1] > y and mouse[1] < y + height:
        if click[0] == 1 and ready:
            web.open('https://vk.com/public200658818', new=2)
            ready = False
        rect = pg.draw.rect(display, color_2, rect_1)
        line_font = Font(x, y + int(1 / 3.5 * height), color_3, int(height / (50 / 30)), message='VK')
        line_font.draw_text()
        pg.time.wait(100)
    else:
        rect = pg.draw.rect(display, color_1, rect_1)
        line_font = Font(x, y + int(1 / 3.5 * height), color_4, int(height / (50 / 30)), message='VK')
        line_font.draw_text()
    return ready


def draw_dis(x, y, weight, height, ready):
    color_1 = (104, 61, 224)
    color_2 = (129, 92, 230)
    color_3 = (223, 224, 242)
    color_4 = (173, 177, 219)
    rect_1 = (x, y, weight, height)
    click = pg.mouse.get_pressed()
    mouse = pg.mouse.get_pos()
    if mouse[0] > x and mouse[0] < x + weight and mouse[1] > y and mouse[1] < y + height:
        if click[0] == 1 and ready:
            web.open('https://discord.gg/D5RVaHXcZu', new=2)
            ready = False
        rect = pg.draw.rect(display, color_2, rect_1)
        line_font = Font(x + int(weight * 1 / 12), y + int(1 / 3.5 * height), color_3, int(height / (50 / 30)),
                         message='DS')
        line_font.draw_text()
        pg.time.wait(100)
    else:
        rect = pg.draw.rect(display, color_1, rect_1)
        line_font = Font(x + int(weight * 1 / 12), y + int(1 / 3.5 * height), color_4, int(height / (50 / 30)),
                         message='DS')
        line_font.draw_text()
    return ready


def main_menu():
    show_menu = True
    while show_menu:
        event = pg.event.poll()
        if event.type == pg.QUIT:
            output_settings()
        display.fill(COLOR_DISPLAY)
        x_main_text = int(__SIZE[0] / 2 - int((170 / 800) * __SIZE[0]))
        font = int(__SIZE[1] / (600 / 40))
        main_text = Font(x_main_text, int(__SIZE[1] / 24), MAIN_COLOR_FONT, message='Math Trainer', font_size=font)
        version_text = Font(int(__SIZE[0] - 234), int(__SIZE[1] / 1.03), COLOR_VERSION_SCORE,
                            message='Beta Version: 0.0.5', \
                            font_size=20)
        button_play = Button(int(__SIZE[0] / 2 - (__SIZE[0] / 8)), int(__SIZE[1] / 6.4), int(__SIZE[0] / 4),
                             int(__SIZE[1] / 12), COLOR_BUTTON_1, 'Play',
                             font_type='/shrift/play_menu.otf', active_color=ACTIVE_COLOR,
                             actived_color=MAIN_COLOR_FONT,
                             font_size=int(__SIZE[1] / 24),
                             message_x=int(__SIZE[0] / 2 - (35 / 800) * __SIZE[0]),
                             message_y=int(__SIZE[1] / 6.4 + int(__SIZE[1] / (80 / 1.2))), second_color=COLOR_BUTTON_2)
        button_level = Button(int(__SIZE[0] / 2 - (__SIZE[0] / 8)), int(__SIZE[1] / 3.55555556), int(__SIZE[0] / 4),
                              int(__SIZE[1] / 12),
                              COLOR_BUTTON_1, 'Level', font_size=int(__SIZE[1] / 24),
                              font_type='/shrift/play_menu.otf', active_color=ACTIVE_COLOR,
                              actived_color=MAIN_COLOR_FONT,
                              message_x=int(__SIZE[0] / 2 - (40 / 800) * __SIZE[0]),
                              message_y=int(__SIZE[1] / 3.5555555556 + int(__SIZE[1] / (80 / 1.2))),
                              second_color=COLOR_BUTTON_2)
        button_achivment = Button(int(__SIZE[0] / 2 - (__SIZE[0] / 8)), int(__SIZE[1] / (800 / 325)),
                                  int(__SIZE[0] / 4), int(__SIZE[1] / 12),
                                  COLOR_BUTTON_1, 'Achivment', font_size=int(__SIZE[1] / 30),
                                  font_type='/shrift/play_menu.otf', active_color=ACTIVE_COLOR,
                                  actived_color=MAIN_COLOR_FONT,
                                  message_x=int(__SIZE[0] / 2 - (65 / 800) * __SIZE[0]),
                                  message_y=int(__SIZE[1] / (800 / 325) + int(__SIZE[1] / (80 / 1.2))),
                                  second_color=COLOR_BUTTON_2)
        button_anygames = Button(int(__SIZE[0] / 2 - (__SIZE[0] / 8)), int(__SIZE[1] / (800 / 425)), int(__SIZE[0] / 4),
                                 int(__SIZE[1] / 12), COLOR_BUTTON_1,
                                 'Any Games', font_size=int(__SIZE[1] / 30),
                                 font_type='/shrift/play_menu.otf', active_color=ACTIVE_COLOR,
                                 actived_color=MAIN_COLOR_FONT,
                                 message_x=int(__SIZE[0] / 2 - (60 / 800) * __SIZE[0]),
                                 message_y=int(__SIZE[1] / (800 / 425) + int(__SIZE[1] / (80 / 1.2))),
                                 second_color=COLOR_BUTTON_2)
        button_help = Button(0, 0, int(__SIZE[0] / (800 / 75)), int(__SIZE[1] / (600 / 75)), COLOR_BUTTON_SETUP_1, 'H',
                             BLACK_COLOR,
                             font_type='shrift/play_menu.otf', active_color=MAIN_COLOR_FONT,
                             actived_color=COLOR_BUTTON_2,
                             message_x=int(__SIZE[0] / (800 / 75) / 2 - int((24 / 800) * __SIZE[0])),
                             message_y=int(__SIZE[1] / 0.8 / 80), second_color=COLOR_BUTTON_SETUP_2,
                             font_size=int(__SIZE[1] / 10))
        button_setup = Button(int(__SIZE[0] / (800 / 725)), 0, int(__SIZE[0] / (800 / 75)), int(__SIZE[1] / (600 / 75)),
                              COLOR_BUTTON_SETUP_1,
                              message='S', font_color=BLACK_COLOR, font_type='shrift/play_menu.otf',
                              active_color=MAIN_COLOR_FONT,
                              actived_color=COLOR_BUTTON_2,
                              message_x=int(__SIZE[0] - (__SIZE[0] / (800 / 75) / 2) - int((1 / 40) * __SIZE[0])),
                              message_y=int(__SIZE[1] / 0.8 / 80),
                              second_color=COLOR_BUTTON_SETUP_2, font_size=int(__SIZE[1] / 10))
        button_setup.draw()
        button_help.draw()
        button_achivment.draw()
        button_anygames.draw()
        button_level.draw()
        draw_triangle([0, __SIZE[1]], [int(__SIZE[0] / (800 / 200)), __SIZE[1]],
                      [int(__SIZE[0] / (800 / 100)), int(__SIZE[1] / (600 / 400))], 'k', color=FIRST_FIGURE_COLOR)
        draw_circle([int(__SIZE[0] / (800 / 100)), int(__SIZE[1] / (600 / 360))], int(__SIZE[0] / (800 / 50)),
                    THRE_FIGURE_COLOR)
        button_play.draw()
        version_text.draw_text()
        main_text.draw_text()
        pg.display.update()
        if button_play.action:
            pg.time.wait(50)
            start_play()
        elif button_setup.action:
            pg.time.wait(50)
            setup_menu_start()
        elif button_level.action:
            pg.time.wait(50)
            start_level()
        elif button_achivment.action:
            pg.time.wait(50)
            achivment()
        elif button_help.action:
            pg.time.wait(50)
            help()
        elif button_anygames.action:
            pg.time.wait(50)
            any_game_menu_eng()
        if Exit:
            show_menu = False


def help():
    h = 0
    k = 0
    ready1 = True
    ready2 = True
    show_menu_help = True
    font_vk = Font(int(__SIZE[0] / (800 / 100)), int(__SIZE[1] / (600 / 225)), COLOR_VERSION_SCORE,
                   int(__SIZE[1] / (600 / 20)),
                   message='Click here that check our Vk')
    font_ds = Font(int(__SIZE[0] / (800 / 100)), int(__SIZE[1] / (600 / 350)), COLOR_VERSION_SCORE,
                   int(__SIZE[1] / (600 / 20)),
                   message='Click here that check our Discord')
    main_text_font = Font(int(__SIZE[0] / (800 / 350)), int(__SIZE[1] / (600 / 20)), MAIN_COLOR_FONT,
                          int(__SIZE[1] / (600 / 40)),
                          message='Help')
    while show_menu_help:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                output_settings()
            if event.type == pg.VIDEOEXPOSE:
                ready1 = False
                ready2 = False
            elif event.type != pg.VIDEOEXPOSE:
                ready1 = True
                ready2 = True
        display.fill(COLOR_DISPLAY)
        get_code_eng()
        ready1 = draw_vk(int(__SIZE[0] / (800 / 500)), int(__SIZE[1] / (600 / 200)), int(__SIZE[0] / (800 / 50)),
                         int(__SIZE[0] / (800 / 50)), ready1)
        ready2 = draw_dis(int(__SIZE[0] / (800 / 560)), int(__SIZE[1] / (600 / 325)), int(__SIZE[0] / (800 / 50)),
                          int(__SIZE[0] / (800 / 50)), ready2)
        font_ds.draw_text()
        font_vk.draw_text()
        main_text_font.draw_text()
        show_menu_help = draw_exit(show_menu_help)
        pg.display.update()
        pg.time.wait(150)


def achivment():
    show_menu_achivment = True
    if SCORE >= 0 and SCORE < 500:
        rank = pg.image.load('image/iron.png')
        rank_name = 'Iron'
    elif SCORE >= 500 and SCORE < 1000:
        rank = pg.image.load('image/bronze.png')
        rank_name = 'Bronze'
    elif SCORE >= 1000 and SCORE < 2000:
        rank = pg.image.load('image/silver.png')
        rank_name = 'Silver'
    elif SCORE >= 2000 and SCORE < 3000:
        rank = pg.image.load('image/gold.png')
        rank_name = 'Gold'
    elif SCORE >= 3000 and SCORE < 5000:
        rank = pg.image.load('image/platium.png')
        rank_name = 'Platium'
    elif SCORE >= 5000 and SCORE < 10000:
        rank = pg.image.load('image/diamond.png')
        rank_name = 'Diamond'
    elif SCORE >= 10000 and SCORE < 20000:
        rank = pg.image.load('image/master.png')
        rank_name = 'Master'
    elif SCORE >= 20000 and SCORE < 100000:
        rank = pg.image.load('image/gr_master.png')
        rank_name = 'Grand-Master'
    elif SCORE >= 100000:
        rank = pg.image.load('image/legend.png')
        rank_name = 'Legend'
    elif SCORE == 666:
        rank = pg.image.load('image/belaz.png')
    text_1 = Font(int(__SIZE[0] / (800 / 280)), int(__SIZE[1] / (600 / 400)), COLOR_VERSION_SCORE,
                  int(__SIZE[1] / (600 / 34)),
                  message=f'Your rank is {rank_name}', font_type='shrift/math_prem.otf')
    text_2 = Font(int(__SIZE[0] / 2 - __SIZE[0] / (600 / 100)), int(__SIZE[1] / (600 / 440)), COLOR_VERSION_SCORE,
                  int(__SIZE[1] / (600 / 30)), message=f'Your score is {SCORE}', font_type='shrift/math_prem.otf')
    while show_menu_achivment:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                output_settings()
        display.fill(COLOR_DISPLAY)
        rank_rect = rank.get_rect(center=(int(__SIZE[0] / 2), int(__SIZE[1] / 2 - __SIZE[1] / (600 / 100))))
        text_1.draw_text()
        text_2.draw_text()
        display.blit(rank, rank_rect)
        show_menu_achivment = draw_exit(show_menu_achivment)
        pg.display.update()


def setup_lang():
    global LANG
    show_menu_lang_setup = True
    ok_1 = False
    ok_2 = False
    if LANG == 1:
        ok_1 = True
    elif LANG == 2:
        ok_2 = True
    okey_1 = Window_ok(int(__SIZE[0] / 2 - (__SIZE[0] / 4)) + int(__SIZE[0] / 2) - int(__SIZE[0] / (800 / 50)),
                       int(__SIZE[1] / (800 / 175)), int(__SIZE[0] / (800 / 50)), int(__SIZE[1] / (600 / 50)),
                       ANTI_VERSION_SCORE_COLOR,
                       ACTIVE_COLOR, COLOR_VERSION_SCORE, ACTIVE_COLOR, COLOR_VERSION_SCORE, ok_1, 5)
    okey_2 = Window_ok(int(__SIZE[0] / 2 - (__SIZE[0] / 4)) + int(__SIZE[0] / 2) - int(__SIZE[0] / (800 / 50)),
                       int(__SIZE[1] / (800 / 375)), int(__SIZE[0] / (800 / 50)), int(__SIZE[1] / (600 / 50)),
                       ANTI_VERSION_SCORE_COLOR,
                       ACTIVE_COLOR, COLOR_VERSION_SCORE, ACTIVE_COLOR, COLOR_VERSION_SCORE, ok_2, 5)
    button_eng = Button_rect(int(__SIZE[0] / 2 - (__SIZE[0] / 4)), int(__SIZE[1] / (800 / 175)),
                             int(__SIZE[0] / 2),
                             int(__SIZE[1] / 12), COLOR_SETUP_MENU_1, 'English',
                             font_type='/shrift/play_menu.otf', active_color=MAIN_COLOR_FONT,
                             actived_color=MAIN_COLOR_FONT,
                             font_size=int(__SIZE[1] / 24),
                             message_x=int(__SIZE[0] / 2 - (200 / 800) * __SIZE[0]),
                             message_y=int(__SIZE[1] / (800 / 190)),
                             second_color=COLOR_BUTTON_2)
    button_rus = Button_rect(int(__SIZE[0] / 2 - (__SIZE[0] / 4)), int(__SIZE[1] / (800 / 375)), int(__SIZE[0] / 2),
                             int(__SIZE[1] / 12), COLOR_SETUP_MENU_1, 'Russian',
                             font_type='/shrift/play_menu.otf', active_color=MAIN_COLOR_FONT,
                             actived_color=MAIN_COLOR_FONT,
                             font_size=int(__SIZE[1] / 24),
                             message_x=int(__SIZE[0] / 2 - (200 / 800) * __SIZE[0]),
                             message_y=int(__SIZE[1] / (800 / 390)),
                             second_color=COLOR_BUTTON_2)
    main_sett_font = Font(int(__SIZE[0] / 2 - __SIZE[0] / (800 / 100)), int(__SIZE[1] / (800 / 40)),
                          message='Language',
                          font_size=int(__SIZE[1] / (800 / 50)), font_color=MAIN_COLOR_FONT)
    while show_menu_lang_setup:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                output_settings()
        display.fill(COLOR_DISPLAY)
        show_menu_lang_setup = draw_exit(show_menu_lang_setup)
        button_eng.draw()
        button_rus.draw()
        okey_1.draw()
        okey_2.draw()
        main_sett_font.draw_text()
        if okey_1.action:
            LANG = 1
            okey_2.ok = False
        elif okey_2.action:
            LANG = 2
            okey_1.ok = False
        pg.display.update()
        okey_1.action = False
        okey_2.action = False


def start_level():
    global EX_1
    button_5_class = Button_rect(int(__SIZE[0] / 2 - (__SIZE[0] / 4)), int(__SIZE[1] / (800 / 175)), int(__SIZE[0] / 2),
                                 int(__SIZE[1] / 12), COLOR_SETUP_MENU_1, '5 class',
                                 font_type='/shrift/play_menu.otf', active_color=MAIN_COLOR_FONT,
                                 actived_color=MAIN_COLOR_FONT,
                                 font_size=int(__SIZE[1] / 24),
                                 message_x=int(__SIZE[0] / 2 - (60 / 800) * __SIZE[0]),
                                 message_y=int(__SIZE[1] / (800 / 190)), second_color=COLOR_BUTTON_2)
    button_6_class = Button_rect(int(__SIZE[0] / 2 - (__SIZE[0] / 4)), int(__SIZE[1] / (800 / 375)), int(__SIZE[0] / 2),
                                 int(__SIZE[1] / 12), COLOR_SETUP_MENU_1, '6 class',
                                 font_type='/shrift/play_menu.otf', active_color=MAIN_COLOR_FONT,
                                 actived_color=MAIN_COLOR_FONT,
                                 font_size=int(__SIZE[1] / 24),
                                 message_x=int(__SIZE[0] / 2 - (50 / 800) * __SIZE[0]),
                                 message_y=int(__SIZE[1] / (800 / 390)),
                                 second_color=COLOR_BUTTON_2)
    button_7_class = Button_rect(int(__SIZE[0] / 2 - (__SIZE[0] / 4)), int(__SIZE[1] / (800 / 575)), int(__SIZE[0] / 2),
                                 int(__SIZE[1] / 12), COLOR_SETUP_MENU_1, '7 class',
                                 font_type='/shrift/play_menu.otf', active_color=MAIN_COLOR_FONT,
                                 actived_color=MAIN_COLOR_FONT,
                                 font_size=int(__SIZE[1] / 24),
                                 message_x=int(__SIZE[0] / 2 - (50 / 800) * __SIZE[0]),
                                 message_y=int(__SIZE[1] / (800 / 590)),
                                 second_color=COLOR_BUTTON_2)
    main_sett_font = Font(int(__SIZE[0] / 2 - __SIZE[0] / (800 / 220)), int(__SIZE[1] / (800 / 40)),
                          message='Chosse your class',
                          font_size=int(__SIZE[1] / (800 / 50)), font_color=MAIN_COLOR_FONT)
    show_menu_level = True
    while show_menu_level:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                output_settings()
        display.fill(COLOR_DISPLAY)
        show_menu_level = draw_exit(show_menu_level)
        button_5_class.draw()
        button_6_class.draw()
        main_sett_font.draw_text()
        pg.display.update()
        if button_5_class.action:
            EX_1 = 5
            menu_level_class()
        elif button_6_class.action:
            EX_1 = 6
            menu_level_class()


def menu_level_class():
    global EX_2
    show_menu_setup_five_class = True
    ok_1 = False
    ok_2 = False
    ok_3 = False
    if EX_2 == 1:
        ok_1 = True
    elif EX_2 == 2:
        ok_2 = True
    elif EX_2 == 3:
        ok_3 = True
    okey_1 = Window_ok(int(__SIZE[0] / 2 - (__SIZE[0] / 4)) + int(__SIZE[0] / 2) - int(__SIZE[0] / (800 / 50)),
                       int(__SIZE[1] / (800 / 175)), int(__SIZE[0] / (800 / 50)), int(__SIZE[1] / (600 / 50)),
                       ANTI_VERSION_SCORE_COLOR,
                       ACTIVE_COLOR, COLOR_VERSION_SCORE, ACTIVE_COLOR, COLOR_VERSION_SCORE, ok_1, 5)
    okey_2 = Window_ok(int(__SIZE[0] / 2 - (__SIZE[0] / 4)) + int(__SIZE[0] / 2) - int(__SIZE[0] / (800 / 50)),
                       int(__SIZE[1] / (800 / 375)), int(__SIZE[0] / (800 / 50)), int(__SIZE[1] / (600 / 50)),
                       ANTI_VERSION_SCORE_COLOR,
                       ACTIVE_COLOR, COLOR_VERSION_SCORE, ACTIVE_COLOR, COLOR_VERSION_SCORE, ok_2, 5)
    okey_3 = Window_ok(int(__SIZE[0] / 2 - (__SIZE[0] / 4)) + int(__SIZE[0] / 2) - int(__SIZE[0] / (800 / 50)),
                       int(__SIZE[1] / (800 / 575)), int(__SIZE[0] / (800 / 50)), int(__SIZE[1] / (600 / 50)),
                       ANTI_VERSION_SCORE_COLOR,
                       ACTIVE_COLOR, COLOR_VERSION_SCORE, ACTIVE_COLOR, COLOR_VERSION_SCORE, ok_3, 5)
    button_easy = Button_rect(int(__SIZE[0] / 2 - (__SIZE[0] / 4)), int(__SIZE[1] / (800 / 175)),
                              int(__SIZE[0] / 2),
                              int(__SIZE[1] / 12), COLOR_SETUP_MENU_1, 'Easy',
                              font_type='/shrift/play_menu.otf', active_color=MAIN_COLOR_FONT,
                              actived_color=MAIN_COLOR_FONT,
                              font_size=int(__SIZE[1] / 24),
                              message_x=int(__SIZE[0] / 2 - (200 / 800) * __SIZE[0]),
                              message_y=int(__SIZE[1] / (800 / 190)),
                              second_color=COLOR_BUTTON_2)
    button_medium = Button_rect(int(__SIZE[0] / 2 - (__SIZE[0] / 4)), int(__SIZE[1] / (800 / 375)), int(__SIZE[0] / 2),
                                int(__SIZE[1] / 12), COLOR_SETUP_MENU_1, 'Medium',
                                font_type='/shrift/play_menu.otf', active_color=MAIN_COLOR_FONT,
                                actived_color=MAIN_COLOR_FONT,
                                font_size=int(__SIZE[1] / 24),
                                message_x=int(__SIZE[0] / 2 - (200 / 800) * __SIZE[0]),
                                message_y=int(__SIZE[1] / (800 / 390)),
                                second_color=COLOR_BUTTON_2)
    button_hard = Button_rect(int(__SIZE[0] / 2 - (__SIZE[0] / 4)), int(__SIZE[1] / (800 / 575)), int(__SIZE[0] / 2),
                              int(__SIZE[1] / 12), COLOR_SETUP_MENU_1, 'Hard',
                              font_type='/shrift/play_menu.otf', active_color=MAIN_COLOR_FONT,
                              actived_color=MAIN_COLOR_FONT,
                              font_size=int(__SIZE[1] / 24),
                              message_x=int(__SIZE[0] / 2 - (200 / 800) * __SIZE[0]),
                              message_y=int(__SIZE[1] / (800 / 590)),
                              second_color=COLOR_BUTTON_2)
    main_sett_font_level = Font(int(__SIZE[0] / 2 - __SIZE[0] / (800 / 200)), int(__SIZE[1] / (800 / 40)),
                                message='Chosse level',
                                font_size=int(__SIZE[1] / (800 / 50)), font_color=MAIN_COLOR_FONT)
    while show_menu_setup_five_class:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                output_settings()
        display.fill(COLOR_DISPLAY)
        show_menu_setup_five_class = draw_exit(show_menu_setup_five_class)
        main_sett_font_level.draw_text()
        button_easy.draw()
        okey_1.draw()
        button_medium.draw()
        okey_2.draw()
        button_hard.draw()
        okey_3.draw()
        pg.display.update()
        theme_upload(THEME)
        if okey_2.action:
            okey_1.ok = False
            okey_3.ok = False
            EX_2 = 2
        elif okey_3.action:
            okey_1.ok = False
            okey_2.ok = False
            EX_2 = 3
        elif okey_1.action:
            okey_2.ok = False
            okey_3.ok = False
            EX_2 = 1
        okey_1.action = False
        okey_2.action = False
        okey_3.action = False


def start_play():
    button_go = False
    h = 0
    global SCORE
    draw_ok = False
    draw_notok = False
    valid = True
    show_play = True
    need_input = False
    input_text = ''
    score = SCORE
    okey = True
    need_generaite = True
    examp = Example(__SIZE)
    button_answer = Button_rect(int(__SIZE[0] / (800 / 250)), int(__SIZE[1] / (800 / 650)),
                                int(__SIZE[0] / (800 / 300)),
                                int(__SIZE[1] / (800 / 60)), COLOR_BUTTON_1, 'Answer', (0, 0, 0),
                                int(__SIZE[1] / (600 / 30)),
                                'shrift\math_prem1.ttf', (0, 0, 0), (0, 0, 0), int(__SIZE[0] / (800 / 330)),
                                int(__SIZE[1] / (800 / 660)), COLOR_BUTTON_2)
    while show_play:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                output_settings()
            if need_input and event.type == pg.KEYDOWN:
                if event.unicode == '1' or event.unicode == '2' or event.unicode == '3' or event.unicode == '4' or event.unicode == '5' \
                        or event.unicode == '6' or event.unicode == '7' or event.unicode == '8' or event.unicode == '9' or event.unicode == '0' \
                        or event.unicode == '.' or event.unicode == '-' or event.unicode == ',':
                    valid = True
                else:
                    valid = False
                if len(input_text) >= 20:
                    okey = False
                if event.key == pg.K_BACKSPACE:
                    input_text = input_text[0:-1]
                    okey = True
                    valid = True
                elif okey and valid:
                    if event.unicode == ',':
                        event.unicode = '.'
                    input_text += event.unicode
                if event.key == pg.K_RETURN and input_text != '':
                    valid = True
                    if examp.bool_pr(input_text):
                        examp.gen_ex()
                        input_text = ''
                        draw_ok = True
                        draw_time_ok = 1
                        SCORE += examp.score
                        score += examp.score
                        draw_notok = False
                    else:
                        draw_notok = True
                        draw_time_nok = 1
                    button_go = False
        if need_generaite:
            examp.gen_ex()
        error_1 = Font(int(__SIZE[0] / (800 / 560)), int(__SIZE[1] / (800 / 520)) + int(__SIZE[1] / (800 / 15)),
                       font_size=int(__SIZE[1] / (600 / 14)), font_color=(255, 0, 0), message='Error: too long answer')
        error_2 = Font(int(__SIZE[0] / (800 / 560)), int(__SIZE[1] / (800 / 520)) + int(__SIZE[1] / (800 / 15)),
                       font_size=int(__SIZE[1] / (600 / 14)), font_color=(255, 0, 0), message='Error: Validation Error')
        entry_otvet = Entry_text(ANTI_VERSION_SCORE_COLOR, ACTIVE_COLOR, COLOR_ENTRY_TEXT, input_text,
                                 int(__SIZE[1] / (600 / 24)),
                                 'shrift\math_prem1.ttf', int(__SIZE[0] / (800 / 250)), int(__SIZE[1] / (800 / 500)),
                                 int(__SIZE[0] / (800 / 300)),
                                 int(__SIZE[1] / (800 / 60)), ACTIVE_COLOR, need_input, int(__SIZE[0] / (800 / 260)),
                                 int(__SIZE[1] / (800 / 500)) + int(__SIZE[1] / (800 / 15)))
        if input_text == '':
            entry_otvet.text = 'Enter the answer here'
        display.fill(COLOR_DISPLAY)
        examp.draw()
        entry_otvet.draw()
        button_answer.draw()
        show_play = draw_exit(show_play)
        score_font = Font(int(__SIZE[0] - (len(str(score)) + 5) * 25), 20, COLOR_VERSION_SCORE,
                          int(__SIZE[1] / (600 / 28)), message=f'Score: {score}')
        score_font.draw_text()
        if not okey:
            error_1.draw_text()
        if not valid:
            error_2.draw_text()
        if draw_ok and draw_time_ok <= 1000 and okey and valid:
            draw_okay(int(__SIZE[0] / (800 / 600)), int(__SIZE[1] / (800 / 520)) + int(__SIZE[1] / (800 / 15)),
                      int(__SIZE[0] / (800 / 40)))
            draw_time_ok += 1
        if draw_notok and draw_time_nok <= 1000 and okey and valid:
            draw_no_okay(int(__SIZE[0] / (800 / 600)), int(__SIZE[1] / (800 / 520)) + int(__SIZE[1] / (800 / 15)),
                         int(__SIZE[0] / (800 / 40)))
            draw_time_nok += 1
        pg.display.update()
        need_input = entry_otvet.need_input
        need_generaite = False
        if button_answer.action:
            need_input = True
            if h == 2:
                if input_text != '':
                    valid = True
                    if examp.bool_pr(input_text):
                        examp.gen_ex()
                        input_text = ''
                        draw_ok = True
                        draw_time_ok = 1
                        SCORE += examp.score
                        score += examp.score
                        draw_notok = False
                    else:
                        draw_notok = True
                        draw_time_nok = 1
                h = 0
            else:
                h += 1
        pg.time.wait(1)


def setup_menu_start():
    global Exit
    button_display = Button_rect(int(__SIZE[0] / 2 - (__SIZE[0] / 4)), int(__SIZE[1] / (800 / 175)), int(__SIZE[0] / 2),
                                 int(__SIZE[1] / 12), COLOR_SETUP_MENU_1, 'Display',
                                 font_type='/shrift/play_menu.otf', active_color=MAIN_COLOR_FONT,
                                 actived_color=MAIN_COLOR_FONT,
                                 font_size=int(__SIZE[1] / 24),
                                 message_x=int(__SIZE[0] / 2 - (60 / 800) * __SIZE[0]),
                                 message_y=int(__SIZE[1] / (800 / 190)), second_color=COLOR_BUTTON_2)
    button_theme = Button_rect(int(__SIZE[0] / 2 - (__SIZE[0] / 4)), int(__SIZE[1] / (800 / 375)), int(__SIZE[0] / 2),
                               int(__SIZE[1] / 12), COLOR_SETUP_MENU_1, 'Theme',
                               font_type='/shrift/play_menu.otf', active_color=MAIN_COLOR_FONT,
                               actived_color=MAIN_COLOR_FONT,
                               font_size=int(__SIZE[1] / 24),
                               message_x=int(__SIZE[0] / 2 - (50 / 800) * __SIZE[0]),
                               message_y=int(__SIZE[1] / (800 / 390)),
                               second_color=COLOR_BUTTON_2)
    button_lang = Button_rect(int(__SIZE[0] / 2 - (__SIZE[0] / 4)), int(__SIZE[1] / (800 / 575)), int(__SIZE[0] / 2),
                              int(__SIZE[1] / 12), COLOR_SETUP_MENU_1, 'Language',
                              font_type='/shrift/play_menu.otf', active_color=MAIN_COLOR_FONT,
                              actived_color=MAIN_COLOR_FONT,
                              font_size=int(__SIZE[1] / 24),
                              message_x=int(__SIZE[0] / 2 - (65 / 800) * __SIZE[0]),
                              message_y=int(__SIZE[1] / (800 / 590)),
                              second_color=COLOR_BUTTON_2)
    main_sett_font = Font(int(__SIZE[0] / 2 - __SIZE[0] / (800 / 100)), int(__SIZE[1] / (800 / 40)), message='Settings',
                          font_size=int(__SIZE[1] / (800 / 50)), font_color=MAIN_COLOR_FONT)
    show_menu_setup = True
    while show_menu_setup:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                output_settings()
        display.fill(COLOR_DISPLAY)
        show_menu_setup = draw_exit(show_menu_setup)
        button_display.draw()
        button_lang.draw()
        button_theme.draw()
        main_sett_font.draw_text()
        pg.display.update()
        if button_theme.action:
            menu_theme_settings()
        elif button_lang.action:
            setup_lang()
        elif button_display.action:
            menu_display_settings()
    Exit = True


def menu_theme_settings():
    global THEME
    show_menu_setup_theme = True
    ok_1 = False
    ok_2 = False
    ok_3 = False
    if THEME == 1:
        ok_1 = True
    elif THEME == 2:
        ok_2 = True
    elif THEME == 3:
        ok_3 = True
    okey_1 = Window_ok(int(__SIZE[0] / 2 - (__SIZE[0] / 4)) + int(__SIZE[0] / 2) - int(__SIZE[0] / (800 / 50)),
                       int(__SIZE[1] / (800 / 175)), int(__SIZE[0] / (800 / 50)), int(__SIZE[1] / (600 / 50)),
                       ANTI_VERSION_SCORE_COLOR,
                       ACTIVE_COLOR, COLOR_VERSION_SCORE, ACTIVE_COLOR, COLOR_VERSION_SCORE, ok_1, 5)
    okey_2 = Window_ok(int(__SIZE[0] / 2 - (__SIZE[0] / 4)) + int(__SIZE[0] / 2) - int(__SIZE[0] / (800 / 50)),
                       int(__SIZE[1] / (800 / 375)), int(__SIZE[0] / (800 / 50)), int(__SIZE[1] / (600 / 50)),
                       ANTI_VERSION_SCORE_COLOR,
                       ACTIVE_COLOR, COLOR_VERSION_SCORE, ACTIVE_COLOR, COLOR_VERSION_SCORE, ok_2, 5)
    okey_3 = Window_ok(int(__SIZE[0] / 2 - (__SIZE[0] / 4)) + int(__SIZE[0] / 2) - int(__SIZE[0] / (800 / 50)),
                       int(__SIZE[1] / (800 / 575)), int(__SIZE[0] / (800 / 50)), int(__SIZE[1] / (600 / 50)),
                       ANTI_VERSION_SCORE_COLOR,
                       ACTIVE_COLOR, COLOR_VERSION_SCORE, ACTIVE_COLOR, COLOR_VERSION_SCORE, ok_3, 5)
    button_standart = Button_rect(int(__SIZE[0] / 2 - (__SIZE[0] / 4)), int(__SIZE[1] / (800 / 175)),
                                  int(__SIZE[0] / 2),
                                  int(__SIZE[1] / 12), COLOR_SETUP_MENU_1, 'Standart',
                                  font_type='/shrift/play_menu.otf', active_color=MAIN_COLOR_FONT,
                                  actived_color=MAIN_COLOR_FONT,
                                  font_size=int(__SIZE[1] / 24),
                                  message_x=int(__SIZE[0] / 2 - (200 / 800) * __SIZE[0]),
                                  message_y=int(__SIZE[1] / (800 / 190)),
                                  second_color=COLOR_BUTTON_2)
    button_dracula = Button_rect(int(__SIZE[0] / 2 - (__SIZE[0] / 4)), int(__SIZE[1] / (800 / 375)), int(__SIZE[0] / 2),
                                 int(__SIZE[1] / 12), COLOR_SETUP_MENU_1, 'Dracula',
                                 font_type='/shrift/play_menu.otf', active_color=MAIN_COLOR_FONT,
                                 actived_color=MAIN_COLOR_FONT,
                                 font_size=int(__SIZE[1] / 24),
                                 message_x=int(__SIZE[0] / 2 - (200 / 800) * __SIZE[0]),
                                 message_y=int(__SIZE[1] / (800 / 390)),
                                 second_color=COLOR_BUTTON_2)
    button_white = Button_rect(int(__SIZE[0] / 2 - (__SIZE[0] / 4)), int(__SIZE[1] / (800 / 575)), int(__SIZE[0] / 2),
                               int(__SIZE[1] / 12), COLOR_SETUP_MENU_1, 'Light',
                               font_type='/shrift/play_menu.otf', active_color=MAIN_COLOR_FONT,
                               actived_color=MAIN_COLOR_FONT,
                               font_size=int(__SIZE[1] / 24),
                               message_x=int(__SIZE[0] / 2 - (200 / 800) * __SIZE[0]),
                               message_y=int(__SIZE[1] / (800 / 590)),
                               second_color=COLOR_BUTTON_2)
    main_sett_font_theme = Font(int(__SIZE[0] / 2 - __SIZE[0] / (800 / 100)), int(__SIZE[1] / (800 / 40)),
                                message='Theme',
                                font_size=int(__SIZE[1] / (800 / 50)), font_color=MAIN_COLOR_FONT)
    while show_menu_setup_theme:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                output_settings()
        display.fill(COLOR_DISPLAY)
        show_menu_setup_theme = draw_exit(show_menu_setup_theme)
        main_sett_font_theme.draw_text()
        button_standart.draw()
        okey_1.draw()
        button_white.draw()
        okey_3.draw()
        button_dracula.draw()
        okey_2.draw()
        pg.display.update()
        theme_upload(THEME)
        if okey_2.action:
            okey_1.ok = False
            okey_3.ok = False
            THEME = 2
        elif okey_3.action:
            okey_1.ok = False
            okey_2.ok = False
            THEME = 3
        elif okey_1.action:
            okey_2.ok = False
            okey_3.ok = False
            THEME = 1
        okey_1.action = False
        okey_2.action = False
        okey_3.action = False


def menu_display_settings():
    global SIZE
    show_menu_setup_display = True
    ok_1 = False
    ok_2 = False
    ok_3 = False
    if SIZE == 1:
        ok_1 = True
    elif SIZE == 2:
        ok_2 = True
    elif SIZE == 3:
        ok_3 = True
    okey_1 = Window_ok(int(__SIZE[0] / 2 - (__SIZE[0] / 4)) + int(__SIZE[0] / 2) - int(__SIZE[0] / (800 / 50)),
                       int(__SIZE[1] / (800 / 175)), int(__SIZE[0] / (800 / 50)), int(__SIZE[1] / (600 / 50)),
                       ANTI_VERSION_SCORE_COLOR,
                       ACTIVE_COLOR, COLOR_VERSION_SCORE, ACTIVE_COLOR, COLOR_VERSION_SCORE, ok_1, 5)
    okey_2 = Window_ok(int(__SIZE[0] / 2 - (__SIZE[0] / 4)) + int(__SIZE[0] / 2) - int(__SIZE[0] / (800 / 50)),
                       int(__SIZE[1] / (800 / 375)), int(__SIZE[0] / (800 / 50)), int(__SIZE[1] / (600 / 50)),
                       ANTI_VERSION_SCORE_COLOR,
                       ACTIVE_COLOR, COLOR_VERSION_SCORE, ACTIVE_COLOR, COLOR_VERSION_SCORE, ok_2, 5)
    okey_3 = Window_ok(int(__SIZE[0] / 2 - (__SIZE[0] / 4)) + int(__SIZE[0] / 2) - int(__SIZE[0] / (800 / 50)),
                       int(__SIZE[1] / (800 / 575)), int(__SIZE[0] / (800 / 50)), int(__SIZE[1] / (600 / 50)),
                       ANTI_VERSION_SCORE_COLOR,
                       ACTIVE_COLOR, COLOR_VERSION_SCORE, ACTIVE_COLOR, COLOR_VERSION_SCORE, ok_3, 5)
    button_800_600 = Button_rect(int(__SIZE[0] / 2 - (__SIZE[0] / 4)), int(__SIZE[1] / (800 / 175)),
                                 int(__SIZE[0] / 2),
                                 int(__SIZE[1] / 12), COLOR_SETUP_MENU_1, '800 X 600',
                                 font_type='/shrift/play_menu.otf', active_color=MAIN_COLOR_FONT,
                                 actived_color=MAIN_COLOR_FONT,
                                 font_size=int(__SIZE[1] / 24),
                                 message_x=int(__SIZE[0] / 2 - (200 / 800) * __SIZE[0]),
                                 message_y=int(__SIZE[1] / (800 / 190)),
                                 second_color=COLOR_BUTTON_2)
    button_1000_800 = Button_rect(int(__SIZE[0] / 2 - (__SIZE[0] / 4)), int(__SIZE[1] / (800 / 375)),
                                  int(__SIZE[0] / 2),
                                  int(__SIZE[1] / 12), COLOR_SETUP_MENU_1, '1000 X 700',
                                  font_type='/shrift/play_menu.otf', active_color=MAIN_COLOR_FONT,
                                  actived_color=MAIN_COLOR_FONT,
                                  font_size=int(__SIZE[1] / 24),
                                  message_x=int(__SIZE[0] / 2 - (200 / 800) * __SIZE[0]),
                                  message_y=int(__SIZE[1] / (800 / 390)),
                                  second_color=COLOR_BUTTON_2)
    button_1200_900 = Button_rect(int(__SIZE[0] / 2 - (__SIZE[0] / 4)), int(__SIZE[1] / (800 / 575)),
                                  int(__SIZE[0] / 2),
                                  int(__SIZE[1] / 12), COLOR_SETUP_MENU_1, '1200 X 900',
                                  font_type='/shrift/play_menu.otf', active_color=MAIN_COLOR_FONT,
                                  actived_color=MAIN_COLOR_FONT,
                                  font_size=int(__SIZE[1] / 24),
                                  message_x=int(__SIZE[0] / 2 - (200 / 800) * __SIZE[0]),
                                  message_y=int(__SIZE[1] / (800 / 590)),
                                  second_color=COLOR_BUTTON_2)
    main_sett_font_display = Font(int(__SIZE[0] / 2 - __SIZE[0] / (800 / 100)), int(__SIZE[1] / (800 / 40)),
                                  message='Display',
                                  font_size=int(__SIZE[1] / (800 / 50)), font_color=MAIN_COLOR_FONT)
    while show_menu_setup_display:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                output_settings()
        display.fill(COLOR_DISPLAY)
        main_sett_font_display.draw_text()
        show_menu_setup_display = draw_exit(show_menu_setup_display)
        button_800_600.draw()
        okey_1.draw()
        button_1000_800.draw()
        okey_2.draw()
        button_1200_900.draw()
        okey_3.draw()
        if okey_2.action:
            okey_1.ok = False
            okey_3.ok = False
            SIZE = 2
        elif okey_3.action:
            okey_1.ok = False
            okey_2.ok = False
            SIZE = 3
        elif okey_1.action:
            okey_2.ok = False
            okey_3.ok = False
            SIZE = 1
        okey_1.action = False
        okey_2.action = False
        okey_3.action = False
        pg.display.update()


def get_code_eng():
    mouse = pg.mouse.get_pos()
    click = pg.mouse.get_pressed()
    x = int(__SIZE[0] / 2 - (__SIZE[0] / 4))
    y = int(__SIZE[1] / (600 / 450))
    weight = int(__SIZE[0] / 2)
    height = int(__SIZE[1] / 12)
    get_code = Button_rect(int(__SIZE[0] / 2 - (__SIZE[0] / 4)), int(__SIZE[1] / (600 / 450)), int(__SIZE[0] / 2),
                           int(__SIZE[1] / 12), COLOR_VERSION_SCORE, 'Get code',
                           font_type='/shrift/play_menu.otf', active_color=MAIN_COLOR_FONT,
                           actived_color=MAIN_COLOR_FONT,
                           font_size=int(__SIZE[1] / 24),
                           message_x=int(int(__SIZE[0] / 2 - (__SIZE[0] / 4) + (__SIZE[0] / (800 / 130)))),
                           message_y=int(__SIZE[1] / (600 / 470)),
                           second_color=COLOR_BUTTON_2)
    get_code.draw()
    if x < mouse[0] < x + weight and y < mouse[1] < y + height:
        if click[0] == 1 and x < mouse[0] < x + weight and y < mouse[1] < y + height:
            ps = 'hi'
            codes = rand_shifr(str(SCORE))
            pyperclip.copy(codes)


def get_code_rus():
    mouse = pg.mouse.get_pos()
    click = pg.mouse.get_pressed()
    x = int(__SIZE[0] / 2 - (__SIZE[0] / 4))
    y = int(__SIZE[1] / (600 / 450))
    weight = int(__SIZE[0] / 2)
    height = int(__SIZE[1] / 12)
    get_code = Button_rect(int(__SIZE[0] / 2 - (__SIZE[0] / 4)), int(__SIZE[1] / (600 / 450)), int(__SIZE[0] / 2),
                           int(__SIZE[1] / 12), COLOR_VERSION_SCORE, 'Получить код',
                           font_type='/shrift/play_menu.otf', active_color=MAIN_COLOR_FONT,
                           actived_color=MAIN_COLOR_FONT,
                           font_size=int(__SIZE[1] / 24),
                           message_x=int(int(__SIZE[0] / 2 - (__SIZE[0] / 4) + (__SIZE[0] / (800 / 90)))),
                           message_y=int(__SIZE[1] / (600 / 464)),
                           second_color=COLOR_BUTTON_2)
    get_code.draw()
    if x < mouse[0] < x + weight and y < mouse[1] < y + height:
        if click[0] == 1 and x < mouse[0] < x + weight and y < mouse[1] < y + height:
            ps = 'hi'
            codes = rand_shifr(str(SCORE))
            pyperclip.copy(codes)


def any_game_menu_eng():
    show_menu_any_game = True
    text = Font(int(__SIZE[0] / (800 / 300)), int(__SIZE[1] / (600 / 40)), MAIN_COLOR_FONT, int(__SIZE[1] / (600 / 30)),
                message='Any Games')
    yes_or_no = Button_rect(int(__SIZE[0] / 2 - (__SIZE[0] / 4)), int(__SIZE[1] / (600 / 300)),
                            int(__SIZE[0] / (800 / 400)),
                            int(__SIZE[1] / 12), COLOR_SETUP_MENU_1, 'True or False',
                            font_type='/shrift/play_menu.otf', active_color=MAIN_COLOR_FONT,
                            actived_color=MAIN_COLOR_FONT,
                            font_size=int(__SIZE[1] / 24),
                            message_x=int(int(__SIZE[0] / 2 - (__SIZE[0] / 4) + (__SIZE[0] / (800 / 95)))),
                            message_y=int(__SIZE[1] / (600 / 315)),
                            second_color=COLOR_BUTTON_2)
    while show_menu_any_game:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                output_settings()
        display.fill(COLOR_DISPLAY)
        show_menu_any_game = draw_exit(show_menu_any_game)
        text.draw_text()
        yes_or_no.draw()
        if yes_or_no.action:
            pg.time.wait(50)
            yes_or_no_eng()
        pg.display.update()


def yes_or_no_eng():
    s = 40
    d = 60
    color_list = [0, 0, 200]
    color_list_2 = [0, 0, 100]
    color_list_3 = [0, 0, 100]
    flag = 1
    show_menu_y_r = True
    h = 0
    play_button = New_button(int(__SIZE[0] / (800 / 250)), int(__SIZE[1] / (600 / 300)), int(__SIZE[0] / (800 / 300)),
                             int(__SIZE[1] / (600 / 80)), 'Play', (0, 0, 0), int(__SIZE[1] / (600 / 36)),
                             active_color=ACTIVE_COLOR,
                             message_x=int(__SIZE[0] / (800 / 347)), message_y=int(__SIZE[1] / (600 / 320)),
                             sukam=int(__SIZE[0] / (800 / 10)))
    rule_button = New_button(int(__SIZE[0] / (800 / 250)), int(__SIZE[1] / (600 / 450)), int(__SIZE[0] / (800 / 300)),
                             int(__SIZE[1] / (600 / 80)), 'Rule', (0, 0, 0), int(__SIZE[1] / (600 / 36)),
                             active_color=ACTIVE_COLOR,
                             message_x=int(__SIZE[0] / (800 / 347)),
                             message_y=int(__SIZE[1] / (600 / 470)), sukam=int(__SIZE[0] / (800 / 10)))
    main_text = Font(int(__SIZE[0] / (800 / 203)), int(__SIZE[1] / (600 / 100)), font_size=int(__SIZE[1] / (600 / 46)),
                     message='True or False')
    while show_menu_y_r:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                output_settings()
        display.fill(tuple(color_list))
        show_menu_y_r = draw_exit(show_menu_y_r)
        play_button.draw(tuple(color_list_2), tuple(color_list_3))
        main_text.font_color = tuple(color_list_3)
        main_text.draw_text()
        pg.display.update()
        if flag == 10:
            color_list = new_color(color_list, 200)
            if color_list[0] > s:
                color_list_2[0] = color_list[0] - s
                if color_list[0] > d:
                    color_list_3[0] = color_list[0] - d
                else:
                    color_list_3[0] = color_list_2[0]
            else:
                color_list_2[0] = 0
                color_list_3[0] = 0
            if color_list[1] > s:
                color_list_2[1] = color_list[1] - s
                if color_list[1] > d:
                    color_list_3[1] = color_list[1] - d
            else:
                color_list_2[1] = 0
                color_list_3[1] = 0
            if color_list[2] > s:
                color_list_2[2] = color_list[2] - s
                if color_list[1] > d:
                    color_list_3[1] = color_list[1] - d
            else:
                color_list_2[2] = 0
                color_list_3[2] = 0
            flag = 0
        flag += 1
        if play_button.action:
            h += 1
            if h == 4:
                pg.time.wait(50)
                true_or_false_play_eng()
                h = 0
        elif rule_button.action:
            pass


def new_color(color_list, x):
    if color_list[0] <= x and color_list[1] == 0 and color_list[0] != 0:
        if color_list[2] < x:
            color_list[2] += 1
        elif color_list[0] != 0:
            color_list[0] -= 1
        else:
            color_list[0] = 0
    elif color_list[2] <= x and color_list[0] == 0 and color_list[2] != 0:
        if color_list[1] < x:
            color_list[1] += 1
        elif color_list[2] != 0:
            color_list[2] -= 1
        else:
            color_list[2] = 0
    elif color_list[1] <= x and color_list[2] == 0 and color_list[1] != 0:
        if color_list[0] < x:
            color_list[0] += 1
        elif color_list[1] != 0:
            color_list[1] -= 1
        else:
            color_list[1] = 0
    return color_list


def true_or_false_play_eng():
    global RECORD
    colot_display = (15, 0, 176)
    show_pley_menu = True
    flag = 1
    record = RECORD
    while show_pley_menu:
        start_play_T_F()
        score = playing_start_T_F()
        retry = retry_eng()
        if score > RECORD:
            RECORD = score
        if not retry:
            break


def start_play_T_F():
    flag = 1
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                output_settings()
        display.fill((15, 0, 176))
        flag += 1
        if flag > 1 and flag < 1000:
            font = Font(int(__SIZE[0] / (800 / 200)), int(__SIZE[1] / (600 / 200)), (0, 251, 255),
                        int(__SIZE[1] / (600 / 50)), message='Lets start ...')
            font.draw_text()
        elif flag > 1000 and flag < 1700:
            font = Font(int(__SIZE[0] / (800 / 350)), int(__SIZE[1] / (600 / 220)), (0, 251, 255),
                        int(__SIZE[1] / (600 / 120)), message='3')
            font.draw_text()
        elif flag > 1700 and flag < 2400:
            font = Font(int(__SIZE[0] / (800 / 350)), int(__SIZE[1] / (600 / 220)), (0, 251, 255),
                        int(__SIZE[1] / (600 / 120)), message='2')
            font.draw_text()
        elif flag > 2400 and flag < 3100:
            font = Font(int(__SIZE[0] / (800 / 350)), int(__SIZE[1] / (600 / 220)), (0, 251, 255),
                        int(__SIZE[1] / (600 / 120)), message='1')
            font.draw_text()
        elif flag > 3100 and flag < 4000:
            font = Font(int(__SIZE[0] / (800 / 220)), int(__SIZE[1] / (600 / 200)), (0, 251, 255),
                        int(__SIZE[1] / (600 / 80)), message='Start!!!')
            font.draw_text()
        pg.display.update()
        if flag == 4000:
            break


def playing_start_T_F():
    score = 0
    show_menu_y_r = True
    flag = 1500
    n = 1500
    button_true = Button_rect(int(__SIZE[0] / 2 - (__SIZE[0] / 3)), int(__SIZE[1] / (800 / 400)), int(__SIZE[0] / 4),
                              int(__SIZE[1] / 6), (255, 206, 0), 'True',
                              font_type='/shrift/play_menu.otf', active_color=MAIN_COLOR_FONT,
                              actived_color=MAIN_COLOR_FONT,
                              font_size=int(__SIZE[1] / (600 / 32)),
                              message_x=int(int(__SIZE[0] / 2 - (__SIZE[0] / 3) + __SIZE[0] / (800 / 45))),
                              message_y=int(__SIZE[1] / (800 / 440)), second_color=(255, 164, 0))
    button_false = Button_rect(int(__SIZE[0] / 2 + (__SIZE[0] / 3) - __SIZE[0] / 4), int(__SIZE[1] / (800 / 400)),
                               int(__SIZE[0] / 4),
                               int(__SIZE[1] / 6), (255, 206, 0), 'False',
                               font_type='/shrift/play_menu.otf', active_color=MAIN_COLOR_FONT,
                               actived_color=MAIN_COLOR_FONT,
                               font_size=int(__SIZE[1] / (600 / 32)),
                               message_x=int(
                                   int(__SIZE[0] / 2 + (__SIZE[0] / 3) - __SIZE[0] / 4 + __SIZE[0] / (800 / 45))),
                               message_y=int(__SIZE[1] / (800 / 440)), second_color=(255, 164, 0))
    score_txt = Font(int(__SIZE[0] / (800 / 600)), int(__SIZE[1] / (600 / 10)), message=f'Score: {score}',
                     font_size=int(__SIZE[1] / (600 / 26)), font_color=COLOR_VERSION_SCORE)
    reccord_txt = Font(int(__SIZE[0] / (800 / 15)), int(__SIZE[1] / (600 / 10)), message=f'Record: {RECORD}',
                       font_size=int(__SIZE[1] / (600 / 26)), font_color=COLOR_VERSION_SCORE)
    yes = False
    t, ex = generate()
    ex.font_size = int(__SIZE[1] / (600 / 46))
    ex.font_color = COLOR_VERSION_SCORE
    while show_menu_y_r:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                output_settings()
        display.fill((15, 0, 176))
        pg.draw.line(display, (0, 255, 0), [0, 590], [int(__SIZE[0] * flag / n), 590], int(__SIZE[1] / (600 / 14)))
        score_txt.draw_text()
        reccord_txt.draw_text()
        button_true.draw()
        button_false.draw()
        ex.draw_text()
        pg.display.update()
        flag -= 1
        if button_false.action:
            if not t:
                yes = True
            else:
                yes = False
        elif button_true.action:
            if t:
                yes = True
            else:
                yes = False
        if yes:
            score += 1
            score_txt.message = f'Score: {score}'
            n = 1500 - score * 10
            flag = n
            t, ex = generate()
            ex.font_size = int(__SIZE[1] / (600 / 40))
            ex.font_color = COLOR_VERSION_SCORE
            yes = False
            pg.time.wait(150)
        elif flag == 1 or ((button_true.action or button_false.action) and not yes):
            break
    return score


def generate():
    pain = rand.randint(1, 2)
    if pain == 1:
        r = rand.randint(1, 6)
        if r == 1:
            a = rand.randint(1, 30)
            b = rand.randint(1, 20)
            c = a + b
            ex = Font(int(__SIZE[0] / (800 / 280)), int(__SIZE[1] / (600 / 130)), message=f'{a} + {b} = {c}')
        elif r == 2:
            a = rand.randint(20, 50)
            b = rand.randint(1, 20)
            c = a - b
            ex = Font(int(__SIZE[0] / (800 / 280)), int(__SIZE[1] / (600 / 130)), message=f'{a} - {b} = {c}')
        elif r == 3:
            a = rand.randint(1, 30)
            b = rand.randint(1, 20)
            g = a + b
            c = g + rand.randint(int(g / 10), int(g / 4))
            if c == g:
                c += rand.randint(1, 10)
            ex = Font(int(__SIZE[0] / (800 / 280)), int(__SIZE[1] / (600 / 130)), message=f'{a} + {b} < {c}')
        elif r == 4:
            a = rand.randint(1, 30)
            b = rand.randint(1, 20)
            g = a + b
            c = g - rand.randint(int(g / 10), int(g / 4))
            if c == g:
                c -= rand.randint(1, 10)
            ex = Font(int(__SIZE[0] / (800 / 280)), int(__SIZE[1] / (600 / 130)), message=f'{a} + {b} > {c}')
        elif r == 5:
            a = rand.randint(10, 40)
            b = rand.randint(1, 20)
            g = a - b
            if g >= 0:
                c = g + rand.randint(int(g / 10), int(g / 4))
            else:
                c = g + rand.randint(int((g * (-1)) / 10), int((g * (-1)) / 4))
            if c == g:
                c += rand.randint(1, 10)
            ex = Font(int(__SIZE[0] / (800 / 280)), int(__SIZE[1] / (600 / 130)), message=f'{a} - {b} < {c}')
        elif r == 6:
            a = rand.randint(1, 30)
            b = rand.randint(1, 20)
            g = a - b
            if g >= 0:
                c = g - rand.randint(int(g / 10), int(g / 4))
            else:
                c = g - rand.randint(int((g * (-1)) / 10), int((g * (-1)) / 4))
            if c == g:
                c -= rand.randint(1, 10)
            ex = Font(int(__SIZE[0] / (800 / 280)), int(__SIZE[1] / (600 / 130)), message=f'{a} - {b} > {c}')
        return True, ex
    elif pain == 2:
        r = rand.randint(1, 6)
        if r == 1:
            a = rand.randint(1, 30)
            b = rand.randint(1, 20)
            g = a + b
            c = rand.randint(g - 10, g + 10)
            if g == c:
                c -= rand.randint(1, 5)
            ex = Font(int(__SIZE[0] / (800 / 280)), int(__SIZE[1] / (600 / 130)), message=f'{a} + {b} = {c}')
        elif r == 2:
            a = rand.randint(10, 40)
            b = rand.randint(1, 20)
            g = a - b
            c = rand.randint(int(g - g / 5), int(g + g / 4))
            if g == c:
                c += rand.randint(1, 6)
            ex = Font(int(__SIZE[0] / (800 / 280)), int(__SIZE[1] / (600 / 130)), message=f'{a} - {b} = {c}')
        elif r == 3:
            a = rand.randint(1, 30)
            b = rand.randint(1, 20)
            g = a + b
            if g >= 0:
                c = g - rand.randint(int(g / 10), int(g / 4))
            else:
                c = g - rand.randint(int((g * (-1)) / 10), int((g * (-1)) / 4))
            if c == g:
                c -= rand.randint(1, 10)
            ex = Font(int(__SIZE[0] / (800 / 280)), int(__SIZE[1] / (600 / 130)), message=f'{a} + {b} < {c}')
        elif r == 4:
            a = rand.randint(1, 30)
            b = rand.randint(1, 20)
            g = a - b
            if g >= 0:
                c = g - rand.randint(int(g / 10), int(g / 4))
            else:
                c = g - rand.randint(int((g * (-1)) / 10), int((g * (-1)) / 4))
            if c == g:
                c -= rand.randint(1, 10)
            ex = Font(int(__SIZE[0] / (800 / 280)), int(__SIZE[1] / (600 / 130)), message=f'{a} - {b} < {c}')
        elif r == 5:
            a = rand.randint(1, 30)
            b = rand.randint(1, 20)
            g = a + b
            if g >= 0:
                c = g + rand.randint(int(g / 10), int(g / 4))
            else:
                c = g + rand.randint(int((g * (-1)) / 10), int((g * (-1)) / 4))
            if c == g:
                c += rand.randint(1, 10)
            ex = Font(int(__SIZE[0] / (800 / 280)), int(__SIZE[1] / (600 / 130)), message=f'{a} + {b} > {c}')
        elif r == 6:
            a = rand.randint(1, 30)
            b = rand.randint(1, 20)
            g = a - b
            if g >= 0:
                c = g + rand.randint(int(g / 10), int(g / 4))
            else:
                c = g + rand.randint(int((g * (-1)) / 10), int((g * (-1)) / 4))
            if c == g:
                c += rand.randint(1, 10)
            ex = Font(int(__SIZE[0] / (800 / 280)), int(__SIZE[1] / (600 / 130)), message=f'{a} - {b} > {c}')
        return False, ex


def retry_eng():
    show_menu_retry = True
    okey = True
    go = False
    h = 0
    button_yes = Button_rect(int(__SIZE[0] / 2 - (__SIZE[0] / 3)), int(__SIZE[1] / (800 / 300)), int(__SIZE[0] / 4),
                             int(__SIZE[1] / 6), (255, 206, 0), 'Yes',
                             font_type='/shrift/play_menu.otf', active_color=MAIN_COLOR_FONT,
                             actived_color=MAIN_COLOR_FONT,
                             font_size=int(__SIZE[1] / (600 / 32)),
                             message_x=int(int(__SIZE[0] / 2 - (__SIZE[0] / 3) + __SIZE[0] / (800 / 68))),
                             message_y=int(__SIZE[1] / (800 / 340)), second_color=(255, 164, 0))
    button_not = Button_rect(int(__SIZE[0] / 2 + (__SIZE[0] / 3) - __SIZE[0] / 4), int(__SIZE[1] / (800 / 300)),
                             int(__SIZE[0] / 4),
                             int(__SIZE[1] / 6), (255, 206, 0), 'No',
                             font_type='/shrift/play_menu.otf', active_color=MAIN_COLOR_FONT,
                             actived_color=MAIN_COLOR_FONT,
                             font_size=int(__SIZE[1] / (600 / 32)),
                             message_x=int(
                                 int(__SIZE[0] / 2 + (__SIZE[0] / 3) - __SIZE[0] / 4 + __SIZE[0] / (800 / 80))),
                             message_y=int(__SIZE[1] / (800 / 340)), second_color=(255, 164, 0))
    quest = Font(int(__SIZE[0] / (800 / 100)), int(__SIZE[1] / (600 / 50)), COLOR_VERSION_SCORE,
                 int(__SIZE[1] / (600 / 44)), message='Are you want retry?')
    while show_menu_retry:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                output_settings()
        display.fill((15, 0, 176))
        button_not.draw()
        button_yes.draw()
        quest.draw_text()
        if button_yes.action and go:
            okey = True
            break
        elif button_not.action and go:
            okey = False
            break
        pg.display.update()
        if h == 10:
            go = True
        else:
            h += 1
    return okey


code = True
while code:
    if LANG == 1:
        main_menu()
    else:
        main_menu_rus()
    Exit = False
