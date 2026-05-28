Card(name="Bioluminescence", power=0, chances=3, powMod=5, isRanged=False, desc=[
    "A blinding white flash",
    "is released by a gland",
    "on your neck.",
    "> Inflict 2 shocked.",
    "> Mass attack.",
], attackScripts={"onHit": "card-scripts/bioluminescence.atk"}, massAttack=True, cost=3)