import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 1000
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

font = pygame.font.Font(None, 36)
text_color = BLACK

class Throw:
    def __init__(self, name, position, image_path):
        self.name = name
        self.position = position
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect = (self.position, HEIGHT // 2)

    def rock_position(self, target_position):
        self.position += ((target_position - self.position) * 0.5)
        self.rect = (self.position, HEIGHT // 2)

    def print_position(self):
        print(f"Le {self.name} est à {self.position} mètres.")

class RockThrowing:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Dichotomy")
        self.rock = Throw("Rock", 0, "images/rock.png")
        self.tree = Throw("Tree", 10, "images/tree.png")
        self.clock = pygame.time.Clock()
    
    def run(self):
        while self.rock.position < self.tree.position:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.rock.rock_position(self.tree.position)

            self.screen.fill(WHITE)

            self.screen.blit(self.tree.image, self.tree.rect)
            self.screen.blit(self.rock.image, self.rock.rect)

            self.rock.print_position()

            rock_text = font.render(f"{self.rock.name}: {self.rock.position} mètres", True, text_color)
            
            self.screen.blit(rock_text, (10, 10))

            pygame.display.flip()

            self.clock.tick(1)

        print("Le rocher a touché l'arbre!")

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    throwing = RockThrowing()
    throwing.run()