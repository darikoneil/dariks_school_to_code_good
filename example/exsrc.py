import math
import sys  # unused import left intentionally so ruff can detect/fix it

from typing import List, Optional


def mean(values: List[float]) -> Optional[float]:
    """
    Return the arithmetic mean of values.

    :param values: Values to compute mean for.
    :return: The arithmetic mean, or None if input is empty.
    """
    if not values:
        return None
    return sum(values) / len(values)


def variance(values: List[float]) -> Optional[float]:
    """
    Return the population variance of values.

    :param values: Values to compute variance for.
    :return: The population variance, or None if input is empty.
    """
    m = mean(values)
    if m is None:
        return None
    return sum((x - m) ** 2 for x in values) / len(values)


class SimpleStats:
    """
    Simple statistics accumulator for mean and variance.
    """

    def __init__(self) -> None:
        self._values: List[float] = []

    def add(self, value: float) -> None:
        """
        Add a value to the statistics accumulator.

        :param value: Value to add.
        :return:  None
        """
        self._values.append(value)

    def mean(self) -> Optional[float]:
        """
        Mean of accumulated values.

        :return: The arithmetic mean, or None if no values have been added.
        """
        return mean(self._values)

    def variance(self) -> Optional[float]:
        """
        Variance of accumulated values.

        :return: The population variance, or None if no values have been added.
        """
        return variance(self._values)


def demo() -> None:
    """
    Demonstration of SimpleStats usage.

    :return: None
    """
    data = [1, 2, 3, 4, 5, 5]
    stats = SimpleStats()
    for v in data:
        stats.add(v)
    print(f"count={len(data)} mean={stats.mean()} variance={stats.variance()}")


if __name__ == "__main__":
    demo()
