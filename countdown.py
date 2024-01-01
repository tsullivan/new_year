import pygame
import time
from datetime import datetime, timedelta

# Initialize Pygame
pygame.init()

class Constants:
    # Set the dimensions of the window
    WIDTH, HEIGHT = 800, 600

    # Load the custom font and set the font size
    FONT = pygame.font.Font('SF Funk Master.ttf', 120)

    # Set the colors
    TEXT_COLOR = (0, 255, 255)
    BACKGROUND_COLOR = (0, 0, 0)
    END_STATE_COLOR = (255, 215, 0)

# Function to display the countdown timer
def countdown():
    # Calculate the time remaining until midnight
    midnight = datetime.now().replace(hour=0, minute=0, second=0) + timedelta(days=1)
    t = int((midnight - datetime.now()).total_seconds())

    while t:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_t:
                    display_end_state()
                    continue
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_t:
                    continue

        hours, remainder = divmod(t, 3600)
        mins, secs = divmod(remainder, 60)
        timer = '{:02d}:{:02d}:{:02d}'.format(hours, mins, secs)
        text = Constants.FONT.render(timer, True, Constants.TEXT_COLOR)
        screen = pygame.display.set_mode((Constants.WIDTH, Constants.HEIGHT), pygame.RESIZABLE)
        screen.fill(Constants.BACKGROUND_COLOR)
        text_rect = text.get_rect(center=(Constants.WIDTH/2, Constants.HEIGHT/2))
        screen.blit(text, text_rect)
        pygame.display.update()
        time.sleep(1)
        t -= 1

    display_end_state()

# Function to display the end state
def display_end_state():
    # Display "HAPPY NEW YEAR!!!" when the countdown ends
    text = Constants.FONT.render("HAPPY NEW YEAR!!!", True, Constants.END_STATE_COLOR)
    screen = pygame.display.set_mode((Constants.WIDTH, Constants.HEIGHT), pygame.RESIZABLE)
    screen.fill(Constants.BACKGROUND_COLOR)
    text_rect = text.get_rect(center=(Constants.WIDTH/2, Constants.HEIGHT/2))
    screen.blit(text, text_rect)
    pygame.display.update()

# Start the countdown
countdown()

# Keep the window open
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
