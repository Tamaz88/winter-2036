Entity(name="The Listener", maxHP=110, DEX=50, deck=[
            Card("Smackdown", power=8, chances=1, powMod=7, desc=[
                "\"JUST SHUT UP!\"",
                "> Inflict 4 shock.",
                "> Gains 1 block."
            ], attackScripts={"onHit": "card-scripts/smackdown.atk", "onLose": ""}, cost=3),
            Card("Rib breaker", power=5, chances=2, powMod=3, desc=[
                "\"ENOUGH! ENOUGH!\"",
                "> Inflict 2 shock."
            ], attackScripts={"onHit": "card-scripts/blunt_trauma.atk", "onLose": ""}, cost=1),
            Card("Low sweep", power=4, chances=2, powMod=4, desc=[
                "\"STOP! HALT!\"",
                "> Inflict 2 shock.",
                "> Inflict 1 constriction."
            ], attackScripts={"onHit": "card-scripts/low_sweep.atk", "onLose": ""}, cost=2),
            Card("Ease the pain", power=0, chances=2, powMod=8, desc=[
                "\"IT HURTS! IT HURTS!\"",
                "> Effects apply on",
                "  clash loss too.",
                "> Gain 20 focus.",
                "> Takes 5 damage."
            ], attackScripts={"onHit": "card-scripts/ease_pain.atk", "onLose": "card-scripts/ease_pain.atk"}, isDefensive=True),
            Card("Parry", power=0, chances=4, powMod=4, desc=[
                "> If the target is",
                "  using an offensive",
                "  card, lower",
                "  the target's",
                "  AGT by 1."
            ], attackScripts={"onHit": "card-scripts/parry.atk", "onLose": ""}, isDefensive=True),
        ], AGT=1, description=[
            "A starved frame of a naked old man, barely having any fat around it's",
            "seemingly fragile bones. Antenna-like spires of lead and bone strech out",
            "from his head proudly. In his right hand, he wields a slightly bent copper pipe.",
            "",
            "As you approach him, he screeches continuously, his head twiching",
            "in many directions like a radar looking for a signal.",
            "He is however, not looking for any signal at all. He wants all the signals to",
            "be gone from his head. Each and every ray of radiation is agonizing",
            "for him to hear as a deafening noise, thanks to his antennae growing out of his head.",
            "He has to continuously strike his own head with a copper pipe to relieve the immense pain",
            "that he has to endure because of his condition."
        ], skin=art.the_listener, attackSlots=3, pattern=[
            Pattern([3, 2, 2], "self.clock == 1"),
            Pattern([3, 0, 1], "self.clock == 2"),
            Pattern([4, 1, 0], "self.clock == 3"),
            Pattern([3, 3, 0], "self.clock == 0"),
        ], maxStamina=6
    )