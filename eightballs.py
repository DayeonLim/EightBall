import pygame
import random
from pygame import *
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("683835__seth_makes_sounds__video-game-music.wav")
pygame.mixer.music.play(-1, 0.0)
window = pygame.display.set_mode([500, 700])
window.fill((5, 54, 2))
loc1 = [600, 600, 600, 600]
balls1 = [[], [], [], []]
ball1 = pygame.transform.scale(pygame.image.load("1.png"), (90, 90))
window.blit(ball1, (200,25))
beep = pygame.mixer.Sound("571502__kagateni__cute1.mp3")
drop = pygame.mixer.Sound("ball_dropping.wav")
fail = pygame.mixer.Sound("457753__tissman__fail10.wav")
r1 = 1
pygame.draw.ellipse(window, (255, 255, 255), [45, 650, 100, 50], 2)
pygame.draw.ellipse(window, (255, 255, 255), [150, 650, 100, 50], 2)
pygame.draw.ellipse(window, (255, 255, 255), [255, 650, 100, 50], 2)
pygame.draw.ellipse(window, (255, 255, 255), [360, 650, 100, 50], 2)
pygame.draw.line(window, (255, 255, 255), [45, 200], [45, 675])
pygame.draw.line(window, (255, 255, 255), [145, 200], [145, 675])
pygame.draw.line(window, (255, 255, 255), [150, 200], [150, 675])
pygame.draw.line(window, (255, 255, 255), [250, 200], [250, 675])
pygame.draw.line(window, (255, 255, 255), [255, 200], [255, 675])
pygame.draw.line(window, (255, 255, 255), [355, 200], [355, 675])
pygame.draw.line(window, (255, 255, 255), [360, 200], [360, 675])
pygame.draw.line(window, (255, 255, 255), [460, 200], [460, 675])

pygame.font.init()
my_font = pygame.font.SysFont('Silom', 30)
window.blit(my_font.render('1', False, (255,255,255)), (85,655))
window.blit(my_font.render('2', False, (255,255,255)), (190,655))
window.blit(my_font.render('3', False, (255,255,255)), (295,655))
window.blit(my_font.render('4', False, (255,255,255)), (400,655))
pygame.display.flip()

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    start1 = ["1.png", "2.png", "3.png", "4.png"]
    options1 = ["1.png", "2.png", "3.png", "4.png", "5.png", "6.png", "7.png", "8.png"]
    keys = pygame.key.get_pressed()
    for i in range(4):
        if keys[K_1 + i]:
            pygame.draw.rect(window, (5, 54, 2), pygame.Rect(0, 0, 505, 125))
            pygame.display.flip()
            for j in range(50, loc1[i], 5):
                pygame.time.delay(15)
                pygame.draw.circle(window, (5, 54, 2), (95 + i * 105, j + 40), 49, 45)
                window.blit(ball1, (50 + i * 105, j))
                pygame.display.flip()
            pygame.mixer.Sound.play(beep)
            balls1[i].append(r1)

            while len(balls1[i]) >= 2 and balls1[i][-1] == balls1[i][-2]:
                pygame.time.delay(100)
                balls1[i][-2] += 1
                balls1[i].pop()
                replace = pygame.transform.scale(pygame.image.load(options1[r1]), (90, 90))
                r1 += 1
                pygame.draw.circle(window, (5, 54, 2), (95 + i * 105, loc1[i] + 40), 49)
                window.blit(replace, (50 + i * 105, loc1[i] + 80))
                pygame.display.flip()
                loc1[i] += 85
                pygame.mixer.Sound.play(beep)
                if balls1[i][-1] == 8:
                    pygame.draw.rect(window, (5, 54, 2), pygame.Rect(0, 0, 1010, 700))
                    eight = pygame.transform.scale(pygame.image.load(options1[-1]), (130, 130))
                    window.blit(eight, (250, 300))
                    window.blit(my_font.render('You Win!', False, (255,255,255)), (150,300))
                    pygame.display.flip()
                    pygame.time.delay(5000)
                    break
            if balls1[i][-1] == 8:
                running = False
                break
            loc1[i] -= 85
            if len(balls1[i]) > 5:
                pygame.mixer.Sound.play(fail)
                pygame.draw.rect(window, (5, 54, 2), pygame.Rect(0, 0, 505, 700))
                pygame.draw.line(window, (255, 255, 255), [505, 0], [505, 1000])
                pygame.draw.ellipse(window, (255, 255, 255), [45, 650, 100, 50], 2)
                pygame.draw.ellipse(window, (255, 255, 255), [150, 650, 100, 50], 2)
                pygame.draw.ellipse(window, (255, 255, 255), [255, 650, 100, 50], 2)
                pygame.draw.ellipse(window, (255, 255, 255), [360, 650, 100, 50], 2)
                pygame.draw.line(window, (255, 255, 255), [45, 200], [45, 675])
                pygame.draw.line(window, (255, 255, 255), [145, 200], [145, 675])
                pygame.draw.line(window, (255, 255, 255), [150, 200], [150, 675])
                pygame.draw.line(window, (255, 255, 255), [250, 200], [250, 675])
                pygame.draw.line(window, (255, 255, 255), [255, 200], [255, 675])
                pygame.draw.line(window, (255, 255, 255), [355, 200], [355, 675])
                pygame.draw.line(window, (255, 255, 255), [360, 200], [360, 675])
                pygame.draw.line(window, (255, 255, 255), [460, 200], [460, 675])
                window.blit(my_font.render('1', False, (255,255,255)), (85,655))
                window.blit(my_font.render('2', False, (255,255,255)), (190,655))
                window.blit(my_font.render('3', False, (255,255,255)), (295,655))
                window.blit(my_font.render('4', False, (255,255,255)), (400,655))
                pygame.display.flip()
                balls1 = [[], [], [], []]
                loc1 = [600, 600, 600, 600]

            r1 = random.choice([1, 2, 3, 4])
            ball1 = pygame.transform.scale(pygame.image.load(start1[r1 - 1]), (90, 90))
            window.blit(ball1, (200,25))
            pygame.display.flip()
            pygame.time.delay(200)