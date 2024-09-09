import pygame
from sys import exit

class Robot:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.angle = 0  # Initialize the angle to 0
        
    def draw(self, screen):
        # Create a surface for the robot
        robot_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        robot_surface.fill(self.color)
        
        # Rotate the surface
        rotated_surface = pygame.transform.rotate(robot_surface, self.angle)
        
        # Calculate the top-left corner based on the center coordinates
        top_left_x = self.x - rotated_surface.get_width() // 2
        top_left_y = self.y - rotated_surface.get_height() // 2
        
        # Blit the rotated surface onto the screen
        screen.blit(rotated_surface, (top_left_x, top_left_y))
        
    def move(self, x, y):
        self.x += x
        self.y += y
        
    def rotate(self, angle):
        self.angle += angle  # Update the angle


def main():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))

    teren = pygame.image.load("./teren/vinyle_table_2024_FINAL_V1.png")

    # Define the color black
    black = (0, 0, 0)

    robot = Robot(90, 90, 120, 120, black)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                
        screen.blit(teren, (0, 0))
        robot.draw(screen)
        robot.rotate(1)  # Rotate the robot by 1 degree
        
        
        # Draw a black rectangle
        
        
        pygame.display.update()

if __name__ == "__main__":
    main()