Entity(name="Ironstork", maxHP=20, deck=[
        Card(name="Puncture", power=1, chances=1, powMod=7, attackScripts={"onHit": "card-scripts/puncture.atk", "onLose": ""}, desc=[
            "Apply 3 bleed."
        ], cost=2),
        Card(name="Short flight", power=0, chances=5, powMod=2, isDefensive=True)
    ], AGT=3, DEX=60, description=[
        "Radiation kills many, but life eventually finds a way.",
        "The ashes that once made the beasts of this realm wither away",
        "now grant them an amount of strength that is barely comparable",
        "to those that the old world's animals used to wield.",
        "",
        "A stork with a heavy, reinforced beak. It's beak is so heavy infact",
        "that the bird is unable to fly long distances, but it can and",
        "probably will deliver a deadly blow."
    ], skin=art.ironstork, pattern=[
        Pattern([1], "self.clock == 0"),
        Pattern([0], "self.clock == 1"),
    ]
)