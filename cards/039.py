Card("Grand wings", power=5, powMod=2, chances=5, desc=[
    "Flapping your wings,",
    "you fly with pride.",
    "",
    "> Gain 3 block.",
    "> All defensive",
    "  cards gain +3",
    "  power.",
], attackScripts={"onHit": "card-scripts/wothp.atk", "onLose": "card-scripts/wothp.atk"}, rarity=1, isDefensive=True)