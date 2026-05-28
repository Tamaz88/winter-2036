Entity(name="Alpha raywolf", maxHP=65, deck=[
        Card(name="Strong bite", power=6, powMod=6, chances=1, cost=2),
        Card(name="Howl", power=6, chances=2, powMod=4, desc=[
            "> Effects apply on",
            "  clash loss too.",
            "> Gain 5 bravery.",
            "> Apply 1 clumsy."
        ], attackScripts={"onHit": "card-scripts/howl.atk", "onLose": "card-scripts/howl.atk"}, isDefensive=True)
    ], description=[
    "Radiation kills many, but life eventually finds a way.",
    "The ashes that once made the beasts of this realm wither away",
    "now grant them an amount of strength that is barely comparable",
    "to those that the old world's animals used to wield.",
    "",
    "The raywolf, though still covered in boils from the radiation,",
    "has adapted for survival in this harsh enviroment.",
    "It's almost twice the size of an old wolf, standing at waist-hight."
    ], skin=art.alpha_raywolf, attackSlots=2, pattern=[
        Pattern([0, 0], "self.clock == 1"),
        Pattern([0, 1], "self.clock == 0"),
    ], maxStamina=3
)