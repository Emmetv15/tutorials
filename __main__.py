from pygame_wrapper import *
from pygame import Vector2 as Vec

if __name__ == '__main__':

    class Player(Sprite):
        def __init__(self, *args, **kwargs):
            super().__init__(*args)
            self.max_speed = kwargs.get('speed', 5)
            self.move_velocity = Vec(0)
            self.name = kwargs.get('name', "pew")

        def update(self):
            if self.move_velocity.magnitude() > self.max_speed:
                self.position += self.move_velocity/1.414
            else:
                self.position += self.move_velocity
            self.position += self.velocity

        def set_move_vel(self, value):
            self.move_velocity = value

        def add_move_vel(self, value):
            self.move_velocity += value

        def register_events(self, window):
            window.registerEvent(Event(pygame.KEYDOWN, lambda:{
                self.add_move_vel(Vec(0, self.max_speed))}, pygame.K_DOWN
            ).attach())
            window.registerEvent(Event(pygame.KEYDOWN, lambda:{
                self.add_move_vel(Vec(0, -self.max_speed))}, pygame.K_UP
            ).attach())
            window.registerEvent(Event(pygame.KEYDOWN, lambda:{
                self.add_move_vel(Vec(self.max_speed, 0))}, pygame.K_RIGHT
            ).attach())
            window.registerEvent(Event(pygame.KEYDOWN, lambda:{
                self.add_move_vel(Vec(-self.max_speed, 0))}, pygame.K_LEFT
            ).attach())

            window.registerEvent(Event(pygame.KEYUP, lambda:{
                self.add_move_vel(Vec(0, -self.max_speed))}, pygame.K_DOWN
            ).attach())
            window.registerEvent(Event(pygame.KEYUP, lambda:{
                self.add_move_vel(Vec(0, self.max_speed))}, pygame.K_UP
            ).attach())
            window.registerEvent(Event(pygame.KEYUP, lambda:{
                self.add_move_vel(Vec(-self.max_speed, 0))}, pygame.K_RIGHT
            ).attach())
            window.registerEvent(Event(pygame.KEYUP, lambda:{
                self.add_move_vel(Vec(self.max_speed, 0))}, pygame.K_LEFT
            ).attach())

    class Obstacle(Sprite):
        def __init__(self, *args):
            super(Obstacle, self).__init__(*args)
        
        def update(self):
            pass

    class Game(Window):
        def __init__(self, *args):
            super().__init__(*args)

        def update(self):
            # for sprite in self.sprites:
            #     for otherSprite in self.sprites:
            #         if sprite.get_rect().colliderect(otherSprite.get_rect()) and sprite != otherSprite:
            #             rect1, rect2 = [sprite.get_rect(), otherSprite.get_rect()]
            #             if abs(rect2.top - rect1.bottom) > collisionThreshold and sprite.get_vel() > 0:
            #                 #TODO: Make sprite velocity coordinates seperate.
            #                 pass
            pass

        def start(self):
            print("Game Started")

            character = Player([100,100], [148/2,198/2], (255,0,0), 'Not Emmet.png', speed=7).display()
            self.registerSprite(character)
            character.register_events(self)

            character2 = Player([100,100], [148/2,198/2], (255,0,0), 'Not Emmet.png', name="pew2").display()
            self.registerSprite(character2)
            character2.register_events(self)

            super().start()

    game = Game([1000, 600], "Window", (0, 0, 0))
    game.start()