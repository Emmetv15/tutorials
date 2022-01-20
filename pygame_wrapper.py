# -*- coding: utf-8 -*-
"""Pygame wrapper for easier simple game development

This module was created by S294151 at 16:19 13/11/2021
The standard library to act as a wrapper for pygame to simplify the
game logic and minimise repeated code.

  Typical usage example:

  window = Window([1000, 600], "Window", (0, 0, 0))
  foo.run()
  
  window.registerEvent(Event(pygame.KEYDOWN, lambda: print("Hello world"), pygame.K_SPACE).attach())

Example:
    The following example shows a basic window created with this library::

        $ python pygame_wrapper.py

TODO:
    make a paralax background effect.

"""

import pygame
import os
from pygame import Vector2 as Vec


class Window():
    """A Window with all the functionality needed to create a simple game

    This creates an abstract wrapper that can be used to interact with pygame.

    Args:
        dimensions (tuple): Dimensions of the window in pixels (width, height).
        title (str): Title of the window.
        background (tuple): Background color of the screen.

    Returns:
        A Window instance that can be used to register sprites and events.
    """

    def __init__(self, dimensions, title, background):

        self.rect = pygame.Rect(0, 0, *dimensions)
        pygame.init()
        pygame.display.set_caption(title)

        self.surface = pygame.display.set_mode(self.rect.size)
        self.background = background                    

        self.font = pygame.font.SysFont("Roboto", 25)
        self.text_pause = self.font.render("PAUSE", True, (255, 0, 0))

        self.text_pause_rect = self.text_pause.get_rect(center=self.surface.get_rect().center) 

        self.events = []
        self.sprites = []

        self.RUNNING = True

    # TODO: make a paralax background effect.
    # def draw_background_image(self, image):
    #     temp = pygame.Surface(self.rect.size, pygame.SRCALPHA, 32).convert_alpha()
    #     image_rect = image.get_rect()

    #     for x in range(0, self.rect.width, 60):
    #         for y in range(0,self.rect.width, 60):
    #             temp.blit(image,(x,y))

    #     return temp

    @property
    def running(self):
        return self.RUNNING

    def reset(self):
        """Resets the display
        """
        self.surface.fill(self.background)

    def registerEvent(self, handler):
        """Add a handler to the window
        Args:
            handler (Event): The event handler to register
        """
        self.events.append(handler)

    def registerSprite(self, sprite):
        self.sprites.append(sprite)
        sprite.setSurface(self.surface)
    
    def draw(self):
        for sprite in self.sprites:
            sprite.update()
            if sprite.isVisible():
                sprite.draw()
    
    def start(self):

        clock = pygame.time.Clock()

        self.RUNNING = True
        PAUSED = False

        while self.RUNNING:

            for event in pygame.event.get():
                for handler in self.events:
                    if event.type == handler.type:
                        if handler.key:
                            if event.key == handler.key:
                                handler.execute()
                        
                if event.type == pygame.QUIT:
                    self.RUNNING = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.RUNNING = False

            self.update()
            self.reset()
            self.draw()

            fps = self.font.render("FPS: %s" % str(round(clock.get_fps())), True, (255, 255, 255))
            fps.set_alpha(0.60*255)
            self.surface.blit(fps, (0, 0))

            pygame.display.update()
            clock.tick(120)

        pygame.quit()

    def update(self):
        pass


class Event():
    """This is used to create an event that can be added to the window.    

    Args:
        event: The event to be added to the window. e.g. pygame.KEYDOWN
        callback (Callable): The code that is executed when the event is executed.
        key (optional): If the event involves a key, you can specify the key here.
    """

    def __init__(self, event, callback, key=None):
        self.type = event
        if key:
            self.key = key
        self.callback = callback
        self.enabled = False
        
    def execute(self):
        self.callback()
            
    def isEnabled(self):
        return self.enabled
    
    def attach(self, enabled=True):
        self.enabled = enabled
        return self


class Sprite(pygame.sprite.Sprite):
    """A class that utilizes pygame's sprite class to generate an image/rectangle in a desired frame.

    This class can used to make many sprites easily and effectively, and
    then registered into a window which displays them.
    It is also possible to move the sprite around and hide/show it.
    
    Args:
        position (list): Position of the sprite [x, y], use -1 isntead to have it centered.
        size (list): Size of the sprite [width, height].
        color (tuple): Color of the sprite [r, g, b].
        image (string): Path to the image 'image.png'.
    
    Returns:
        An instance that can be used to draw the sprite on the screen.
    """

    def __init__(self, position, size, color, image=None):
        pygame.sprite.Sprite.__init__(self)
        self.surface = None
        self.isImage = False
        self.pixels = None
        self.visible = False
        self.size = size
        self.rect = pygame.Rect(*position, *size)
        self.position = Vec(position)
        self.velocity = Vec(0)
        self.color = color
        if image:
            self.isImage = True
            if not self.size == [0, 0]:
                self.pixels = pygame.transform.scale(pygame.image.load(os.path.join('resources', image)).convert_alpha(), self.size)
            else:
                self.pixels = pygame.image.load(os.path.join('resources', image))

    def update(self):
        self.position += self.velocity

    def draw(self):
        if not self.surface: return
        self.rect.update(*[self.position[0] - self.size[0]/2, self.position[1] - self.size[1]/2], *self.size)

        if self.isImage:
            self.surface.blit(self.pixels, [self.position[0] - self.size[0]/2, self.position[1] - self.size[1]/2])
        else:
            pygame.draw.rect(self.surface, self.color, self.rect)

    def setSurface(self, surface):
        self.surface = surface

    def isVisible(self):
        return self.visible
    
    def display(self, visible=True):
        self.visible = visible
        return self

    def set_pos(self):
        return self.position
    
    def get_pos(self, value):
        self.position = value

    def add_pos(self, value):
        self.position += value

    def set_vel(self, value):
        self.velocity = value

    def get_vel(self, value):
        return self.velocity
    
    def add_vel(self, value):
        self.velocity += value

    def get_rect(self):
        return self.rect

if __name__ == "__main__":
    class Game(Window):
        def __init__(self, *args):
            super().__init__(*args)

        def update(self):
            pass
        
        def start(self):
            print("Game Started")

            character = Sprite([100,100], [148/2,198/2], (255,0,0), 'Not Emmet.png').display()
            self.registerSprite(character)
            
            self.registerEvent(Event(pygame.KEYDOWN, lambda:{
                character.add_vel(Vec(0, 10))}, pygame.K_DOWN
            ).attach())
            self.registerEvent(Event(pygame.KEYDOWN, lambda:{
                character.add_vel(Vec(0, -10))}, pygame.K_UP
            ).attach())
            self.registerEvent(Event(pygame.KEYDOWN, lambda:{
                character.add_vel(Vec(10, 0))}, pygame.K_RIGHT
            ).attach())
            self.registerEvent(Event(pygame.KEYDOWN, lambda:{
                character.add_vel(Vec(-10, 0))}, pygame.K_LEFT
            ).attach())

            self.registerEvent(Event(pygame.KEYUP, lambda:{
                character.add_vel(Vec(0, 0))}, pygame.K_DOWN
            ).attach())
            self.registerEvent(Event(pygame.KEYUP, lambda:{
                character.add_vel(Vec(0, 0))}, pygame.K_UP
            ).attach())
            self.registerEvent(Event(pygame.KEYUP, lambda:{
                character.add_vel(Vec(0, 0))}, pygame.K_RIGHT
            ).attach())
            self.registerEvent(Event(pygame.KEYUP, lambda:{
                character.add_vel(Vec(0, 0))}, pygame.K_LEFT
            ).attach())


            super().start()

    game = Game([1000, 600], "Window", (0, 0, 0))
    game.start()
