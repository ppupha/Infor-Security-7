from pygame import init, time, display, draw, event, QUIT
from math import *
from random import *
def run():
    FPS = 60
    WIN_WIDTH = 800
    WIN_HEIGHT = 500

    BLACK = (0, 0, 0)
    BACKGROUND = (205, 205, 205)
    GROUND = (235, 235, 235)
    LIGHT_GREY1 = (185, 185, 185)
    LIGHT_GREY2 = (165, 165, 165)
    YELLOW = (251, 236, 93)
    BROWN = (150, 75, 0)
    LIGHT_BROWN = (141, 107, 73)
    DARK_BROWN = (101, 67, 33)
    GREEN = (23, 114, 69)
    BLUE = (200, 255, 255)

    init()

    clock = time.Clock()

    sc = display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    x1 = 0
    x2 = 150
    x3 = 200
    x4 = 300
    x5 = -150
    x6 = 450
    x7 = 600
    s = 0
    k = 0
    m = 0
    # Снег
    array_of_snowflakes = []
    x = []
    y = []
    for i in range(150):
        y += [randint(-100, 160)]
        x += [randint(10, 790)]
        array_of_snowflakes += [[draw.aaline(sc, BLUE, [x[i], 145 + y[i]], [x[i], 155 + y[i]])],
                                [draw.aaline(sc, BLUE, [x[i] - 5, 150 + y[i]], [x[i] + 5, 150 + y[i]])],
                                [draw.aaline(sc, BLUE, [x[i] - 4, 146 + y[i]], [x[i] + 4, 154 + y[i]])],
                                [draw.aaline(sc, BLUE, [x[i] - 4, 154 + y[i]], [x[i] + 4, 146 + y[i]])]]

    while 1:
        sc.fill(BACKGROUND)

        trajectory1 = sin(s * 2) * 6
        trajectory2 = sin(s * 2 + 0.5) * 6
        trajectory3 = sin(s * 2 + 1) * 6
        trajectory4 = sin(s * 2 + 1.5) * 6
        trajectory5 = sin(s * 2 + 2) * 6
        trajectory6 = sin(s * 2 + 2.5) * 6
        trajectory7 = sin(s * 2 + 2.5) * 7

        for i in event.get():
            if i.type == QUIT: return

        draw.ellipse(sc, LIGHT_GREY2, (x3+trajectory1, 15+trajectory1+80, 50, 20))
        draw.ellipse(sc, LIGHT_GREY2, (x3+trajectory1+2, 8+trajectory1+80, 18, 18))
        draw.ellipse(sc, LIGHT_GREY2, (x3+trajectory1+10, 4+trajectory1+80, 30, 30))
        draw.ellipse(sc, LIGHT_GREY2, (x3+trajectory1+30, 8+trajectory1+80, 18, 18))
        draw.ellipse(sc, LIGHT_GREY2, (x3+trajectory1-3, 15+trajectory1+80, 18, 18))
        draw.ellipse(sc, LIGHT_GREY2, (x3+trajectory1+35, 15+trajectory1+80, 18, 18))
        if x3 >= WIN_WIDTH:
            x3 = -56
        else:
            x3 += 1

        draw.polygon(sc, LIGHT_GREY1, [[-10, 0], [30, 0], [15, 15]])
        draw.ellipse(sc, LIGHT_GREY1, (x1+trajectory2, 30+trajectory2+4, 100, 40))
        draw.ellipse(sc, LIGHT_GREY1, (x1+trajectory2+4, 16+trajectory2+4, 36, 36))
        draw.ellipse(sc, LIGHT_GREY1, (x1+trajectory2+20, 8+trajectory2+4, 60, 60))
        draw.ellipse(sc, LIGHT_GREY1, (x1+trajectory2+60, 16+trajectory2+4, 36, 36))
        draw.ellipse(sc, LIGHT_GREY1, (x1+trajectory2-6, 30+trajectory2+4, 36, 36))
        draw.ellipse(sc, LIGHT_GREY1, (x1+trajectory2+70, 30+trajectory2+4, 36, 36))

        if x1 >= WIN_WIDTH:
            x1 = -112
        else:
            x1 += 1.5

        draw.ellipse(sc, LIGHT_GREY1, (x2+trajectory3, 30*0.8+trajectory3+10, 100*0.8, 40*0.8))
        draw.ellipse(sc, LIGHT_GREY1, (x2+trajectory3+4*0.8, 16*0.8+trajectory3+10, 36*0.8, 36*0.8))
        draw.ellipse(sc, LIGHT_GREY1, (x2+trajectory3+20*0.8, 8*0.8+trajectory3+10, 60*0.8, 60*0.8))
        draw.ellipse(sc, LIGHT_GREY1, (x2+trajectory3+60*0.8, 16*0.8+trajectory3+10, 36*0.8, 36*0.8))
        draw.ellipse(sc, LIGHT_GREY1, (x2+trajectory3-6*0.8, 30*0.8+trajectory3+10, 36*0.8, 36*0.8))
        draw.ellipse(sc, LIGHT_GREY1, (x2+trajectory3+70*0.8, 30*0.8+trajectory3+10, 36*0.8, 36*0.8))

        if x2 >= WIN_WIDTH:
            x2 = -112
        else:
            x2 += 1.55

        draw.ellipse(sc, LIGHT_GREY1, (x4+trajectory4+10, 28+trajectory4+10, 60, 56))
        draw.ellipse(sc, LIGHT_GREY1, (x4+trajectory4+42, 50+trajectory4+10, 42, 42))
        draw.ellipse(sc, LIGHT_GREY1, (x4+trajectory4+60, 30+trajectory4+10, 54, 54))
        draw.ellipse(sc, LIGHT_GREY1, (x4+trajectory4+30, 14+trajectory4+10, 40, 40))
        draw.ellipse(sc, LIGHT_GREY1, (x4+trajectory4+56, 10+trajectory4+10, 46, 46))

        if x4 >= WIN_WIDTH:
            x4 = -112
        else:
            x4 += 1.53

        draw.ellipse(sc, LIGHT_GREY1, (x5+trajectory5+10*0.75, 28*0.75+trajectory5+10, 60*0.75, 56*0.75))
        draw.ellipse(sc, LIGHT_GREY1, (x5+trajectory5+42*0.75, 50*0.75+trajectory5+10, 42*0.75, 42*0.75))
        draw.ellipse(sc, LIGHT_GREY1, (x5+trajectory5+60*0.75, 30*0.75+trajectory5+10, 54*0.75, 54*0.75))
        draw.ellipse(sc, LIGHT_GREY1, (x5+trajectory5+30*0.75, 14*0.75+trajectory5+10, 40*0.75, 40*0.75))
        draw.ellipse(sc, LIGHT_GREY1, (x5+trajectory5+56*0.75, 10*0.75+trajectory5+10, 46*0.75, 46*0.75))
        if x5 >= WIN_WIDTH:
            x5 = -112
        else:
            x5 += 1.51

        draw.ellipse(sc, LIGHT_GREY1, (x6+trajectory6+10*0.75, 28*0.75+trajectory6+10, 60*0.75, 56*0.75))
        draw.ellipse(sc, LIGHT_GREY1, (x6+trajectory6+42*0.75, 50*0.75+trajectory6+10, 42*0.75, 42*0.75))
        draw.ellipse(sc, LIGHT_GREY1, (x6+trajectory6+60*0.75, 30*0.75+trajectory6+10, 54*0.75, 54*0.75))
        draw.ellipse(sc, LIGHT_GREY1, (x6+trajectory6+30*0.75, 14*0.75+trajectory6+10, 40*0.75, 40*0.75))
        draw.ellipse(sc, LIGHT_GREY1, (x6+trajectory6+56*0.75, 10*0.75+trajectory6+10, 46*0.75, 46*0.75))
        if x6 >= WIN_WIDTH:
            x6 = -112
        else:
            x6 += 1.5

        draw.ellipse(sc, LIGHT_GREY1, (x7+trajectory7+10, 28+trajectory7+10, 60, 56))
        draw.ellipse(sc, LIGHT_GREY1, (x7+trajectory7+42, 50+trajectory7+10, 42, 42))
        draw.ellipse(sc, LIGHT_GREY1, (x7+trajectory7+60, 30+trajectory7+10, 54, 54))
        draw.ellipse(sc, LIGHT_GREY1, (x7+trajectory7+30, 14+trajectory7+10, 40, 40))
        draw.ellipse(sc, LIGHT_GREY1, (x7+trajectory7+56, 10+trajectory7+10, 46, 46))

        if x7 >= WIN_WIDTH:
            x7 = -112
        else:
            x7 += 1.54

        draw.ellipse(sc, GROUND, (-200, WIN_HEIGHT-150, WIN_WIDTH+400, 200))
        # Елки за домами
        f = [240, 30, -250, -150, -286, -282, -270, -290, -280, -20, 330, 480, 450, 420, 400, 300, 104, 155, -180]
        f_1 = [30, 50, 40, 80, 30, 80, 100, 120, 136, 125, 20, 50, 115, 120, 130, 120, 126, 20, 20]
        for i in range(17, 19):
            draw.polygon(sc, DARK_BROWN, [[300+f[i], 360+f_1[i]], [308+f[i], 360+f_1[i]], [304+f[i], 320+f_1[i]]])
            draw.aalines(sc, BLACK, True, [[300+f[i], 360+f_1[i]], [308+f[i], 360+f_1[i]], [304+f[i], 320+f_1[i]]])
            draw.polygon(sc, GREEN, [[285+f[i], 354+f_1[i]], [323+f[i], 354+f_1[i]], [304+f[i], 332+f_1[i]]])
            draw.aalines(sc, BLACK, True, [[285+f[i], 354+f_1[i]], [323+f[i], 354+f_1[i]], [304+f[i], 332+f_1[i]]])
            draw.polygon(sc, GREEN, [[290+f[i], 335+f_1[i]], [318+f[i], 335+f_1[i]], [304+f[i], 318+f_1[i]]])
            draw.aalines(sc, BLACK, True, [[290+f[i], 335+f_1[i]], [318+f[i], 335+f_1[i]], [304+f[i], 318+f_1[i]]])
            draw.polygon(sc, GREEN, [[295+f[i], 320+f_1[i]], [313+f[i], 320+f_1[i]], [304+f[i], 309+f_1[i]]])
            draw.aalines(sc, BLACK, True, [[295+f[i], 320+f_1[i]], [313+f[i], 320+f_1[i]], [304+f[i], 309+f_1[i]]])

        h = [0, -350, 220, -40]
        h_1 = [0, 20, 40, 80]
        for i in range(4):
            # Фронт дома
            draw.polygon(sc, LIGHT_BROWN, [[460+h[i], 370+h_1[i]], [500+h[i], 370+h_1[i]], [500+h[i], 400+h_1[i]], [460+h[i], 400+h_1[i]]])
            draw.aalines(sc, BLACK, True, [[460+h[i], 370+h_1[i]], [500+h[i], 370+h_1[i]], [500+h[i], 400+h_1[i]], [460+h[i], 400+h_1[i]]])

            # Боковина дома
            draw.polygon(sc, LIGHT_BROWN, [[500+h[i], 400+h_1[i]], [530+h[i], 385+h_1[i]], [530+h[i], 355+h_1[i]], [500+h[i], 370+h_1[i]]])
            draw.aalines(sc, BLACK, True, [[500+h[i], 400+h_1[i]], [530+h[i], 385+h_1[i]], [530+h[i], 355+h_1[i]], [500+h[i], 370+h_1[i]]])

            # Фронт крыши дома
            draw.polygon(sc, DARK_BROWN, [[500+h[i], 370+h_1[i]], [460+h[i], 370+h_1[i]], [480+h[i], 350+h_1[i]]])
            draw.aalines(sc, BLACK, True, [[500+h[i], 370+h_1[i]], [460+h[i], 370+h_1[i]], [480+h[i], 350+h_1[i]]])

            # Боковина крыши дома
            draw.polygon(sc, DARK_BROWN, [[530+h[i], 355+h_1[i]], [515+h[i], 335+h_1[i]], [480+h[i], 350+h_1[i]], [500+h[i], 370+h_1[i]]])
            draw.aalines(sc, BLACK, True, [[530+h[i], 355+h_1[i]], [515+h[i], 335+h_1[i]], [480+h[i], 350+h_1[i]], [500+h[i], 370+h_1[i]]])

            # Дверь
            draw.polygon(sc, BROWN, [[475+h[i], 400+h_1[i]], [485+h[i], 400+h_1[i]], [485+h[i], 385+h_1[i]], [475+h[i], 385+h_1[i]]])
            draw.aalines(sc, BLACK, True, [[475+h[i], 400+h_1[i]], [485+h[i], 400+h_1[i]], [485+h[i], 385+h_1[i]], [475+h[i], 385+h_1[i]]])

            # Окно
            draw.polygon(sc, YELLOW, [[508+h[i], 390+h_1[i]], [522+h[i], 383+h_1[i]], [522+h[i], 365+h_1[i]], [508+h[i], 372+h_1[i]]])
            draw.aalines(sc, BLACK, True, [[508+h[i], 390+h_1[i]], [522+h[i], 383+h_1[i]], [522+h[i], 365+h_1[i]], [508+h[i], 372+h_1[i]]])
            draw.aalines(sc, BLACK, True, [[508+h[i], 381+h_1[i]], [522+h[i], 374+h_1[i]]])
            draw.aalines(sc, BLACK, True, [[515+h[i], 386+h_1[i]], [515+h[i], 368+h_1[i]]])

        # Елки перед домами
        for i in range(17):
            draw.polygon(sc, DARK_BROWN, [[300+f[i], 360+f_1[i]], [308+f[i], 360+f_1[i]], [304+f[i], 320+f_1[i]]])
            draw.aalines(sc, BLACK, True, [[300+f[i], 360+f_1[i]], [308+f[i], 360+f_1[i]], [304+f[i], 320+f_1[i]]])
            draw.polygon(sc, GREEN, [[285+f[i], 354+f_1[i]], [323+f[i], 354+f_1[i]], [304+f[i], 332+f_1[i]]])
            draw.aalines(sc, BLACK, True, [[285+f[i], 354+f_1[i]], [323+f[i], 354+f_1[i]], [304+f[i], 332+f_1[i]]])
            draw.polygon(sc, GREEN, [[290+f[i], 335+f_1[i]], [318+f[i], 335+f_1[i]], [304+f[i], 318+f_1[i]]])
            draw.aalines(sc, BLACK, True, [[290+f[i], 335+f_1[i]], [318+f[i], 335+f_1[i]], [304+f[i], 318+f_1[i]]])
            draw.polygon(sc, GREEN, [[295+f[i], 320+f_1[i]], [313+f[i], 320+f_1[i]], [304+f[i], 309+f_1[i]]])
            draw.aalines(sc, BLACK, True, [[295+f[i], 320+f_1[i]], [313+f[i], 320+f_1[i]], [304+f[i], 309+f_1[i]]])
        if k <= 2*pi:
            k += 0.03
        else:
            k = 0
        for i in range(0, 25):
            if y[i]*2 + 150 < WIN_HEIGHT - 100:
                y[i] += 1.2
                array_of_snowflakes[i] = [[draw.aaline(sc, BLUE, [2*(x[i]/2 - 5*sin(k)), 2*(150 + y[i]*2 - (5*cos(k)))], [2*(x[i]/2 + 5*sin(k)), 2*(150 + y[i]*2 + (5*cos(k)))])],
                                          [draw.aaline(sc, BLUE, [2*(x[i]/2 - (5*cos(k))), 2*(150 + y[i]*2 + 5*sin(k))], [2*(x[i]/2 + (5*cos(k))), 2*(150 + y[i]*2 - 5*sin(k))])],
                                          [draw.aaline(sc, BLUE, [2*(x[i]/2 - (4*cos(k)+4*sin(k))), 2*(150 + y[i]*2 - (4*cos(k)-4*sin(k)))], [2*(x[i]/2 + (4*cos(k)+4*sin(k))), 2*(150 + y[i]*2 + (4*cos(k)-4*sin(k)))])],
                                          [draw.aaline(sc, BLUE, [2*(x[i]/2 - (4*cos(k)-4*sin(k))), 2*(150 + y[i]*2 + (4*cos(k)+4*sin(k)))], [2*(x[i]/2 + (4*cos(k)-4*sin(k))), 2*(150 + y[i]*2 - (4*cos(k)+4*sin(k)))])]]
            if y[i]*2 + 150 >= WIN_HEIGHT - 100:
                x[i] = randint(10, 790)
                y[i] = randint(-80, -70)
                array_of_snowflakes[i] = [[draw.aaline(sc, BLUE, [x[i], 145 + y[i]], [x[i], 155 + y[i]])],
                                          [draw.aaline(sc, BLUE, [x[i] - 5, 150 + y[i]], [x[i] + 5, 150 + y[i]])],
                                          [draw.aaline(sc, BLUE, [x[i] - 4, 146 + y[i]], [x[i] + 4, 154 + y[i]])],
                                          [draw.aaline(sc, BLUE, [x[i] - 4, 154 + y[i]], [x[i] + 4, 146 + y[i]])]]
        for i in range(25, 50):
            if y[i] < WIN_HEIGHT - 150:
                y[i] += 1.45
                array_of_snowflakes[i] = [[draw.aaline(sc, BLUE, [x[i] - 5 * sin(k), 150 + y[i] - (5 * cos(k))],
                                                              [x[i] + 5 * sin(k), 150 + y[i] + (5 * cos(k))])],
                                          [draw.aaline(sc, BLUE, [x[i] - (5 * cos(k)), 150 + y[i] + 5 * sin(k)],
                                                              [x[i] + (5 * cos(k)), 150 + y[i] - 5 * sin(k)])],
                                          [draw.aaline(sc, BLUE, [x[i] - (4 * cos(k) + 4 * sin(k)),
                                                                         150 + y[i] - (4 * cos(k) - 4 * sin(k))],
                                                              [x[i] + (4 * cos(k) + 4 * sin(k)),
                                                               150 + y[i] + (4 * cos(k) - 4 * sin(k))])],
                                          [draw.aaline(sc, BLUE, [x[i] - (4 * cos(k) - 4 * sin(k)),
                                                                         150 + y[i] + (4 * cos(k) + 4 * sin(k))],
                                                              [x[i] + (4 * cos(k) - 4 * sin(k)),
                                                               150 + y[i] - (4 * cos(k) + 4 * sin(k))])]]
            if y[i] >= WIN_HEIGHT - 150:
                x[i] = randint(10, 790)
                y[i] = randint(-60, -40)
                array_of_snowflakes[i] = [[draw.aaline(sc, BLUE, [x[i], 145 + y[i]], [x[i], 155 + y[i]])],
                                          [draw.aaline(sc, BLUE, [x[i] - 5, 150 + y[i]], [x[i] + 5, 150 + y[i]])],
                                          [draw.aaline(sc, BLUE, [x[i] - 4, 146 + y[i]], [x[i] + 4, 154 + y[i]])],
                                          [draw.aaline(sc, BLUE, [x[i] - 4, 154 + y[i]], [x[i] + 4, 146 + y[i]])]]

        for i in range(50, 75):
            if y[i] < WIN_HEIGHT - 200:
                y[i] += 1.6
                array_of_snowflakes[i] = [[draw.aaline(sc, BLUE, [x[i] - 5 * sin(k), 150 + y[i] - (5 * cos(k))],
                                                              [x[i] + 5 * sin(k), 150 + y[i] + (5 * cos(k))])],
                                          [draw.aaline(sc, BLUE, [x[i] - (5 * cos(k)), 150 + y[i] + 5 * sin(k)],
                                                              [x[i] + (5 * cos(k)), 150 + y[i] - 5 * sin(k)])],
                                          [draw.aaline(sc, BLUE, [x[i] - (4 * cos(k) + 4 * sin(k)),
                                                                         150 + y[i] - (4 * cos(k) - 4 * sin(k))],
                                                              [x[i] + (4 * cos(k) + 4 * sin(k)),
                                                               150 + y[i] + (4 * cos(k) - 4 * sin(k))])],
                                          [draw.aaline(sc, BLUE, [x[i] - (4 * cos(k) - 4 * sin(k)),
                                                                         150 + y[i] + (4 * cos(k) + 4 * sin(k))],
                                                              [x[i] + (4 * cos(k) - 4 * sin(k)),
                                                               150 + y[i] - (4 * cos(k) + 4 * sin(k))])]]
            if y[i] >= WIN_HEIGHT - 200:
                x[i] = randint(10, 790)
                y[i] = randint(-70, -50)
                array_of_snowflakes[i] = [[draw.aaline(sc, BLUE, [x[i], 145 + y[i]], [x[i], 155 + y[i]])],
                                          [draw.aaline(sc, BLUE, [x[i] - 5, 150 + y[i]], [x[i] + 5, 150 + y[i]])],
                                          [draw.aaline(sc, BLUE, [x[i] - 4, 146 + y[i]], [x[i] + 4, 154 + y[i]])],
                                          [draw.aaline(sc, BLUE, [x[i] - 4, 154 + y[i]], [x[i] + 4, 146 + y[i]])]]

        for i in range(75, 100):
            if y[i] < WIN_HEIGHT - 250:
                y[i] += 1.75
                array_of_snowflakes[i] = [[draw.aaline(sc, BLUE, [x[i] - 5 * sin(k), 150 + y[i] - (5 * cos(k))],
                                                              [x[i] + 5 * sin(k), 150 + y[i] + (5 * cos(k))])],
                                          [draw.aaline(sc, BLUE, [x[i] - (5 * cos(k)), 150 + y[i] + 5 * sin(k)],
                                                              [x[i] + (5 * cos(k)), 150 + y[i] - 5 * sin(k)])],
                                          [draw.aaline(sc, BLUE, [x[i] - (4 * cos(k) + 4 * sin(k)),
                                                                         150 + y[i] - (4 * cos(k) - 4 * sin(k))],
                                                              [x[i] + (4 * cos(k) + 4 * sin(k)),
                                                               150 + y[i] + (4 * cos(k) - 4 * sin(k))])],
                                          [draw.aaline(sc, BLUE, [x[i] - (4 * cos(k) - 4 * sin(k)),
                                                                         150 + y[i] + (4 * cos(k) + 4 * sin(k))],
                                                              [x[i] + (4 * cos(k) - 4 * sin(k)),
                                                               150 + y[i] - (4 * cos(k) + 4 * sin(k))])]]
            if y[i] >= WIN_HEIGHT - 250:
                x[i] = randint(10, 790)
                y[i] = randint(-80, -60)
                array_of_snowflakes[i] = [[draw.aaline(sc, BLUE, [x[i], 145 + y[i]], [x[i], 155 + y[i]])],
                                          [draw.aaline(sc, BLUE, [x[i] - 5, 150 + y[i]], [x[i] + 5, 150 + y[i]])],
                                          [draw.aaline(sc, BLUE, [x[i] - 4, 146 + y[i]], [x[i] + 4, 154 + y[i]])],
                                          [draw.aaline(sc, BLUE, [x[i] - 4, 154 + y[i]], [x[i] + 4, 146 + y[i]])]]

        for i in range(100, 125):
            if y[i] < WIN_HEIGHT - 300:
                y[i] += 1.9
                array_of_snowflakes[i] = [[draw.aaline(sc, BLUE, [x[i] - 5 * sin(k), 150 + y[i] - (5 * cos(k))],
                                                              [x[i] + 5 * sin(k), 150 + y[i] + (5 * cos(k))])],
                                          [draw.aaline(sc, BLUE, [x[i] - (5 * cos(k)), 150 + y[i] + 5 * sin(k)],
                                                              [x[i] + (5 * cos(k)), 150 + y[i] - 5 * sin(k)])],
                                          [draw.aaline(sc, BLUE, [x[i] - (4 * cos(k) + 4 * sin(k)),
                                                                         150 + y[i] - (4 * cos(k) - 4 * sin(k))],
                                                              [x[i] + (4 * cos(k) + 4 * sin(k)),
                                                               150 + y[i] + (4 * cos(k) - 4 * sin(k))])],
                                          [draw.aaline(sc, BLUE, [x[i] - (4 * cos(k) - 4 * sin(k)),
                                                                         150 + y[i] + (4 * cos(k) + 4 * sin(k))],
                                                              [x[i] + (4 * cos(k) - 4 * sin(k)),
                                                               150 + y[i] - (4 * cos(k) + 4 * sin(k))])]]
            if y[i] >= WIN_HEIGHT - 300:
                x[i] = randint(10, 790)
                y[i] = randint(-90, -70)
                array_of_snowflakes[i] = [[draw.aaline(sc, BLUE, [x[i], 145 + y[i]], [x[i], 155 + y[i]])],
                                          [draw.aaline(sc, BLUE, [x[i] - 5, 150 + y[i]], [x[i] + 5, 150 + y[i]])],
                                          [draw.aaline(sc, BLUE, [x[i] - 4, 146 + y[i]], [x[i] + 4, 154 + y[i]])],
                                          [draw.aaline(sc, BLUE, [x[i] - 4, 154 + y[i]], [x[i] + 4, 146 + y[i]])]]

        for i in range(125, 150):
            if y[i] < WIN_HEIGHT - 250:
                y[i] += 2.05
                array_of_snowflakes[i] = [[draw.aaline(sc, BLUE, [x[i] - 5 * sin(k), 150 + y[i] - (5 * cos(k))],
                                                              [x[i] + 5 * sin(k), 150 + y[i] + (5 * cos(k))])],
                                          [draw.aaline(sc, BLUE, [x[i] - (5 * cos(k)), 150 + y[i] + 5 * sin(k)],
                                                              [x[i] + (5 * cos(k)), 150 + y[i] - 5 * sin(k)])],
                                          [draw.aaline(sc, BLUE, [x[i] - (4 * cos(k) + 4 * sin(k)),
                                                                         150 + y[i] - (4 * cos(k) - 4 * sin(k))],
                                                              [x[i] + (4 * cos(k) + 4 * sin(k)),
                                                               150 + y[i] + (4 * cos(k) - 4 * sin(k))])],
                                          [draw.aaline(sc, BLUE, [x[i] - (4 * cos(k) - 4 * sin(k)),
                                                                         150 + y[i] + (4 * cos(k) + 4 * sin(k))],
                                                              [x[i] + (4 * cos(k) - 4 * sin(k)),
                                                               150 + y[i] - (4 * cos(k) + 4 * sin(k))])]]
            if y[i] >= WIN_HEIGHT - 250:
                x[i] = randint(10, 790)
                y[i] = randint(-100, -80)
                array_of_snowflakes[i] = [[draw.aaline(sc, BLUE, [x[i], 145 + y[i]], [x[i], 155 + y[i]])],
                                          [draw.aaline(sc, BLUE, [x[i] - 5, 150 + y[i]], [x[i] + 5, 150 + y[i]])],
                                          [draw.aaline(sc, BLUE, [x[i] - 4, 146 + y[i]], [x[i] + 4, 154 + y[i]])],
                                          [draw.aaline(sc, BLUE, [x[i] - 4, 154 + y[i]], [x[i] + 4, 146 + y[i]])]]

        display.update()

        if s >= pi:
            s = 0
        else:
            s += 0.01

        clock.tick(FPS)
        

