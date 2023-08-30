from abc import ABC, abstractmethod


class Session:
    def __init__(self, dress: str) -> None:
        self.dress = dress

    @abstractmethod
    def render(self):
        raise NotImplementedError()


class StrengthSession(Session):
    def __init__(self, dress: str) -> None:
        super().__init__(dress)


class ESDSession(Session):
    def __init__(self, dress: str) -> None:
        super().__init__(dress)


class GPPSession(Session):
    def __init__(self, dress: str) -> None:
        super().__init__(dress)


class ELCSession(Session):
    def __init__(self, dress: str) -> None:
        super().__init__(dress)
