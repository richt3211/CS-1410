import pygame
import math
import game_mouse
import frogger

# Starter code for PyGame applications

class PygameStarter(game_mouse.Game):

    def __init__(self, width, height, size, fps):

        game_mouse.Game.__init__(self, "Pygame Starter",
                                 width,
                                 height,
                                 fps)
        self.mFrogger = frogger.Frogger(width, height, size)
        return

        
    def game_logic(self, keys, newkeys, buttons, newbuttons, mouse_position):
        x = mouse_position[0]
        y = mouse_position[1]

        if pygame.K_a in newkeys:
            print("a key pressed")
        
        if 1 in newbuttons:
            print("button clicked")
        self.mFrogger.update( 1 , newkeys)

        return
    
    def paint(self, surface):
        self.mFrogger.draw(surface)
        return

def main():
    screen_width = 840
    screen_height = 910
    size = 70
    frames_per_second = 30
    game = PygameStarter(screen_width, screen_height, size , frames_per_second)
    game.main_loop()
    return
    
if __name__ == "__main__":
    main()

