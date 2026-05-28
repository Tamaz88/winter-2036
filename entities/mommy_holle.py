Entity(name="Sixth sprite of Frau Holle", maxHP=180, deck=[
        Card("Warming up", power=6, powMod=6, chances=1, desc=[
            "A dynamo turns with",
            "each trust of this",
            "blade.",
            "> Effects apply on",
            "  clash loss too.",
            "> Gain 1 electric",
            "  charge.",
        ], attackScripts={"onHit": "card-scripts/charge_up.atk", "onLose": "card-scripts/charge_up.atk"}, cost=1),
        obtainableCards[12],
        Card("Tardrop", power=8, powMod=6, chances=2, desc=[
            "\"SHE WHO IS DEEMED",
            "TO BE A SINNER BY",
            "FRAU HOLLE SHALL BE",
            "DOUSED IN BOILING TAR!\"",
            "> Inflict 2 burn",
            "  for each electric",
            "  charge owned.",
        ], attackScripts={"onHit": "card-scripts/tardrop.atk", "onLose": ""}, cost=3),
    ], AGT=4, DEF=1, DEX=50, description=[
        "For each movemement, there exists an opposition. In the case of the Purists, seven of their most",
        "skilled knights and dames have left their ranks to protect the less fortunate mutants of the new world.",
        "",
        "The sixth sprite doesn't care much about protecting anyone. She views massacre as entertainment, often",
        "enjoying the thrill of combat even when she is on the losing side. While it can be said that she is not",
        "driven by the same words of a just world as her other six comrades, she does believe that her cruelty",
        "towards her targets is justified, as it is part of her quest to end villainy on a worldwide scale after all.",
        "She wields the shortsword Tardrop, which leaves terribly painful and deep burns all over one's body thanks",
        "to the electric current flowing through its blade.",
    ], skin=art.sixth_sprite, attackSlots=2, pattern=[
        Pattern([0, 0], "self.clock == 1"),
        Pattern([0, 1], "self.clock == 2"),
        Pattern([0, 2], "self.clock == 0"),
    ]
)