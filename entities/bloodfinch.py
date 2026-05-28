Entity(name="Bloodfinch", maxHP=10, deck=[
        Card(name="Rip wound", power=4, chances=1, powMod=3, attackScripts={"onHit": "card-scripts/rip_wound.atk", "onLose": ""}, isRanged=True, desc=[
            "Apply 1 bleed.",
            "Extend bleed duration",
            "by 2."
        ], cost=5),
        Card(name="Flight", power=0, chances=5, powMod=4, desc=[
            "Gain +1 AGT."
        ], attackScripts={"onHit": "card-scripts/reflex.atk", "onLose": ""}, isDefensive=True)
    ], AGT=2, DEX=65, description=[
        "Radiation kills many, but life eventually finds a way.",
        "The ashes that once made the beasts of this realm wither away",
        "now grant them an amount of strength that is barely comparable",
        "to those that the old world's animals used to wield.",
        "",
        "Unlike almost everything else in this forest, the tiny bloodfinch",
        "looks way too pure to belong in such a cruel and unforgiving world.",
        "The price for it's beauty is payed by it's prey, however. Blood keeps",
        "the tiny bird flying and forever beautiful. Let it starve, and its",
        "beauty withers in no time."
    ], skin=art.bloodfinch, pattern=[
        Pattern([1], "self.clock == 0"),
        Pattern([0], "self.clock == 1"),
    ], maxStamina=3
)