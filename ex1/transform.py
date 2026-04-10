from abc import ABC, abstractmethod


class TransformCapability (ABC):
    def __init__(self):
        self.transformed = False

    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass
