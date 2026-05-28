# audio jungle
Entity(name="Child of the stars", maxHP=80, DEF=1, AGT=1, deck=[
            Card("Wings of a child", power=5, powMod=2, chances=5, desc=[ #39
                "\"I shall fly!",
                "I shall unite",
                "with the stars!\"",
                "",
                "> Gain 2 block.",
                "> All defensive",
                "  cards gain +1",
                "  power.",
            ], attackScripts={"onHit": "card-scripts/woac.atk", "onLose": "card-scripts/woac.atk"}, rarity=1, isDefensive=True),
            Card("Sacrifice", power=14, powMod=-2, chances=5, desc=[
                "If there are allies:",
                "> Kill an ally.",
                "> Gain 10 frenzy.",
                "",
                "If there are no allies:",
                "> Gain 3 bleed.",
                "> Gain 5 frenzy."
            ], attackScripts={"onHit": "card-scripts/sacrifice.atk", "onLose": ""}, isDefensive=True),
            Card("Impale", power=12, powMod=-6, chances=1, desc=[
                "> Inflict 3 bleed."
            ], attackScripts={"onHit": "card-scripts/puncture.atk", "onLose": ""}, cost=5),
        ], description=[
            "In times of despiration people seem to lust for an answer for their problems,",
            "even if the answer lies way beyond what can be considered rational. By that of course,",
            "I mean religious answers. A particular owl-like fellow, notorious for his obsession towards the stars",
            "beyond the grey clouds, which are never to be seen again. He believes that once their light",
            "returns to us, we will live in a more peaceful world. His followers, blinded by the promise",
            "of a better world, are willing to yield anything to the high priest in order for this world to be born anew.",
            "",
            "Children of the stars are high ranking stellar priests, too valuable to be used as fodder or sacrifice.",
            "They are the subordinates of the High priest, spreading his word wherever they go and collecting",
            "only the finest sacrifices for him and the stars with great zeal.",
        ], skin=art.high_priest, attackSlots=2, passives=[
            Passive(name="Flight", callingOrder=3, desc=[
                "Gain +1 AGT at the end of every turn."
                "(Max 5)"
            ], effectScript="passive-scripts/flight.atk")
        ], pattern=[
            Pattern([0, 2], "self.clock == 1"),
            Pattern([1, 2], "self.clock == 2"),
            Pattern([0, 1], "self.clock == 0"),
        ]
    )   