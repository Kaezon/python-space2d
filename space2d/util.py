import esper
import pygame

from .models.camera import Camera2d
from .models.common import Position, Registry


def makeDotSurface(size: int) -> pygame.Surface:
    """Create a surface with a dot on it.
    Args:
        size (int): Diameter of the dot and size of the surface.
    """
    surface = pygame.Surface((size, size))
    pygame.draw.circle(surface, (255,255,255), (size/2,size/2), size/2)
    return surface


def makeRect(origin: Position, extent: Position) -> pygame.Rect:
    """Create a rect using two :obj:`Position` objects.
    Args:
        origin (:obj:`Position`): The coordinates of the top-left corner.
        extent (:obj:`Position`): The size of the rect.
    """
    return pygame.Rect(origin.x, origin.y, extent.x, extent.y)


def worldToScreenCoords(coords: tuple) -> tuple:
    """Transform world coordinates to screen coordinates.
    Args:
        coords (float, float): World coordinates to transform.
    Returns:
        (float, float)
    """
    camera_position = esper.component_for_entity(
        Registry().get("activeCamera"), Camera2d).position
    screen_rect = Registry().get("screen").get_rect()
    (x, y) = coords

    return (
        x - camera_position.x + screen_rect.centerx,
        y - camera_position.y + screen_rect.centery
    )

def worldToScreenRect(rect: pygame.Rect) -> pygame.Rect:
    """Transform Rect from world coords to screen coords.
    Args:
        rect (:obj:`pygame.Rect`): World coordinates to transform.
    Returns:
        (:obj:`pygame.Rect`)
    """
    camera_position = esper.component_for_entity(
        Registry().get("activeCamera"), Camera2d).position
    screen_rect = Registry().get("screen").get_rect()

    return rect.move(-camera_position.x + screen_rect.centerx,
                     -camera_position.y + screen_rect.centery)