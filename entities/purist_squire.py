Entity(name="Purist squire", maxHP=30, ATK=1, AGT=1, maxStamina=1, deck=[
            Card("Charge up", power=5, chances=3, powMod=3, desc=[
                "> Gain 1",
                "  Electric charge"
            ], attackScripts={"onHit": "card-scripts/charge_up.atk", "onLose": ""}, isDefensive=True),
            obtainableCards[0]
        ], description=[
            "In the ruins of far-gone cities, some refuse to change and keep holding onto their pure body",
            "seeing it as a virtue. In a city filled to the brim with impure filth, they don't tolerate even",
            "the tinyest sign of genetic distortion. Though this kind of hatred is now etched in an ideology",
            "that is in practice closer to being a religion than an actual political doctrine, it mostly",
            "stems from one of the most basic fears a human ever has to face: the distortion the natural body.",
            "",
            "Equipped mostly with simple melee weapons, the purist squires of Bucharest carry energy reserves",
            "for their masters, who are basically dependent on said reserves when using their weapons.",
            "They produce energy mostly by diesel generators that are attached to their backs, and are",
            "constantly required to be in the direct proximity of the knight they serve.",
        ], skin=art.purist_squire, attackSlots=1, pattern=[
            Pattern([1], "self.clock == 0"),
            Pattern([0], "self.clock == 1"),
        ]
    )