# audio jungle
Entity(name="Stellar servant", maxHP=30, ATK=0, AGT=3, deck=[
            Card("Impale", power=10, powMod=-5, chances=2, desc=[
                "> Inflict 3 bleed."
            ], attackScripts={"onHit": "card-scripts/puncture.atk", "onLose": ""}, cost=2),
            Card("Buttstroke", power=3, powMod=8, chances=1, desc=[
                "> Extend bleed duration",
                "  by 2.",
            ], attackScripts={"onHit": "card-scripts/needle.atk", "onLose": ""}, cost=2),
        ], description=[
            "In times of despiration people seem to lust for an answer for their problems,",
            "even if the answer lies way beyond what can be considered rational. By that of course,",
            "I mean religious answers. A particular owl-like fellow, notorious for his obsession towards the stars",
            "beyond the grey clouds, which are never to be seen again. He believes that once their light",
            "returns to us, we will live in a more peaceful world. His followers, blinded by the promise",
            "of a better world, are willing to yield anything to the high priest in order for this world to be born anew.",
            "",
            "Servants are not known for their grand combat experience and more often than not are just used as fodder, or sacrifices.",
        ], skin=art.stellar_servant, attackSlots=1, pattern=[
            Pattern([1], "self.clock == 0"),
            Pattern([0], "self.clock == 1"),
        ], maxStamina=1
    )   