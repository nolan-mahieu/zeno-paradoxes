import pygame
import sys

# Constantes
WIDTH, HEIGHT = 800, 400
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT_SIZE = 36

class Runner:
    def __init__(self, name, speed, x_position, image_path):
        self.name = name
        self.speed = speed
        self.position = x_position
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.center = (x_position, HEIGHT // 2)

    def move_forward(self):
        self.position += self.speed
        self.rect.center = (self.position, HEIGHT // 2)

class RaceGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Achille & La Tortue")
        self.runners = [
            Runner("Achille", 20, 100, "images/achille.png"),
            Runner("La Tortue", 2, 250, "images/turtle.png")
        ]
        self.clock = pygame.time.Clock()
        self.race_distance = 10000
        self.font = pygame.font.Font(None, FONT_SIZE)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def run(self):
        while any(runner.position < self.race_distance for runner in self.runners):
            self.handle_events()
            self.screen.fill(WHITE)

            for runner in self.runners:
                runner.move_forward()
                self.screen.blit(runner.image, runner.rect)
                text = self.font.render(f"{runner.name}: {runner.position} mètres", True, BLACK)
                text_rect = text.get_rect()
                text_rect.topleft = (10, self.runners.index(runner) * FONT_SIZE + 10)
                self.screen.blit(text, text_rect)

            pygame.display.flip()
            self.clock.tick(1)

            if self.runners[0].position >= self.runners[1].position:
                print("Achille a dépassé La Tortue.")
                break

        print("Course terminée !")

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    race_game = RaceGame()
    race_game.run()
