import pygame

pygame.mixer.init()
pygame.mixer.music.load("v")
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    continue
