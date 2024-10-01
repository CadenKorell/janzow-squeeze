import pygame


class Game:
    
    def __init__(self, height, width, caption) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((height, width))
        pygame.display.set_caption(caption)
        self.clock = pygame.time.Clock()
    
    def run(self):
        ...
        