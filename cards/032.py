Card("Sporophytes", power=4, powMod=3, chances=4, desc=[
    "The cloud of spores",
    "from beneath your skin",
    "begin to settle on",
    "the skin of your enemies.",
    "Many little pods begin",
    "to grow on them.",
    "> Consumes 1 spore.",
    "> If successful, gain",
    "  spore equal to the",
    "  number of opponents",
    "  in combat (includes",
    "  dead enemies).",
], attackScripts={"onHit": "card-scripts/sporophytes.atk"}, cost=2)