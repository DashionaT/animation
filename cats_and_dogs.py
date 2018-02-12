# Computer Programming 1
# Unit 11 - Graphics
#
# A scene that uses loops to make stars and make a picket fence.


# Imports
import pygame
import random

# Initialize game engine
pygame.mixer.pre_init()
pygame.init()

#Images
cloud = pygame.image.load('cloud.png')
cat = pygame.image.load('cat.png')
sky = pygame.image.load('sky.jpeg')
noodles = pygame.image.load('ground.jpeg')
meatball = pygame.image.load('planet.png')
dolphin = pygame.image.load('dolphin.png')

# Window
SIZE = (800, 600)
TITLE = "It's Raining Cats"
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
GRAY = (75, 75, 75)

# Make clouds
stormy = True

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
    screen.blit(cloud, (x, y))

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
    screen.blit(cat, (x,y))

# Dolphin
num_dolphin = 8
stand = []
for i in range(num_dolphin):
    x = random.randrange(0, 800)
    y = random.randrange(400, 500)
    v = random.randrange(1, 2)
    place = [x, y, v]
    stand.append(place)

def animal(place):
    x = place[0]
    y = place[1]

    screen.blit(dolphin, (x,y))

lightning_timer = 0

# Sound Effects
pygame.mixer.music.load("thunder_rain.ogg")

# Game loop
pygame.mixer.music.play(-1)

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

    for s in stand:
        s[0] -= s[2]

        if s[0] > 900:
            s[0] = random.randrange(900, 50)
            s[1] = random.randrange(400, 500)


    ''' flash lighting '''
    if stormy:
        if random.randrange(0, 150) == 0:
            lightning_timer = 5
        else:
            lightning_timer -= 1
            
    # Drawing code
    ''' sky '''
    if lightning_timer > 0:
        screen.fill(YELLOW)
    else:
        screen.fill(GRAY)
        
    ''' sun '''
    screen.blit(meatball, (550, -10))

    ''' water '''
    screen.blit(noodles, (0, 400))

    ''' rain '''
    for r in rain:
        draw_rain(r)
        
    ''' dolphins '''
    for s in stand:
        animal(s)
        
    ''' clouds '''
    for c in clouds:
        draw_cloud(c)


    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)

# Close window on quit
pygame.quit()
