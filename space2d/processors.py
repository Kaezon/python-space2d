"""Contains the project's Processor classes."""
import esper

from space2d.models.common import Registry, Renderable, Position
from space2d.util import worldToScreenCoords

class RenderProcessor(esper.Processor):
    """A proccessor for Renderable components."""
    def process(self):
        screen = Registry().get("screen")

        for entity, (renderable, position) \
                in esper.get_components(Renderable, Position):
            screen.blit(
                renderable.surface,
                worldToScreenCoords((position.x, position.y))
            )