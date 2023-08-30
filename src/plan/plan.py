from typing import List


class Day:
    def __init__(self, day_number: int) -> None:
        self.day_number: int = day_number


class Week:
    def __init__(self, week_number: int) -> None:
        self.week_number: int = week_number
        self.days: List[Day] = []


class Plan:
    def __init__(self) -> None:
        start_date: str = None  # FIXME
        end_date: str = None  # FIXME
        self.weeks: List[Week] = []
