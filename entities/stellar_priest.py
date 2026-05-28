# audio jungle
Entity(name="Stellar priest", maxHP=45, DEF=1, AGT=1, deck=[
            Card("Counter", power=2, powMod=5, chances=3, desc=[
                "> Effects apply on",
                "  clash loss too.",
                "> Deal 5 damage.",
            ], attackScripts={"onHit": "card-scripts/counter.atk", "onLose": "card-scripts/counter.atk"}, isDefensive=True),
            Card("Chant", power=10, powMod=-2, chances=4, desc=[
                "> Deal +2 damage",
                "  for each ally."
            ], attackScripts={"onHit": "card-scripts/chant.atk", "onLose": ""}, cost=3),
        ], description=[
            "In times of despiration people seem to lust for an answer for their problems,",
            "even if the answer lies way beyond what can be considered rational. By that of course,",
            "I mean religious answers. A particular owl-like fellow, notorious for his obsession towards the stars",
            "beyond the grey clouds, which are never to be seen again. He believes that once their light",
            "returns to us, we will live in a more peaceful world. His followers, blinded by the promise",
            "of a better world, are willing to yield anything to the high priest in order for this world to be born anew.",
            "",
            "Priests are the most zealous of servants, who are competent and devoted enough to speak for the stars in",
            "the name of the High priest. They make the best sacrifices too.",
        ], skin=art.stellar_priest, attackSlots=1, pattern=[
            Pattern([1], "self.clock == 0"),
            Pattern([0], "self.clock == 1"),
        ], maxStamina=1
    )   