"""Simulation of a Kepler orbit.

I wanted to make some reusable components to simulate Kepler orbits
for use in context of games. Rather than running a physics simulation,
I figured it would be for more efficient to use the mathmatical models
of Kepler orbits.

Required Packages:
- pygame
- esper
"""
import esper
import pygame
from pygame.locals import *

from space2d.models.camera import Camera2d
from space2d.models.common import (Position,
                                   Registry,
                                   Renderable)
from space2d.models.orbits import Orbit, OrbitProcessor
from space2d.processors import RenderProcessor
from space2d.util import makeDotSurface

DISPLAY_WIDTH = 500
DISPLAY_HEIGHT = 500


if __name__ == '__main__':
    # Init pygame
    pygame.init()
    screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT),
                                     pygame.SCALED)
    pygame.display.set_caption("Orbit Test")
    pygame.mouse.set_visible(True)
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))
    clock = pygame.time.Clock()

    # Get Registry
    registry = Registry()
    registry.set("background", background)
    registry.set("screen", screen)
    registry.set("time", 0)

    # Init Esper
    esper.add_processor(OrbitProcessor())
    esper.add_processor(RenderProcessor())

    # Init Camera
    camera = esper.create_entity(
        Camera2d(
            position = Position(x=DISPLAY_WIDTH/4, y=DISPLAY_HEIGHT/4),
            speed = 1,
            zoom = 1
        )
    )

    registry.set("activeCamera", camera)

    # Init planet
    celestial_body = esper.create_entity(
        Renderable(makeDotSurface(10)),
        Position(x=DISPLAY_WIDTH/2, y=DISPLAY_HEIGHT/2),
        Orbit(argument_of_periapsis=0.0,
              center=Position(DISPLAY_WIDTH/2, DISPLAY_HEIGHT/2),
              eccentricity=0.0,
              period=1000,
              semimajor_axis=50.0,
              true_anomaly=0.0)
    )

    # Init star
    star = esper.create_entity(
        Renderable(makeDotSurface(10)),
        Position(x=DISPLAY_WIDTH/2, y=DISPLAY_HEIGHT/2)
    )

    # Initial BG fill
    screen.blit(background, (0, 0))

    quit = False
    while not quit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit = True

        registry.set("dirty_rects", [], overwrite=True)
        esper.process()
        pygame.display.update(registry.get("dirty_rects"))
        registry.set("time",
                     registry.get("time")+clock.tick(60),
                     overwrite=True)

    pygame.quit()
