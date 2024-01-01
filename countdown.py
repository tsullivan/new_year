import pygame
import time
from datetime import datetime, timedelta

# Initialize Pygame
pygame.init()

class Constants:
    # Set the dimensions of the window
    WIDTH, HEIGHT = 1600, 600

    # Load the custom font and set the font size
    FONT = pygame.font.Font('SF Funk Master.ttf', 120)

    # Set the colors
    TEXT_COLOR = (0, 255, 255)
    BACKGROUND_COLOR = (0, 0, 0)
    END_STATE_COLOR = (255, 215, 0)

screen = pygame.display.set_mode((Constants.WIDTH, Constants.HEIGHT), pygame.RESIZABLE)

# Function to display the countdown timer
def countdown():
    # Calculate the time remaining until midnight
    midnight = datetime.now().replace(hour=0, minute=0, second=0) + timedelta(days=1)
    t = 1

    while t:
        t = int((midnight - datetime.now()).total_seconds())
        hours, remainder = divmod(t, 3600)
        mins, secs = divmod(remainder, 60)
        timer = '{:02d}:{:02d}:{:02d}'.format(hours, mins, secs)
        text = Constants.FONT.render(timer, True, Constants.TEXT_COLOR)
        screen.fill(Constants.BACKGROUND_COLOR)
        text_rect = text.get_rect(center=(screen.get_width()/2, screen.get_height()/2))
        screen.blit(text, text_rect)
        pygame.display.update()
        time.sleep(1)

    display_end_state()

# Function to display the end state
def display_end_state():
    # Display "HAPPY NEW YEAR!!!" when the countdown ends
    text = Constants.FONT.render("HAPPY NEW YEAR!!!", True, Constants.END_STATE_COLOR)
    screen.fill(Constants.BACKGROUND_COLOR)
    text_rect = text.get_rect(center=(screen.get_width()/2, screen.get_height()/2))
    screen.blit(text, text_rect)
    pygame.display.update()

# Start the countdown
countdown()

# Keep the window open
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
