import pygame as pg
from time import sleep
class Entity:

    def __init__(self, name, health, damage, armor) -> None:
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor


hero = Entity("c", 6,6,6)
 

pg.init()


screen = pg.display.set_mode((1000, 900))
is_tablet = False
num = 0
clock = pg.time.Clock()
choice = pg.image.load("choice.png")
stroke = pg.image.load("stroke.png")
grass = pg.image.load("grass.png")
sky = pg.image.load("sky.png")
hero = Entity("hero", 100, 60, 0, "hero.png", "hero_left.gif")
stroke_coords = (0, 213)

is_working = True
while is_working:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            is_working = False
    pressed = pg.key.get_pressed()

    
    
    if is_tablet:
        screen.blit(choice, (0, 0))
        screen.blit(stroke, (214, 223 + (stroke_coords[num % 2])))
        if pressed[pg.K_DOWN]:
            screen.fill((0, 0, 0))
            num += 1
    screen.blit(hero.animation(), (500, 500))
    screen.blit(sky, (0, 0))
    screen.blit(grass, (0, 0))
    screen.blit(hero, (300, 300))
    pg.display.flip()  
    clock.tick(60) 
    sleep(0.09)

pg.quit()