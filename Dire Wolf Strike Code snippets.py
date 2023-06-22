# These are code snippets from the source code. 
# The snippets are not in order and are taken from random areas.
import pygame, sys, os, random, csv

pygame.init() # initialize's pygame 

# Screen size measurements
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720#int(SCREEN_WIDTH * 0.8)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE) # this is the game window itself its a pygame surface 
screen_rect = screen.get_rect() # gets the screen windows rect available for positioning purposes 
pygame.display.set_caption('Dire Wolf Strike') # title of the window 
# set fps
clock = pygame.time.Clock() # act as a timer, allow fps setting and be used as a time to base animations and intervals of different aspects 





# Figuring out how to make collsisions work

# MASK collision points on wolf forms
#FACING LEFT
head_coll_left =[(33, 26), (30, 32), (30, 33), (31, 33), (32, 33), (33, 33), (34, 33), (35, 33), (35, 32), (35, 31), (35, 30), (35, 29), (35, 28), (36, 27), (36, 26), (36, 25), (36, 24), (36, 23), (36, 22), (37, 21), (39, 20), (39, 19), (39, 18), (39, 17), (40, 16), (42, 15), (42, 14), (44, 13), (44, 12), (41, 16), (41, 17), (41, 18), (41, 19), (41, 20), (41, 21), (41, 22), (41, 23), (41, 24), (41, 25), (41, 26), (41, 27), (40, 27), (40, 28), (39, 29), (38, 30), (38, 31), (37, 31), (34, 31), (34, 32), (33, 32), (32, 32), (31, 32), (35, 22)]

tail_coll_left = [(99, 24), (99, 25), (99, 26), (99, 27), (99, 28), (99, 29), (99, 30), (99, 31), (99, 32), (99, 33), (99, 34), (99, 35), (99, 36), (99, 37), (99, 38), (99, 39), (99, 40), (99, 41), (99, 42), (99, 43), (99, 44), (99, 45), (99, 46), (99, 47), (99, 48), (99, 49), (99, 50), (103, 51), (103, 52), (103, 53), (103, 54), (103, 55), (103, 56), (103, 57), (101, 58), (101, 59), (101, 60)]

feet_coll_left = [(64, 60), (64, 59), (66, 58), (67, 57), (69, 55), (69, 54), (69, 53), (70, 53), (71, 53), (81, 59), (72, 52), (73, 52), (84, 51), (84, 52), (86, 53), (86, 54), (86, 55), (84, 56), (84, 57), (83, 58), (83, 59), (83, 60)]

torso_coll_left = [(50, 14), (50, 15), (47, 16), (48, 16), (49, 16), (50, 16), (51, 16), (52, 16), (53, 16), (54, 16), (55, 16), (56, 16), (57, 16), (58, 16), (59, 16), (60, 16), (61, 16), (62, 16), (63, 16), (64, 16), (65, 16), (66, 16), (67, 17), (68, 17), (69, 17), (70, 17), (71, 17), (72, 17), (73, 17), (74, 17), (75, 17), (76, 21), (77, 21), (78, 21), (79, 22), (80, 22), (81, 22)]

# FACING RIGHT 
head_coll_right = [(125, 33), (124, 33), (123, 33), (122, 33), (121, 33), (120, 33), (119, 33), (119, 32), (119, 31), (119, 30), (119, 29), (119, 28), (119, 27), (119, 26), (119, 25), (119, 24), (119, 23), (119, 22), (117, 21), (116, 17), (115, 16), (114, 16), (114, 17), (114, 18), (114, 19), (114, 20), (114, 21), (114, 22), (114, 23), (114, 24), (114, 25), (114, 26), (114, 27), (114, 28), (114, 29), (114, 30), (113, 30), (111, 30), (110, 30), (110, 29), (110, 28), (110, 27), (110, 26), (110, 25), (110, 24), (110, 23), (110, 22), (110, 21), (110, 20), (110, 19), (110, 17), (111, 16), (111, 15) , (110, 25), (110, 24), (110, 23), (110, 22), (110, 21), (110, 20), (110, 19), (110, 17), (111, 16), (111, 15), (111, 14), (111, 13), (111, 12), (112, 14), (113, 14), (115, 17), (116, 18), (118, 21), (118, 22), (118, 23), (118, 24), (118, 25), (118, 26), (118, 27), (118, 28), (118, 29), (117, 29), (116, 29), (115, 29), (113, 29), (112, 29), (111, 29), (109, 29), (109, 27), (109, 26), (109, 25), (109, 24), (109, 23), (109, 22), (109, 21), (109, 20), (109, 19), (109, 18), (109, 17), (112, 15), (113, 15), (115, 18), (116, 20), (116, 21), (116, 22), (116, 23), (116, 24), (116, 25), (116, 26), (116, 27), (116, 28), (116, 30), (115, 30), (112, 30), (109, 30)]

tail_coll_right = [(55, 24), (55, 25), (47, 26), (47, 27), (47, 28), (47, 29), (47, 30), (47, 31), (47, 32), (47, 33), (47, 34), (47, 35), (47, 36), (47, 37), (47, 38), (53, 39), (53, 40), (55, 41), (55, 42), (55, 43), (51, 44), (51, 45), (50, 46), (50, 47), (50, 48), (50, 49), (50, 50), (50, 51), (50, 52), (48, 53), (48, 54), (48, 55), (48, 56), (48, 57), (48, 59), (48, 60)]

feet_coll_right = [(84, 60), (84, 59), (84, 58), (74, 59), (73, 59), (72, 58), (71, 57), (70, 57), (69, 57), (68, 57), (67, 57), (66, 57), (65, 57), (67, 58), (68, 59), (68, 60), (84, 57), (84, 56), (84, 55), (73, 60)]

torso_coll_right = [(92, 14), (91, 14), (90, 14), (89, 14), (88, 14), (87, 14), (80, 17), (60, 22), (59, 22), (58, 22)]


# self.checkcollisionsx(world.obstacle_list)
# self.checkcollisionsy(world.obstacle_list)
# Check collision with ground tiles ***********************************************
collision_locations_list = []
# for tile in world.obstacle_list:
#     offset_x = tile[1].x - self.rect.x # sutracting 
#     offset_y = tile[1].y - (self.rect.y)
#     coll_area = self.mask.overlap(tile[2],(offset_x, offset_y))
#     collision_locations_list.append(coll_area)
#     if coll_area:
#         if self.direction == 1:
#             if coll_area in head_coll_right or tile[1].colliderect((self.rect.topright[0]) + self.dx, self.rect.y, self.width, self.height):
#                 self.dx = 0
#         elif self.direction == -1:
#             if coll_area in head_coll_left:
#                 self.dx = 0
#         if coll_area in feet_coll_left or feet_coll_right:
#             if self.vel_y >= 0:# check for falling
#                 self.vel_y = 0
#                 self.in_air = False # make sure we can jump as soon as we touch the ground
#                 self.dy = 0
#         elif coll_area in torso_coll_left or torso_coll_right:
#             if self.vel_y < 0:#check for jumping
#                 self.vel_y = 0
#                 self.dy = 0
#************************************************

for tile in world.obstacle_list:
    #check collision with ground tiles in x-axis
    if tile[1].colliderect(self.body_rect.x + self.dx, self.body_rect.y, self.width, self.height):
        self.dx = 0
    # collision in y-axis
    if tile[1].colliderect(self.body_rect.x, self.body_rect.y + self.dy, self.width, self.height):
        # check jumping
        if self.vel_y < 0:
            self.vel_y = 0
            self.dy = tile[1].bottom - self.body_rect.top
        # check for falling
        if self.vel_y > 0:
            self.vel_y = 0
            self.in_air = False
            self.dy = tile[1].top - self.body_rect.bottom
    

    #check collision with ground tiles in x-axis
    # if tile[1].colliderect((self.mask_rect.x) + self.dx, self.rect.y, self.width, self.height):
    #     self.dx = 0
    #     self.idling = True
    # collision in y-axis
    # if tile[3].colliderect(self.mask_rect.x, self.mask_rect.y + self.dy , self.width, self.height):
    #     if self.vel_y < 0:#check for jumping
    #         self.vel_y = 0
    #         self.dy = tile[3].bottom# - self.mask_rect.top

    #     elif self.vel_y >= 0:# check for falling
    #         self.vel_y = 0
    #         self.in_air = False # make sure we can jump as soon as we touch the ground
    #         self.dy = tile[3].top # - self.mask_rect.bottom

    # if self.rect.bottom + self.dy > 600: # we are calculating th gap between thr units feet and the line on 600
    #     self.dy = (600 - self.rect.bottom) # becomes the difference between the bottom of units feet and the floor 
    #     self.in_air = False

# update rect coord  This needs to be at the end so that we actually apply the additions/subrations to the x/y coord of the image rect
self.rect.x += self.dx 
self.rect.y += self.dy 
self.body_rect.centerx = self.rect.centerx
self.body_rect.centery = self.rect.centery
#update scroll based on player position
if self.char_type == 'player':
    if self.rect.right > SCREEN_WIDTH - scroll_threshold or self.body_rect.left < scroll_threshold: 
        screen_scroll = -self.dx
        self.rect.x -= self.dx
        # for enemy in enemy_group:
        #     enemy.idling = True

#***********************************************************************
# def get_hits(self, tiles):
#     hits = []
#     for tile in tiles:
#         if self.rect.colliderect(tile[1]):
#             hits.append(tile)
#     return hits

# def checkcollisionsx(self, tiles):
#     collisions = self.get_hits(tiles)
#     for tile in collisions:
#         if self.dx > 0: # hit tile moving right
#             self.dx = tile.rect.left - self.rect.w
#             self.rect.x += self.dx 
#         elif self.dx < 0:# hit tile moving left
#             self.dx = tile.rect.right
#             self.rect.x = self.dx 
# def checkcollisionsy(self, tiles):
#     self.in_air = True 
#     self.rect.bottom += 1
#     collisions = self.get_hits(tiles)
#     for tile in collisions:
#         if self.vel_y > 0:# hit tile from the top
#             self.in_air = False
#             self.jump = False 
#             self.vel_y = 0
#             self.dy = tile.rect.top
#             self.rect.bottom = self.dy
#         elif self.vel_y < 0:
#             self.vel_y = 0
#             self.dy = tile.rect.bottom + self.rect.h

# Part of the enemy AI 


def ai(self):
    '''logic for enabaling automated movement, chasing and shooting'''

    # health bar rectangle center needs constant updating to be able to move with unit. 
    self.bar_bg.center = (self.rect.centerx -25, self.rect.centery - 40)
    self.bar_health.center = (self.rect.centerx -25, self.rect.centery - 40)

    if self.alive and player.alive: # as long as they are alive they will be moving
        # Display health bar
        if enable_heath_bars:
            pygame.draw.rect(screen, RED, (self.bar_bg.centerx, self.bar_bg.centery, (self.image.get_width()- 90), 10))
            pygame.draw.rect(screen, GREEN, (self.bar_health.centerx, self.bar_health.centery, ((self.image.get_width() - 90) * (self.health/self.max_health)) , 10)) # ratio is health/max_health
        # handles the movement
        if self.idling == False and random.randint(1, 200) == 1: # check if ai is idling
            self.update_action(0) # idle
            self.idling = True  
            self.idling_counter = 100


 #KEYBOARD handler
    for event in pygame.event.get():
        # Quit game 
        if event.type == pygame.QUIT:
            sys.exit()
        # key press
        if event.type == pygame.KEYDOWN: # this can be refactored 
            if event.key == pygame.K_a:
                moving_left = True
            if event.key == pygame.K_d:
                moving_right = True 
            if ((event.key == pygame.K_w and player.alive) and player.triple_jump < 2): # this has a slight delay
                player.jump = True 
                # the following: enables a triple jump ability 
                player.triple_jump += 1
            if not player.in_air:
                player.triple_jump = 0
            if event.key == pygame.K_SPACE:
                shoot = True
                player.in_melee_range = True
            if event.key == pygame.K_LALT:
                grenade = True
            if event.key == pygame.K_CAPSLOCK:
                if enable_heath_bars != True:
                    enable_heath_bars = True
                elif enable_heath_bars != False:
                    enable_heath_bars = False
            if event.key == pygame.K_ESCAPE:
                sys.exit()
        # key release 
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                moving_left = False
            if event.key == pygame.K_d:
                moving_right = False
            if event.key == pygame.K_SPACE:
                shoot = False
                player.in_melee_range = False
            if event.key == pygame.K_LALT:
                grenade = False
                grenade_thrown = False

    pygame.display.update() # update the game window with all newer elements/updates taken into account.