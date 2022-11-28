#! bin/python3

import pygame as pyg

pyg.init()

class MyRunner:
    
    HEIGTH = 720
    WIDTH = 1000
    
    def __init__(self) -> None:
        # Initialization of the game
        self.game_window = pyg.display.set_mode(flags=pyg.FULLSCREEN)
        
        self.isplaying = True
        
        # Start the game
        self.game_loop()
        
        
    def game_loop(self) -> None:
        while self.isplaying:
            # get the keys dict
            keys = pyg.key.get_pressed()
            
            if keys[pyg.K_g]:
                pass
            
            for event in pyg.event.get():
                if event == pyg.QUIT or keys[pyg.K_ESCAPE]:
                    self.isplaying = False
                    return
                