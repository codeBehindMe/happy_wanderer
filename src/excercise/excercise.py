from typing import Dict


class Excercise:
    def __init__(self, name: str) -> None:
        self.name: str = name


class StrengthExcercise(Excercise):
    def __init__(
        self,
        name: str,
        sets: int,
        reps: int,
        rest: int,
        weight: int = None,
        low: float = None,
        high: float = None,
    ) -> None:
        super().__init__()
        self.name = name
        self.sets: int = sets
        self.reps: int = reps
        self.weight: int = weight
        self.rest: int = rest
        self.low = low
        self.high = high


class ESDExcercise(Excercise):
    def __init__(self, name: str, mhr: float, sets: int, rest: int) -> None:
        super().__init__(name)
        self.mhr = mhr
        self.sets = sets
        self.rest = rest


class GPPExcercise(Excercise):
    def __init__(self, name: str) -> None:
        super().__init__(name)


class BaselineTestExcercise(Excercise):
    def __init__(self, name: str) -> None:
        super().__init__(name)


def test_factory():
    raise NotImplementedError()


def str_excercise_factory(d: Dict):
    raise NotImplementedError()


EXCERCISE_FACTORY_FUNCTION_SWITCH = {"TEST": test_factory, "STR": str_excercise_factory}


def excercise_factory(excercise_dict: Dict) -> Excercise:
    kind = excercise_dict["kind"]
