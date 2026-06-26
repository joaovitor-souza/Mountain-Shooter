import pygame

print('Stup Start')
pygame.init()
window = pygame.display.set_mode(size=(600,400))
print('Stup End')

print('Loop Start')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Close Window
            print("Quitting...")
            quit() # end pygame
