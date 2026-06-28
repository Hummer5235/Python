import pygame
pygame.mouse.set_visible(False)
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
 
    sc.fill(WHITE)
 
    pos = pygame.mouse.get_pos()
    if pygame.mouse.get_focused():
        pygame.draw.circle(sc, BLUE, pos, 7)
 
    pressed = pygame.mouse.get_pressed()
    if pressed[0]:
        if sp is None:
            sp = pos
 
        width = pos[0] - sp[0]
        height = pos[1] - sp[1]
        pygame.draw.rect(sc, RED, pygame.Rect(sp[0], sp[1], width, height))
    else:
        sp = None
 
    pygame.display.update()
 
    clock.tick(FPS)