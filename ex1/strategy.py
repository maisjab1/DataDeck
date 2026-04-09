from abc import ABC, abstractmethod


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid() -> bool:
        pass

    @abstractmethod
    def act():
        pass


class NormalStrategy(BattleStrategy):
       
    def is_valid() -> bool:
        pass

    def act():
        pass


class AggressiveStrategy(BattleStrategy):
    def is_valid() -> bool:
        pass

    def act():
        pass


class DefensiveStrategy(BattleStrategy):
    def is_valid() -> bool:
        pass
    
    def act():
        pass
