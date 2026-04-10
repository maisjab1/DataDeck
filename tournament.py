from ex0 import FlameFactory, AquaFactory
from ex0.factory import CreatureFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import NormalStrategy, AggressiveStrategy, DefensiveStrategy
from ex2.strategy import BattleStrategy, InvalidStrategyError


def tournament(name: str, opp: list[tuple[CreatureFactory, BattleStrategy]]):
    print(name)
    display = []
    for f, s in opp:
        fname = f.__class__.__name__.replace("Factory", "")
        sname = s.__class__.__name__.replace("Strategy", "")
        display.append(f"({fname}+{sname})")
    print("[ " + ", ".join(display) + " ]")
    print("** Tournament **")
    print(f"{len(opp)} opp involved")
    for i in range(len(opp)):

        for j in range(i + 1, len(opp)):
            factory1, strategy1 = opp[i]
            factory2, strategy2 = opp[j]
            c1 = factory1.create_base()
            c2 = factory2.create_base()
            print("\n--- Battle ---")
            print(c1.describe())
            print("vs.")
            print(c2.describe())
            print("now fight!")
            try:
                strategy1.act(c1)
            except InvalidStrategyError as e:
                print(f"Battle Error, aborting tournament: {e}")
            try:
                strategy2.act(c2)
            except InvalidStrategyError as e:
                print(f"Battle Error, aborting tournament: {e}")


if __name__ == "__main__":

    t0 = [
        (FlameFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
    ]

    t1 = [
        (FlameFactory(), AggressiveStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
    ]

    t2 = [
        (AquaFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
        (TransformCreatureFactory(), AggressiveStrategy()),
    ]

    tournament("Tournament 0 (basic)", t0)
    print()
    tournament("Tournament 1 (error)", t1)
    print()
    tournament("Tournament 2 (multiple)", t2)
