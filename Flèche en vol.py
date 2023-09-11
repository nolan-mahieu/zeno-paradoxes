import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 600, 300
WHITE = (255, 255, 255)
BLACK = 0, 0, 0

font = pygame.font.Font(None, 36)
text_color = BLACK

class Archery:
    def __init__(self, name, speed, position, image_path):
        self.name = name
        self.speed = speed
        self.position = position
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.center = (self.position, HEIGHT // 2)

    def arrow_position(self):
        self.position += self.speed
        self.rect.center = (self.position, HEIGHT // 2)

    def print_position(self):
        print(f"La flèche est actuellement à {self.position} mètres.")
        

class Shooting:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Flying arrow")
        self.clock = pygame.time.Clock()
        self.target = Archery("Target", 0, 250, "images/target.png")
        self.arrow = Archery("Arrow", 25, 0, "images/arrow.png")

    def run(self):
        while self.arrow.position < self.target.position:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.arrow.arrow_position()

            self.screen.fill(WHITE)

            self.screen.blit(self.target.image, self.target.rect)
            self.screen.blit(self.arrow.image, self.arrow.rect)

            self.arrow.print_position()

            arrow_text = font.render(f"{self.arrow.name}: {self.arrow.position} mètres", True, text_color)

            self.screen.blit(arrow_text, (10, 10))

            pygame.display.flip()

            self.clock.tick(1)

        print("La flèche a touché la cible!")

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    shooting = Shooting()
    shooting.run()