import pygame

gameBG = pygame.image.load('graphics/bg_fill.png')
bullet_img = pygame.image.load('graphics/projectile/bullet.png')
rocket_img = pygame.image.load('graphics/projectile/rocket.png')
straightWall = pygame.image.load('graphics/environment/0.png')
health_pickup = pygame.image.load('graphics/health_pickup.png')
title_model = pygame.image.load('graphics/player1/idle/0.png')
title_model = pygame.transform.scale(title_model, (int(title_model.get_width() * 15), int(title_model.get_height() * 15)))
title_model = pygame.transform.flip(title_model, flip_x=True, flip_y=False)
title_model2 = pygame.image.load('graphics/player2/idle/0.png')
title_model2 = pygame.transform.scale(title_model2, (int(title_model2.get_width() * 15), int(title_model2.get_height() * 15)))
title_model2 = pygame.transform.flip(title_model2, flip_x=False, flip_y=False)
timer_BG = pygame.image.load('graphics/timer_BG.png')
help_screen_BG = pygame.image.load('graphics/help_screen_BG.png')

window_icon = pygame.image.load('graphics/window_icon.png')

