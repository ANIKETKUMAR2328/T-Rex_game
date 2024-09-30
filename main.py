import pygame
import random

pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("T-Rex Game")
 
class Dinosaur:
    def __init__(self):
        self.width = 50
        self.height = 50
        self.x = 50
        self.y = height - self.height
        self.jump = False
        self.jump_count = 10
        self.gravity = 1
        self.velocity = 5

    def jump_up(self):
        if not self.jump:
            self.jump = True

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.x += self.velocity
        if keys[pygame.K_LEFT]:
            self.x -= self.velocity

    def draw(self):
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.width, self.height))

class Obstacle:
    def __init__(self):
        self.width = 20
        self.height = 50
        self.x = width
        self.y = height - self.height
        self.velocity = 5

    def update(self):
        self.x -= self.velocity

    def draw(self):
        pygame.draw.rect(screen, (0, 255, 0), (self.x, self.y, self.width, self.height))

def main():
    dinosaur = Dinosaur()
    obstacles = []
    score = 0
    clock = pygame.time.Clock()
    run = True
    obstacle_spacing = 300  # Adjust the spacing between obstacles

    while run:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    dinosaur.jump_up()

        keys = pygame.key.get_pressed()
        dinosaur.move()

        if dinosaur.jump:
            if dinosaur.jump_count >= -10:
                neg = 1
                if dinosaur.jump_count < 0:
                    neg = -1
                dinosaur.y -= (dinosaur.jump_count ** 2) * 0.5 * neg
                dinosaur.jump_count -= 1
            else:
                dinosaur.jump = False
                dinosaur.jump_count = 10

        else:
            if dinosaur.y < height - dinosaur.height:
                dinosaur.y += dinosaur.gravity

        screen.fill((255, 255, 255))

        dinosaur.draw()

        if random.randint(0, 100) < 2:
            if len(obstacles) == 0 or obstacles[-1].x < width - obstacle_spacing:
                obstacle = Obstacle()
                obstacles.append(obstacle)

        for obstacle in obstacles:
            obstacle.update()
            obstacle.draw()
            if (dinosaur.x < obstacle.x + obstacle.width and
                    dinosaur.x + dinosaur.width > obstacle.x and
                    dinosaur.y < obstacle.y + obstacle.height and
                    dinosaur.y + dinosaur.height > obstacle.y):
                run = False

        pygame.display.update()

    pygame.quit()
    print("Your score:", score)

if __name__ == "__main__":
    main()
