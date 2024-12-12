
import pygame
from pygame import mixer
from sys import exit
from Charactersbackup import Character

#initalize game
pygame.init()

mixer.init()# music for the game

#Window Formatting
window_size = (800, 600)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Fighting Game")

#game countdown
countdown = 3
countdown_update = pygame.time.get_ticks()

#set volume for music
pygame.mixer.music.load('Assets/03 Samurai Spirit.mp3')
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1, 0.0, 3000)

#game fonts for the score and countdown
countdown_font = pygame.font.Font("Assets/Karate.ttf", 80)
score_font =  pygame.font.Font("Assets/Karate.ttf", 30)

#score mechanics
character1_score = [0] #character's 1 score (ninja)
character2_score = [0] #character 2 score (bulky guy)
round_end = False
round_cooldown = 2000

#round start sound effect
yoo_sound = pygame.mixer.Sound('Assets/Yoooo.mp3')
yoo_sound.set_volume(0.1)
yoo_sound.play()

#characters sword sound effects
ninja_fx = pygame.mixer.Sound('Assets/Katana Swing Cut - Sound Effect for editing.mp3')
ninja_fx.set_volume(0.3)
bulky_guy_fx = pygame.mixer.Sound('Assets/Sword Stab Sound Effect (HD).mp3')
bulky_guy_fx.set_volume(0.2)

#when hit sound effect
being_hit = pygame.mixer.Sound('Assets/Minecraft Damage - Sound Effect.mp3')
being_hit.set_volume(0.3)

#jumping sound effect
jump = pygame.mixer.Sound('Assets/Jump Sound Effect (High Quality).mp3')
jump.set_volume(0.3)

# Background image
background1 = pygame.image.load("Assets/bamboo forest (2).jpg").convert_alpha()
# Characters
character1 = Character('Character 1', (90,100), (100, 800), False, ninja_fx, being_hit, jump)
character2 = Character('Character 2', (90, 100), (600, 800), True, bulky_guy_fx, being_hit, jump)

def display_assets():
    # Draw background and characters
    window.blit(background1, (2, 0))
    character1.update()
    character2.update()
    character1.draw(window)
    character2.draw(window)

def display_text(txt, font, color, x, y):
    img = font.render(txt, True, color)
    window.blit(img, (x, y))


def health_bar(health, x, y):
    health_percentage = health /1000
    pygame.draw.rect(window, (255, 255, 255), (x-15, y-10, 230, 60))
    pygame.draw.rect(window, (0, 0, 0), (x, y, 200, 40))
    pygame.draw.rect(window, (0, 255, 0), (x, y, 200 * health_percentage, 40))

def main_game():
    global countdown_update, countdown, countdown_font, score_font, yoo_sound, character2_score, character1_score, round_end, round_cooldown, character1, character2, round_time
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        window.fill((0, 0, 0))

        display_assets() #displays the background

        health_bar(character1.health, 30, 30)
        health_bar(character2.health, 570, 30)

        display_text(str(character1_score[0]), countdown_font, (255,0,0), 800/4.5, 600/7)
        display_text(str(character2_score[0]), countdown_font, (255,0,0), 575, 600/7 )

        keys = pygame.key.get_pressed()
        if countdown <= 0:
            # Character movements
            character1.move(keys, pygame.K_a, pygame.K_d, pygame.K_w, window, character2)
            character2.move(keys, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, window, character1)
        else:
            display_text(str(countdown), countdown_font, (255,0,0), 800 / 2, 600 / 3)

            if (pygame.time.get_ticks() - countdown_update) >= 1000:
                countdown -= 1
                countdown_update = pygame.time.get_ticks()

        if round_end == False:
            if character1.alive == False:
                character2_score[0] += 1
                round_end = True
                round_time = pygame.time.get_ticks()
                print(character2_score)
            elif character2.alive == False:
                character1_score[0] += 1
                round_end = True
                round_time = pygame.time.get_ticks()
        else:
            if pygame.time.get_ticks() - round_time > round_cooldown:
                round_end = False
                countdown = 3
                character1 = Character('Character 1', (90, 100), (100, 800), False, ninja_fx, being_hit, jump)
                character2 = Character('Character 2', (90, 100), (600, 800), True, bulky_guy_fx, being_hit, jump)

        pygame.display.flip()
        clock.tick(60)

#run game
main_game()
