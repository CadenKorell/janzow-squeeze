
import pygame
import os
import sys
from pathlib import Path

assets_path = Path("Assets")

assets_path / "empty_timer.png"

# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
FPS = 60
TIMER_START = 10  # in seconds

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Janzow Squeeze")

# Load images
janz_background = pygame.image.load(
    assets_path/"janz_bg.png").convert()


chad_default = pygame.image.load(
    assets_path/"chad_default.png").convert_alpha()
chad_default_but_no_legs = pygame.image.load(
    assets_path/"chad_default_but_no_legs.png").convert_alpha()


empty_timer = pygame.image.load(
    assets_path/"empty_timer.png")

timer_images = [
    pygame.image.load(
        assets_path/"timer_1.png").convert_alpha(),
    pygame.image.load(
        assets_path/"timer_2.png").convert_alpha(),
    pygame.image.load(
        assets_path/"timer_3.png").convert_alpha(),
    pygame.image.load(
        assets_path/"timer_4.png").convert_alpha(),
    pygame.image.load(
        assets_path/"timer_5.png").convert_alpha(),
    pygame.image.load(
        assets_path/"timer_6.png").convert_alpha(),
    pygame.image.load(
        assets_path/"timer_7.png").convert_alpha(),
    pygame.image.load(
        assets_path/"timer_8.png").convert_alpha(),
    pygame.image.load(
        assets_path/"timer_9.png").convert_alpha(),
    pygame.image.load(
        assets_path/"timer_10.png").convert_alpha()
]



chad_walk_left_images = [
    pygame.image.load(
        assets_path/"chad_walk_left_1.png").convert_alpha(),
    pygame.image.load(
        assets_path/"chad_walk_left_2.png").convert_alpha(),
    pygame.image.load(
        assets_path/"chad_walk_left_3.png").convert_alpha(),
    pygame.image.load(
        assets_path/"chad_walk_left_4.png").convert_alpha()
]
chad_walk_right_images = [
    pygame.image.load(
        assets_path/"chad_walk_right_1.png").convert_alpha(),
    pygame.image.load(
        assets_path/"chad_walk_right_2.png").convert_alpha(),
    pygame.image.load(
        assets_path/"chad_walk_right_3.png").convert_alpha(),
    pygame.image.load(
        assets_path/"chad_walk_right_4.png").convert_alpha()
]
chad_walk_up_images = [
    pygame.image.load(
        assets_path/"chad_walk_up_1.png").convert_alpha(),
    pygame.image.load(
        assets_path/"chad_walk_up_2.png").convert_alpha()
]
chad_walk_down_images = [
    pygame.image.load(
        assets_path/"chad_walk_down_1.png").convert_alpha(),
    pygame.image.load(
        assets_path/"chad_walk_down_2.png").convert_alpha()
]



# Animation settings
current_frame = 0
frame_rate = 7
frame_counter = 0



# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Player settings
player_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
player_speed = 13

# Timer settings
timer = TIMER_START
timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event, 1000)  # 1 second interval


TIMER_WIDTH, TIMER_HEIGHT = empty_timer.get_size()

# Constants for camera
CAMERA_WIDTH = SCREEN_WIDTH
CAMERA_HEIGHT = SCREEN_HEIGHT


# Background dimensions
background_width, background_height = janz_background.get_size()
print(janz_background.get_size)

screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
pygame.display.set_caption("Janzow Squeeze")
clock = pygame.time.Clock()


# Main game loop
def main():
    global timer, current_frame, frame_counter

    # clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == timer_event:
                if timer > 0:
                    timer -= 1

        # Player movement
        keys = pygame.key.get_pressed()
        moving = False
        moving_left = False
        moving_right = False
        moving_up = False
        moving_down = False
        
        if keys[pygame.K_LEFT]:
            player_pos[0] -= player_speed
            moving_left = True
            moving = True
            
        if keys[pygame.K_RIGHT]:
            player_pos[0] += player_speed
            moving_right = True
            moving = True
            
        if keys[pygame.K_UP]:
            player_pos[1] -= player_speed
            moving_up = True
            moving = True
            
        if keys[pygame.K_DOWN]:
            player_pos[1] += player_speed
            moving_down = True
            moving = True

        # Keep player on screen
        player_pos[0] = max(0, min(background_width - chad_default.get_width(), player_pos[0]))
        player_pos[1] = max(0, min(background_height - chad_default.get_height(), player_pos[1]))

        # Calculate camera position
        camera_x = player_pos[0] - CAMERA_WIDTH // 2
        camera_y = player_pos[1] - CAMERA_HEIGHT // 2

        # Make sure camera does not go out of bounds
        camera_x = max(0, min(camera_x, background_width - CAMERA_WIDTH*2))
        camera_y = max(0, min(camera_y, background_height - CAMERA_HEIGHT))


        # Update animation frame
        if moving:
            frame_counter += 1
            if frame_counter >= frame_rate:
                if moving_left:
                    current_frame = (current_frame + 1) % len(chad_walk_left_images)
                    frame_counter = 0
                if moving_right:
                    current_frame = (current_frame + 1) % len(chad_walk_right_images)
                    frame_counter = 0
                if moving_up:
                    current_frame = (current_frame + 1) % len(chad_walk_up_images)
                    frame_counter = 0
                if moving_down:
                    current_frame = (current_frame + 1) % len(chad_walk_down_images)
                    frame_counter = 0

        else:
            current_frame = 0  # Reset to the first frame if not moving


        # Drawing
        # Draw the background at the camera's position
        screen.blit(janz_background, (-camera_x, -camera_y))
        # Draw the current frame of the walking animation
        if moving_left and moving_right:
            moving_left = False
            moving_right = False
            moving = False
            current_frame = 0
            
        if moving_up and moving_down:
            moving_up = False
            current_frame = 0
            
        if moving_down and moving_left:    # have to do this to avoid annoying index errors {
            moving_left = False
            current_frame = 0
        if moving_down and moving_right:
            moving_right = False
            current_frame = 0

        if moving_up and moving_left:
            moving_left = False
            current_frame = 0
        if moving_up and moving_right:
            moving_right = False
            current_frame = 0

                                            #   }
            
        if moving_left:
            screen.blit(chad_walk_left_images[current_frame], (player_pos[0] - camera_x, player_pos[1] - camera_y))
        if moving_right:
            screen.blit(chad_walk_right_images[current_frame], (player_pos[0] - camera_x, player_pos[1] - camera_y))
        if moving_up:
            screen.blit(chad_walk_up_images[current_frame], (player_pos[0] - camera_x, player_pos[1] - camera_y))
        if moving_down:
            screen.blit(chad_default_but_no_legs, (player_pos[0] - camera_x, player_pos[1] - camera_y))
            screen.blit(chad_walk_down_images[current_frame], (player_pos[0] - camera_x, player_pos[1] - camera_y))
        if moving == False:
            screen.blit(chad_default, (player_pos[0] - camera_x, player_pos[1] - camera_y))

        # Draw timer on screen
        if timer > 0:
            screen.blit(timer_images[timer-1], (0,0))
        else:
            screen.blit(empty_timer, (0,0))

        # Refresh screen
        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()

