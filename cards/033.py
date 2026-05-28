Card("Fungal regeneration", power=0, powMod=4, chances=4, desc=[
    "No matter how deep",
    "your wounds are,",
    "the fungal threads",
    "that run deep in your",
    "flesh keep holding on.",
    "> Heal 3 + 1 HP for each",
    "  spore you have.",
], attackScripts={"onHit": "card-scripts/regen.atk"}, isDefensive=True)