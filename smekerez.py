import pygame
from sys import exit
import random
import time

class PID:
    def __init__(self, kp, ki, kd):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.previous_error = 0
        self.integral = 0

    def compute(self, setpoint, measured_value):
        error = setpoint - measured_value
        self.integral += error
        derivative = error - self.previous_error
        self.previous_error = error
        return self.kp * error + self.ki * self.integral + self.kd * derivative


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
        
    def _rotate(self, angle):
        self.angle += min(angle, 0.5) # are si el o viteza maxima cum zic..
        
    def rotate(self, gyro, target_angle):
        pid = PID(0.1, 0, 0.05)
        current_angle = gyro.get_angle()
        control_signal = pid.compute(target_angle, current_angle)
        self._rotate(control_signal)
        return current_angle

class Gyro:
    def __init__(self, robot: Robot):
        self.robot = robot
        self.precision = 5.0
        
    def get_angle(self):
        return self.robot.angle + random.uniform(-self.precision, self.precision)
    

def main():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))

    teren = pygame.image.load("./teren/vinyle_table_2024_FINAL_V1.png")
    clock = pygame.time.Clock()

    # Define the color black
    black = (0, 0, 0)

    robot = Robot(90, 90, 120, 120, black)
    gyro = Gyro(robot)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                
        screen.blit(teren, (0, 0))
        robot.draw(screen)
        
        robot.rotate(gyro, 90)
        clock.tick(60)
        
        
        
        # Draw a black rectangle
        
        
        pygame.display.update()

if __name__ == "__main__":
    main()