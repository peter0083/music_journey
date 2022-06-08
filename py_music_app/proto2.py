import pygame, math
import os
import vlc
import time

# create vlc media player object
player = vlc.MediaPlayer()
# media object
media = vlc.Media("../music_app/src/audio/Flower_Sample.mp3")
# setting media to the media player
player.set_media(media)


os.environ["SDL_VIDEO_CENTERED"]='1'

white, black, purple, blue = (255, 255, 255), (0, 0 ,0), (100, 0, 100), (21, 71, 200)
width, height = 1000, 1000

pygame.init()
pygame.display.set_caption("Fractal Tree")
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

speed = 0.001

def FractalTree(position, angle, z_value, n_value, direction,color=black, depth=0):
    branch_ratio = 0.30
    branch = z_value * branch_ratio
    angle_x = branch * math.cos(direction)
    angle_y = branch * math.sin(direction)
    (x, y) = n_value
    next_position = (x + angle_x, y + angle_y)
    pygame.draw.line(screen, color, n_value, next_position)

    if position > 0:
        if depth == 0:
            color2 = blue
            color1 = purple
        else:
            color1 = color
            color2 = color

        new = z_value * (1 - branch_ratio)
        FractalTree(position-1, angle, new, next_position, direction-angle, color1, depth+1)
        FractalTree(position-1, angle, new, next_position, direction+angle, color1, depth+1)


def main(ms_duration):
    sec_duration = ms_duration / 1000  # convert milliseconds to seconds
    start_ticks=pygame.time.get_ticks() #starter tick
    angle = 0
    while True:
        seconds=(pygame.time.get_ticks()-start_ticks)/1000 #calculate how many seconds
        if seconds > sec_duration: # if more than 10 seconds close the game
            break
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        angle += speed
        screen.fill(white)
        FractalTree(9, angle, height * 0.9, (width//2, width-50), -math.pi/2)
        pygame.display.update()

if __name__=='__main__':
    player.play()
    time.sleep(5)
    play_time = player.get_length() # music play time in milliseconds
    print(play_time)
    main(play_time)
    pygame.quit()