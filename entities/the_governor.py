Entity(name="The Governor", maxHP=150, DEF=1, ATK=1, deck=[
            Card("Struggle", power=16, powMod=-12, chances=1, desc=[
                "> Inflict 2",
                "  fragile.",
                "> Lose 5",
                "  momentum.",
            ], attackScripts={"onHit": "card-scripts/struggle.atk", "onLose": ""}),
            Card("Tail sweep", power=8, powMod=-3, chances=2, desc=[
                "> Inflict 2",
                "  clumsy.",
            ], attackScripts={"onHit": "card-scripts/tail_sweep.atk", "onLose": ""}),
            Card("Reinforce", power=16, powMod=-3, chances=4, desc=[
                "> Gain 1 block.",
            ], isDefensive=True, attackScripts={"onHit": "card-scripts/chitin_guard.atk", "onLose": ""}),
            obtainableCards[3]
        ], description=[
            "goo goo ga ga",
            "goo goo ga gaaa",
        ], skin=art.the_governor, attackSlots=3)