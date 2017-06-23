from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *

window = Window(1280, 840)
# windowmenu= Window(640,405)
window.set_title("Soap Bubbles Attack")
mouse = Window.get_mouse()
keyboard = window.get_keyboard()

game_state = 0

start=GameImage("start.png")
start.x=window.width/2-start.width/2
start.y=window.height/2-start.height/2

# Mapa do jogo
background = GameImage("background.jpg")

# Animais para compra
bird_c = GameImage("bird.png")
llama_c = GameImage("llama.png")
elephant_c = GameImage("elephant.png")

# Animais de torre
bird = Sprite("bird.png")
llama = Sprite("llama.png")
elephant = Sprite("elephant.png")

# Torre a ser defendida
eye = Sprite("eye.png")

# bolhas
b1 = Sprite("b1.png")
b2 = Sprite("b2.png")
b3 = Sprite("b3.png")

# Posicao animais de compra
bird_c.x = window.width / 10
bird_c.y = window.height - bird_c.height
llama_c.x = 2 * window.width / 10
llama_c.y = window.height - llama_c.height
elephant_c.x = 3 * window.width / 10
elephant_c.y = window.height - elephant_c.height

# Posicao da base
eye.x = window.width - eye.width
eye.y = window.height / 2 - eye.height

speed = 200

bolhas1 = []
bolhas2 = []
bolhas3 = []
t = 1
delta = window.delta_time()

newbird = []

animal_selecionado = "bird"

def cria_bolhas(bolha, grupo, tipo):
    global t

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

    t += window.delta_time()

def criando_torres(grupo, animal, animal_compra):
    global animal_selecionado

    if mouse.is_button_pressed(1) and  mouse.is_over_object(animal_compra):
        animal_selecionado = animal

    if mouse.is_button_pressed(3):
        animal = Sprite(animal + ".png")
        animal.set_position(mouse.get_position()[0], mouse.get_position()[1])
        grupo.append(animal)

    for i in range(len(grupo)):
        grupo[i].draw()

while True:

    while game_state == 0:
        background.draw()
        start.draw()

        if mouse.is_button_pressed(1):
            if mouse.is_over_object(start):
                game_state = 1

        window.update()

    while game_state == 1:
        background.draw()
        bird_c.draw()
        llama_c.draw()
        elephant_c.draw()
        eye.draw()

        delta += window.delta_time()

        cria_bolhas(b1, bolhas1, 1)

        for i in range(len(bolhas1)):
            bolhas1[i].draw()

        if delta > 3:
            cria_bolhas(b2, bolhas2, 2)
            for i in range(len(bolhas2)):
                bolhas2[i].draw()

        if delta > 5:
            cria_bolhas(b3, bolhas3, 3)
            for i in range(len(bolhas3)):
                bolhas3[i].draw()

        criando_torres(newbird, "bird", bird_c)

        if mouse.is_button_pressed(1) and mouse.is_over_object(bird_c):
            bird = Sprite("bird.png")
        if mouse.is_button_pressed(3):
            newbird.append(bird)
            bird.set_position(mouse.get_position()[0], mouse.get_position()[1])
        for i in range (len(newbird)):
            newbird[i].draw()

        if keyboard.key_pressed("ESC"):
            window.close()

        window.update()