import numpy as np
import sys
import pygame


class World:
    def __init__(self):
        self.meter_to_pixel = 50
        self.window_width: int = 800
        self.window_height: int = 600

        pygame.init()
        self.font = pygame.font.SysFont("monospace", 15)
        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption("Robot")

    def xy_to_screen(self, x: float, y: float):
        return (
            self.window_width / 2 + x * self.meter_to_pixel,
            self.window_height / 2 - y * self.meter_to_pixel,
        )

    def screen_to_xy(self, x: int, y: int):
        return (
            (x - self.window_width / 2) / self.meter_to_pixel,
            -(y - self.window_height / 2) / self.meter_to_pixel,
        )

    def load_image(self, filename: str):
        return pygame.image.load("robot.png")

    def set_image_pose(self, image, x: float, y: float, orientation: float):
        x, y = self.xy_to_screen(x, y)
        draw_image = pygame.transform.rotozoom(image, np.degrees(orientation), .5)
        rect = draw_image.get_rect()
        rect.left = x - rect.width / 2
        rect.top = y - rect.height / 2
        self.window.blit(draw_image, rect)

    def draw_line(self, x1: float, y1: float, x2: float, y2: float, color: tuple, thickness: int = 4):
        pygame.draw.line(self.window, color, self.xy_to_screen(x1, y1), self.xy_to_screen(x2, y2), thickness)

    def draw_circle(self, x: float, y: float, radius: int, color: tuple):
        pygame.draw.circle(self.window, color, self.xy_to_screen(x, y), radius)

    def draw_text(self, x: float, y: float, text: str, color: tuple = (0, 0, 0)):
        label = self.font.render(text, 1, color)
        self.window.blit(label, self.xy_to_screen(x, y))

    def draw_grid(self, size: int = 16):
        self.window.fill((220, 220, 220))
        for k in range(-size // 2, 1 + size // 2):
            self.draw_line(k, -size / 2, k, size / 2, (200, 200, 200), 1)
            self.draw_line(-size / 2, k, size / 2, k, (200, 200, 200), 1)

    def draw_frame(self, name: str, T_world_frame: np.ndarray):
        O = (T_world_frame @ [0, 0, 1])[:2]
        x = (T_world_frame @ [1, 0, 1])[:2]
        y = (T_world_frame @ [0, 1, 1])[:2]
        self.draw_line(*O, *x, (255, 0, 0), 2)
        self.draw_line(*O, *y, (0, 255, 0), 2)
        self.draw_text(O[0] - 0.25, O[1], "{" + name + "}")

    def draw_point(self, x: float, y:float, label:str):
        self.draw_circle(x, y, 5, (0, 128, 255))
        self.draw_text(x+.1, y+.3, label)

    def reset(self):
        pygame.display.flip()
        self.draw_grid()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("bye bye ...")
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return True
