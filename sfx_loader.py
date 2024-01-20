import pygame
from pygame import  mixer

mixer.init()

shoot_sfx = pygame.mixer.Sound('sfx/shoot_sfx.wav')
health_pickup_sfx = pygame.mixer.Sound('sfx/health_pickup_sfx.wav')
rocket_pickup_sfx = pygame.mixer.Sound('sfx/rocket_pickup_sfx.wav')
death_sfx = pygame.mixer.Sound('sfx/death_sfx.wav')
hurt_sfx = pygame.mixer.Sound('sfx/hurt_sfx.wav')

