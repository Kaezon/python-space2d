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


def makeRect(origin: tuple[float, float],
             extent: tuple[float, float]) -> pygame.Rect:
    """Create a rect using two :obj:`Position` objects.
    Args:
        origin (float, float): The coordinates of the top-left corner.
        extent (float, float): The size of the rect.
    Returns:
        :obj:`pygame.Rect`
    """
    return pygame.Rect(origin[0], origin[1], extent[0], extent[1])


def worldToScreenCoords(coords: tuple[float, float]) -> tuple:
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