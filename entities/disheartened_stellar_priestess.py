# audio jungle
Entity(name="Disheartened priestess", maxHP=55, ATK=1, AGT=3, deck=[
            Card("Counter", power=2, powMod=5, chances=3, desc=[
                "> Effects apply on",
                "  clash loss too.",
                "> Deal 5 damage.",
            ], attackScripts={"onHit": "card-scripts/counter.atk", "onLose": "card-scripts/counter.atk"}, isDefensive=True),
            Card("Broken Chant", power=12, powMod=-2, chances=4, desc=[
                "> Deal +5 damage",
                "  for every 15 HP",
                "  lost."
            ], attackScripts={"onHit": "card-scripts/broken_chant.atk", "onLose": ""}, cost=3),
        ], description=[
            "In times of despiration people seem to lust for an answer for their problems,",
            "even if the answer lies way beyond what can be considered rational. By that of course,",
            "I mean religious answers. A particular owl-like fellow, notorious for his obsession towards the stars",
            "beyond the grey clouds, which are never to be seen again. He believes that once their light",
            "returns to us, we will live in a more peaceful world. His followers, blinded by the promise",
            "of a better world, are willing to yield anything to the high priest in order for this world to be born anew.",
            "",
            "She has lost her faith, and that's partially your fault.",
        ], skin=art.stellar_priest, attackSlots=2, pattern=[
            Pattern([1, 1], "self.health < self.maxHealth/2"),
            Pattern([0, 0], "self.clock == 0"),
            Pattern([0, 1], "self.clock == 1"),
        ]
    )   