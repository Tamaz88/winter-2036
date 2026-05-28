Entity(name="Hivedeer", maxHP=70, deck=[
            Card(name="Swarm", power=6, chances=4, powMod=2, desc=["> Summons an ant", "  swarm."], attackScripts={"onHit": "card-scripts/swarm.atk", "onLose": ""}, isDefensive=True),
            Card(name="Antler charge", power=10, chances=1, powMod=-8, cost=3)
        ], AGT=-2, DEX=50, description=[
            "In this hostile enviroment, some animals are forced to form",
            "more or less equal relationships with eachother, be it parasitic",
            "or symbiotic.",
            "",
            "The hivedeer is a prime example of this behaviour. Millions of ants",
            "live inside it's body, constantly crawling underneath it's hide and skin.",
            "The deer is kept safe from any one of the many parasites",
            "in this forest, while the ants recieve protection from the elements."
        ], skin=art.hivedeer, pattern=[
            Pattern([1], "self.clock == 0"),
            Pattern([0], "self.clock == 1"),
        ]
    )