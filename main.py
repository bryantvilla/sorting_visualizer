from matplotlib.pyplot import draw
import pygame
import DrawInfo
import random


draw_info = DrawInfo.DrawInfo

def draw(draw_info):
   draw_info.window.fill(draw_info.BACKGROUND_COLOR)
   draw_list(draw_info)
   pygame.display.update()

def draw_list(draw_info):
    lst = draw_info.lst

    for i, val in enumerate(lst):
        x = draw_info.start_x + i * draw_info.block_width
        y = draw_info.height - (val - draw_info.min_val) * draw_info.block_height

        color = draw_info.GRADIENTS[i % 3]

        pygame.draw.rect(draw_info.window, color, (x,y, draw_info.block_width, draw_info.height))

def generate_starting_list(n, min_val, max_value):
    lst = []

    for _ in range(n):
        val = random.randint(min_val, max_value)
        lst.append(val)
    return lst

def main():
    running = True
    clock = pygame.time.Clock()

    n = 50
    min_val = 0
    max_val = 100

    lst = generate_starting_list(n, min_val, max_val)
    draw_info = DrawInfo.DrawInfo(800, 600, lst)

    pygame.display.update

    while running:
        clock.tick(60)
        draw(draw_info)
        for event in pygame.event.get():    
            if event.type == pygame.QUIT:
                    running = False
    pygame.quit()

if  __name__ == '__main__':
    main()