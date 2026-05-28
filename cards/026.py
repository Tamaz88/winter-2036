Card(name="Leap and smash", power=10, chances=1, powMod=7, isRanged=False, desc=[
    "You leap into the",
    "air and crash into",
    "your opponent with",
    "full force.",
    "> Inflict 4 shock.",
    "> Discard a card",
    "  from your hand."
], attackScripts={"onHit": "card-scripts/leap_and_smash.atk"}, cost=1)