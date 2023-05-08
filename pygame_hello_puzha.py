import pygame

pygame.init()

# Set the dimensions of the window
WINDOW_WIDTH, WINDOW_HEIGHT = 400, 300
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)

# Set the title of the window
pygame.display.set_caption("Puzhis Game")

# Load the image
image = pygame.image.load("C:\pytest\photo_2023-05-08_14-58-34.jpg")

# Get the dimensions of the image
image_width, image_height = image.get_size()

# Create the window
window = pygame.display.set_mode(WINDOW_SIZE)

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the window with a white background
    window.fill((255, 255, 255))

    # Draw the image in the center of the window
    image_x = (WINDOW_WIDTH - image_width) // 2
    image_y = (WINDOW_HEIGHT - image_height) // 2
    window.blit(image, (image_x, image_y))

    # Update the screen
    pygame.display.update()

pygame.quit()
