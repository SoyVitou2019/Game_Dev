import pygame
import os

# Initialize Pygame
pygame.init()

# Set screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Character Movement with Animation")

# Define colors
WHITE = (255, 255, 255)

# Load player sprites
player_path = "./player/"
idle_sprites = [pygame.image.load(os.path.join(player_path, f"idle/idle_{i}.png")) for i in range(1, 9)]
walk_sprites = [pygame.image.load(os.path.join(player_path, f"walking/walk_{i}.png")) for i in range(1, 9)]
jump_sprites = [pygame.image.load(os.path.join(player_path, f"jump/jump_{i}.png")) for i in range(1, 9)]

# Flip walk sprites for left movement
flipped_walk_sprites = [pygame.transform.flip(sprite, True, False) for sprite in walk_sprites]

# Set initial player position
player_x, player_y = 300, 340
player_speed = 5

# Set animation parameters
player_walk_speed = 4
ground_level = 400


# Set player state variables
is_idle = True
is_walking = False
is_running = False
is_jumping = False
is_facing_left = False  # New variable to track player's facing direction
i = 0
j = 0
# Main game loop
running = True
while running:
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

   # Player movement
    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and not is_jumping:  # Check if not already jumping
        is_jumping = True
        jump_velocity = -10  # Initial upward velocity

    # if is_jumping:
    #     screen.blit(jump_sprites[current_frame], (player_x, player_y))

    
    
    i += 1
    screen.blit(walk_sprites[j], (player_x, player_y))
    if i > player_walk_speed:
        j += 1  
        i = 0
        if j == 7:
            j = 0
        

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

pygame.quit()
