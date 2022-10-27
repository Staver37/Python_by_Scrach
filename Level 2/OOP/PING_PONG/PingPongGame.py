import random
import pygame
import sys

# Initialize the PyGame engine
pygame.init()

# Create size tuple and set it to PyGame display
size = width, height = (800, 480)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("PONG")

# Set game frame limit
fps = 30
fps_clock = pygame.time.Clock()

# Write game name to the window
font = pygame.font.SysFont('FreeSans.ttf', 48)
text = font.render('PONG', True, 'white')
text_box = text.get_rect()
text_box.center = (width/2, 20)

# Create some color variabless
color_white = (255, 255, 255)
color_black = (0, 0, 0)

# Create a ball object
ball = pygame.image.load("Assets\\ball.png")
ball_box = ball.get_rect()
ball_speed = [5, 5]

# Create player1 paddle
player1 = pygame.image.load("Assets\\paddle.png")
player1_x = 0
player1_y = height / 2
player1_up = False
player1_down = False
player1_box = player1.get_rect(topleft=(player1_x, player1_y))  # Code for creating a collision box for the player

# Create player2 paddle
player2 = pygame.image.load("Assets\\paddle.png")
player2_x = width - 32
player2_y = height / 2
player2_up = False
player2_down = False
player2_box = player2.get_rect(topleft=(player2_x, player2_y))

# Player speed, collision and score variables
players_speed = 5
collide1 = False
collide2 = False
player1_score = 0
player2_score = 0

play = False

# Create game loop
while True:
    player1_box = player1.get_rect(topleft=(player1_x, player1_y))  # Update collision box code in game loop
    player2_box = player2.get_rect(topleft=(player2_x, player2_y))
    # Write player scores to the screen
    font1 = pygame.font.SysFont('Copperplate Gothic.ttf', 48)
    score1 = font1.render(str(player1_score), True, 'white')
    text1_x = 20
    text1_y = 10
    text1_pos = (text1_x, text1_y)

    score2 = font1.render(str(player2_score), True, 'white')
    text2_x = width - 40
    text2_y = 10
    text2_pos = (text2_x, text2_y)
    # Loop for events in loop
    for event in pygame.event.get():
        # Exit game if 'X' is clicked
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Look for key presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player1_up = True
            if event.key == pygame.K_s:
                player1_down = True
            if event.key == pygame.K_UP:
                player2_up = True
            if event.key == pygame.K_DOWN:
                player2_down = True
            if event.key == pygame.K_SPACE:
                play = True
        # Look for key releases
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player1_up = False
            if event.key == pygame.K_s:
                player1_down = False
            if event.key == pygame.K_UP:
                player2_up = False
            if event.key == pygame.K_DOWN:
                player2_down = False

    # If player1 presses keys, move player1
    if player1_up:
        if player1_y > 0:
            player1_y = player1_y - players_speed
    if player1_down:
        if player1_y < height - 96:
            player1_y = player1_y + players_speed

    # If player2 presses keys, move player2
    if player2_up:
        if player2_y > 0:
            player2_y = player2_y - players_speed
    if player2_down:
        if player2_y < height - 96:
            player2_y = player2_y + players_speed

    # If space is pressed start ball, else center ball
    if not play:
        ball_box.center = (width/2, height/2)
        choice = [[5, 5], [-5, -5], [5, -5], [-5, 5]]
        ball_speed = random.choice(choice)
    if play:
        # Make ball collide with and bounce off walls and player paddles
        ball_box = ball_box.move(ball_speed)
        if ball_box.left < 0 or ball_box.right > width:
            ball_speed[0] = -ball_speed[0]
            if ball_box.left < 0:
                player2_score = player2_score + 1
                play = False
            elif ball_box.right > width:
                player1_score = player1_score + 1
                play = False
        if ball_box.top < 0 or ball_box.bottom > height:
            ball_speed[1] = -ball_speed[1]
        if ball_box.colliderect(player1_box):
            collide1 = True
            ball_speed[0] = ball_speed[0] - 1
            ball_speed[1] = random.choice([ball_speed[1]+1, ball_speed[1]-1])
        else:
            collide1 = False
        if ball_box.colliderect(player2_box):
            collide2 = True
            ball_speed[0] = ball_speed[0] + 1
            random.choice([ball_speed[1]+1, ball_speed[1]-1])
        else:
            collide2 = False
        if collide1:
            ball_speed[0] = -ball_speed[0]
        if collide2:
            ball_speed[0] = -ball_speed[0]

    # Add background color and title and player scores
    screen.fill(color_black)
    pygame.draw.line(screen, color_white, (width / 2, 0), (width / 2, height), width=2)
    screen.blit(text, text_box)
    screen.blit(score1, text1_pos)
    screen.blit(score2, text2_pos)

    # Draw paddles and ball to screen
    screen.blit(player1, player1_box)   # Apply collision box to blit function box and player move in sync
    screen.blit(player2, player2_box)
    screen.blit(ball, ball_box)

    # Update screen at desired frame-rate
    pygame.display.flip()
    fps_clock.tick(fps)
