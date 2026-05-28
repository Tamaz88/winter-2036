Card("Fungal infection", power=6, powMod=4, chances=3, desc=[
    "We are one now, all",
    "conjoint in the",
    "embrace of the same",
    "threads.",
    "",
    "> MASS ATTACK.",
    "> Consume 1 spore.",
    "  for each target.",
    "> Inflict 1",
    "  constriction on",
    "  each target.",
], attackScripts={"onHit": "card-scripts/fungal_infection.atk"}, massAttack=True, exhaust=True, rarity=1, cost=4)