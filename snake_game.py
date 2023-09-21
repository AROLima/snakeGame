import pygame
import time
import random

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('assets/PinkFox_-_Farewell_Memories__Full_Version_.mp3')
pygame.mixer.music.set_volume(0.3)

black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

dis_width = 600
dis_height = 400
dis = pygame.display.set_mode((dis_width, dis_height))

clock = pygame.time.Clock()
snake_block = 10
snake_speed = 25

font_style = pygame.font.SysFont(None, 35)
score_font = pygame.font.SysFont(None, 35)


def message(msg, color, x, y):
    mesg = font_style.render(msg, True, color)
    mesg_rect = mesg.get_rect(center=(x/2, y/2))
    dis.blit(mesg, mesg_rect.center)


def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    pygame.mixer.music.play(-1)

    while not game_over:

        while game_close == True:
            dis.fill(black)
            message("You Lost! Press C to continue or Q to quit", red, dis_width / 6, dis_height / 3)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
                    gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            ####### Snake moving #######
                    ##x-axis moving (left and right)##
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = snake_block
                    y1_change = 0

                    ##y-axis moving (up and down)##
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = snake_block
                    x1_change = 0
        
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        ###Set new snake position##
        x1 += x1_change
        y1 += y1_change

        ### setting background color###
        dis.fill(blue)

        

            ##drawing snake , and snake head collide##
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        for x in snake_List:
            pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
