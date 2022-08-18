import pygame

pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('m01.mp3') #COLOCAR NOME DO ARQUIVO DA MÚSICA DENTRO DO PARÊNTESES
pygame.mixer.music.queue('m02.mp3') #ESSE COMANDO FAZ COM QUE TROQUE A MÚSICA E TOQUE A QUE ESTÁ DENTRO DO PARÊNTESE
pygame.mixer.music.play()
pygame.event.wait()
