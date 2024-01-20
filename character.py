import pygame


class Character(pygame.sprite.Sprite):
    def __init__(self, char_type, x, y, scale, speed, ammo, rocket_ammo):
        pygame.sprite.Sprite.__init__(self)
        self.alive = True
        self.char_type = char_type
        self.speed = speed
        self.ammo = ammo
        self.start_ammo = ammo
        self.rocket_ammo = rocket_ammo
        self.max_rocket_ammo = rocket_ammo
        self.shoot_cooldown = 0
        self.entityhealth = 100
        self.maxentityhealth = self.entityhealth
        self.direction = 1
        self.flip = False
        self.animation_list = []
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()
        animation_types = ['idle', 'run', 'shoot', 'death']
        for animation in animation_types:
            temp_list = []
            num_of_frames = len(os.listdir(f'graphics/{self.char_type}/{animation}'))
            for i in range(num_of_frames):
                img = pygame.image.load(f'graphics/{self.char_type}/{animation}/{i}.png').convert_alpha()
                img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
                temp_list.append(img)
            self.animation_list.append(temp_list)
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect = self.rect.inflate(-20, 10)
        self.rect.center = (x, y)

    def update(self):
        self.update_animation()
        self.check_alive()
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1

    def movement(self, moving_up, moving_right, moving_down, moving_left):
        dx = 0
        dy = 0

        if moving_up:
            dy = -self.speed
        if moving_right:
            dx = self.speed
            self.flip = False
            self.direction = 1
        if moving_down:
            dy = self.speed
        if moving_left:
            dx = -self.speed
            self.flip = True
            self.direction = -1

        self.rect.x += dx
        self.rect.y += dy

    def movement2(self, moving_up2, moving_right2, moving_down2, moving_left2):
        dx = 0
        dy = 0

        if moving_up2:
            dy = -self.speed
        if moving_right2:
            dx = self.speed
            self.flip = False
            self.direction = 1
        if moving_down2:
            dy = self.speed
        if moving_left2:
            dx = -self.speed
            self.flip = True
            self.direction = -1

        self.rect.x += dx
        self.rect.y += dy

    def shoot(self):
        if self.shoot_cooldown == 0 and self.ammo > 0:
            self.shoot_cooldown = 20
            bullet = Projectile(self.rect.centerx + (0.8 * self.rect.size[0] * self.direction),
                                self.rect.centery + (0.2 * self.rect.size[0]), self.direction, 1)
            bullet_group.add(bullet)
            self.ammo -= 1

    def shoot2(self):
        if self.shoot_cooldown == 0 and self.ammo > 0:
            self.shoot_cooldown = 20
            bullet2 = Projectile(self.rect.centerx + (0.8 * self.rect.size[0] * self.direction),
                                 self.rect.centery + (0.2 * self.rect.size[0]), self.direction, 1)
            bullet_group2.add(bullet2)
            self.ammo -= 1

    def rocket(self):
        if self.shoot_cooldown == 0 and self.rocket_ammo > 0:
            self.shoot_cooldown = 20
            rocket = Rocket(self.rect.centerx + (0.8 * self.rect.size[0] * self.direction),
                            self.rect.centery + (0.2 * self.rect.size[0]), self.direction, 1)
            rocket_group.add(rocket)
            self.rocket_ammo -= 1

    def rocket2(self):
        if self.shoot_cooldown == 0 and self.rocket_ammo > 0:
            self.shoot_cooldown = 20
            rocket2 = Rocket(self.rect.centerx + (0.8 * self.rect.size[0] * self.direction),
                             self.rect.centery + (0.2 * self.rect.size[0]), self.direction, 1)
            rocket_group2.add(rocket2)
            self.rocket_ammo -= 1

    def update_animation(self):
        ANIMATION_SLEEP = 100
        self.image = self.animation_list[self.action][self.frame_index]
        if pygame.time.get_ticks() - self.update_time > ANIMATION_SLEEP:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        if self.frame_index >= len(self.animation_list[self.action]):
            if self.action == 3:
                self.frame_index = len(self.animation_list[self.action]) - 1
            else:
                self.frame_index = 0

    def update_action(self, new_action):
        if new_action != self.action:
            self.action = new_action
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

    def check_alive(self):
        if self.entityhealth <= 0:
            self.enitityhealth = 0
            self.speed = 0
            self.alive = 0
            self.update_action(3)

    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)