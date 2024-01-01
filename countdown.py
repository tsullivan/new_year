import pygame
import time

# Initialize Pygame
pygame.init()

# Set the dimensions of the window
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

# Load the custom font and set the font size
font = pygame.font.Font('SF Funk Master.ttf', 120)

# Set the colors
gold = (218, 165, 32)
cyan = (0, 255, 255)
light_green = (144, 238, 144)

# Function to display the countdown timer
def countdown(t):
    while t:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_t:
                    display_end_state()
                    continue
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_t:
                    continue

        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        text = font.render(timer, True, gold)
        screen.fill((0,0,0))
        text_rect = text.get_rect(center=(width/2, height/2))
        screen.blit(text, text_rect)
        pygame.display.update()
        time.sleep(1)
        t -= 1

    display_end_state()

# Function to display the end state
def display_end_state():
    # Display "HAPPY NEW YEAR!!!" when the countdown ends
    text = font.render("HAPPY NEW YEAR!!!", True, gold)
    screen.fill((0,0,0))
    text_rect = text.get_rect(center=(width/2, height/2))
    screen.blit(text, text_rect)
    pygame.display.update()

# Start the countdown
countdown(10)

# Keep the window open
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
# Write your code here :-)
