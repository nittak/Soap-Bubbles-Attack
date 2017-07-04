from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.sound import *

window = Window(1280, 840)
window.set_title("Soap Bubbles Attack")
mouse = Window.get_mouse()
keyboard = window.get_keyboard()

game_state = 0

# Menu
start = GameImage("start.png")
gameover = GameImage('gameover.png')
start.x = window.width / 2 - start.width / 2
start.y = 1 * window.height / 4 - start.height / 2
gameover.x = window.width / 2 - start.width / 2
gameover.y = 1 * window.height / 4 - start.height / 2

# Mapa do jogo
background = GameImage("background.jpg")

# Animais para compra
birdc = GameImage("birdc.png")
llamac = GameImage("llamac.png")
elephantc = GameImage("elephantc.png")

# Animais de torre
bird = Sprite("bird.png")
llama = Sprite("llama.png")
elephant = Sprite("elephant.png")

# Torre a ser defendida
eye = GameImage("eye.png")

# bolhas
b1 = Sprite("b1.png")
b2 = Sprite("b2.png")
b3 = Sprite("b3.png")

# Posição da base
eye.x = window.width - eye.width
eye.y = 1.05 * window.height / 2 - eye.height

# sound = Sound('bubblesound.ogg')

speed = 100

bolhas1 = []
bolhas2 = []
bolhas3 = []
t = 1
delta = window.delta_time()


def cria_bolhas(bolha, grupo, tipo):
    global t
    global cont
    if t >= 2:
        t = 0

        dicionario_tipos = {1: "b1.png", 2: "b2.png", 3: "b3.png"}[tipo]

        bolha = Sprite(dicionario_tipos)
        bolha.set_position(-b3.width, window.height / 2 - bolha.height)

        grupo.append(bolha)

    for i in grupo:
        i.x += speed * window.delta_time()
        if i.x > window.width - 3 * bolha.width:
            grupo.remove(i)
            cont -= tipo
    t += window.delta_time()


B = []  # vetor de birds
L = []  # vetor de llamas
E = []  # vetor de elephants

cont = 50  # Contador para o game over

TL = []  # Vetor de tiros llama
TE = []  # Vetor de tiros elephant
TP = []  # Vetor de tiros bird
contl = 1
conte = 1
contp = 1
ponto = 0
teclado = 't'  # para só atirar um animal de cada vez


def tiros_llama():
    global speed
    global contl
    if contl > 1.5 and keyboard.key_pressed("S") and teclado == 's':
        contl = 0
        for i in range(3):
            t1 = Sprite("tiro.png")
            t1.set_position((i + 1) * 5 * window.width / 22, (i + 2) * window.width / 22 - llamac.height)
            TL.append(t1)
    contl += window.delta_time()
    for k in TL:
        k.y = k.y + (speed * window.delta_time())


def tiros_elephant():
    global speed
    global conte
    if conte > 1.75 and keyboard.key_pressed("A") and teclado == 'a':
        conte = 0
        for i in range(3):
            t2 = Sprite("tiro3r.png")
            t2.set_position((i + 1) * 5 * window.width / 20, (i + 12) * window.width / 22 - elephantc.height)
            TE.append(t2)
    conte += window.delta_time()
    for k in TE:
        k.x = k.x + 2*(-speed * window.delta_time())
        k.y = k.y + 2 * (-speed * window.delta_time())

def tiros_bird():
    global speed
    global contp
    if contp > 2  and keyboard.key_pressed("W") and teclado == 'w':
        contp = 0
        for i in range(3):
            t3 = Sprite("tiro2.png")
            t3.set_position((i + 1.5) * 5 * window.width / 22, 9 * window.width / 22 - birdc.height)
            TP.append(t3)
    contp += window.delta_time()
    for k in TP:
        k.y = k.y + 2 * (-speed * window.delta_time())




def destroi_bolhas(vetor, grupo, tipo, vida):
    global ponto
    for i in range(len(vetor)):
        for j in grupo:
            if vetor[i].collided(j):
                if vida == 1:
                    grupo.remove(j)
                    ponto += tipo

                else:
                    vida = vida - 1


while True:

    while game_state == 0:
        background.draw()
        start.draw()
        if mouse.is_button_pressed(1) and mouse.is_over_object(start) or keyboard.key_pressed("ENTER"):
            game_state = 1
        if keyboard.key_pressed("ESC"):
            window.close()
        window.update()

    while game_state == 1:
        background.draw()

        for i in range(3):
            B.append(birdc)
            B[i].x = (i + 1.5) * 5 * window.width / 22
            B[i].y = 9 * window.width / 22 - birdc.height
            B[i].draw()

        for i in range(3):
            L.append(llamac)
            L[i].x = (i + 1) * 5 * window.width / 22
            L[i].y = (i + 2) * window.width / 22 - llamac.height
            L[i].draw()

        for i in range(3):
            E.append(elephantc)
            E[i].x = (i + 1) * 5 * window.width / 20
            E[i].y = (i + 12) * window.width / 22 - elephantc.height
            E[i].draw()

        eye.draw()

        delta += window.delta_time()


        cria_bolhas(b1, bolhas1, 1)
        for i in range(len(bolhas1)):
            bolhas1[i].draw()

        if delta > 5:
            cria_bolhas(b2, bolhas2, 2)
            for i in range(len(bolhas2)):
                bolhas2[i].draw()

        if delta > 15:
            cria_bolhas(b3, bolhas3, 3)
            for i in range(len(bolhas3)):
                bolhas3[i].draw()

        if cont <= 0:
            game_state = 3
            cont = 50

        if keyboard.key_pressed("A"):
            teclado = 'a'
        elif keyboard.key_pressed("S"):
            teclado = 's'
        elif keyboard.key_pressed("W"):
            teclado = 'w'

        tiros_llama()
        tiros_elephant()
        tiros_bird()


        destroi_bolhas(TL, bolhas1, 1, 1)
        destroi_bolhas(TL, bolhas2, 2, 2)
        destroi_bolhas(TL, bolhas3, 3, 3)
        destroi_bolhas(TE, bolhas1, 1, 1)
        destroi_bolhas(TE, bolhas2, 2, 2)
        destroi_bolhas(TE, bolhas3, 3, 3)
        destroi_bolhas(TP, bolhas1, 1, 1)
        destroi_bolhas(TP, bolhas2, 2, 1)
        destroi_bolhas(TP, bolhas3, 3, 1)


        for i in range(len(TE)):
            TE[i].draw()
        for i in range(len(TL)):
            TL[i].draw()
        for i in range(len(TP)):
            TP[i].draw()

        if keyboard.key_pressed("ESC"):
            window.close()

        window.draw_text("Ponto: "+ str(ponto), 3*window.width/4, 0 , 20, (255,255,255), font_name="Rockwell", bold=True, italic=False)
        window.draw_text("Vida: "+str(cont), 2*window.width/4, 0, 20, (255, 255, 255), font_name="Rockwell", bold=True, italic=False)


        window.update()

        while game_state == 3:
            gameover.draw()
            if keyboard.key_pressed("ESC"):
                window.close()
            window.update()