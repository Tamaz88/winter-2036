Card("Acidic blood", power=6, chances=3, powMod=3, desc=[
    "You will hurt them",
    "like they have hurt you.",
    "> Mass attack.",
    "> Inflict 1 acid for",
    "  each bleed you have.",
], attackScripts={"onHit": "card-scripts/acidic_blood.atk"}, isDefensive=True, massAttack=True, cost=3)