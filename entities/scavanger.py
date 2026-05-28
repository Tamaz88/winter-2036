Entity(name="Scavanger", maxHP=20, DEF=1, ATK=1, AGT=1, deck=[
            Card(name="Crowbar strike", power=6, powMod=6, chances=1, cost=1),
            Card("Counter", power=2, powMod=5, chances=3, desc=[
                "> Effects apply on",
                "  clash loss too.",
                "> Deal 5 damage.",
            ], attackScripts={"onHit": "card-scripts/counter.atk", "onLose": "card-scripts/counter.atk"}, isDefensive=True),
            Card(name="Pistol shot",  power=4, chances=1, powMod=6, isRanged=True, cost=2)
        ], description=[
            "In the ruins of far-gone cities, some people are able to survive even in such a",
            "harsh enviroment. They constantly patrol the streets for food, and in desperate times",
            "the term \"food\" might be broad enough to include other humans.",
            "",
            "The lowest of the low, the scavangers are the ones who are only granted cancer",
            "for their efforts of survival in this radioactive hellhole. They are mostly fragile",
            "and weak."
        ], skin=art.scavanger, attackSlots=2, pattern=[
            Pattern([1, 2], "self.clock == 0"),
            Pattern([0, 1], "self.clock == 1"),
        ], maxStamina=2
    )