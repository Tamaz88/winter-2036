Entity(name="Purist knight", maxHP=60, DEF=2, ATK=1, maxStamina=2, deck=[
            Card("Rip...", power=6, powMod=4, chances=2, desc=[
                "> On hit, replace",
                "  this card with",
                "  \"...and tear\""
            ], attackScripts={"onHit": "card-scripts/rip_and_tear1.atk", "onLose": ""}, cost=2),
            Card("Taunt", power=2, powMod=2, chances=5, desc=[
                "> Reduce hand draw",
                "  by 2 for the next",
                "  turn."
            ], attackScripts={"onHit": "card-scripts/taunt.atk", "onLose": ""}, isDefensive=True),
            Card("Disarm & purify", power=6, powMod=4, chances=2, desc=[
                "> Deal 1 additional",
                "  damage for every 2",
                "  cards in your deck."
            ], attackScripts={"onHit": "card-scripts/purify.atk", "onLose": ""}, cost=2)
        ], description=[
            "In the ruins of far-gone cities, some refuse to change and keep holding onto their pure body",
            "seeing it as a virtue. In a city filled to the brim with impure filth, they don't tolerate even",
            "the tinyest sign of genetic distortion. Though this kind of hatred is now etched in an ideology",
            "that is in practice closer to being a religion than an actual political doctrine, it mostly",
            "stems from one of the most basic fears a human ever has to face: the distortion the natural body.",
            "",
            "Armed with chainsaws powered by electricity and guarded by some light armor, the purist knights of Bukarest",
            "are the core of the purist inquisition, wishing to restore order in the new, ever frozen world.",
            "Their titles - as opposed to medieval knights - not given by a greater authority, but are granted by",
            "the will of their fellow squires and other knights who deem them worthy of bearing their saw and",
            "holding their shields in their sacred mission to purify mankind once more.",
        ], skin=art.purist_knight, attackSlots=2, pattern=[
            Pattern([1, 0], "self.clock == 0"),
            Pattern([1, 0], "self.clock == 1"),
            Pattern([2, 0], "self.clock == 1"),
        ]
    )