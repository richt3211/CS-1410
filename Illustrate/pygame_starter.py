import pygame
import math
import game_mouse
import picture

# Starter code for PyGame applications

class PygameStarter(game_mouse.Game):

    def __init__(self, width, height, fps):

        game_mouse.Game.__init__(self, "Pygame Starter",
                                 width,
                                 height,
                                 fps)
        self.mPicture = picture.Picture ( width, height )
        return
        
    def game_logic(self, keys, newkeys, buttons, newbuttons, mouse_position):
        x = mouse_position[0]
        y = mouse_position[1]

        if pygame.K_a in newkeys:
            print("a key pressed")
        
        if 1 in newbuttons:
            print("button clicked")

        return
    
    def paint(self, surface):
        self.mPicture.draw(surface)
        return

def main():
    screen_width = 900
    screen_height = 700
    frames_per_second = 10
    game = PygameStarter(screen_width, screen_height, frames_per_second)
    game.main_loop()
    return
    
if __name__ == "__main__":
    main()

