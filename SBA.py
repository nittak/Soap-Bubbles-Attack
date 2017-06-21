from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from random import randint

window = Window(1280, 840)
window.set_title("Soap Bubbles Attack")
mouse=Window.get_mouse()
teclado=Window.get_keyboard()

game_state=0

window = Window(1280, 840)
#windowmenu= Window(640,405)
window.set_title("Soap Bubbles Attack")
mouse=Window.get_mouse()
teclado=Window.get_keyboard()

game_state=0


#Menu
start=GameImage("start.png")
start.x=window.width/2-start.width/2
start.y=1*window.height/4-start.height/2

#Mapa do jogo
background = GameImage("background.png")
caminho= GameImage("caminho.png")

#Animais para compra
bird_c = GameImage("bird.png")
llama_c = GameImage("llama.png")
elephant_c = GameImage("elephant.png")

#Animais de torre
bird = Sprite("bird.png")
llama = Sprite("llama.png")
elephant = Sprite("elephant.png")

#Torre a ser defendida
eye=Sprite("eye.png")

#Posição animais de compra.
bird_c.x = window.width / 10
bird_c.y = window.height - bird_c.height
llama_c.x = 2 * window.width / 10
llama_c.y = window.height - llama_c.height
elephant_c.x = 3 * window.width / 10
elephant_c.y = window.height - elephant_c.height

#Posição da base.
eye.x=window.width - eye.width
eye.y=18*(window.height/21)  - eye.height

#bolhas
b1=Sprite("b1.png")
b2=Sprite("b2.png")
b3=Sprite("b3.png")

b1.x=window.width/21 - b1.width
b1.y=4*window.height/21
wave1=10

speed_x=100
speed_y=100
t=1

h=1

while True:

    while game_state==0:
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

        for i in range(wave1):
            if t >= 1:
                t = 0
                b1 = Sprite("b1.png")
                bubbles1 = []
                b2 = Sprite("b2.png")
                b3 = Sprite("b3.png")
                b1.set_position(window.width / 21 - b1.width, 4 * window.height / 21)
                bubbles1.append(b1)
            t = t + window.delta_time()

        for i in range(len(bubbles1)):
            bubbles1[i].draw()

        for i in range(len(bubbles1)):
            bubbles1[i].x = bubbles1[i].x + (speed_x * window.delta_time())

            if bubbles1[i].x < 3 * window.width / 21:
                bubbles1[i].x = bubbles1[i].x + (speed_x * window.delta_time())
            elif bubbles1[i].x >= 3 * window.width / 21:
                speed_x = 0
                bubbles1[i].y = bubbles1[i].y + (speed_y * window.delta_time())
            elif bubbles1[i].y > 13 * window.height / 21:
                speed_x = 10
                speed_y = 0
            elif bubbles1[i].x >= 10.75 * window.width / 21:
                speed_x = 0
                speed_y = -10
                if bubbles1[i].y <= 9.5 * window.height / 21:
                    speed_y = 0
                    speed_x = 10
            elif bubbles1[i].x >= 14.8 * window.width / 21:
                speed_x = 0
                speed_y = 10
            elif bubbles1[i].y >= 16.5 * window.height / 21:
                speed_x = 10
                speed_y = 0

        if mouse.is_button_pressed(1):
            if mouse.is_over_object(bird_c):
                h=2
        if h==2:
            if mouse.is_button_pressed(1):
                bird.set_position(mouse.get_position()[0], mouse.get_position()[1])
            bird.draw()

        if teclado.key_pressed("ESC"):
            game_state=0

        window.update()