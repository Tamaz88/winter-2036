Entity(name="Listening deer", maxHP=75, deck=[
            Card(name="Brutal charge", power=10, chances=1, powMod=-8, desc=["> Inflict 2", "  shock."], attackScripts={"onHit": "card-scripts/blunt_trauma.atk", "onLose": ""}, cost=2),
            Card(name="Await", power=6, chances=3, powMod=2, desc=["> Effects only", "  apply on", "  clash loss.", "> Inflict 2", "  shock."], attackScripts={"onHit": "", "onLose": "card-scripts/blunt_trauma.atk"}, isDefensive=True),
            Card(name="Bash and tear", power=10, chances=1, powMod=-8, desc=[
                "> Inflict 2",
                "  shock.",
                "> Deal 1 additional",
                "  damage for each",
                "  shock on the",
                "  target."
            ], attackScripts={"onHit": "card-scripts/bash_and_tear.atk", "onLose": ""}, cost=3)
        ], AGT=2, DEX=50, description=[
            "In this hostile enviroment, some animals are forced to form",
            "more or less equal relationships with eachother, be it parasitic",
            "or symbiotic.",
            "",
            "The antennae on the beast's head sense all radiation as terrible, deafening",
            "noise, causing it a constant headache, for which to cease it oftentimes",
            "charges into trees, rocks, or other creatures (such as you) aggressively."
        ], skin=art.listening_deer, pattern=[
            Pattern([0], "self.clock == 0"),
            Pattern([1], "self.clock == 1"),
            Pattern([1], "self.clock == 2"),
            Pattern([2], "self.clock == 3"),
        ], maxStamina=3
    )