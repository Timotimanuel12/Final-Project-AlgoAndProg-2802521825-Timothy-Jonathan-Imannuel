import pygame

class Character(pygame.sprite.Sprite):
    def __init__(self, char_type, size, position, flip, sound, ouch, jump_sound):
        super().__init__()  # Initialize sprite class
        self.char_type = char_type
        self.animation_list = []
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        self.actions = 0

        # Animation lists/initializing
        temp_list = []
        for i in range(4):  # idle animation (0)
            img = pygame.image.load(f'Assets/{char_type}/idle/{i}.png').convert_alpha()
            img = pygame.transform.scale(img, size)  # Scale the image
            temp_list.append(img)
        self.animation_list.append(temp_list)
        temp_list = []
        for i in range(8):  # running animation (1)
            img = pygame.image.load(f'Assets/{char_type}/run/{i}.png').convert_alpha()
            img = pygame.transform.scale(img, size)  # Scale the image
            temp_list.append(img)
        self.animation_list.append(temp_list)
        temp_list = []
        for i in range(2):  # jumping animation (2)
            img = pygame.image.load(f'Assets/{char_type}/jump/{i}.png').convert_alpha()
            img = pygame.transform.scale(img, size)  # Scale the image
            temp_list.append(img)
        self.animation_list.append(temp_list)
        temp_list = []
        for i in range(2):  # falling animation (3)
            img = pygame.image.load(f'Assets/{char_type}/drop/{i}.png').convert_alpha()
            img = pygame.transform.scale(img, size)  # Scale the image
            temp_list.append(img)
        self.animation_list.append(temp_list)
        temp_list = []
        for i in range(4):  # attack1 animation (4)
            img = pygame.image.load(f'Assets/{char_type}/attack1/{i}.png').convert_alpha()
            img = pygame.transform.scale(img, size)  # Scale the image
            temp_list.append(img)
        self.animation_list.append(temp_list)
        temp_list = []
        for i in range(4):  # attack2 animation (5)
            img = pygame.image.load(f'Assets/{char_type}/attack2/{i}.png').convert_alpha()
            img = pygame.transform.scale(img, size)  # Scale the image
            temp_list.append(img)
        self.animation_list.append(temp_list)
        temp_list = []
        for i in range(3):  # gets hit animation (6)
            img = pygame.image.load(f'Assets/{char_type}/takehit/{i}.png').convert_alpha()
            img = pygame.transform.scale(img, size)  # Scale the image
            temp_list.append(img)
        self.animation_list.append(temp_list)
        temp_list = []
        for i in range(7):  # death animation (7)
            img = pygame.image.load(f'Assets/{char_type}/death/{i}.png').convert_alpha()
            img = pygame.transform.scale(img, size)  # Scale the image
            temp_list.append(img)
        self.animation_list.append(temp_list)

        self.image = self.animation_list[self.actions][self.frame_index]
        self.rect = self.image.get_rect(topleft=position)

        # Character attributes
        self.jump_state = False
        self.jump_velocity = 0
        self.gravity = 1.75
        self.attack_state = False
        self.health = 1000
        self.flip = flip
        self.sound_fx = sound
        self.hit_sound = ouch
        self.jumping = jump_sound
        self.cooldown_duration = 1000  # Cooldown duration in milliseconds
        self.last_attack_time = 0  # Timestamp of the last attack
        self.attack_type = 0
        self.hit = False
        self.alive = True

    def update(self):
        cooldown = 40
        self.image = self.animation_list[self.actions][self.frame_index]
        if pygame.time.get_ticks() - self.update_time > cooldown:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        if self.frame_index >= len(self.animation_list[self.actions]):
            if self.alive == False:
                self.frame_index = len(self.animation_list[self.actions]) - 1
            else:
                self.frame_index = 0
                if self.actions in [4, 5]:
                    self.attack_state = False
                if self.actions == 6:
                    self.hit = False

    def diff_action(self, new_action):
        if new_action != self.actions:  # Ensure current action is new
            self.actions = new_action
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

    # Updated move method
    def move(self, keys, left, right, up, surface, target, speed=5):
        # Screen boundaries
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x + self.rect.width > surface.get_width():
            self.rect.x = surface.get_width() - self.rect.width

        # If the character is attacking or hit, prioritize those actions
        if self.attack_state == True and self.alive == True:
            if self.attack_type == 1:
                self.diff_action(4)  # Attack 1 animation
            elif self.attack_type == 2:
                self.diff_action(5)  # Attack 2 animation
        elif self.health == 0:
            self.alive = False
            self.health = 0
            self.diff_action(7)
        elif self.hit:
            self.diff_action(6)  # Getting hit animation
        elif keys[up]:
            self.diff_action(2)  # Jumping animation
        elif keys[right] or keys[left]:
            self.diff_action(1)  # Running animation
        else:
            self.diff_action(0)  # Idle animation

        # Only move if not attacking or hit
        if not self.attack_state or not self.jump_state:
            if self.char_type == 'Character 1' and self.alive == True:  # Character 1 controls
                if keys[left]:
                    self.flip = True
                    self.rect.x -= 1 * speed
                elif keys[right]:
                    self.flip = False
                    self.rect.x += speed

                if keys[up] and not self.jump_state:
                    self.jump_velocity = -25  # Jump height
                    self.jump_state = True
                    self.jumping.play()

                current_time = pygame.time.get_ticks()
                # Check for attack buttons and ensure cooldown
                if (keys[pygame.K_t] or keys[pygame.K_g]) and current_time - self.last_attack_time >= self.cooldown_duration:
                    self.attack(0.5, target, surface)
                    self.last_attack_time = current_time
                    if keys[pygame.K_g]:
                        self.attack_type = 1
                    if keys[pygame.K_t]:
                        self.attack_type = 2

            elif self.char_type == 'Character 2' and self.alive == True:# Character 2 controls
                if keys[left]:
                    self.flip = True
                    self.rect.x -= speed
                elif keys[right]:
                    self.flip = False
                    self.rect.x += speed

                if keys[up] and not self.jump_state:
                    self.jump_velocity = -25  # Jump height
                    self.jump_state = True
                    self.jumping.play()

                current_time = pygame.time.get_ticks()
                # Check for attack buttons and ensure cooldown
                if (keys[pygame.K_l] or keys[pygame.K_p]) and current_time - self.last_attack_time >= self.cooldown_duration:
                    self.attack(0.5, target, surface)
                    self.last_attack_time = current_time
                    if keys[pygame.K_l]:
                        self.attack_type = 1
                    if keys[pygame.K_p]:
                        self.attack_type = 2

        # Gravity effect if jumping
        if self.jump_state:
            self.rect.y += self.jump_velocity
            self.jump_velocity += self.gravity

        # Land back
        if self.rect.y + self.rect.height >= surface.get_height() - 100:
            self.rect.y = surface.get_height() - self.rect.height - 100
            self.jump_state = False
            self.jump_velocity = 0

    def attack(self, width_multiplier, target, surface):
        self.attack_state = True
        self.sound_fx.play()
        if not self.flip:  # Character facing right
            attack_area = pygame.Rect(self.rect.centerx,self.rect.y, width_multiplier * self.rect.width,self.rect.height)
        else:  # Character facing left
            attack_area = pygame.Rect(self.rect.centerx - width_multiplier * self.rect.width, self.rect.y, width_multiplier * self.rect.width, self.rect.height)

        if attack_area.colliderect(target.rect):
            self.hit_sound.play()
            if target.rect.centerx > self.rect.centerx:
                target.rect.x += 50
                target.health -= 50
                target.hit = True
            if self.rect.centerx > target.rect.centerx:
                target.rect.x -= 50
                target.health -= 50
                target.hit = True
            if target.health == 0:
                target.alive = False
                print("VICTORY!!")

    def draw(self, surface):
        # Draw the character image
        if self.flip:
            flipped_image = pygame.transform.flip(self.image, True, False)
            surface.blit(flipped_image, self.rect)
        else:
            surface.blit(self.image, self.rect)


