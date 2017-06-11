from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *

window = Window(1280, 840)
#windowmenu= Window(640,405)
window.set_title("Soap Bubbles Attack")
mouse=Window.get_mouse()
teclado=Window.get_keyboard()

game_state=0

#Menu
menu=GameImage("Menu.jpg")
#menu1.x=window.width/2-menu1.width/2
#menu1.y=window.height/2-menu1.height/2
bolhas=Sprite("bolhas.gif")


start=GameImage("start.png")
#start.x=windowmenu.width/2-start.width/2
#start.y=windowmenu.height/2-start.height/2

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

#Demonstração
bird.x=17*window.width/21 - bird.width
bird.y=8*window.height/21
elephant.x=8*window.width/21
elephant.y=10*window.height/21


#Torre a ser defendida
eye=Sprite("eye.png")

#bolhas
b1=Sprite("b1.png")
b2=Sprite("b2.png")
b3=Sprite("b3.png")
b1.x=window.width/21 - b1.width
b1.y=4*window.height/21



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


speed_x=100
speed_y=100
speed=0
while True:
    while game_state==0:
        menu.draw()
        bolhas.draw()
        start.draw()


        if mouse.is_button_pressed(1):
            if mouse.is_over_object(start):
                game_state = 1
        if teclado.key_pressed("ESC"):
            window.close()

        window.update()

    while game_state==1:

        background.draw()
        bird_c.draw()
        llama_c.draw()
        elephant_c.draw()
        eye.draw()
        bird.draw()
        llama.draw()
        elephant.draw()
        caminho.draw()

        b1.move_x(speed_x * window.delta_time())

        if b1.x<3*window.width/21:
            speed_x=speed_x
        if b1.x>=2.75*window.width/21 :
            speed_x=0
            b1.move_y(speed_y * window.delta_time())
        if b1.y>13*window.height/21:
            speed_x=100
            speed_y=0
        if b1.x>=10.75*window.width/21:
            speed_x=0
            speed_y=-100
            if b1.y<=9.5*window.height/21:
                speed_y=0
                speed_x=100
        if b1.x>=14.8*window.width/21:
            speed_x=0
            speed_y=100
        if b1.y>=16.7*window.height/21:
            speed_x=100
            speed_y=0
        b1.draw()


        window.update()