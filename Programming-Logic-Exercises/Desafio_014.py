#Abrir e reproduzir um áudio em MP3

import pygame

pygame.init()
pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play()
input('Pressione ENTER para sair')



