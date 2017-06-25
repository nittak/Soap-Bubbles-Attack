from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *

window = Window(1280, 840)
#windowmenu= Window(640,405)
window.set_title("Soap Bubbles Attack")
mouse = Window.get_mouse()
keyboard = window.get_keyboard()

game_state=1

#Menu
#menu=GameImage("Menu.jpg")
#menu1.x=window.width/2-menu1.width/2
#menu1.y=window.height/2-menu1.height/2
#bolhas=Sprite("bolhas.gif")

#start=GameImage("start.png")
#start.x=windowmenu.width/2-start.width/2
#start.y=windowmenu.height/2-start.height/2

#Mapa do jogo
background = GameImage("background.png")

#Animais para compra
birdc = GameImage("birdc.png")
llamac = GameImage("llamac.png")
elephantc = GameImage("elephantc.png")

#Animais de torre
bird = Sprite("bird.png")
llama = Sprite("llama.png")
elephant = Sprite("elephant.png")

#Demonstração
bird.x = 17*window.width/21 - bird.width
bird.y = 9*window.height/22 - bird.height
llama.x = 13*window.width/21 - llama.width
llama.y = 9*window.height/22 - llama.height
elephant.x = 15*window.width/22
elephant.y = 15*window.height/22 - elephant.height

#Torre a ser defendida
eye = Sprite("eye.png")

#bolhas
b1 = Sprite("b1.png")
b2 = Sprite("b2.png")
b3 = Sprite("b3.png")

#Posição da base
eye.x = window.width - eye.width
eye.y = window.height/2 - eye.height

speed = 100

bolhas1 = []
bolhas2 = []
bolhas3 = []
t = 1
delta = window.delta_time()

    
def cria_bolhas(bolha, grupo, tipo):
    global t

    if t >= 2:
        t = 0

        dicionario_tipos = {1: "b1.png", 2: "b2.png", 3: "b3.png"}[tipo]

        bolha = Sprite(dicionario_tipos)
        bolha.set_position(-b3.width, window.height/2 - bolha.height)

        grupo.append(bolha)

    for i in grupo:
        i.x += speed * window.delta_time()
        if i.x > window.width -3*bolha.width:
            grupo.remove(i)

    t += window.delta_time()

B = [] #vetor de birds
L = [] #vetor de llamas
E = [] #vetor de elephants

while True:
 
    while game_state==1:
        background.draw()
                
        for i in range(3):
            B.append(birdc)
            B[i].x = (i+1)*4*window.width/22
            if i == 1:
                B[i].y = 6*window.width/22 - birdc.height
            else:
                B[i].y = 9*window.width/22 - birdc.height
            B[i].draw()

        for i in range(3):
            L.append(llamac)
            L[i].x = (i+1)*5*window.width/22
            L[i].y = (i+2)*window.width/22 - llamac.height
            L[i].draw()        
        
        for i in range(3):
            E.append(elephantc)
            E[i].x = (i**3+i+5)*window.width/22
            E[i].y = (i+12)*window.width/22 - elephantc.height
            E[i].draw()        
        
        
        eye.draw()
        bird.draw()
        llama.draw()
        elephant.draw()

        delta += window.delta_time()
            
        cria_bolhas(b1,bolhas1,1)

        for i in range(len(bolhas1)):
            bolhas1[i].draw()

        if delta > 5: 
            cria_bolhas(b2,bolhas2,2)
            for i in range(len(bolhas2)):
                bolhas2[i].draw()

        if delta > 15: 
            cria_bolhas(b3,bolhas3,3)
            for i in range(len(bolhas3)):
                bolhas3[i].draw()
        
        if keyboard.key_pressed("ESC"):
            window.close()

        window.update()
