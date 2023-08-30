class Excercise:
    def __init__(self, name: str) -> None:
        self.name: str = name


class StrengthExcercise(Excercise):
    def __init__(self, name: str, sets: int, reps: int, weight: int, rest: int) -> None:
        super().__init__()
        self.name = name
        self.sets: int = sets
        self.reps: int = reps
        self.weight: int = weight
        self.rest: int = rest


class ESDExcercise(Excercise):
    def __init__(self, name: str, mhr: float, sets: int, rest: int) -> None:
        super().__init__(name)
        self.mhr = mhr
        self.sets = sets
        self.rest = rest


class GPPExcercise(Excercise):
    def __init__(self, name: str) -> None:
        super().__init__(name)
