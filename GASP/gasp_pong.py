import gasp
import time 

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600 

DIST = 20 #distance beetween wall and paddle

PADDLE_H = 40 #paddle width,height and speed
PADDLE_W = 5
PADDLE_SPEED = 5

CUBE_W = 10 #cube properties˚
CUBE_SPD = 5

TXT_DIST = 100 #more stuff for the text, again it is now useless
TXT_Y = 80


RX = SCREEN_WIDTH - DIST

def stuffs():

    run = True

    ly = SCREEN_HEIGHT // 2 - PADDLE_H // 2 #initializing the starting y values of the paddles
    ry = SCREEN_HEIGHT // 2 - PADDLE_H // 2

    x = SCREEN_WIDTH // 2 - CUBE_W #initializing the starting position of the cube
    y = SCREEN_HEIGHT // 2 - CUBE_W

    vectx = -1 #vectors controlling the x and y direction, remember, in pong it will always be travelling diagonally
    vecty = -1 #so in both cases 0 should actually be -1 but hey.

    l_score = 0 #useless
    r_score = 0

    gasp.begin_graphics(width=SCREEN_WIDTH, height=SCREEN_HEIGHT, title="My Game", background=gasp.color.BLACK)

    cube = gasp.Box((x + CUBE_W / 2, y + CUBE_W / 2), CUBE_W, CUBE_W, filled=True, color=gasp.color.WHITE, thickness=0)

    paddle_r = gasp.Box((RX + PADDLE_W / 2, ry + PADDLE_H / 2), PADDLE_W, PADDLE_H, filled=True, color=gasp.color.WHITE, thickness=0)

    paddle_l = gasp.Box((DIST + PADDLE_W / 2, ly + PADDLE_H / 2), PADDLE_W, PADDLE_H, filled=True, color=gasp.color.WHITE, thickness=0)

    while True:


        '''keys = gasp.keys_pressed()
        if keys.dict_keys() == 'Up':
            ry = ry - PADDLE_SPEED #each moves ry or ly which controlls the y position of the paddles
            gasp.move_by(paddle_r,0,-PADDLE_SPEED)
            print("up")
        if keys == [pg.K_DOWN]:
            ry = ry + PADDLE_SPEED
            gasp.move_by(paddle_r,0,PADDLE_SPEED)
            print("down")
        if keys == [pg.K_w]:
            ly = ly - PADDLE_SPEED
            gasp.move_by(paddle_l,0,-PADDLE_SPEED)
            print("w")
        if keys == [pg.K_s]:
            ly = ly + PADDLE_SPEED
            gasp.move_by(paddle_l,0,PADDLE_SPEED)
            print("s")'''


        #collisions:
        #floor:
        if y - CUBE_SPD <= 0 and vecty == -1:
            print(y,vecty)
            vecty = 1 
        #cieling:
        if y + CUBE_SPD >= SCREEN_HEIGHT and vecty == 1:
            vecty = -1
        
        #left
        if x <= DIST + PADDLE_W and x >= DIST and y >= ly and y <= ly + PADDLE_H:
            vectx = 1
        #right
        if x + CUBE_W >= RX and x + CUBE_W <= RX + PADDLE_W and y >= ry and y <= ry + PADDLE_H:
            vectx = -1

        
        #reseting if cube goes offscreen:
        #left:
        if x <= 0 and vectx == -1:
            r_score += 1
            x = SCREEN_WIDTH // 2 - CUBE_W
            y = SCREEN_HEIGHT // 2 - CUBE_W
            vectx = 1
        #right:
        if x + CUBE_W >= SCREEN_WIDTH and vectx == 1:
            l_score += 1
            x = SCREEN_WIDTH // 2 - CUBE_W
            y = SCREEN_HEIGHT // 2 - CUBE_W
            vectx = -1


        #movement based on vectors
        if vecty == 1:
            y = y + CUBE_SPD
            temp_y = CUBE_SPD
        else:
            y = y - CUBE_SPD
            temp_y = -CUBE_SPD
        if vectx == 1:
            x = x + CUBE_SPD
            temp_x = CUBE_SPD
        else:
            x = x - CUBE_SPD
            temp_x = -CUBE_SPD

        #gasp.move_by(cube,temp_x,temp_y)
        gasp.move_to(cube,(x,y))

        #print("y: ", y)

        time.sleep(0.01)



        


    gasp.end_graphics()



if __name__ =="__main__":
    stuffs()
