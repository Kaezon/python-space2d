from dataclasses import dataclass as component
from typing import Any, Dict, Optional

import pygame


@component
class Position:
    """A component for object which exist in 2D space.
    Attributes:
        x (float): The position on the X axis.
        y (float): The position on the y axis.
    """
    x: float = 0.0
    y: float = 0.0

    def asTuple(self):
        return (self.x, self.y)


@component
class Renderable:
    """A component for renderable objects.
    Attributes:
        surface (:obj:`pygame.Surface`): The renderable surface.
    """
    surface: Optional[pygame.Surface] = None


class Registry:
    """A singleton class built around a dict."""
    __instance = None
    __dict: Dict[str, Any] = {}
    
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = obj = object.__new__(cls)
            obj.__dict = {}
        return cls.__instance

    def get(self, name):
        return self.__dict.get(name)

    def set(self, name: str, value: Any, overwrite: Optional[bool] = False):
        if name not in self.__dict or overwrite:
            self.__dict[name] = value
