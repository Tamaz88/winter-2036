Entity(name="Purist acolyte", maxHP=35, ATK=1, AGT=2, deck=[
            Card("Sever", power=4, powMod=10, chances=1, desc=[
                "> Inflict 1 + 1 shock",
                "  for each",
                "  Electric charge in",
                "  the battle.",
            ], attackScripts={"onHit": "card-scripts/sever.atk", "onLose": ""}, cost=2),
            obtainableCards[1]
        ], description=[
            "In the ruins of far-gone cities, some refuse to change and keep holding onto their pure body",
            "seeing it as a virtue. In a city filled to the brim with impure filth, they don't tolerate even",
            "the tinyest sign of genetic distortion. Though this kind of hatred is now etched in an ideology",
            "that is in practice closer to being a religion than an actual political doctrine, it mostly",
            "stems from one of the most basic fears a human ever has to face: the distortion the natural body.",
            "",
            "Though in rank they are still squires, the acolytes are assigned the task of leading and protecting the",
            "squires under their command by their superior knight. They are only assigned this task for a short time",
            "before returning to their original position as mobile energy providers. Nevertheless, it is a great",
            "honor to bear the rank of acolyte.",
        ], skin=art.purist_acolyte, attackSlots=1, pattern=[
            Pattern([1], "self.clock == 0"),
            Pattern([0], "self.clock == 1"),
        ], maxStamina=3
    )