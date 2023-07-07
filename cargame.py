import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Car Game")

# Set up the colors
black = (0, 0, 0)
white = (255, 255, 255)

# Set up the car
car_width = 73
car_height = 82
car_img = pygame.image.load("car.png")  # Replace "car.png" with your car image file
car_img = pygame.transform.scale(car_img, (50,100))

blast_img = pygame.image.load("blast.png") 
blast_img = pygame.transform.scale(blast_img, (100,100))

def car(x, y):
    screen.blit(car_img, (x, y))

# Set up the obstacles
obstacle_width = 100
obstacle_height = 100
obstacle_img = pygame.image.load("obstacle.png")  # Replace "obstacle.png" with your obstacle image file
obstacle_img = pygame.transform.scale(obstacle_img, (50,50))

obstacle_img2 = pygame.image.load("obstacle.png")  # Replace "obstacle.png" with your obstacle image file
obstacle_img2 = pygame.transform.scale(obstacle_img2, (50,50))

def obstacles(obstacle_x, obstacle_y):
    screen.blit(obstacle_img, (obstacle_x, obstacle_y))

clock = pygame.time.Clock()

def display():
    welcome = True
    while welcome:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game()

        pygame.display.update()
        font = pygame.font.SysFont(None, 40)
        text1 = font.render("game over", True, (255,0,0))
        screen.blit(text1, (150,150))
        text2 = font.render("Press enter to restart", True, (255,255,255))
        screen.blit(text2, (150,250))



def game():
    car_x = screen_width // 2 - car_width // 2
    car_y = screen_height - car_height - 10
    car_speed = 0

    obstacle_x = random.randint(0, screen_width - obstacle_width)
    obstacle_y = -obstacle_height

    obstacle_x2 = random.randint(0, screen_width - obstacle_width)
    obstacle_y2 = -obstacle_height

    obstacle_speed = 5

    game_over = False
    score = 0
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    car_speed = -5
                elif event.key == pygame.K_RIGHT:
                    car_speed = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    car_speed = 0

        car_x += car_speed

        screen.fill(black)
        car(car_x, car_y)
        obstacles(obstacle_x, obstacle_y)
        obstacles(obstacle_x2, obstacle_y2)
        obstacle_y += obstacle_speed
        obstacle_y2 += obstacle_speed

        if car_x < 0 or car_x + car_width > screen_width:
            game_over = True

        if obstacle_y > screen_height:
            obstacle_y = -obstacle_height
            obstacle_x = random.randint(0, screen_width - obstacle_width)
            score+=1

        if obstacle_y2 > screen_height:
            obstacle_y2 = -obstacle_height - 100
            obstacle_x2 = random.randint(0, screen_width - obstacle_width)
            score+=1

        if car_x+50 > obstacle_x and car_x < obstacle_x + 50 and car_y > obstacle_y and car_y < obstacle_y + 50:
            screen.blit(blast_img,(car_x,car_y))
            display()

        if car_x +50 > obstacle_x2 and car_x < obstacle_x2 + 50 and car_y > obstacle_y2 and car_y < obstacle_y2 + 50:
            screen.blit(blast_img,(car_x,car_y))
            display()

        font = pygame.font.SysFont(None, 40)
        score_label = font.render("Score = "+str(score), True, (255,255,255))
        screen.blit(score_label, (5,15))

        pygame.display.update()
        clock.tick(60)

game()
