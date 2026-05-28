Entity(name="Grandfather", maxHP=10000, ATK=20, AGT=-2, deck=[
            Card("Reload", power=0, chances=4, powMod=6, attackScripts={"onHit": "", "onLose": ""}, isDefensive=True),
            Card("Dandy shotgun", power=3, chances=3, powMod=3, desc=[
                "> Inflict 1",
                "  fragile."
            ], attackScripts={"onHit": "card-scripts/knights_saw.atk", "onLose": ""}, isRanged=True),
            obtainableCards[18]
        ], description=[
            "An old man with a trench coat resembling that of a socialist hungarian solider from the cold war.",
            "He wields an awfully outdated but still well-maintained shotgun and an old combat knife.",
            "His eyes are covered by an old cap of the Hungarian People's Army, (again a relic of the past)",
            "making each and every one of his expressions as enigmatic as possible.",
            "Though his old fashioned attire is quite a strange sight in itself, the truly alarming detail is",
            "the parasite nested atop of his heart, silently and insidiously spying with its little",
            "chitin-covered tentacles as the man goes by with his tasks.",
            "The grandfather seems to posess significant physical strength, possibly due to the presence of the",
            "parasite.",
        ], skin=art.grandfather, attackSlots=2, pattern=[
            Pattern([1, 2], "self.clock == 0"),
            Pattern([0, 2], "self.clock == 1"),
        ]
    )