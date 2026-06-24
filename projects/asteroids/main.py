import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH

def main():
    print(
        f"Starting Asteroids with pygame version: {pygame.version.ver} "
        f"(Screen width: {SCREEN_WIDTH})"
        f"(Screen height: {SCREEN_HEIGHT})"
    )


if __name__ == "__main__":
    main()
