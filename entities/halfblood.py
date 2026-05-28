Entity(name="Halfblood", maxHP=50, DEF=1, ATK=2, AGT=1, maxStamina=3, deck=[
            obtainableCards[4],
            obtainableCards[8],
            obtainableCards[18],
            obtainableCards[13]
        ], description=[
            "In the ruins of far-gone cities, some people are able to survive even in such a",
            "harsh enviroment. They constantly patrol the streets for food, and in desperate times",
            "the term \"food\" might be broad enough to include other humans.",
            "",
            "The halfblood are much more adaptive, and oftentimes gain mutations that help them",
            "during combat. They aren't that useful outside of combat though, as said mutations often",
            "come with severe disabilities in speech, thinking or movement, reducing them to nothing",
            "but a walking arsenal of teeth, limbs and tentacles."
        ], skin=art.halfblood, attackSlots=2, pattern=[
            Pattern([0, 1], "self.clock == 1"),
            Pattern([0, 3], "self.clock == 2"),
            Pattern([1, 2], "self.clock == 0"),
        ]
    )