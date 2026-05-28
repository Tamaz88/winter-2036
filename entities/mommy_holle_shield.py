Entity(name="The Listening shield", maxHP=50, deck=[
        Card("Simple Guard", power=4, powMod=4, chances=3, desc=[
            "> Effects apply on",
            "  clahs loss too.",
            "> Apply 5 endurance",
            "  to your owner.",
            "> Apply 1 block",
            "  to your owner.",
        ], attackScripts={"onHit": "card-scripts/simple_guard.atk", "onLose": "card-scripts/simple_guard.atk"}, isDefensive=True),
        Card("Tremor drain", power=4, powMod=4, chances=3, desc=[
            "> Remove 2 shock from",
            "  your owner.",
        ], attackScripts={"onHit": "card-scripts/tremor_drain.atk", "onLose": ""}, isDefensive=True),
    ], DEX=50, AGT=99, description=[
        "The shield of the sixth sprite of Frau Holle, orenated by the skull of a listening deer.",
        "It is quite durable, and",
    ], skin=art.holle_shield, attackSlots=1, pattern=[
        Pattern([1], "self.clock == 1"),
        Pattern([0], "self.clock == 0"),
    ]
)