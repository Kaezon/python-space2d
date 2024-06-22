from dataclasses import dataclass as component
from math import cos, sin

import esper

from .common import Position, Registry, Renderable
from ..util import makeRect


@component
class Orbit:
    """Structured data describing a simplified orbit.
    
    For more info, see:
    https://en.wikipedia.org/wiki/Orbital_elements

    Attributes:
        argument_of_periapsis (float): Defines the orientation of the ellipse
            in the orbital plane, as an angle measured from the ascending node
            to the periapsis.
        center (:obj:`Position`): The center point of the orbit.
        eccentricity (float): Shape of the ellipse, describing how much it is
            elongated compared to a circle.
            https://en.wikipedia.org/wiki/Orbital_eccentricity
        period (float): The time it takes to complete one full orbit.
        semimajor_axis (float): The sum of the periapsis and apoapsis distances
            divided by two.
        true_anomaly (float): Defines the position of the orbiting body along
            the ellipse at a specific time (the "epoch").
    """
    argument_of_periapsis: float = 0.0
    center: Position = Position(0.0, 0.0)
    eccentricity: float = 0.0
    period: float = 0.0
    semimajor_axis: float = 1.0
    true_anomaly: float = 0.0


class OrbitProcessor(esper.Processor):
    """A processor for :obj:`Orbit` components.

    Moves entities in 2D space according to a model of ideal orbits.

    For more info, see:
    https://en.wikipedia.org/wiki/Elliptic_orbit
    https://en.wikipedia.org/wiki/Kepler_orbit
    http://www.physics.csbsju.edu/orbit/orbit.2d.html
    https://math.stackexchange.com/a/3711214
    """
    def process(self):
        for entity, (orbit, position, renderable) \
                in esper.get_components(Orbit,
                                        Position,
                                        Renderable):
            registry = Registry()
            # Add current position to dirty_rects and fill it with the background image
            extents = renderable.surface.get_size()
            old_rect = makeRect(
                position,
                Position(x=extents[0], y=extents[1])
            )
            registry.get("screen")\
                .blit(registry.get("background"),
                      (position.x, position.y),
                      old_rect)
            registry.get("dirty_rects").append(old_rect)

            # Set position to the calculated posiiton on the orbit elipse
            time = registry.get("time")
            x = orbit.semimajor_axis \
                * (cos((time/orbit.period)+orbit.true_anomaly) \
                   - orbit.eccentricity)
            y = orbit.semimajor_axis \
                * (1 - orbit.eccentricity**2)**0.5 \
                * sin((time/orbit.period)+orbit.true_anomaly)

            position.x = x * cos(orbit.argument_of_periapsis) \
                         - y * sin(orbit.argument_of_periapsis) \
                         + orbit.center.x
            position.y = x * sin(orbit.argument_of_periapsis) \
                         + y * cos(orbit.argument_of_periapsis) \
                         + orbit.center.y

            # Add new position to dirty_rects
            registry.get("dirty_rects").append(
                makeRect(
                    position,
                    Position(x=extents[0], y=extents[1]))
            )


class StarSystem:
    """A collection of planets and a star."""

    def __init__(self, star, planets: list):
        pass
