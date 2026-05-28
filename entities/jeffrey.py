# audio jungle
Entity(name="Jeffrey Hidleton", maxHP=80, DEF=1, AGT=2, deck=[
            Card("Wings of the high priest", power=5, powMod=2, chances=5, desc=[ #39
                "\"Watch me fly!",
                "Watch me unite",
                "with the stars!\"",
                "",
                "> Gain 3 block.",
                "> All defensive",
                "  cards gain +3",
                "  power.",
            ], attackScripts={"onHit": "card-scripts/wothp.atk", "onLose": "card-scripts/wothp.atk"}, rarity=1, isDefensive=True),
            Card("Sacrifice", power=14, powMod=-2, chances=5, desc=[
                "If there are allies:",
                "> Kill an ally.",
                "> Gain 10 frenzy.",
                "",
                "If there are no allies:",
                "> Gain 3 bleed.",
                "> Gain 5 frenzy."
            ], attackScripts={"onHit": "card-scripts/sacrifice.atk"}, isDefensive=True),
            Card("Impale", power=6, powMod=6, chances=1, desc=[
                "> Inflict 3 bleed."
            ], attackScripts={"onHit": "card-scripts/puncture.atk"}, cost=5),
            Card("Go for the eyes", power=12, powMod=-6, chances=1, desc=[
                "> Inflict 1 bleed."
                "> Inflict 1",
                "  fragile for",
                "  each bleed",
                "  on target",
                "  (max 3).",
            ], attackScripts={"onHit": "card-scripts/go_for_the_eyes.atk"}, cost=5),
            Card("Dive", power=10, rarity=1, powMod=15, chances=1, desc=[
                "On clashing:",
                "> Gain 3 haste.",
                "> Gain 1 power",
                "  for each haste",
                "  on self (max 5).",
                "",
                "On hit:",
                "> Deal damage equal",
                "  to haste on self.",
                "> Gain shock",
                "  equal to haste",
                "  on self.",
                "> Clear all haste",
                "  on self.",
            ], attackScripts={"onHit": "card-scripts/dive.atk", "onClash": "card-scripts/dive_onclash.atk"}, cost=5),
        ], description=[
            "In times of despiration people seem to lust for an answer for their problems,",
            "even if the answer lies way beyond what can be considered rational. By that of course,",
            "I mean religious answers. A particular owl-like fellow, notorious for his obsession with the stars",
            "beyond the grey clouds, which are never to be seen again. He believes that once their light",
            "returns to us, we will live in a more peaceful world. His followers, blinded by the promise",
            "of a better world, are willing to yield anything to the high priest in order for this world to be born anew.",
            "",
            "Jeffrey Hidleton, the head of the Stellar cult, the one who was the first to praise these dots of light that",
            "shine upon us is the one you see before you. More owl than man, only human enough to preach to his",
            "priests and to judge the ones he deems sinful by the last spark of rational thought he has left in his",
            "head stuffed with lunacy and adoration towards a deity which may or may not exist.",
            "",
            "Judging by appearence, it's no wonder that many survivors of the war either feared or adored him.",
            "Many have more faith in their leader himself rather than the stars he believes in himself as a matter of fact.",
            "How could his huge eyes and wide wings not evoke the image of an angel in one's head after all?",
        ], skin=art.jeffrey, attackSlots=2, passives=[
            Passive(name="Lunacy", callingOrder=0, desc=[
                "Upon a successful attack, gain 2 frenzy.",
                "",
                "Upon a reaching 20 frenzy, change attack pattern.",
            ], effectScript="passive-scripts/lunacy.atk"),
            Passive(name="Flight", callingOrder=3, desc=[
                "Gain +1 AGT at the end of every turn.",
                "(Max 5)",
                "",
                "Upon reaching maximum haste, use a special attack.",
            ], effectScript="passive-scripts/flight.atk"),
        ], pattern=[
            # ULTIMATE
            Pattern([0, 4], "self.getEffect('Haste').count >= 5"),
            # SECOND PHASE
            Pattern([0, 3], "self.clock == 1 and self.getEffect('Frenzy').count >= 20"),
            Pattern([2, 3], "self.clock == 2 and self.getEffect('Frenzy').count >= 20"),
            Pattern([0, 2], "self.clock == 2 and self.getEffect('Frenzy').count >= 20"),
            # FIRST PHASE
            Pattern([0, 1], "self.clock == 1"),
            Pattern([1, 2], "self.clock == 2"),
            Pattern([0, 1], "self.clock == 0"),
        ]
    )