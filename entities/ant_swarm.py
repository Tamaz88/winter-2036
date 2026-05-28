Entity(name="Ant swarm", maxHP=5, expendable=True, deck=[
            Card(name="Spit acid", isRanged=True, power=1, chances=1, powMod=8, desc=["Apply 3 acid."], attackScripts={"onHit": "card-scripts/spit_acid.atk", "onLose": ""})
        ], AGT=-2, DEX=50, description=[
            "In this hostile enviroment, some animals are forced to form",
            "more or less equal relationships with eachother, be it parasitic",
            "or symbiotic.",
            "",
            "These ants live their whole lives inside a Hivedeer, the body",
            "that nourishes them from their earliest stages of life.",
            "So, it is logical that these ants have to protect the body that",
            "shields them from the cruel outside world."
        ], skin=art.ant_swarm, passives=[Passive(name="Decaying swarm", desc=[
            "Lose 2 HP each time the swarm attacks."
        ], effectScript="events/swarm.eff", callingOrder=0)], pattern=[Pattern([0], "True")]
    )