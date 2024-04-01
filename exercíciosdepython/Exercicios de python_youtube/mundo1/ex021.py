import pygame
pygame.init()

pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()

# Loop para manter a janela aberta até que a música termine
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if not pygame.mixer.music.get_busy():
        # A música terminou de tocar
        running = False

pygame.quit()
