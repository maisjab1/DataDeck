from abc import ABC, abstractmethod
from typing import cast

from ex0.creature import Creature
from ex1.heal import HealCapability
from ex1.transform import TransformCapability


class InvalidStrategyError(Exception):
    pass


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass

    @abstractmethod
    def act(self, creature: Creature) -> None:
        pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> None:
        print(creature.attack())


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            creature_name = creature.__class__.__name__
            creature_name = creature_name.replace("creature", " ")
            raise InvalidStrategyError(
                f"Invalid creature '{creature_name}' for "
                f"this Aggressive Strategy")
        c = cast(TransformCapability, creature)
        print(c.transform())
        print(creature.attack())
        print(c.revert())


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            creature_name = creature.__class__.__name__
            creature_name = creature_name.replace("creature", " ")
            raise InvalidStrategyError(
                f"Invalid creature '{creature_name}' for "
                f"this Defensive Strategy")
        c = cast(HealCapability, creature)
        print(creature.attack())
        print(c.heal())
