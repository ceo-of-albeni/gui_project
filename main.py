import mymodule
import button
import pygame, sys

pygame.init()

background_colour = (192, 190, 192)
black = (0, 0, 0)

font = pygame.font.Font('font.ttf', 9)

img = pygame.image.load('interface/alatoo.png')
image = pygame.transform.scale(img, [200, 200])

start_img = pygame.image.load('interface/start_btn.png').convert_alpha()
exit_img = pygame.image.load('interface/exit_btn.png').convert_alpha()
options_img1 = pygame.image.load('interface/options.png').convert_alpha()
options_img = pygame.transform.scale(options_img1, (50, 50))
return_img1 = pygame.image.load('interface/return.png').convert_alpha()
return_img = pygame.transform.scale(return_img1, (150, 150))

start_button = button.Button(150, 270, start_img, 0.2)
exit_button = button.Button(150, 360, exit_img, 0.2)
options_button = button.Button(340, 40, options_img, 0.8)

pygame.display.set_caption('GUI')
screen = pygame.display.set_mode((400, 500))

def inter():
    running = True
    while True:
        screen.fill(background_colour)
        screen.blit(image, (95, 35))
        pygame.display.set_caption('GUI')
        if start_button.draw(screen):
            mymodule.inst1
        if options_button.draw(screen):
            about()
        if exit_button.draw(screen):
            running = False
            pygame.quit()
            break
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit

        pygame.display.update()
        pygame.display.flip()

def textt(text, x, y):
    x = x
    y = y
    mes = font.render(text, True, black)
    textRect = mes.get_rect()
    textRect.center = (x // 2, y // 2)
    screen.blit(mes, textRect)
    pygame.display.update()


def about():
    screen.fill(background_colour)
    while True:
        pygame.display.set_caption('About')
        return_button = button.Button(30, 250, return_img, 0.2)
        textt('About GUI', 390, 200)
        textt('~ applies b/w filter and crops to', 310, 250)
        textt('1080*1080 size all images in img folder.', 394, 280)
        textt('~ adds to all images a watermark', 300, 400)
        textt('at right bottom corner.', 250, 430)

        if return_button.draw(screen):
            inter()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        pygame.display.update()
        pygame.display.flip()
    
# loop
running = True
while running:
    screen.fill(background_colour)
    screen.blit(image, (95, 35))

    if start_button.draw(screen):
        mymodule.Openfolder()
    if options_button.draw(screen):
        about()
    if exit_button.draw(screen):
        running = False
        break

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
    pygame.display.flip()

pygame.quit()
