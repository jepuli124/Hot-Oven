import pygame

pygame.init()

Ix = 1920
Iy = 1080

Ikkuna = pygame.display.set_mode((Ix, Iy))

pygame.display.set_caption("Ikkuna")

A1 = pygame.image.load("pict/Bg.png")
Ikkuna.blit(A1, (0, 0))
font = pygame.font.Font('freesansbold.ttf', 150)
starttext = font.render("Loading", True, (255, 255, 255))
Ikkuna.blit(starttext, ((Ix/2)-300, (Iy/2)-75))
pygame.display.flip()


def drawing():
    global huva, mx, my, il, cl1, cl2, cl3, cl4, cl5, oven, comcount, Input, anicount, selection, FPS, ovens
    if anicount >= FPS + 1:
        anicount = 1
    else:
        anicount += 1

    if huva == 1:
        Ikkuna.blit(A1, (0, 0))
        for x in range(5):
            if mx == x:
                if my == 0:
                    if ovens[x]:
                        Ikkuna.blit(B2, (225 + (250 * x), 500))
                    else:
                        Ikkuna.blit(B1, (225 + (250 * x), 500))
                    Ikkuna.blit(B3, (225 + (250 * x), 650))
                    Ikkuna.blit(B4s, (235 + (250 * x), 350))
                elif my == 1:
                    if ovens[x]:
                        Ikkuna.blit(B2s, (225 + (250 * x), 500))
                    else:
                        Ikkuna.blit(B1s, (225 + (250 * x), 500))
                    Ikkuna.blit(B3, (225 + (250 * x), 650))
                    Ikkuna.blit(B4, (235 + (250 * x), 350))
                elif my == 2:
                    if ovens[x]:
                        Ikkuna.blit(B2, (225 + (250 * x), 500))
                    else:
                        Ikkuna.blit(B1, (225 + (250 * x), 500))
                    Ikkuna.blit(B3s, (225 + (250 * x), 650))
                    Ikkuna.blit(B4, (235 + (250 * x), 350))

            else:
                if ovens[x]:
                    Ikkuna.blit(B2, (225 + (250 * x), 500))
                else:
                    Ikkuna.blit(B1, (225 + (250 * x), 500))
                Ikkuna.blit(B3, (225 + (250 * x), 650))
                Ikkuna.blit(B4, (235 + (250 * x), 350))
            Ikkuna.blit(IconCold, (220 + (250 * x), 200))
    elif huva == 2:
        Ikkuna.blit(A1, (0, 0))
        if mx == 4:
            Ikkuna.blit(CtrlC, (200, 200))
        elif mx == 3:
            Ikkuna.blit(CtrlR, (200, 200))
        elif mx == 2:
            Ikkuna.blit(CtrlA, (200, 200))
        elif mx == 1:
            Ikkuna.blit(CtrlN, (200, 200))
        elif mx == 5:
            Ikkuna.blit(CtrlSD, (200, 200))
        elif mx == 6:
            Ikkuna.blit(CtrlSU, (200, 200))
        else:
            Ikkuna.blit(Ctrl, (200, 200))
        f1 = pygame.font.Font('freesansbold.ttf', 75)
        t1 = f1.render(str(il[0]), True, (0, 0, 0))
        t2 = f1.render(str(il[1]), True, (0, 0, 0))
        t3 = f1.render(str(il[2]), True, (0, 0, 0))
        Ikkuna.blit(t1, (910, 390))
        Ikkuna.blit(t2, (910, 510))
        Ikkuna.blit(t3, (910, 630))
        if oven == 0:
            uunilista(cl1)
        elif oven == 1:
            uunilista(cl2)
        elif oven == 2:
            uunilista(cl3)
        elif oven == 3:
            uunilista(cl4)
        elif oven == 4:
            uunilista(cl5)
        if anicount <= FPS / 2:
            if Input:
                if selection == 1:
                    pit = len(str(il[0]))
                    Ikkuna.blit(Bar, (911 + (pit * 43), 380))
                if selection == 2:
                    pit = len(str(il[1]))
                    Ikkuna.blit(Bar, (911 + (pit * 43), 500))
                if selection == 3:
                    pit = len(str(il[2]))
                    Ikkuna.blit(Bar, (911 + (pit * 43), 620))
    else:
        Ikkuna.blit(A1, (0, 0))


def uunilista(cl):
    global comcount
    f2 = pygame.font.Font('freesansbold.ttf', 30)
    c = 0
    for x in cl:
        x0 = str(x[0])
        x1 = str(x[1])
        x2 = str(x[2])
        tt1 = f2.render(str(x0), True, (0, 0, 0))
        tt2 = f2.render(str(x1), True, (0, 0, 0))
        tt3 = f2.render(str(x2), True, (0, 0, 0))
        if comcount > len(cl) - 4 or comcount == -1:
            comcount = len(cl) - 4
        if comcount <= c <= comcount + 3:
            if mx == 7 + (c * 3) - (comcount * 3):
                Ikkuna.blit(comUp, (1292, 407 + ((c - comcount) * 95)))
            elif mx == 7 + (c * 3) + 1 - (comcount * 3):
                Ikkuna.blit(comDown, (1292, 407 + ((c - comcount) * 95)))
            elif mx == 7 + (c * 3) + 2 - (comcount * 3):
                Ikkuna.blit(comDel, (1292, 407 + ((c - comcount) * 95)))
            else:
                Ikkuna.blit(com, (1292, 407 + ((c - comcount) * 95)))
            Ikkuna.blit(tt1, (1430, 462 + ((c - comcount) * 95)))
            Ikkuna.blit(tt2, (1302, 462 + ((c - comcount) * 95)))
            Ikkuna.blit(tt3, (1551, 462 + ((c - comcount) * 95)))
        c += 1


def napp():  # did this
    global run, huva, mouse, tuna
    nappain = pygame.key.get_pressed()
    if not Input and tuna <= 0:
        if nappain[pygame.K_ESCAPE]:
            run = False
            return
    c1 = pygame.mouse.get_pressed(num_buttons=3)
    e1 = pygame.mouse.get_pos()
    if huva == 1:
        if huva1(e1, c1) == 2:
            huva = 2
    elif huva == 2:
        if huva2(e1, c1, nappain) == 1:
            huva = 1
    if c1[0]:
        tuna = 1
    else:
        tuna -= 1


def huva1(e1, c1):  # do that
    global mx, my, oven, tuna, comcount
    luva = 1
    if e1:
        for x in range(5):
            if (220 + (250 * x)) <= e1[0] <= (328 + (250 * x)):
                mx = x
                break
            else:
                mx = -1
        if 350 <= e1[1] <= 478:
            my = 0
        elif 500 <= e1[1] <= 556:
            my = 1
            if c1[0] and tuna <= 0:
                active(mx)
        elif 650 <= e1[1] <= 706:
            my = 2
            if c1[0] and tuna <= 0:
                deactive(mx)
        else:
            mx = -1
        if my == 0 and mx >= 0 and c1[0] and tuna <= 0:
            luva = 2
            comcount = -1
            oven = mx
    tuna -= 1
    return luva


def huva2(e1, c1, nappain):  # do that
    global Input, mx, oven, selection, tuna, comcount, ovens
    luva = 0
    if not Input:
        if 200 <= e1[1] <= 276:
            if 200 <= e1[0] <= 960:
                mx = 1
                if c1[0] and tuna <= 0:
                    luva = 1
                    oven = -1
                    return luva
            elif 960 <= e1[0] <= 1720:
                mx = 2
                if c1[0] and tuna <= 0:
                    luva = 1
                    oven = -1
                    return luva
            else:
                mx = -1
        else:
            mx = -1
        if not ovens[oven]:
            if 772 <= e1[1] <= 840:
                if 906 <= e1[0] <= 1066:
                    mx = 3
                    if c1[0] and tuna <= 0:
                        savenot()
                        tuna = 4
                    return luva
                elif 1067 <= e1[0] <= 1233:
                    mx = 4
                    if c1[0] and tuna <= 0:
                        save()
                        tuna = 4
                    return luva
            if 1292 <= e1[0] <= 1681:
                if 373 <= e1[1] <= 398:
                    mx = 6
                    if c1[0] and tuna <= 0:
                        if not comcount <= 0:
                            comcount -= 1
                    return luva
                elif 817 <= e1[1] <= 844:
                    mx = 5
                    if c1[0] and tuna <= 0:
                        comcount += 1
            if 1410 <= e1[0] <= 1441:  # Vaihtaa komentorivien järjestystä
                for i in range(4):
                    if 418 + (i * 95) <= e1[1] <= 446 + (i * 95):
                        if i == 0:
                            mx = 7
                            if c1[0] and tuna <= 0:
                                switch(oven, 1, comcount)
                            return luva
                        elif i == 1:
                            mx = 10
                            if c1[0] and tuna <= 0:
                                switch(oven, 1, comcount + 1)
                            return luva
                        elif i == 2:
                            mx = 13
                            if c1[0] and tuna <= 0:
                                switch(oven, 1, comcount + 2)
                            return luva
                        elif i == 3:
                            mx = 16
                            if c1[0] and tuna <= 0:
                                switch(oven, 1, comcount + 3)
                            return luva
            elif 1530 <= e1[0] <= 1561:  # Vaihtaa komentorivien järjestystä
                for i in range(4):
                    if 418 + (i * 95) <= e1[1] <= 446 + (i * 95):
                        if i == 0:
                            mx = 8
                            if c1[0] and tuna <= 0:
                                switch(oven, 0, comcount)
                            return luva
                        elif i == 1:
                            mx = 11
                            if c1[0] and tuna <= 0:
                                switch(oven, 0, comcount + 1)
                            return luva
                        elif i == 2:
                            mx = 14
                            if c1[0] and tuna <= 0:
                                switch(oven, 0, comcount + 2)
                            return luva
                        elif i == 3:
                            mx = 17
                            if c1[0] and tuna <= 0:
                                switch(oven, 0, comcount + 3)
                            return luva
            elif 1638 <= e1[0] <= 1669:  # Poistaa komentorivin
                for i in range(4):
                    if 418 + (i * 95) <= e1[1] <= 446 + (i * 95):
                        if i == 0:
                            mx = 9
                            if c1[0] and tuna <= 0:
                                tuna = 4
                                delete(comcount, oven)
                            return luva
                        elif i == 1:
                            mx = 12
                            if c1[0] and tuna <= 0:
                                tuna = 4
                                delete(comcount + 1, oven)
                            return luva
                        elif i == 2:
                            mx = 15
                            if c1[0] and tuna <= 0:
                                tuna = 4
                                delete(comcount + 2, oven)
                            return luva
                        elif i == 3:
                            mx = 18
                            if c1[0] and tuna <= 0:
                                tuna = 4
                                delete(comcount + 3, oven)
                            return luva

            if (905 <= e1[0] <= 1232) and (367 <= e1[1] <= 482) and c1[0] and tuna <= 0:  # Valitsee kohde lämpötilan
                Input = True
                selection = 1
                tuna = 4

            elif (905 <= e1[0] <= 1232) and (483 <= e1[1] <= 595) and c1[0] and tuna <= 0:  # Valitsee ajan jossa lämpötilaan tulee päästä
                Input = True
                selection = 2
                tuna = 4

            elif (905 <= e1[0] <= 1232) and (596 <= e1[1] <= 711) and c1[0] and tuna <= 0:  # Valitse aika kuinka pitkään lämpötilassa pitää olla
                Input = True
                selection = 3
                tuna = 4

    if Input:  # input vaihe
        if (905 >= e1[0] or e1[0] >= 1232) and (367 >= e1[1] or 482 <= e1[1]) and c1[0] and tuna <= 0:
            inf()

        if nappain and tuna <= 0:
            if nappain[pygame.K_1]:
                insert(1)
                tuna = 4
            elif nappain[pygame.K_2]:
                insert(2)
                tuna = 4
            elif nappain[pygame.K_3]:
                insert(3)
                tuna = 4
            elif nappain[pygame.K_4]:
                insert(4)
                tuna = 4
            elif nappain[pygame.K_5]:
                insert(5)
                tuna = 4
            elif nappain[pygame.K_6]:
                insert(6)
                tuna = 4
            elif nappain[pygame.K_7]:
                insert(7)
                tuna = 4
            elif nappain[pygame.K_8]:
                insert(8)
                tuna = 4
            elif nappain[pygame.K_9]:
                insert(9)
                tuna = 4
            elif nappain[pygame.K_0]:
                insert(0)
                tuna = 4
            elif nappain[pygame.K_BACKSPACE]:
                insertnot()
                tuna = 4
            elif nappain[pygame.K_ESCAPE]:
                inf()
                tuna = 4
            elif nappain[pygame.K_RETURN]:
                inf()
                tuna = 4
            else:
                tuna = 0

    return luva


def intr():  # aloittaa input vaiheen
    global Input
    Input = True


def inf():  # lopettaa input vaiheen
    global Input, selection
    Input = False
    selection = -1


def insert(a):  # tallentaa numeron välitilaan il listalle
    global il, selection
    if selection == 1:
        il[0] = (il[0] * 10) + a
    elif selection == 2:
        il[1] = (il[1] * 10) + a
    elif selection == 3:
        il[2] = (il[2] * 10) + a


def insertnot():  # poistaa uusimman numeron välitilasta (il listasta)
    global il, selection
    if selection == 1:
        il[0] //= 10
    elif selection == 2:
        il[1] //= 10
    elif selection == 3:
        il[2] //= 10


def save():  # tallentaa komennon komentosarjaan ja tiedostoon
    global oven, il, cl1, cl2, cl3, cl4, cl5, comcount
    count = 0
    comcount = -1
    file = open("file.txt", "r")
    filer = file.readlines()
    filed = open("file.txt", "w")
    if oven == 0:
        a = (il[0], il[1], il[2])
        cl1.append(a)
    if oven == 1:
        a = (il[0], il[1], il[2])
        cl2.append(a)
    if oven == 2:
        a = (il[0], il[1], il[2])
        cl3.append(a)
    if oven == 3:
        a = (il[0], il[1], il[2])
        cl4.append(a)
    if oven == 4:
        a = (il[0], il[1], il[2])
        cl5.append(a)
    for x in filer:
        count += 1
        if count == (4 * oven) + 1:
            filed.write(x + "," + str(il[0]))
        elif count == (4 * oven) + 2:
            filed.write(x + "," + str(il[1]))
        elif count == (4 * oven) + 3:
            filed.write(x + "," + str(il[2]))
        else:
            filed.write(x)
    il = [0, 0, 0]


def savenot():  # tyhjentää komentosarjan
    global il
    il = [0, 0, 0]


"""
 def rtf():  # Ram to file
    global cl1, cl2, cl3, cl4, cl5
    a = []
    b = []
    c = []
    filed = open("file.txt", "w")
    filed.write("Oven 1\n")
    for x in cl1:
        a.append(x[0])
        b.append(x[1])
        c.append(x[2])
    filed.write(",")
    a.reverse()
    b.reverse()
    c.reverse()
    for x in a:
        filed.write(str(x)+",")
    filed.write("\n,")
    for x in b:
        filed.write(str(x)+",")
    filed.write("\n,")
    for x in c:
        filed.write(str(x)+",")
    filed.write("\n")
    a = []
    b = []
    c = []
    filed.write("Oven 2\n")
    for x in cl2:
        a.append(x[0])
        b.append(x[1])
        c.append(x[2])
    filed.write(",")
    a.reverse()
    b.reverse()
    c.reverse()
    for x in a:
        filed.write(str(x)+",")
    filed.write("\n,")
    for x in b:
        filed.write(str(x)+",")
    filed.write("\n,")
    for x in c:
        filed.write(str(x)+",")
    filed.write("\n")
    a = []
    b = []
    c = []
    filed.write("Oven 3\n")
    for x in cl3:
        a.append(x[0])
        b.append(x[1])
        c.append(x[2])
    filed.write(",")
    a.reverse()
    b.reverse()
    c.reverse()
    for x in a:
        filed.write(str(x)+",")
    filed.write("\n,")
    for x in b:
        filed.write(str(x)+",")
    filed.write("\n,")
    for x in c:
        filed.write(str(x)+",")
    filed.write("\n")
    a = []
    b = []
    c = []
    filed.write("Oven 4\n")
    for x in cl4:
        a.append(x[0])
        b.append(x[1])
        c.append(x[2])
    filed.write(",")
    a.reverse()
    b.reverse()
    c.reverse()
    for x in a:
        filed.write(str(x)+",")
    filed.write("\n,")
    for x in b:
        filed.write(str(x)+",")
    filed.write("\n,")
    for x in c:
        filed.write(str(x)+",")
    filed.write("\n")
    a = []
    b = []
    c = []
    filed.write("Oven 5\n")
    for x in cl5:
        a.append(x[0])
        b.append(x[1])
        c.append(x[2])
    filed.write(",")
    a.reverse()
    b.reverse()
    c.reverse()
    for x in a:
        filed.write(str(x)+",")
    filed.write("\n,")
    for x in b:
        filed.write(str(x)+",")
    filed.write("\n,")
    for x in c:
        filed.write(str(x)+",")
    filed.write("\n,")
"""


def rtf2():  # Ram to file 2 made by asking chatGPT to optimaze my code and then adding globals and fixing missing , from file
    global cl1, cl2, cl3, cl4, cl5
    filed = open("file.txt", "w")
    oven_names = ["Oven 1", "Oven 2", "Oven 3", "Oven 4", "Oven 5"]
    furnaces = [cl1, cl2, cl3, cl4, cl5]

    for oven_name, furnace in zip(oven_names, furnaces):
        filed.write(oven_name + "\n")

        a, b, c = [], [], []
        for x in furnace:
            a.append(x[0])
            b.append(x[1])
            c.append(x[2])

        a.reverse()
        b.reverse()
        c.reverse()

        if a:
            filed.write("," + ",".join(str(x) for x in a) + ",\n")
        else:
            filed.write("," + "\n")
        if b:
            filed.write("," + ",".join(str(x) for x in b) + ",\n")
        else:
            filed.write("," + "\n")
        if c:
            filed.write("," + ",".join(str(x) for x in c) + ",\n")
        else:
            filed.write("," + "\n")


def startfile():  # ohjelman käynnistyessä yrittää luoda uuden tiedoston, jos tiedosto on olemassa kutsuu ftr():n
    try:
        open("file.txt", "x")
        file = open("file.txt", "w")
        file.write(
            "Oven 1\n,\n,\n,\nOven 2\n,\n,\n,\nOven 3\n,\n,\n,\nOven 4\n,\n,\n,\nOven 5\n,\n,\n,\nEnd of file"
        )
    except FileExistsError:
        ftr()


def ftr():  # suorittaa komentojen siirron tiedostosta (file.txt) ohjelmalle
    global cl1, cl2, cl3, cl4, cl5
    file = open("file.txt", "r")
    filer = file.readlines()
    count = 0
    count2 = 0
    a = []
    b = []
    c = []
    for x in filer:
        count += 1
        if count != 1 and count != 5 and count != 9 and count != 13 and count != 17 and count != 21:
            count2 += 1
            if count2 == 1:
                a = x.split(",")
            elif count2 == 2:
                b = x.split(",")
            elif count2 == 3:
                c = x.split(",")
                count2 = 0
            else:
                count2 = 0
            if count == 4:
                while 1 <= len(a) and 1 <= len(b) and 1 <= len(c):
                    if not a[-1] == '\n' and not b[-1] == '\n' and not c[-1] == '\n':
                        if not a[-1] == '' and not b[-1] == '' and not c[-1] == '':
                            cl1.append((a[-1], b[-1], c[-1]))
                    a.pop()
                    b.pop()
                    c.pop()
            if count == 8:
                while 1 <= len(a) and 1 <= len(b) and 1 <= len(c):
                    if not a[-1] == '\n' and not b[-1] == '\n' and not c[-1] == '\n':
                        if not a[-1] == '' and not b[-1] == '' and not c[-1] == '':
                            cl2.append((a[-1], b[-1], c[-1]))
                    a.pop()
                    b.pop()
                    c.pop()
            if count == 12:
                while 1 <= len(a) and 1 <= len(b) and 1 <= len(c):
                    if not a[-1] == '\n' and not b[-1] == '\n' and not c[-1] == '\n':
                        if not a[-1] == '' and not b[-1] == '' and not c[-1] == '':
                            cl3.append((a[-1], b[-1], c[-1]))
                    a.pop()
                    b.pop()
                    c.pop()
            if count == 16:
                while 1 <= len(a) and 1 <= len(b) and 1 <= len(c):
                    if not a[-1] == '\n' and not b[-1] == '\n' and not c[-1] == '\n':
                        if not a[-1] == '' and not b[-1] == '' and not c[-1] == '':
                            cl4.append((a[-1], b[-1], c[-1]))
                    a.pop()
                    b.pop()
                    c.pop()
            if count == 20:
                while 1 <= len(a) and 1 <= len(b) and 1 <= len(c):
                    if not a[-1] == '\n' and not b[-1] == '\n' and not c[-1] == '\n':
                        if not a[-1] == '' and not b[-1] == '' and not c[-1] == '':
                            cl5.append((a[-1], b[-1], c[-1]))
                    a.pop()
                    b.pop()
                    c.pop()
    return


def delete(n, lista):
    global cl1, cl2, cl3, cl4, cl5
    if lista == 0:
        if 0 <= n < len(cl1):
            cl1.pop(n)
            rtf2()
    elif lista == 1:
        if 0 <= n < len(cl2):
            cl2.pop(n)
            rtf2()
    elif lista == 2:
        if 0 <= n < len(cl3):
            cl3.pop(n)
            rtf2()
    elif lista == 3:
        if 0 <= n < len(cl4):
            cl4.pop(n)
            rtf2()
    elif lista == 4:
        if 0 <= n < len(cl5):
            cl5.pop(n)
            rtf2()
    return


def switch(uuni, b, co):
    global cl1, cl2, cl3, cl4, cl5
    if uuni == 0:
        if b:
            if co != 0:
                a = cl1[co]
                cl1.pop(co)
                cl1.insert(co-1, a)
        else:
            a = cl1[co]
            cl1.pop(co)
            if co >= len(cl1):
                cl1.append(a)
            else:
                cl1.insert(co+1, a)
    if uuni == 1:
        if b:
            if co != 0:
                a = cl2[co]
                cl2.pop(co)
                cl2.insert(co-1, a)
        else:
            a = cl2[co]
            cl2.pop(co)
            if co >= len(cl2):
                cl2.append(a)
            else:
                cl2.insert(co+1, a)
    if uuni == 2:
        if b:
            if co != 0:
                a = cl3[co]
                cl3.pop(co)
                cl3.insert(co-1, a)
        else:
            a = cl3[co]
            cl3.pop(co)
            if co >= len(cl3):
                cl3.append(a)
            else:
                cl3.insert(co+1, a)
    if uuni == 3:
        if b:
            if co != 0:
                a = cl4[co]
                cl4.pop(co)
                cl4.insert(co-1, a)
        else:
            a = cl4[co]
            cl4.pop(co)
            if co >= len(cl4):
                cl4.append(a)
            else:
                cl4.insert(co+1, a)
    if uuni == 4:
        if b:
            if co != 0:
                a = cl5[co]
                cl5.pop(co)
                cl5.insert(co-1, a)
        else:
            a = cl5[co]
            cl5.pop(co)
            if co >= len(cl5):
                cl5.append(a)
            else:
                cl5.insert(co+1, a)
    rtf2()


def active(act):
    global ovens
    if act == 0:
        ovens[0] = True
    elif act == 1:
        ovens[1] = True
    elif act == 2:
        ovens[2] = True
    elif act == 3:
        ovens[3] = True
    elif act == 4:
        ovens[4] = True


def deactive(act):
    global ovens
    if act == 0:
        ovens[0] = False
    elif act == 1:
        ovens[1] = False
    elif act == 2:
        ovens[2] = False
    elif act == 3:
        ovens[3] = False
    elif act == 4:
        ovens[4] = False


def upkeep():
    global ovens, ovenscl
    pass

B1 = pygame.image.load("pict/Start.png")
B1s = pygame.image.load("pict/Start s.png")
B2 = pygame.image.load("pict/Active.png")
B2s = pygame.image.load("pict/Active S.png")
B3 = pygame.image.load("pict/Stop.png")
B3s = pygame.image.load("pict/Stop S.png")
B4 = pygame.image.load("pict/gear.png")
B4s = pygame.image.load("pict/gear S.png")
Ctrl = pygame.image.load("pict/Control.png")
CtrlC = pygame.image.load("pict/Control Command.png")
CtrlR = pygame.image.load("pict/Control Reset.png")
CtrlA = pygame.image.load("pict/Control Accept.png")
CtrlN = pygame.image.load("pict/Control No.png")
CtrlSD = pygame.image.load("pict/Control sdown.png")
CtrlSU = pygame.image.load("pict/Control sup.png")
CtrlSB = pygame.image.load("pict/Control sboth.png")
IconCold = pygame.image.load("pict/Cold Icon.png")
IconHeat = pygame.image.load("pict/Heat Icon.png")
Bar = pygame.image.load("pict/bar.png")
com = pygame.image.load("pict/Cpanel.png")
comUp = pygame.image.load("pict/CpanelUp.png")
comDown = pygame.image.load("pict/CpanelDown.png")
comDel = pygame.image.load("pict/CpanelDelete.png")
comHeat = pygame.image.load("pict/Cpanel-w.png")
comStay = pygame.image.load("pict/Cpanel-s.png")
comDone = pygame.image.load("pict/Cpanel-d.png")

run = True
Kuva = 0
huva = 1
FPS = 30
clock = pygame.time.Clock()
tuna = 1
mx = -1
my = -1
Input = False
selection = 0
oven = -1
comcount = 0
command = 0
anicount = 0
mouse = True

il = [0, 0, 0]
cl1, cl2, cl3, cl4, cl5 = [], [], [], [], []
ovenscl = [cl1, cl2, cl3, cl4, cl5]
ovens = [False, False, False, False, False]

startfile()

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    napp()
    drawing()
    clock.tick(FPS)
    pygame.display.flip()

pygame.quit()
