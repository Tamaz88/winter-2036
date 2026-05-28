Entity(name="Injured purist squire", maxHP=15, ATK=0, AGT=-1, maxStamina=1, deck=[
            obtainableCards[1],
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
            "Since they are subject to radiation as much as any other organic being, squires may gain muatations.",
            "Those who are less faithful simply leave, never to be seen again, since they know that even the most",
            "subtle mutations can get them executed on spot.",
            "Those who have an unyielding faith however, get rid of the impurities themselves, thus proving that",
            "their mind is still pure. These ones are oftentimes limping for days or weeks after the removal of a",
            "mutation, depending on the size of the affected tissue. They are of course not required to carry generators.",
        ], skin=art.injured_purist_squire, attackSlots=1, pattern=[
        Pattern([1], "self.clock == 0"),
        Pattern([0], "self.clock == 1"),
    ]
    )