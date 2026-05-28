Entity(name="Dreadbear", maxHP=42, deck=[
        Card(name="Claw-claw", power=4, chances=2, powMod=5, cost=3),
        Card(name="Heavy brace", power=0, chances=4, powMod=6, isDefensive=True),
    ], AGT=-1, DEX=60, description=[
        "Radiation kills many, but life eventually finds a way.",
        "The ashes that once made the beasts of this realm wither away",
        "now grant them an amount of strength that is barely comparable",
        "to those that the old world's animals used to wield.",
        "",
        "This bear is undoubtedly an ugly one. Not a single strand of hair",
        "on it's face, not a single ounce of fat in it's belly. Only "
        "frostbitten skin wrapping around the bone below it."
    ], skin=art.dreadbear, pattern=[
        Pattern([1], "self.clock == 0"),
        Pattern([0], "self.clock == 1"),
    ]
)