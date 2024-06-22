"""Contains the Camera class."""
from dataclasses import dataclass as component

from space2d.models.common import Position


@component
class Camera2d:
    """Structured data describing a 2D othogonal camera.
    
    Attributes:
        position (:obj:`Position`): The location of the camera.
        speed (float): The speed at which the camera moves.
        zoom (float): The zoom level of the camera.
    """
    position: Position = Position(0.0, 0.0)
    speed: float = 1.0
    zoom: float = 1.0
