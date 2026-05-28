Card("Sneaky stab", power=8, chances=1, powMod=8, desc=[
    "Not fair, but",
    "it's not meant to",
    "be anyway.",
    "> If there are",
    "  less than 3",
    "  cards in your",
    "  hand, deal",
    "  5 extra damage.",
], attackScripts={"onHit": "card-scripts/sneaky_stab.atk"}, cost=2)