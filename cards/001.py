Card("Parry", power=0, chances=4, powMod=4, desc=[
    "> If the target is",
    "  using an offensive",
    "  card, lower",
    "  the target's",
    "  AGT by 1."
], attackScripts={"onHit": "card-scripts/parry.atk"}, isDefensive=True)