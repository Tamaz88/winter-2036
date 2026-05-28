Entity(name="Rayelk", maxHP=35, deck=[
        Card(name="Headbutt", power=4, chances=2, powMod=3, cost=2), 
        Card(name="Antler charge", power=10, chances=1, powMod=-8, cost=3)
    ], AGT=1, description=[
        "Radiation kills many, but life eventually finds a way.",
        "The ashes that once made the beasts of this realm wither away",
        "now grant them an amount of strength that is barely comparable",
        "to those that the old world's animals used to wield.",
        "",
        "The rayelk's antlers are much larger compared to it's ancestors.",
        "Even though the radiation caused them to have a large deficit in bodyfat",
        "percentage, their mass is still great enough to deal a crushing blow to whatever",
        "they hit."
    ], skin=art.rayelk, pattern=[
        Pattern([1], "self.clock == 0"),
        Pattern([0], "self.clock == 1"),
    ], maxStamina=1
)