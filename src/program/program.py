from typing import Dict, List


class Day:
    def __init__(self, day_number: int, kind: str) -> None:
        self.day_number: int = day_number
        self.kind = kind


class Week:
    def __init__(self, week_number: int, kind: str) -> None:
        self.week_number: int = week_number
        self.kind: str = kind
        self.days: List[Day] = []


class Plan:
    def __init__(self) -> None:
        start_date: str = None  # FIXME
        end_date: str = None  # FIXME
        self.weeks: List[Week] = []

    def add_week(self, w: Week):
        self.weeks.append(w)


def program_factory(d: Dict):
    week: Week
    for week in d["program"]["weeks"]:
        w = Week(week["num"], week["kind"])

        day: Dict
        for day in week["days"]:
            d = Day(day["num"], day["kind"])

            excercise: Dict
            for excercise in day["excercises"]:
                pass
