# Computer Programming 1
# Unit 11 - Graphics
#
# A scene that uses loops to make stars and make a picket fence.


# Imports
import pygame
import random

# Initialize game engine
pygame.init()

#Images
spaghet = pygame.image.load('cloud.png')
noodle = pygame.image.load('cat.png')
sauce = pygame.image.load('sky.png')
noodles = pygame.image.load('ground.png')
meatball = pygame.image.load('planet.png')

# Window
SIZE = (800, 600)
TITLE = "Cats and DOgs"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 30

# Colors
GREEN = (0, 175, 0)
WHITE = (255, 255, 255)
BLUE = (75, 200, 255)
YELLOW = (255, 255, 175)

# Make clouds
num_clouds = 20
clouds = []
for i in range(num_clouds):
    x = random.randrange(-800, 800)
    y = random.randrange(-50, 200)
    loc = [x, y]
    clouds.append(loc)

def draw_cloud(loc):
    x = loc[0]
    y = loc[1]
    screen.blit(spaghet, (x, y))

# Make rain
num_rain = 20
rain = []
for i in range(num_rain):
    x = random.randrange(0, 1000)
    y = random.randrange(-600, 0)
    loc = [x, y]
    rain.append(loc)

def draw_rain(loc):
    x = loc[0]
    y = loc[1]
    screen.blit(noodle, (x,y))

   
# Game loop
done = False

while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True     

    # Game logic
    for c in clouds:
        c[0] += 2

        if c[0] > 900:
           c[0] = random.randrange(-800, -100)
           c[1] = random.randrange(-50, 200)

    for r in rain:
        r[0] -= 2
        r[1] += 9

        if r[1] > 400 or r[0] < -50:
            r[1] = random.randrange(-600, 0)
            r[0] = random.randrange(-10, 900)
             
    # Drawing code
    ''' sky '''
    screen.blit(sauce, (0, 0))

    ''' sun '''
    screen.blit(meatball, (575, 25))

    ''' clouds '''
    for c in clouds:
        draw_cloud(c)

    ''' grass '''
    screen.blit(noodles, (0, 400))


    ''' fence '''
    y = 380
    for x in range(5, 800, 30):
        pygame.draw.polygon(screen, WHITE, [[x+5, y], [x+10, y+5],
                                            [x+10, y+40], [x, y+40],
                                            [x, y+5]])
    pygame.draw.line(screen, WHITE, [0, 390], [800, 390], 5)
    pygame.draw.line(screen, WHITE, [0, 410], [800, 410], 5)

    ''' rain '''
    for r in rain:
        draw_rain(r)


    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)

# Close window on quit
pygame.quit()
