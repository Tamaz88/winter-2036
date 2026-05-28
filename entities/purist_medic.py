Entity(name="Purist medic", maxHP=70, ATK=1, AGT=2, deck=[
            Card("Excisio", power=6, powMod=4, chances=2, desc=[
                "> Deal 1 additional",
                "  damage for every 2",
                "  cards in your deck."
            ], attackScripts={"onHit": "card-scripts/purify.atk", "onLose": ""}, cost=2),
            Card("Surgical precision", power=8, powMod=4, chances=2, desc=[
                "> Gain +2 ATK."
            ], attackScripts={"onHit": "card-scripts/precision.atk", "onLose": ""}),
            obtainableCards[1]
        ], description=[
            "In the ruins of far-gone cities, some refuse to change and keep holding onto their pure body",
            "seeing it as a virtue. In a city filled to the brim with impure filth, they don't tolerate even",
            "the tinyest sign of genetic distortion. Though this kind of hatred is now etched in an ideology",
            "that is in practice closer to being a religion than an actual political doctrine, it mostly",
            "stems from one of the most basic fears a human ever has to face: the distortion the natural body.",
            "",
            "By the nature of being a paramilitary organization, the purist order does tend to suffer quite many",
            "casualities and injuries on the battlefield. The medic's more obvious role is of course, treating",
            "their injured brothers' wounds. The less obvious one is being a sort of inquisitor, looking for",
            "the most minimal signs of impurity on each and every patient.",
            "Of course if any mutated tissue is found in a poor squire, they are getting executed on the spot",
            "without any doubt.",
        ], skin=art.purist_acolyte, attackSlots=2, pattern=[
            Pattern([2, 0], "self.clock == 0"),
            Pattern([2, 1], "self.clock == 1"),
        ], maxStamina=3
    )