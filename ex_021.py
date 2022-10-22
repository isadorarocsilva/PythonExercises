#Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3. 
#OBS: o arquivo .mp3 deve estar junto a pasta do exercício.
import pygame

pygame.init()
pygame.mixer.music.load('spectrum.mp3')
pygame.mixer.music.play()
pygame.event.wait()

#Eu acrescentei uma parte porque descobri essa outra biblioteca, webbrowser, que usa URLs e eu achei interessante.
#Aqui eu tive que configurar o Microsoft Edge, se não abre o Chrome automaticamente (eu uso mais o Edge atualmente). 
#import webbrowser
#edge_path="C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
#webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))
#webbrowser.get('edge').open('https://www.youtube.com/watch?v=fIx6Xg0n9L4')
