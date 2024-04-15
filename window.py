import pygame
pygame.init()

#color
white = (255,255,255)
yellow = (255,255,0)
green = (0,255,0)
black = (0,0,0)

#window size
win_width = 1500
win_height = 800

win = pygame.display.set_mode((win_width,win_height), pygame.RESIZABLE) #1820,1080
win.fill(white)
pygame.display.set_caption("CHECK OUT PAPER")

#align size
align_x = 100
align_y = 100
align_step = 70

#font size
font_size = 40

font_name = pygame.font.SysFont("calibri",font_size)

text1 = font_name.render("Step 1: Collect the paper in tray 2", True, black)
text2 = font_name.render("Step 2: Fill and sign the paper", True, black)
text3 = font_name.render("Step 3: Put the paper to the mailbox 3", True, black)
text4 = font_name.render("Step 4: Confirm your booth information =>", True, black)

textRect1 = text1.get_rect()
textRect2 = text2.get_rect()
textRect3 = text3.get_rect()
textRect4 = text4.get_rect()

textRect1.midleft = (align_x, align_y)
textRect2.midleft = (align_x, align_y + align_step)
textRect3.midleft = (align_x, align_y + 2*align_step)
textRect4.midleft = (align_x, align_y + 3*align_step)

win.blit(text1, textRect1)
win.blit(text2, textRect2)
win.blit(text3, textRect3)
win.blit(text4, textRect4)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.VIDEORESIZE:
            win = pygame.display.set_mode(event.size, pygame.RESIZABLE)
        pygame.display.update()
