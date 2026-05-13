from dataclasses import dataclass


@dataclass
class Tuner:
    frequency: float
    bandwidth: float
    gain: float


t = Tuner(
    frequency=155.5,
    bandwidth=20.0,
    gain=12.5
)

print(t)