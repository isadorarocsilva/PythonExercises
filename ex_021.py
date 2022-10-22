#Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3. 
#Não entendi se o código funciona ou não...
import pygame

pygame.init()
pygame.mixer.music.load('spectrum.mp3')
pygame.mixer.music.play()
pygame.event.wait()

#Eu mudei esse exercício pq descobri essa outra biblioteca, webbrowser, que usa URLs. Muito mais legal.
#Aqui eu tive que configurar o edge pra n abrir o chrome automaticamente. 
#import webbrowser
#edge_path="C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
#webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))
#webbrowser.get('edge').open('https://www.youtube.com/watch?v=fIx6Xg0n9L4')
