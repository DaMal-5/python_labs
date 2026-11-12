import math

class StationStats:

    __slots__ = ("_min", "_max", "_sum", "_count")

    def __init__(self, value: float) -> None:
        self._min = value
        self._max = value
        self._sum = value
        self._count = 1

    @property
    def min(self) -> float:
        return self._min

    @property
    def max(self) -> float:
        return self._max

    @property
    def sum(self) -> float:
        return self._sum

    @property
    def count(self) -> int:
        return self._count

    @property
    def avg(self) -> float:
        avg = self._sum / self._count
        rounded_avg = math.floor(avg * 10 + 0.5) / 10
        return rounded_avg

    def update(self, value: float) -> None:
        if value < self._min:
            self._min = value
        if value > self._max:
            self._max = value
        self._sum += value
        self._count += 1

    def merge(self, other: "StationStats") -> None:
        if other._min < self._min:
            self._min = other._min
        if other._max > self._max:
            self._max = other._max
        self._sum += other._sum
        self._count += other._count

    def __repr__(self) -> str:
        return f"{self.min:.1f};{self.avg:.1f};{self.max:.1f}"