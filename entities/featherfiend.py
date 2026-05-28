Entity(name="Featherfiend", maxHP=40, DEF=1, deck=[
        Card(name="Stealth", power=0, chances=1, powMod=1, attackScripts={"onHit": "card-scripts/stealth.atk", "onLose": "card-scripts/stealth.atk"}, desc=[
            "> Effects apply on",
            "  clash loss too.",
            "> Gain +3 ATK.",
            "> Gain 3 endurance."
        ], cost=2),
        Card(name="Beaks that bite", power=6, chances=1, powMod=6, attackScripts={"onHit": "card-scripts/beaks_that_bite.atk", "onLose": "card-scripts/beaks_that_bite_fail.atk"}, desc=[
            "> If there is no",
            "  bleed on the enemy,",
            "  apply 5 bleed.",
            "> If there is bleed",
            "  on the enemy, extend",
            "  their bleed by 1.",
        ], cost=2),
        Card(name="Claws that catch", power=4, chances=2, powMod=5, attackScripts={"onHit": "card-scripts/parry.atk", "onLose": ""}, desc=[
            "> If the target is",
            "  using an offensive",
            "  card, lower",
            "  the target's",
            "  AGT by 1."
        ]),
    ], AGT=2, DEX=50, description=[
        "Radiation kills many, but life eventually finds a way.",
        "The ashes that once made the beasts of this realm wither away",
        "now grant them an amount of strength that is barely comparable",
        "to those that the old world's animals used to wield.",
        "",
        "This one is an interesting fellow. It had learned the significance of disguise",
        "and mimicry as it began distorting from radiation. Upon further observation",
        "one may see that while it really is a cruel creature, it refuses to harm",
        "children or baby animals out of pure sympathy. Unfortunately for you, its sympathy",
        "does not extend to grown adults.",
    ], skin=art.featherfiend, attackSlots=2, pattern=[
        Pattern([0, 2], "self.clock == 1"),
        Pattern([2, 1], "self.clock == 2"),
        Pattern([2, 1], "self.clock == 0"),
    ]
)