# ┌─┐ 
# │ │ 
# └─┘ 

from math import log
import fynkos_reader as fr
from os import system
from pathlib import Path
import art
import text
import terminal as t
from random import randint, choice, shuffle
from time import sleep
from math import ceil, floor
from copy import deepcopy
from colorama import Fore, Back, Style
import threading
from playsound import playsound

#CLASSES

obtainableCards:list
enemies:dict
effects:dict
class StatusEffect:
    def __init__(self, name:str="Effect", count:int=1, duration:int=1, infinite:bool=False, effectScript:str="", callingOrder:int=3, effectDesc:list[str]=[]):
        self.name = name
        self.count = count
        self.duration = duration
        self.infinite = infinite
        self.effectScript = effectScript
        self.callingOrder = callingOrder
        self.effectDesc = effectDesc
    
    def __repr__(self):
        return f"{self.name} {self.count} {self.duration} {self.infinite}"

    def trigger(self, affectedEntity, locals:dict):
        with open(self.effectScript, "r", encoding="UTF-8") as script: script = script.read()
        cLocals = {"self": self, "entity": affectedEntity, "enemies": enemies, "t":t}
        for key in locals:
            cLocals[key] = locals[key]
        exec(script, cLocals)

class Card:
    def __init__(self, name:str="-", isRanged:bool=False, power:int=0, chances:int=0, powMod:int=0, desc:list=[], attackScripts:dict[str]={}, exhaust:bool=False, consume:bool=False, massAttack:bool=False, isDefensive=False, rarity:int=0, cost:int=1, forcedThought:list[str]=[]):
        self.name = name
        self.power = power
        self.tempPower = power
        self.chances = chances
        self.powMod = powMod
        self.desc = desc
        self.attackScripts = attackScripts
        self.isRanged = isRanged    
        self.isDefensive = isDefensive
        self.exhaust = exhaust
        self.consume = consume
        self.massAttack = massAttack
        self.rarity = rarity
        self.cost = cost
        self.forcedThough = forcedThought
        if self.isDefensive: self.cost = 0

    def __repr__(self):
        return f"{self.name}"
    
    def attackEffect(self, caster, affectedEntity, locals:dict, condition:str="onHit"):
        if condition in self.attackScripts.keys() and len(self.attackScripts[condition])>0:
            with open(self.attackScripts[condition], "r", encoding="UTF-8") as script: script = script.read()
            cLocals = {"self": self, "entity": affectedEntity, "caster": caster, "enemies": enemies, "t":t, "deepcopy":deepcopy}
            for key in locals:
                cLocals[key] = locals[key]
            exec(script, cLocals)
            print()

    def getAttackIndex(self):
        cardSet:list = obtainableCards # []
        # if player.name == "Agnes": cardSet = obtainableCards
        # if player.name == "Esther": cardSet = obtainableCards
        for i in range(len(cardSet)):
            if cardSet[i].name == self.name: return i
        return 0
    
    def getType(self):
        product = []
        for key in categories:
            product += [key for card in categories[key] if card.getAttackIndex() == self.getAttackIndex()]
        return list(set(product))

class Passive:
    def __init__(self, name:str="-", desc:list[str]=[], effectScript:str="", callingOrder:int=1, skirmishModifier:bool=False):
        """Calling order:
        0. On hit
        1. On clash fail
        2. On turn start
        3. On turn end
        4. On combat start"""
        self.name = name
        self.desc = desc
        self.effectScript = effectScript
        self.callingOrder = callingOrder
        self.skirmishModifier = skirmishModifier
        self.clock = 0

    def trigger(self, affectedEntity, locals:dict):
        if len(self.effectScript)>0:
            with open(self.effectScript, "r", encoding="UTF-8") as script: script = script.read()
            cLocals = {"self": self, "entity": affectedEntity, "enemies": enemies, "randint": randint, "t":t}
            for key in locals:
                cLocals[key] = locals[key]
            exec(script, cLocals)

    def getPassiveIndex(self):
        cardSet:list = obtainablePassives
        for i in range(len(cardSet)):
            if cardSet[i].name == self.name: return i
        return 0

class Pattern:
    def __init__(self, cards:list[int], condition:str):
        # "cards" should contain the enemies' card indices in their respective decks
        self.cards = cards
        self.condition = condition

class Entity:
    def __init__(self, alive:bool=True, name:str="dummy", maxHP:int=1, radiation:int=0, DEF:int=0, ATK:int=0, AGT:int=0, DEX:int=50, deck:list[Card]=[], skin:list=art.deafult, description:list=[], effects:list[StatusEffect]=[], passives:list[Passive]=[], attackSlots:int=1, expendable:bool=False, pattern:list[Pattern]=[], maxStamina:int=5):
        self.alive = alive
        self.name = name
        self.health = maxHP
        self.maxHealth = maxHP
        self.radiation = radiation
        self.DEF = DEF
        self.ATK = ATK
        self.AGT = AGT
        self.DEX = DEX
        self.deck = deck
        self.passives = passives
        self.drawPile = deepcopy(deck)
        shuffle(self.drawPile)
        self.discardPile = []
        self.consumePile = []
        self.hand:list[Card] = []
        self.effects:list[StatusEffect] = effects
        self.plannedAttacks:list[Card] = []
        self.attackSlots = attackSlots
        self.skin = skin
        self.description = description
        self.antiRad:int = 0
        self.decayTonic:int = 0
        self.momentum = 0
        self.expendable = expendable
        self.clock = 0
        self.attackPattern = pattern
        self.maxStamina = maxStamina
        self.stamina = maxStamina
        self.intel:list[int] = []
        self.sprogress:list[int] = []
        for _ in skirmishThemes:
            self.intel.append(0)
        for _ in skirmishThemes:
            self.sprogress.append(0)

    def __repr__(self):
        return f"{self.name}"

    def getEffect(self, effectName:str):
        for effect in self.effects:
            if effect.name.lower() == effectName.lower(): return effect
        else: return StatusEffect("Null", 0, 0, False, "")

    def damage(self, amount:int):
        finalDamage = (amount - (self.DEF - self.getEffect("Fragile").count + self.getEffect("Block").count))
        if finalDamage <= 0:
            finalDamage = 0
            t.alert(f"The attack proved futile against {self.name}", clear=False)
        self.health -= finalDamage
        if finalDamage>0: t.centeredInput(f"{self.name} suffered {finalDamage} damage.", clear=False)
        return finalDamage

    def applyEffect(self, effect:StatusEffect, count:int, duration:int, infinite:bool=False):
        canApply = True
        if infinite:
            effect.infinite = True
        cEffect:StatusEffect
        for eff in self.effects:
            if eff.name == effect.name: 
                cEffect = eff
                canApply = False
                break
        if canApply and (count>0 or duration>0):
            newEffect = deepcopy(effect)
            newEffect.count = count
            newEffect.duration = duration
            self.effects.append(newEffect)
        else:
            cEffect.count += count
            if not infinite: cEffect.duration += duration

    def dexCheck(self):
        threshold = self.DEX+self.momentum
        if self.getEffect("Focus").duration > 0:
            threshold += self.getEffect("Focus").count
            print(t.centerText(f"+{self.getEffect("Focus").count} DEX from Focus"))
        if self.getEffect("Bravery").duration > 0:
            threshold += self.getEffect("Bravery").count
            print(t.centerText(f"+{self.getEffect("Bravery").count} DEX from Bravery"))
        if randint(1, 100) <= min(threshold, 90): return True
        return False
    
    def resetDeck(self):
        self.drawPile = deepcopy(self.deck)
        shuffle(self.drawPile)
        self.discardPile.clear()
        self.hand.clear()

    def reshuffle(self, notify=True):
        # if notify:
        #     t.alert(clear=False, e=f"{self.name} reshuffles their deck.")
        self.drawPile.extend(self.discardPile)
        shuffle(self.drawPile)
        self.discardPile.clear()

    def clearHand(self):
        for card in self.hand:
            if card.name not in ("Pass", "Shocked"):
                self.discardPile.append(card)
        self.hand.clear()

    def drawHand(self, cardNum:int):
        self.clearHand()
        self.hand.append(Card( # on december 8th 2042 Mary will get one of yall pregnant 😂
            name="Pass", power=0, powMod=0, chances=1,
            desc=[
                "Just horsing around.",
                "Pretty sure nothing bad",
                "will happen.",
                "> Replenish 1",
                "  stamina."
            ],
            attackScripts={"onHit": "card-scripts/pass.atk", "onLose": "card-scripts/pass.atk"},
            isDefensive=True
        ))
        for c in range(cardNum):
            # print(self.deck)
            # print(self.drawPile)
            # print(c)
            if not len(self.drawPile) > 0:
                if not len(self.discardPile) > 0: break
                self.reshuffle()
            if self.drawPile:
                selectedCard = self.drawPile.pop()
                self.hand.append(selectedCard)

    def getAGT(self):
        return self.AGT+self.getEffect("Reflex").count+self.getEffect("Haste").count-self.getEffect("Clumsy").count-self.getEffect("Sickness").count

    def getATK(self):
        return self.ATK+self.getEffect("Force").count+self.getEffect("Blessing").count+self.getEffect("Lust for blood").count+self.getEffect("Hunger").count+min(self.stamina, 0)
    
    def executePattern(self):
        selectedPattern = []
        for pattern in self.attackPattern:
            if eval(pattern.condition, {"self": self}): selectedPattern = pattern.cards

        if len(selectedPattern) == 0:
            self.clock = 0

        for pattern in self.attackPattern:
            if eval(pattern.condition, {"self": self}): selectedPattern = pattern.cards

        selectedPattern = [self.deck[c] for c in selectedPattern]
        return  selectedPattern

# [text.chapter1scene1, [
#     user1, 
#     [
#         getEntity(enemies["raywolf"]),
#         getEntity(enemies["rayelk"]),
#         getEntity(enemies["raywolf"])
#     ],
#     True
# ], art.scene1, user1, "In medias res"],

class Scene:
    def __init__(self, text:list, battleInfo:list, art:list[str], user:Entity, title:str, endText:list=None):
        self.text = text
        self.endText = endText
        self.battleInfo = battleInfo
        self.user = user
        self.art = art
        self.title = title

#GLOBALS

effects = {
    "acid": StatusEffect(name="Acid", infinite=True, effectDesc=[
        "Apply damage equal to the",
        "effect's count, then reduce",
        "count by 1."
    ], effectScript="effects/acid.eff"),
    "burn": StatusEffect(name="Burn", infinite=True, effectDesc=[
        "Apply damage equal to the",
        "effect's count, then halve the",
        "effect's count."
    ], effectScript="effects/burn.eff"),
    "focus": StatusEffect(name="Focus", callingOrder=0, effectDesc=[
        "Modify your DEX checks by",
        "the effect's count."
    ]),
    "bravery": StatusEffect(name="Bravery", infinite=True, callingOrder=0, effectDesc=[
        "Modify your DEX checks by",
        "the effect's count."
    ]),
    "shock": StatusEffect(name="Shock", callingOrder=0, infinite=True, effectDesc=[
        "If the effect's count reaches",
        "10, pass your turn."
    ]),
    "constriction": StatusEffect(name="Constriction", callingOrder=0, effectDesc=[
        "Reduce the willpower of",
        "all of the target's attacks",
        "by the effect's count."
    ]),
    "block": StatusEffect(name="Block", callingOrder=0, effectDesc=[
        "Block one willpower of a ranged attack, then",
        "reduce count by one."
        "Furthermore, reduce the damage dealt to you by the count of this effect."
    ]),
    "bleed": StatusEffect(name="Bleed", callingOrder=2, effectDesc=[
        "After each offensive attack, lose health",
        "by the effect's count.",
    ], effectScript="effects/bleed.eff"),
    "reflex": StatusEffect(name="Reflex", callingOrder=0, effectDesc=[
        "Enchances AGT by the effect's count."
    ]),
    "haste": StatusEffect(name="Haste", callingOrder=0, effectDesc=[
        "Enchances AGT by the effect's count."
    ]),
    "evil_reflex": StatusEffect(name="Clumsy", callingOrder=0, effectDesc=[
        "Reduces AGT by the effect's count."
    ]),
    "sickness": StatusEffect(name="Sickness", callingOrder=0, effectDesc=[
        "Reduces AGT by the effect's count."
    ]),
    "shield": StatusEffect(name="Shield", effectDesc=[
        "Enchances DEF by the effect's count."
    ]),
    "fragile": StatusEffect(name="Fragile", callingOrder=0, effectDesc=[
        "Reduces DEF by the effect's count."
    ]),
    "force": StatusEffect(name="Force", callingOrder=0, effectDesc=[
        "Enchances ATK by the effect's count."
    ]),
    "blessing": StatusEffect(name="Blessing", callingOrder=0, effectDesc=[
        "Enchances ATK by the effect's count."
    ]),
    "spore": StatusEffect(name="Spore", infinite=True, callingOrder=0, effectDesc=[
        "Can be spent by or can boost spore cards."
    ]),
    "madness": StatusEffect(name="Madness", infinite=True, effectDesc=[
        "Whenever an opponent loses a clash, their attack is played against themselves."
    ]),
    "electric_charge": StatusEffect(name="Electric charge", callingOrder=0, effectDesc=[
        "On its own, this effect serves no purpose, but it can be used by",
        "various other skills and attacks."
    ]),
    "taunted": StatusEffect(name="Taunted", effectDesc=[
        "Reduce the number of cards drawn at the start of the turn by",
        "the effect's count."
    ], effectScript="effects/taunt.eff"),
    "endurance": StatusEffect(name="Endurance", effectDesc=[
        "Boost the power of all defensive cards by the effect's count."
    ]),
    "frenzy": StatusEffect(name="Frenzy", infinite=True, effectDesc=[
        "Deal a critical hit with a 1% chance multiplied by the effect's count.",
        "A critical hit deals 2x damage."
    ]),
    "bloodlust": StatusEffect(name="Lust for blood", infinite=True, effectDesc=[
        "Enchances ATK by the effect's count.",
        "The cap of the effect is determined by the level of Lust passive owned by the entity.",
    ]),
    "hunger": StatusEffect(name="Hunger", infinite=True, effectDesc=[
        "Enchances ATK by the effect's count.",
        "Upon reaching 5 Hunger, become shocked and lose 10 HP at turn start.",
    ], effectScript="effects/hunger.eff"),
}

obtainableCards = []

unobtainableCards = [
    Card(name="Sprout", power=5, chances=3, powMod=4, isRanged=False, desc=[ #0
        "A bud begins to open",
        "slowly, like a hatchling",
        "trying to break it's shell.",
        "> Add one Blossom to",
        "  your deck.",
        "> Exhaust card."
    ], attackScripts={"onHit": "card-scripts/sprout.atk"}, exhaust=True, cost=3),
    Card(name="Blossom", power=5, chances=4, powMod=4, isRanged=False, rarity=1, desc=[ #1
        "A blooming flower of",
        "flesh is now ready to",
        "reap the nutrients of",
        "anyone who may bother you.",
        "> Deal 10 unblockable",
        "  damage.",
        "> Exhaust card."
    ], attackScripts={"onHit": "card-scripts/blossom.atk"}, exhaust=True, cost=5),
    Card(name="Reload M1917", power=4, chances=1, powMod=6, isDefensive=True, desc=[ #2
        "Thrust in God",
        "and keep your",
        "powder dry!",
        "Or whatever that",
        "english guy said.",
        "> Exhaust card.",
        "> Add one.",
        "  \"S&W M1917\"",
        "  to your discard",
        "  pile.",
    ], attackScripts={"onHit": "card-scripts/revolver_reload.atk", "onLose": "card-scripts/revolver_reload.atk"}, exhaust=True, cost=0),
]

obtainablePassives = []

passiveUpgrades = {
    0: 1,
    3: 4,
}

status = fr.initFile("save.lift")
savedSettings = fr.initFile("settings.lift")
story:list
storyLine:list[Scene]
selectedAct:int = 0
storyIndices:list = [
    0,
    8,
    20,
    20,
    20,
    20,
    20,
]
storyTitles:list = [
    "Futtam mint a szarvasok",
    "???",
    "???",
    "???",
    "???",
    "???",
    "???",
]
engBoolDict = {
    True:  "(ON )",
    False: "(OFF)"
}
settings = {
    "auto_check": True,
    "old_mutation": False,
    "compressed": False
}
skirmishThemes = [
    {
        "name": "forest",
        "enemies": ["raywolf", "rayelk", "dreadbear", "ironstork", "bloodfinch"],
        "boss": [
            "ant_swarm",
            "hivedeer",
            "ant_swarm"
        ],
        "waves": 5,
        "events": [
            {
                "title": "Deereater",
                "story": text.deereater,
                "script": "events/deereater.event"
            },
            {
                "title": "The alpha",
                "story": text.the_alpha,
                "script": "events/the_alpha.event"
            },
            {
                "title": "The listening deer",
                "story": text.the_listening_deer,
                "script": "events/the_listening_deer.event"
            },
            {
                "title": "The Featherfiend",
                "story": text.featherfiend,
                "script": "events/featherfiend.event"
            },
        ]
    },
    {
        "name": "purist",
        "enemies": ["purist_squire", "purist_squire2", "purist_acolyte"],
        "boss": [
            "purist_squire",
            "purist_knight",
            "purist_squire"
        ],
        "waves": 5,
        "events": [
            {
                "title": "Purification ritual",
                "story": text.purification,
                "script": "events/purification.event"
            },
            {
                "title": "Prisoner no more",
                "story": text.prisoner_no_more,
                "script": "events/prisoner_no_more.event"
            },
            {
                "title": "Hermit",
                "story": text.hermit,
                "script": "events/hermit.event"
            },
        ]
    },
    {
        "name": "stellar",
        "enemies": ["stellar_servant", "stellar_priest"],
        "boss": [
            "stellar_servant",
            "high_priest",
            "stellar_servant",
        ],
        "waves": 3,
        "events": [
            {
                "title": "Show us how you shine",
                "story": text.show_us_how_you_shine,
                "script": "events/show_us_how_you_shine.event"
            },
            {
                "title": "Ritual",
                "story": text.ritual,
                "script": "events/ritual.event"
            },
        ]
    },
    # "lamplight company": {
    #     "enemies": [],
    #     "boss": [
    #     ],
    #     "waves": 3,
    #     "events": [
    #         # {
    #         #     "title": "",
    #         #     "story": text.,
    #         #     "script": "events/.event"
    #         # },
    #   ],
    # }
]

climaxes = [
    {
        "text": text.climax1,
        "outro": text.climax2outro,
        "boss": [
            "starvation",
        ],
        "index": 0
    },
    {
        "text": text.climax2,
        "outro": text.climax2outro,
        "boss": [
            "scavanger",
            "halfblood",
            "alpha_raywolf",
            "scavanger",
        ],
        "index": 1
    },
    {
        "text": text.climax3,
        "outro": text.climax2outro,
        "boss": [
            "stellar_priest",
            "jeffrey",
            "stellar_priest",
        ],
        "index": 2
    },
]

skirmishTree1 = [
    [0,2],
    [1],
    [2],
]

enemies = {
    "raywolf": "entities/raywolf.py",
    "alpha_raywolf": "entities/alpha_raywolf.py",
    "rayelk": "entities/rayelk.py",
    "dreadbear": "entities/dreadbear.py",
    "ironstork": "entities/ironstork.py",
    "bloodfinch": "entities/bloodfinch.py",
    "hivedeer": "entities/hivedeer.py",
    "listening_deer": "entities/listening_deer.py",
    "ant_swarm": "entities/ant_swarm.py",
    "the_listener": "entities/the_listener.py",
    "scavanger": "entities/scavanger.py",
    "halfblood": "entities/halfblood.py",
    "purist_squire": "entities/purist_squire.py",
    "purist_medic": "entities/purist_medic.py",
    "purist_squire2": "entities/injured_purist_squire.py",
    "purist_acolyte": "entities/purist_acolyte.py",
    "purist_knight": "entities/purist_knight.py",
    "the_governor": "entities/the_governor.py",
    "stellar_servant": "entities/stellar_servant.py",
    "stellar_priest": "entities/stellar_priest.py",
    "jeffrey": "entities/jeffrey.py",
    "high_priest": "entities/high_priest.py",
    "disheartened_stellar_priestess": "entities/disheartened_stellar_priestess.py",
    "featherfiend": "entities/featherfiend.py",
    "starvation": "entities/starvation.py",
    "grandfather": "entities/grandfather.py",
    # "sixth_sprite": "entities/mommy_holle.py",
    # "sixth_sprite_shield": "entities/mommy_holle_shield.py",
}

user1 = Entity(name="Esther", maxHP=80, deck=[], description=[
        "Born on August 13. 2010 in Phoenix, Arizona, dr. Esther Geraldson is an aspiring",
        "chemist who would go on to graduate at Cambridge University in 2032.",
        "",
        "After that, she used to work at a Weinmetall military research facility on",
        "the border of Hungary and Austria until the war began.",
        "Only a Wienmetall AntiRad suit, a survival knife, a revolver and a few",
        "little gadgets keep her alive in this snow-shrouded wasteland."
    ], passives=[]
)

user2 = Entity(name="Agnes", maxHP=95, DEX=60, ATK=2, deck=[], description=[
        "Born on April 25. 2007 in Érpatak, Hungary, Ágnes Fodor is a battlehardened",
        "mercenary who used to serve as a security guard in the same research facility as Esther."
        "",
        "As a special forces unit, her body was treated with chemicals allowing her to build",
        "a formidable resistance against nuclear radiation, making her basically immune to",
        "radiation poisoning. She still needs extra AntiRad ampules to",
        "gain additional mutations though."
], attackSlots=3)

global progress
progress = 0

#FUNCTIONS

def saveGame(quit:bool=True, isSaved:bool=True):
    t.alert("Saving...")
    deck1 = []
    for card in user1.deck:
        deck1.append(card.getAttackIndex())
    intel1 = []
    for i in user1.intel:
        intel1.append(i)
    sprogress1 = []
    for i in user1.sprogress:
        sprogress1.append(i)
    passives1 = []
    for passive in user1.passives:
        passives1.append(passive.getPassiveIndex())
    deck2 = []
    for card in user2.deck:
        deck2.append(card.getAttackIndex())
    intel2 = []
    for i in user2.intel:
        intel2.append(i)
    sprogress2 = []
    for i in user2.sprogress:
        sprogress2.append(i)
    passives2 = []
    for passive in user2.passives:
        passives2.append(passive.getPassiveIndex())
    status = {
        "isSaved": isSaved,
        "radiation1": user1.radiation,
        "antirad1": user1.antiRad,
        "tonic1": user1.decayTonic,
        "deck1": deck1,
        "intel1": intel1,
        "sprogress1": sprogress1,
        "passives1": passives1,
        "atk1": user1.ATK,
        "def1": user1.DEF,
        "agt1": user1.AGT,
        "dex1": user1.DEX,
        "radiation2": user2.radiation,
        "antirad2": user2.antiRad,
        "tonic2": user2.decayTonic,
        "deck2": deck2,
        "intel2": intel2,
        "sprogress2": sprogress2,
        "passives2": passives2,
        "atk2": user2.ATK,
        "def2": user2.DEF,
        "agt2": user2.AGT,
        "dex2": user2.DEX,
        "progress": progress,
    }
    if progress == 0:
        status["isSaved"] = False
    fr.saveFile("save.lift", status)
    # print(status)
    # input()
    if quit: exit()

def saveSettings():
    t.alert("Saving settings...")
    savedSettings = {
        "settings_auto_check": settings["auto_check"],
        "settings_old_mutation": settings["old_mutation"],
        "settings_compressed": settings["compressed"]
    }
    fr.saveFile("settings.lift", savedSettings)
    # print(settings)
    # input()

def loadGame():
    global progress
    status["isSaved"] = True
    user1.radiation = status["radiation1"]
    user1.antiRad = status["antirad1"]
    user1.decayTonic = status["tonic1"]
    user1.ATK = status["atk1"]
    user1.DEF = status["def1"]
    user1.DEX = status["dex1"]
    user1.AGT = status["agt1"]
    deck1 = status["deck1"]
    for i in range(len(deck1)):
        deck1[i] = deepcopy(obtainableCards[int(deck1[i])])
    user1.deck = deck1
    user1.intel = [int(i) for i in status["intel1"]]
    user1.sprogress = [int(i) for i in status["sprogress1"]]
    passives1 = status["passives1"]
    for i in range(len(passives1)):
        passives1[i] = deepcopy(obtainablePassives[int(passives1[i])])
    user1.passives = passives1
    user2.radiation = status["radiation2"]
    user2.antiRad = status["antirad2"]
    user2.decayTonic = status["tonic2"]
    user2.ATK = status["atk2"]
    user2.DEF = status["def2"]
    user2.DEX = status["dex2"]
    user2.AGT = status["agt2"]
    deck2 = status["deck2"]
    for i in range(len(deck2)):
        deck2[i] = deepcopy(obtainableCards[int(deck2[i])])
    user2.deck = deck2
    user2.intel = [int(i) for i in status["intel2"]]
    user2.sprogress = [int(i) for i in status["sprogress2"]]
    passives2 = status["passives2"]
    for i in range(len(passives2)):
        passives2[i] = deepcopy(obtainablePassives[int(passives2[i])])
    user2.passives = passives2
    user1.resetDeck()
    user2.resetDeck()
    progress = status["progress"]

def loadSettings():
    settings["auto_check"] = savedSettings["settings_auto_check"]
    settings["old_mutation"] = savedSettings["settings_old_mutation"]
    settings["compressed"] = savedSettings["settings_compressed"]

def getEntity(path, artFile=art):
    with open(path, "r", encoding="UTF-8") as file: script = file.read()
    return eval(script, {
        "Entity": Entity,
        "Card": Card,
        "Passive": Passive,
        "art": artFile,
        "obtainableCards": obtainableCards,
        "deepcopy": deepcopy,
        "effects": effects,
        "Pattern": Pattern
    })

def getCard(path):
    with open(path, "r", encoding="UTF-8") as file: script = file.read()
    return eval(script)

def createCard(card:Card|Passive, index:int, playerCard:bool=False):
    if type(card) == Card:
        desc = [t.capitalize() for t in card.getType()]
        if not settings["compressed"] or not playerCard: desc = card.desc
        if card.isRanged: isRanged = "Ranged"
        else: isRanged = "Melee"
        if card.isDefensive: isDefensive = "Defensive"
        else: isDefensive = "Offensive"
        return t.createBox(10, 12, [
            f"[{index}] {card.name}",
            f"({isRanged})",
            f"({isDefensive})",
            "",
            f"Cost: {card.cost}",
            f"Power: {card.power}",
            f"Power modifier: {card.powMod}",
            f"Willpower: {card.chances}",
            "",
        ]+desc, boxType=card.rarity)
    elif type(card) == Passive:
        triggers = [
            "successful attack",
            "getting hit",
            "turn start",
            "turn end",
            "combat start",
        ]
        return t.createBox(10, 1, [
            f"{card.name}",
            f"Applies on {triggers[card.callingOrder]}",
            "",
        ]+card.desc)

def createDialogueBox(character:str, dialogue:list):
    print("\n"*3)
    t.printAsciiArt(t.createBox(60, 2, [character, ""]+dialogue))
    print("\n")
    try: 
        t.printAsciiArt(art.characters[character][0])
        print("\n")
    except KeyError: pass
    t.printAsciiArt(t.createBox(2, 1, ["[ENTER] Continue | [M] Menu"]))
    print()
    inp = t.centeredInput("Choose/Continue: ")
    system("cls")
    match inp.lower().replace(" ", ""):
        case "m": return True
        case _: return False

def viewDeck(entity:Entity, clear=True, hand=False, width=5, onlyCards=False, onlyPassives=False, equipmentOnly=False, mutationOnly=False):
    if clear:
        system("cls")
    if not hand:
        print("\n"*3)
        print(t.centerText("DECK VIEWER"))
        print("\n"*3)
    rows = []
    cardList = entity.deck
    if hand: cardList = entity.hand
    if equipmentOnly: cardList = [c for c in cardList if c.rarity == 2]
    if mutationOnly: cardList = [c for c in cardList if c.rarity != 2]
    if not onlyPassives:
        for i in range(ceil(len(cardList)/width)):
            cardRow = []
            for ii in range(width):
                if ii+i*width<len(cardList): cardRow.append(createCard(cardList[ii+i*width], (ii+i*width)+1, True))
            rows.append(t.connectAsciiArt(cardRow, 1))
        for elem in rows:
            t.printAsciiArt(elem)
            print()
        print()
    if not hand and not onlyCards:
        print(t.centerText("╺━━━━━━╸"))
        print()
        for p in entity.passives:
            t.printAsciiArt(createCard(p, 0))
            print()

def createDialogue(dialogueBoxes:list, user):
    dIndex = 0
    while dIndex<len(dialogueBoxes):
        d = dialogueBoxes[dIndex]
        if createDialogueBox(d.character, d.message):
            inPauseMenu = True
            while inPauseMenu:
                try:
                    system("cls")
                    print("\n"*3)
                    print(t.centerText("PAUSE MENU"))
                    print("\n"*3)
                    print(t.centerText("[C] Continue       "))
                    print(t.centerText("[R] Rewind dialogue"))
                    print(t.centerText("[S] Skip dialogue  "))
                    print(t.centerText("[V] View deck      "))
                    print(t.centerText("[Q] Quit game      "))
                    print("\n")
                    pauseMenuOption = t.centeredInput("Choose an option: ")
                    match pauseMenuOption.replace(" ", "").lower():
                        case "c":
                            system("cls")
                            inPauseMenu = False
                        case "r":
                            amount = int(t.centeredInput("By how much?"))
                            if dIndex-amount > 0:
                                dIndex -= amount
                                inPauseMenu = False
                            else:
                                t.alert(clear=False, e="Invalid number")
                        case "s":
                            system("cls")
                            dIndex=len(dialogueBoxes)-1
                            inPauseMenu = False
                        case "v":
                            viewDeck(user)
                            print("\n")
                            t.centeredInput("Exit [ENTER]")
                        case "q":
                            confirmation = t.centeredInput("Are you sure you want to quit? [Y/N] ")
                            match confirmation.replace(" ", "").lower():
                                case "y":
                                    saveGame(quit=True)
                                case _:
                                    pass
                        case _: pass
                    system("cls")
                except IndexError: pass
                except ValueError: pass
        dIndex += 1

def manual(manualPages:list):
    for page in manualPages:
        print()
        system("cls")
        t.printAsciiArt(t.createBox(2, 1, [
            f"Page {manualPages.index(page)+1} out of {len(manualPages)}"
        ]))
        print("\n"*6)
        t.printAsciiArt(t.createBox(2, 1, page))
        print("\n")
        t.centeredInput("Continue [ENTER]")

def mutationAnimation(oldMutation:bool=False):
    if oldMutation:
        for _ in range(t.get_terminal_height()-1):
            genes = ["A", "C", "T", "G"]
            for _ in range(t.get_terminal_width()):
                print(choice(genes), end="")    
            sleep(0.02)
            print()
    else:
        for i in range(10):
            for row in art.dna:
                currentGene = choice(["A", "C", "T", "G"])
                t.alert(row.format(currentGene, currentGene), clear=False, sleepTime=0.0005, lingerTime=0)
        print()

def generateEncounter(theme:str, boss:bool=False):
    chosenEnemies = []
    product = []
    i = 0
    while i<3:
        if not boss: chosenEnemies.append(choice(skirmishThemes[theme]["enemies"]))
        else: 
            chosenEnemies = skirmishThemes[theme]["boss"]
            i = 3

        i += 1
    for enemy in chosenEnemies:
        product.append(getEntity(enemies[enemy]))
    return deepcopy(product)

# COMBAT FUNCTIONS

def userDeath(user:Entity, savedPlayer:Entity, savedEnemies:list[Entity], canRestart:bool=True):
    waysOfDeath = [
        "Your skull shatters,",
        "A wound is torn between your ribs,",
        "Your guts flow out,",
        "You bleed out slowly,",
        "Your spine cracks,",
    ]
    user.effects = []
    death = choice(waysOfDeath)
    if user.radiation>user.maxHealth:
        death = "You died of radiation poisoning. Dumbass."
    for eff in user.effects:
        user.effects.remove(eff)
    if canRestart:
        system("cls")
        print("\n"*6)
        if not user.radiation>user.maxHealth: t.alert(clear=False, e=f"{death} and you see the world no more.")
        else: t.alert(clear=False, e=death)
        t.alert(clear=False, e=f"Will you let it end this way?")
        print("\n"*3)
        print(t.centerText("[N] Restart encounter | [Y] Quit game"))
        print("\n")
        inDeathMenu = True
        while inDeathMenu:
            deathMenuOption = t.centeredInput("Choose: ", clear=True)
            match deathMenuOption.replace(" ", "").lower():
                case "n":
                    inDeathMenu = False
                    user.alive = True
                    for enemy in savedEnemies:
                        enemy.alive = True
                    savedPlayer.alive = True
                    return battle(savedPlayer, savedEnemies)
                case "y":
                    saveGame(quit=True)
                case _:
                    pass
    else:
        return 0

def clash(participant1:Entity, participant2:Entity, battleLocals:dict):
    system("cls")
    participant1.plannedAttacks[0].tempPower = participant1.plannedAttacks[0].power
    participant2.plannedAttacks[0].tempPower = participant2.plannedAttacks[0].power

    if "onClash" in participant1.plannedAttacks[0].attackScripts.keys() or "onClash" in participant2.plannedAttacks[0].attackScripts.keys():
        print("\n")
        t.printAsciiArt(t.createBox(1, 1, [
            "CLASH START"
        ]))
        print("\n"*3)
        participant1.plannedAttacks[0].attackEffect(participant1, participant2, battleLocals, "onClash")
        participant2.plannedAttacks[0].attackEffect(participant2, participant1, battleLocals, "onClash")
        print("\n"*3)
        t.centeredInput("Proceed [ENTER]")

    chances1 = participant1.plannedAttacks[0].chances - participant1.getEffect("Constriction").count
    if chances1<1: chances1 = 1
    chances2 = participant2.plannedAttacks[0].chances - participant2.getEffect("Constriction").count
    if chances2<1: chances2 = 1

    if participant1.plannedAttacks[0].isDefensive and participant2.plannedAttacks[0].isDefensive: return (participant2, participant1)
    while chances1 and chances2:
        system("cls")
        t.printAsciiArt(t.connectAsciiArt([
            t.createBox(1, 1, participant2.skin+["", participant2.name, f"Health: {participant2.health}/{participant2.maxHealth}", "", f"ATK: {participant2.getATK()} | DEF: {participant2.DEF}", f"AGT: {participant2.AGT} | DEX: {participant2.DEX+participant2.momentum}"]),
            createCard(participant2.plannedAttacks[0], 0)
        ]))
        t.printAsciiArt(t.createBox(10, 1, [f"{participant1.name} - VS - {participant2.name}"]))
        print("\n")
        power1 = max(0, participant1.plannedAttacks[0].tempPower+min(participant1.stamina, 0))
        if participant1.plannedAttacks[0].isDefensive==False: 
            power1 += participant1.getATK()
        else: power1 += participant1.getEffect("Endurance").count
        power2 = max(0, participant2.plannedAttacks[0].tempPower+min(participant2.stamina, 0))
        if participant2.plannedAttacks[0].isDefensive==False: 
            power2 += participant2.getATK()
        else: power2 += participant2.getEffect("Endurance").count
        speedDiff = abs((participant2.getAGT())-(participant1.getAGT()))
        if participant1.getAGT()>participant2.getAGT(): 
            if participant1.plannedAttacks[0].isDefensive==False: power1 += speedDiff
        elif participant2.getAGT()>participant1.getAGT(): 
            if participant2.plannedAttacks[0].isDefensive==False: power2 += speedDiff
        print("\n")
        print(t.centerText(f"{participant1.name} (AGT: {(participant1.getAGT())})"), end="\n\n")
        for _ in range(chances1):
            if not settings["auto_check"]: t.centeredInput("DEX check [ENTER]")
            if participant1.dexCheck():
                print(t.centerText(f"DEX CHECK BONUS: {power1} + {participant1.plannedAttacks[0].powMod}"))
                power1 += participant1.plannedAttacks[0].powMod
            else: print(t.centerText(f"DEX CHECK FAILED"))
            sleep(0.2)
        print("\n")
        print(t.centerText(f"{participant2.name} (AGT: {(participant2.getAGT())})"), end="\n\n")
        for _ in range(chances2):
            if participant2.dexCheck():
                print(t.centerText(f"DEX CHECK BONUS: {power2} + {participant2.plannedAttacks[0].powMod}"))
                power2 += participant2.plannedAttacks[0].powMod
            else: print(t.centerText(f"DEX CHECK FAILED"))
            sleep(0.2)
        print()
        print(t.centerText(f"{power1} VS {power2}"))
        print()
        if power1>power2: 
            chances2 -= 1
            t.centeredInput(f"{participant2.name} is becoming more exhausted.")
        elif power2>power1:
            chances1 -= 1
            t.centeredInput(f"{participant1.name} is becoming more exhausted.")
        else:
            print(t.centerText(f"Tie."))

    if participant1.plannedAttacks[0].name == "Shocked" or participant1.plannedAttacks[0].name == "Pass": power1 = 0
    if participant2.plannedAttacks[0].name == "Shocked" or participant2.plannedAttacks[0].name == "Pass": power2 = 0
    if chances1>chances2:
        winnerString = f"{participant1.name.upper()} WON THE CLASH!"
        t.printAsciiArt(t.createBox(10, 1, [winnerString]))
        return (participant2, participant1)
    else:
        winnerString = f"{participant2.name.upper()} WON THE CLASH!"
        t.printAsciiArt(t.createBox(10, 1, [winnerString]))
        return (participant1, participant2)

def rangedCombat(participant1:Entity, participant2:Entity):
    participant1Damage = max(0, participant1.plannedAttacks[0].power+min(participant1.stamina, 0))
    if participant1.plannedAttacks[0].isDefensive==False: participant1Damage += participant1.getATK()
    participant2Damage = max(0, participant2.plannedAttacks[0].power+min(participant2.stamina, 0))
    if participant2.plannedAttacks[0].isDefensive==False: participant2Damage += participant2.getATK()
    speedDiff = abs((participant2.getAGT())-(participant1.getAGT()))
    if participant1.getAGT()>participant2.getAGT(): participant1Damage += speedDiff
    elif participant2.getAGT()>participant1.getAGT(): participant2Damage += speedDiff

    system("cls")
    t.printAsciiArt(t.createBox(1, 1, participant2.skin+["", participant2.name, f"Health: {participant2.health}/{participant2.maxHealth}", "", f"ATK: {participant2.getATK()} | DEF: {participant2.DEF}"]))
    t.printAsciiArt(t.createBox(10, 1, [f"{participant1.name} - VS - {participant2.name}"]))
    print("\n")
    print(t.centerText(participant1.name), end="\n\n")
    t.alert(f"{participant1.name} lost {participant1.plannedAttacks[0].cost} momentum!", clear=False)    
    participant1.momentum -= participant1.plannedAttacks[0].cost
    if participant1.plannedAttacks[0].isRanged:
        for _ in range(participant1.plannedAttacks[0].chances):
            if not participant2.getEffect("Block").count > 0:
                if participant1.plannedAttacks[0].isRanged:
                    if not settings["auto_check"]: t.centeredInput("DEX check [ENTER]")
                    if participant1.dexCheck():
                        print(t.centerText(f"DEX CHECK BONUS: {participant1Damage} + {participant1.plannedAttacks[0].powMod}"))
                        participant1Damage += participant1.plannedAttacks[0].powMod
                    else: print(t.centerText(f"DEX CHECK FAILED"))
                    sleep(0.2)
                    print()
            else:
                print(t.centerText(f"THE RANGED ATTACK WAS BLOCKED BY {participant2.name}"))
                participant2.getEffect("Block").count -= 1
        if participant1Damage>0 and (participant1.plannedAttacks[0].isRanged or participant1.plannedAttacks[0].isDefensive==False):
            participant2.damage(participant1Damage)
    elif participant1.plannedAttacks[0].isDefensive==False:
        participant2.damage(participant1.plannedAttacks[0].power)
    print("\n")
    print(t.centerText(participant2.name), end="\n\n")
    t.alert(f"{participant2.name} lost {participant2.plannedAttacks[0].cost} momentum!", clear=False)    
    participant2.momentum -= participant2.plannedAttacks[0].cost
    if participant2.plannedAttacks[0].isRanged:
        for _ in range(participant2.plannedAttacks[0].chances):
            if not participant1.getEffect("Block").count > 0:
                if participant2.plannedAttacks[0].isRanged:
                    if participant2.dexCheck():
                        print(t.centerText(f"DEX CHECK BONUS: {participant2Damage} + {participant2.plannedAttacks[0].powMod}"))
                        participant2Damage += participant2.plannedAttacks[0].powMod
                    else: print(t.centerText(f"DEX CHECK FAILED"))
                    sleep(0.2)
                    print()
            else:
                print(t.centerText(f"THE RANGED ATTACK WAS BLOCKED BY {participant1.name}"))
                participant1.getEffect("Block").count -= 1
        if participant2Damage>0 and (participant2.plannedAttacks[0].isRanged or participant2.plannedAttacks[0].isDefensive==False):
            participant1.damage(participant2Damage)
    elif participant2.plannedAttacks[0].isDefensive==False:
        participant1.damage(participant2.plannedAttacks[0].power)
    print("\n")

def battle(player:Entity, battleEnemies:list[Entity], tutorial=False, radiation:int=len(enemies), canRestart:bool=True, expectDefeat=False):
    system("cls")
    player.momentum = 0
    savedEnemies = deepcopy(battleEnemies)
    savedPlayer = deepcopy(player)
    currentEnemies = [deepcopy(e) for e in battleEnemies]

    for entity in [player] + currentEnemies:
        entity.stamina = entity.maxStamina
        entity.effects.clear()

    def summon(id):
        currentEnemies.append(getEntity(enemies[id]))

    for enemy in currentEnemies:
        enemy.clock += currentEnemies.index(enemy)%2

    battleLocals = {
        "currentEnemies": currentEnemies, 
        "effects": effects, 
        "enemies": enemies, 
        "obtainableCards": obtainableCards, 
        "unobtainableCards": unobtainableCards, 
        "randint": randint, 
        "Fore": Fore, 
        "art": art, 
        "system": system, 
        "sleep": sleep, 
        "choice": choice,
        "Attack": Card,
        "Card": Card,
        "summon": summon,
        "floor": floor,
        "ceil": ceil,
        "art": art,
    }

    print("\n"*(floor(t.get_terminal_height()/2)-4))
    t.printAsciiArt(art.battle)
    print()
    t.centeredInput("Begin combat [ENTER]")
    player.resetDeck()

    def lifeCheck():
        isInBattle = 0
        for enemy in currentEnemies:
            if enemy.alive:
                isInBattle = 1
                break
        
        if player.health <= 0:
            if expectDefeat: return 0
            return 2
        return isInBattle

    def visualize(index):
        system("cls")
        # print(locals())
        print("\n"*3)
        enemyDisplay = []

        # input("gate 0")

        enemyCounter = 0
        for enemy in currentEnemies:
            staminaColor = Fore.RESET
            if enemy.health <= 0: enemy.alive = False
            if not enemy.alive: enemy.skin = art.death
            healthString = f"Health: {enemy.health}/{enemy.maxHealth}"
            if enemy.maxHealth > 9999: healthString = f"Health: ???"
            if enemy.stamina <= 0: staminaColor = Fore.RED
            currentEnemyDisplay = [t.createBox(1, 1, enemy.skin+["", enemy.name, healthString, f"Stamina: {enemy.stamina}/{enemy.maxStamina}", "", f"ATK: {enemy.getATK()} | DEF: {enemy.DEF}"])]
            if currentEnemies.index(enemy) == index:
                for slot in range(len(enemy.plannedAttacks)):
                    # input("gate 1a")
                    currentEnemyDisplay.append(createCard(enemy.plannedAttacks[slot], slot+1))
                    # input("gate 1b")
            enemyDisplay.append(t.connectAsciiArt(currentEnemyDisplay, p=1))
            # input("gate 1c")
            enemyCounter += 1
        t.printAsciiArt(t.connectAsciiArt(enemyDisplay))
        print("\n")

        # input("gate 1")

        initiative = "INITIATIVE:"
        for i in range(len(currentEnemies)-1):
            for ii in range(len(currentEnemies)-i-1):
                if currentEnemies[ii].AGT < currentEnemies[ii+1].AGT:
                    currentEnemies[ii], currentEnemies[ii+1] = currentEnemies[ii+1], currentEnemies[ii]
        for char in currentEnemies:
            if char.alive:
                mark = ""
                if index == currentEnemies.index(char): mark = "* "
                initiative += f" -> {mark}{char.name}"
        print(t.centerText(initiative))
        print()
        
        # input("gate 2")

        playerEffectStrings = []
        for i in range(ceil(len(player.effects)/5)):
            effectString = ""
            for ii in range(5):
                if ii+i*5<len(player.effects): 
                    if ii > 0: effectString += " | "
                    effectString += f"{player.effects[ii+i*5].name.upper()[:4]}. {player.effects[ii+i*5].duration} / {player.effects[ii+i*5].count}"
            playerEffectStrings.append(effectString)

        # input("gate 3")
        
        t.printAsciiArt(
            t.connectAsciiArt([
                t.createBox(2, 6+len(playerEffectStrings), [
                    "Effects:",
                    "",
                ]+playerEffectStrings),
                t.createBox(2, 1+len(playerEffectStrings), [
                    player.name,
                    f"Health: {player.health} / {player.maxHealth}",
                    f"Stamina: {player.stamina} / {player.maxStamina}",
                    "",
                    f"DEF: {player.DEF}      |      ATK: {player.getATK()}",
                    f"AGT: {player.getAGT()}{" "*(7-len(str(player.getAGT())))}|      DEX: {player.DEX+player.momentum}",
                ])
            ], p=1)
        )

        print()
        
        # input("gate 4")

        t.printAsciiArt(t.createBox(2, 1, [
            f"[P] Play card  |  [I] Inspect opponent  |  [S] Inspect self | [M] Manual"
        ]))
        print()

    if tutorial:
        manual(manualPages=[
            art.tutorial0,
            art.tutorial1,
            art.tutorial2,
            art.tutorial3,
            art.tutorial4,
            art.tutorial5,
            art.tutorial6,
        ])

    visualize(0)
    if player.radiation:
        player.health -= player.radiation
        t.alert(f"You took {player.radiation} damage from radiation.", lingerTime=1.5)

    for p in player.passives:
        if p.callingOrder == 4: p.trigger(player, locals=battleLocals)

    isInBattle = True
    while isInBattle:
        isInBattle = lifeCheck()

        for p in player.passives: p.clock += 1

        playerHandDraw = 5
        # for enemy in currentEnemies:
        #     if enemy.alive: playerHandDraw += enemy.attackSlots
        player.drawHand(max(1, playerHandDraw-player.getEffect("Taunted").count))
        player.plannedAttacks = [Card()]
        player.plannedAttacks[0] = player.hand[0]

        for enemy in currentEnemies:
            enemy.clock += 1
            for p in enemy.passives: p.clock += 1
            enemy.plannedAttacks.clear()
            enemy.plannedAttacks = enemy.executePattern()
            for slot in range(enemy.attackSlots):
                enemy.stamina -= enemy.plannedAttacks[slot].cost
            #     enemy.plannedAttacks.append(Card())
            #     enemy.plannedAttacks[slot] = choice(enemy.deck)
        
        for entity in currentEnemies+[player]:
            entity.stamina = min(entity.stamina+3, entity.maxStamina)

        visualize(0)
        t.centeredInput("NEW TURN [ENTER]")
        for p in player.passives:
            if p.callingOrder == 2: p.trigger(player, locals=battleLocals)

        for enemy in currentEnemies:
            
            for p in enemy.passives:
                if p.callingOrder == 2: p.trigger(enemy)

            if enemy.getEffect("Shock").count >= 10: 
                visualize(0)
                t.alert(f"{enemy.name}'s shock counter reached 10! {enemy.name} cannot act.")
                enemy.effects.remove(enemy.getEffect("Shock"))
                for slot in range(enemy.attackSlots):
                    enemy.plannedAttacks[slot] = Card(name="Shocked", isRanged=False, power=0, powMod=0, desc=["Awestruck.","Flabbergsated.","Bamboozled.","Cannot act."], isDefensive=True)
            if enemy.momentum <= -35:
                visualize(0)
                t.alert(f"{enemy.name}'s momentum reached -35! {enemy.name} cannot act.")
                enemy.momentum = 0
                for slot in range(enemy.attackSlots):
                    enemy.plannedAttacks[slot] = Card(name="Shocked", isRanged=False, power=0, powMod=0, desc=["Awestruck.","Flabbergsated.","Bamboozled.","Cannot act."], isDefensive=True)

            for _ in range(enemy.attackSlots):

                isInBattle = lifeCheck()
                if isInBattle == 2: 
                    for enemy2 in currentEnemies:
                        for p in enemy2.passives: p.clock = 0
                    for p in player.passives: p.clock = 0
                    if not canRestart: player.deck = [card for card in player.deck if card not in player.consumePile]
                    if expectDefeat: isInBattle = False
                    else: return userDeath(player, savedPlayer, savedEnemies, canRestart)
                
                visualize(currentEnemies.index(enemy))
                canEnemyAct = True
                if not enemy.alive:
                    canEnemyAct = False
                if canEnemyAct:

                    acting = True
                    if player.hand[0].name != "Shocked":
                        if player.momentum <= -35:
                            t.alert(f"{player.name}'s momentum reached -35! {player.name} cannot act.")
                            player.momentum = 0
                            for card in player.hand:
                                if card.name != "Pass":
                                    player.discardPile.append(card)
                            player.hand.clear()
                            for enemy in currentEnemies:
                                for _ in range(enemy.attackSlots):
                                    player.hand.append(Card(name="Shocked", isRanged=False, power=0, powMod=0, desc=["Awestruck.","Flabbergsated.","Bamboozled.","Cannot act."], isDefensive=True))
                        if player.getEffect("Shock").count >= 10: 
                            t.alert(f"{player.name}'s shock counter reached 10! {player.name} cannot act.")
                            player.effects.remove(player.getEffect("Shock"))
                            for card in player.hand:
                                if card.name != "Pass":
                                    player.discardPile.append(card)
                            player.hand.clear()
                            for enemy in currentEnemies:
                                for _ in range(enemy.attackSlots):
                                    player.hand.append(Card(name="Shocked", isRanged=False, power=0, powMod=0, desc=["Awestruck.","Flabbergsated.","Bamboozled.","Cannot act."], isDefensive=True))

                    while acting:
                        try:
                            visualize(currentEnemies.index(enemy))
                            act = t.centeredInput("Choose an action: ")
                            match act.replace(" ", "").lower():
                                case "p":
                                    viewDeck(player, clear=False, hand=True, width=7)
                                    cardNum = int(t.centeredInput("Choose a card [CARD NUMBER]: "))
                                    player.plannedAttacks[0] = player.hand[cardNum-1]
                                    if player.plannedAttacks[0].name != "Pass" and player.plannedAttacks[0].name != "Shocked" and not player.plannedAttacks[0].exhaust and not player.plannedAttacks[0].consume:
                                        player.discardPile.append(player.plannedAttacks[0])
                                        player.hand.remove(player.plannedAttacks[0])
                                    elif player.plannedAttacks[0].exhaust:
                                        player.hand.remove(player.plannedAttacks[0])
                                        t.alert(f"{player.plannedAttacks[0].name} was exhausted.")
                                    elif player.plannedAttacks[0].consume:
                                        player.hand.remove(player.plannedAttacks[0])
                                        consumedCard:Card
                                        for c in player.deck:
                                            if c.name == player.plannedAttacks[0].name:
                                                consumedCard = c
                                                break
                                        player.deck.remove(consumedCard)
                                        t.alert(f"{player.plannedAttacks[0].name} was consumed.")
                                    player.stamina -= player.plannedAttacks[0].cost
                                    t.alert(f"{player.name} lost {player.plannedAttacks[0].cost} stamina!")
                                    acting = False
                                case "i":
                                    target = currentEnemies[int(t.centeredInput("Which enemy would you like to inspect [ENEMY NUMBER] "))-1]
                                    targetEffectStrings = []
                                    for i in range(ceil(len(target.effects)/5)):
                                        effectString = ""
                                        for ii in range(5):
                                            if ii+i*5<len(target.effects): 
                                                if ii < 5 and ii > 0: effectString += " | "
                                                effectString += f"{target.effects[ii+i*5].name.upper()[:4]}. {target.effects[ii+i*5].duration} / {target.effects[ii+i*5].count}"
                                        targetEffectStrings.append(effectString)
                                    targetEffectStrings.append("")
                                    targetAttacks = []
                                    for slot in range(len(target.plannedAttacks)):
                                        targetAttacks.append(createCard(target.plannedAttacks[slot], slot+1))
                                    print(t.centerText(f"STATS OF {target.name}"))
                                    print()
                                    t.printAsciiArt(t.connectAsciiArt([
                                        t.createBox(2, 15, target.description+[
                                            "",
                                            f"DEF: {target.DEF}      |      ATK: {target.getATK()}",
                                            f"AGT: {target.getAGT()}{" "*(7-len(str(target.getAGT())))}|      DEX: {target.DEX+target.momentum}",
                                            ""
                                        ]+targetEffectStrings),
                                        t.connectAsciiArt(targetAttacks, 1)
                                    ]))
                                    print()
                                    print(t.centerText("╺━━━━━━╸"))
                                    print()
                                    for p in target.passives:
                                        t.printAsciiArt(createCard(p, 0))
                                    print("\n")
                                    t.centeredInput("Continue [ENTER]")
                                case "s":
                                    target = player
                                    print(t.centerText(f"STATS OF {target.name}"))
                                    print()
                                    playerEffects = []
                                    for effect in player.effects:
                                        playerEffects.append(f"{effect.name}: {effect.duration} duration | {effect.count} count")
                                    t.printAsciiArt(t.connectAsciiArt([
                                        t.createBox(2, 15, target.description+[
                                            "",
                                            f"DEF: {target.DEF}      |      ATK: {target.getATK()}",
                                            f"AGT: {target.getAGT()}{" "*(7-len(str(target.getAGT())))}|      DEX: {target.DEX+target.momentum}",
                                            ""
                                        ]+playerEffects),
                                    ]))
                                    print()
                                    print(t.centerText("╺━━━━━━╸"))
                                    print()
                                    for p in player.passives:
                                        t.printAsciiArt(createCard(p, 0))
                                    print("\n")
                                    t.centeredInput("Continue [ENTER]")
                                case "m":
                                    print(t.centerText(f"MANUALS"))
                                    print()
                                    t.printAsciiArt(t.createBox(2, 1, [
                                        "[1] Combat tutorial",
                                        "[2] Effect descriptions",
                                        "[3] Fancy card terms",
                                    ]))
                                    print()
                                    manualOption = int(t.centeredInput("Choose [Manual number] "))
                                    match manualOption:
                                        case 1:
                                            manual(manualPages=[
                                                art.tutorial0,
                                                art.tutorial1,
                                                art.tutorial2,
                                                art.tutorial3,
                                                art.tutorial4,
                                                art.tutorial5,
                                                art.tutorial6
                                            ])
                                        case 2:
                                            currentEffects = player.effects+enemy.effects
                                            seenEffects = {}
                                            for eff in currentEffects:
                                                if eff.name not in seenEffects:
                                                    seenEffects[eff.name] = eff
                                            currentEffects = list(seenEffects.values())
                                            if len(currentEffects)>0:
                                                effectManualPages = []
                                                for eff in currentEffects:
                                                    effectManualPages.append([
                                                        eff.name,
                                                        "",
                                                    ]+eff.effectDesc)
                                                manual(manualPages=effectManualPages)
                                            else:
                                                t.alert("There are no effects applied to anyone.")
                                        case 3:
                                            manual(manualPages=[
                                                art.cardTerms0,
                                                art.cardTerms1,
                                                art.cardTerms2,
                                                art.cardTerms3,
                                                art.cardTerms4
                                            ])
                                        case _:
                                            pass
                                case "/kill":
                                    for enemy in currentEnemies:
                                        enemy.health = 0
                                    visualize(0)
                                case "/die":
                                    player.health = 0
                                    visualize(0)
                                case _: pass
                        except IndexError: pass
                        except ValueError: pass

                    versus = deepcopy(art.versus)
                    playerCardDisplay = createCard(player.plannedAttacks[0], 0)
                    enemyCardDisplay = createCard(enemy.plannedAttacks[0], 0)
                    for i in range(floor(len(createCard(player.plannedAttacks[0], 0))/2)-2):
                        versus = [" "*len(versus[0])]+versus
                    system("cls")
                    print("\n"*(floor(t.get_terminal_height()/2)-floor(len(player.plannedAttacks[0].desc)+4)))
                    padding = len(playerCardDisplay[0])-len(enemyCardDisplay[0])
                    t.printAsciiArt(t.connectAsciiArt([
                        [" "*min(0, -padding)],
                        playerCardDisplay,
                        versus,
                        enemyCardDisplay,
                        [" "*max(0, padding)]
                    ], p=3))
                    del versus
                    print()
                    t.centeredInput("Engage [ENTER]")

                    if not player.plannedAttacks[0].isRanged and not enemy.plannedAttacks[0].isRanged:
                        if player.plannedAttacks[0].isDefensive==False or enemy.plannedAttacks[0].isDefensive==False:
                            clashResults = clash(player, enemy, battleLocals)
                            print()

                            if clashResults[0].plannedAttacks[0].isDefensive:
                                t.alert("Defensive card: No momentum was lost, nor gained.", clear=False)
                            else:
                                if clashResults[1].momentum<35: clashResults[1].momentum += clashResults[0].plannedAttacks[0].cost
                                else: clashResults[1].momentum = 35
                                clashResults[0].momentum -= clashResults[0].plannedAttacks[0].cost
                                t.alert(f"{clashResults[0]} lost {clashResults[0].plannedAttacks[0].cost} momentum!", clear=False)
                                t.alert(f"{clashResults[1]} gained {clashResults[0].plannedAttacks[0].cost} momentum!", clear=False)

                            critMultiplier = 1
                            if randint(1, 100) <= clashResults[1].getEffect("frenzy").count and not clashResults[1].plannedAttacks[0].isDefensive:
                                print()
                                print(t.centerText("! CRITICAL HIT !"))
                                print()
                                critMultiplier = 2
                            print("\n")
                            if clashResults[1].plannedAttacks[0].massAttack:
                                t.alert(f"{clashResults[1].name}: MASS ATTACK")
                                for enemy2 in currentEnemies:
                                    if enemy2.alive:
                                        enemy2.damage(round((clashResults[1].plannedAttacks[0].tempPower + clashResults[1].ATK)*critMultiplier))
                                        clashResults[1].plannedAttacks[0].attackEffect(clashResults[1], enemy2, locals=battleLocals)
                            else:
                                if not clashResults[1].plannedAttacks[0].isDefensive: clashResults[0].damage(round((clashResults[1].plannedAttacks[0].tempPower + clashResults[1].ATK)*critMultiplier))
                                clashResults[1].plannedAttacks[0].attackEffect(clashResults[1], clashResults[0], locals=battleLocals)
                                clashResults[0].plannedAttacks[0].attackEffect(clashResults[0], clashResults[1], locals=battleLocals, condition="onLose")
                            if clashResults[0].getEffect("Madness").count>0 and clashResults[0].plannedAttacks[0].isDefensive==False:
                                t.alert(f"The god of {clashResults[0]} demands atonement.", clear=False)
                                print()
                                clashResults[0].damage(clashResults[0].plannedAttacks[0].tempPower + clashResults[0].ATK)
                                clashResults[0].plannedAttacks[0].attackEffect(clashResults[0], clashResults[0], locals=battleLocals)
                            
                            for p in clashResults[1].passives:
                                if p.callingOrder == 0: p.trigger(clashResults[1], locals=battleLocals | {"target": clashResults[0]})

                            for p in clashResults[0].passives:
                                if p.callingOrder == 1: p.trigger(clashResults[0], locals=battleLocals | {"target": clashResults[1]})

                        else:
                            player.plannedAttacks[0].attackEffect(player, enemy, locals=battleLocals)
                            enemy.plannedAttacks[0].attackEffect(enemy, player, locals=battleLocals)
                    else:
                        rangedCombat(player, enemy)
                        if player.plannedAttacks[0].massAttack:
                                t.alert(f"{player.name}: MASS ATTACK\n")
                                for enemy2 in currentEnemies:
                                    if enemy2.alive:
                                        enemy2.damage(player.plannedAttacks[0].tempPower + player.ATK)
                                        if not enemy2.getEffect("Block").count>0 and not player.plannedAttacks[0].isDefensive: player.plannedAttacks[0].attackEffect(player, enemy2, locals=battleLocals)
                        else:
                            if not enemy.getEffect("Block").count>0 and not player.plannedAttacks[0].isDefensive: player.plannedAttacks[0].attackEffect(player, enemy, locals=battleLocals)
                        if not player.getEffect("Block").count>0 and not enemy.plannedAttacks[0].isDefensive: enemy.plannedAttacks[0].attackEffect(enemy, player, locals=battleLocals)

                    doEffectDescsLinger = False
                    for eff in player.effects:
                        if len(eff.effectScript)>0 and eff.callingOrder==2:
                            eff.trigger(player, locals=battleLocals)
                            doEffectDescsLinger = True
                            # print(eff)
                            # print(eff.name)
                            if eff.duration<=0 or eff.count<=0: player.effects.remove(eff)
                    # input()

                    for eff in enemy.effects:
                        if len(eff.effectScript)>0 and eff.callingOrder==2 and eff in player.effects:
                            eff.trigger(enemy, locals=battleLocals)
                            doEffectDescsLinger = True
                            if eff.duration<=0 or eff.count<=0: enemy.effects.remove(eff)

                    if doEffectDescsLinger:
                        print()
                        t.centeredInput("Continue [ENTER]")

                if len(enemy.plannedAttacks)>0: enemy.plannedAttacks.pop(0)
            
            if canEnemyAct:
                for p in enemy.passives:
                    if p.callingOrder == 3: p.trigger(enemy, locals=battleLocals)

                for eff in enemy.effects:
                    t.refresh()
                    # visualize(currentEnemies.index(enemy))
                    if len(eff.effectScript)>0 and eff.callingOrder==3: eff.trigger(enemy, locals=battleLocals)
                    if not eff.infinite: eff.duration -= 1
                    if eff.duration<=0 or eff.count<=0: enemy.effects.remove(eff)

        for p in player.passives:
            if p.callingOrder == 3: p.trigger(player, locals=battleLocals)

        if len(player.effects)>0: print()
        effectsToRemove = []
        for eff in player.effects:
            # visualize(len(currentEnemies)-1)
            t.refresh()
            if len(eff.effectScript)>0 and eff.callingOrder==3: eff.trigger(player, locals=battleLocals)
            if not eff.infinite: eff.duration -= 1
            if eff.duration<=0 or eff.count<=0: effectsToRemove.append(eff)
        
        for eff in effectsToRemove:
            player.effects.remove(eff)

        currentEnemies = [e for e in currentEnemies if not (e.health<=0 and e.expendable)]

        isInBattle = lifeCheck()

    system("cls")
    for enemy in range(len(currentEnemies)):
        currentEnemies[0].effects.clear()
        del currentEnemies[0]
    player.effects.clear()
    player.resetDeck()
    print("\n"*(floor(t.get_terminal_height()/2)-3))
    player.deck = [card for card in player.deck if card not in player.consumePile]
    for p in player.passives: p.clock = 0
    for e in battleEnemies: e.clock = 0
    if expectDefeat:
        t.printAsciiArt(t.createBox(2, 1, [
            "DEFEAT!"
        ]))
        print()
        t.centeredInput("Continue [ENTER]")
        system("cls")
        return 0
    else:
        t.printAsciiArt(t.createBox(2, 1, [
            "VICTORY!"
        ]))
        print()
        t.centeredInput("Continue [ENTER]")
        system("cls")
        return radiation

# GAME MENU

def skirmish(cPlayer:Entity):
    themeSelection = []
    themeSelectionCards = []
    theme = 0
    cTheme = 0
    if progress>8:
        for _ in range(3):
            themeSelection.append(choice(skirmishThemes))
        for i in range(len(themeSelection)):
            cTheme = i
            themeDesc = [
                f"[{i+1}] "+skirmishThemes[cTheme]["name"].capitalize(),
                "",
                "Possible enemies:",
            ]
            for enemy in skirmishThemes[cTheme]["enemies"]:
                themeDesc.append(" "+getEntity(enemies[enemy]).name)
            themeDesc.append("")
            themeDesc.append("Bossfight:")
            for enemy in skirmishThemes[cTheme]["boss"]:
                themeDesc.append(" "+getEntity(enemies[enemy]).name)
            themeDesc.append("")
            themeDesc.append(f"Waves: {skirmishThemes[cTheme]["waves"]}")
            themeSelectionCards.append(
                t.createBox(0, 0, themeDesc)
            )
        inThemeSelector = True
        while inThemeSelector:
            try:
                system("cls")
                print("\n"*(floor(t.get_terminal_height()/2)-16))
                print(t.centerText("SELECT THEME"))
                print("\n")
                t.printAsciiArt(t.connectAsciiArt(themeSelectionCards))
                print("\n")
                theme = int(t.centeredInput("Select a theme [NUM] "))-1
                inThemeSelector = False
            except ValueError:
                pass
            except IndexError:
                pass
    system("cls")
    print("\n"*(floor(t.get_terminal_height()/2)-8))
    t.printAsciiArt(art.skirmish)
    print("\n")
    t.centeredInput(f"Begin [ENTER]")
    gainedRadiation = 0
    for i in range(skirmishThemes[theme]["waves"]):
        # cPlayer.health = max(cPlayer.maxHealth, cPlayer.health)
        cPlayer.health = min(cPlayer.maxHealth, cPlayer.health+5)
        encounterChoices = []
        for _ in range(3): 
            if randint(1, 3)<3: encounterChoices.append(generateEncounter(theme))
            else: encounterChoices.append("event")
        if i<skirmishThemes[theme]["waves"]-1:
            inEncounterChooser = True
            encounterChoice = None
            while inEncounterChooser:
                try:
                    system("cls")
                    print("\n"*(floor(t.get_terminal_height()/2)-12))
                    t.printAsciiArt(art.skirmish)
                    print("\n"*2)
                    print(t.centerText(f"{i+1}. battle"))
                    print("\n"*2)
                    encounterChoiceCards = []
                    for option in encounterChoices: 
                        if option != "event":
                            encounterChoiceCards.append(t.createBox(6,6,[
                                f"[{encounterChoices.index(option)+1}]",
                                "",
                                option[0].name,
                                option[1].name,
                                option[2].name
                            ]))
                        else:
                            encounterChoiceCards.append(t.createBox(6,3,[
                                f"[{encounterChoices.index(option)+1}]",
                                "",
                                "EVENT"
                            ]))
                    t.printAsciiArt(t.connectAsciiArt(encounterChoiceCards))
                    print()
                    encounterChoice = encounterChoices[int(t.centeredInput("Choose encounter [CARD NUM] "))-1]
                    if encounterChoice != None: inEncounterChooser = False
                except IndexError: t.alert("Invalid card number.")
                except ValueError: pass
                except UnboundLocalError: pass
            if encounterChoice != "event":
                gainedRadiation += battle(cPlayer, encounterChoice, canRestart=False)
                cPlayer.deck = [card for card in cPlayer.deck if card not in cPlayer.consumePile]
            else:
                cEvent = choice(skirmishThemes[theme]["events"])
                system("cls")
                createDialogue(cEvent["story"], cPlayer)
                with open(cEvent["script"], "r", encoding="UTF-8") as file: script = file.read()
                if len(cEvent["script"])>0: exec(script, {
                    "t": t,
                    "Passive": Passive,
                    "player": cPlayer,
                    "obtainableCards": obtainableCards,
                    "effects": effects,
                    "enemies": enemies,
                    "getEntity": getEntity,
                    "battle": battle,
                    "gainedRadiation": gainedRadiation,
                    "deepcopy": deepcopy,
                    "floor": floor,
                    "randint": randint,
                })
        else:
            system("cls")
            print("\n"*(floor(t.get_terminal_height()/2)-8))
            t.printAsciiArt(t.connectAsciiArt([art.death, art.cache_guardian]))
            print()
            t.centeredInput("Continue [ENTER]")
            gainedRadiation += battle(cPlayer, generateEncounter(theme, boss=True), radiation=1, canRestart=False)
        if cPlayer.health<=0:
            system("cls")
            print("\n"*(floor(t.get_terminal_height()/2)-16))
            t.printAsciiArt(art.death)
            print("\n"*2)
            print(t.centerText("Skirmish gone wrong")+"\n")
            sleep(1)
            t.centeredInput("[ENTER]")
            cPlayer.alive = False
            break
    cPlayer.passives = [i for i in cPlayer.passives if not i.skirmishModifier]
    if cPlayer.alive:
        cPlayer.intel[cTheme] += 1

        rewardDisplay = ["Gained 1 dose of AntiRad, and",f"Gained {gainedRadiation} radiation."]
        rewardEquipment = None
        rewardChance = 5
        if cPlayer.name == "Agnes": rewardChance = 2
        if randint(1, rewardChance) == 5:
            if randint (0, 1): rewardEquipment = choice(equipment)
            else: rewardEquipment = "tonic"
            rewardDisplay.append("")
            rewardDisplay.append(f"NEW EQUIPMENT GAINED:")
        if rewardEquipment != None: print("\n"*(floor(t.get_terminal_height()/2)-8))
        else: print("\n"*(floor(t.get_terminal_height()/2)-13))
        t.printAsciiArt(art.skirmish_successful)
        print("\n")
        t.printAsciiArt(t.createBox(2,3,rewardDisplay))
        if rewardEquipment != None:
            print()
            if rewardEquipment != "tonic":
                t.printAsciiArt(createCard(rewardEquipment, 0))
                cPlayer.deck.append(rewardEquipment)
            else:
                t.printAsciiArt(t.createBox(1, 1, ["1 dose of decay tonic"]))
                cPlayer.decayTonic += 1
        cPlayer.antiRad += 1
        cPlayer.radiation += gainedRadiation
        print("\n")
        t.centeredInput(f"Continue [ENTER]")
        saveGame(False)

def gameMenu(storyLine:list[Scene], cPlayer:Entity, returnAct:bool=False):
    player = cPlayer
    def visualize(characterTalking=False, message=text.DialogueBox()):
        player = storyLine[0].user
        system("cls")
        print("\n")
        t.printAsciiArt(t.createBox(2,1,[
            "     GAME MENU      "
        ]))
        t.printAsciiArt(t.createBox(2,1,[
            f"Progress: {progress}"
        ]))
        print("\n"*3)
        speechBox = [""]
        characterArt = art.characters[player.name][0]

        if characterTalking: 
            characterArt = art.characters[player.name][1]
            speechBox = t.createBox(18, 2, [
                player.name,
                "",
            ]+message)

        if player.radiation >= player.maxHealth:
            characterArt = art.characters[player.name][2]
            speechBox = t.createBox(18, 2, [
                player.name,
                "",
                "I need serum...",
                "now...",
            ])
            
        character = t.connectAsciiArt([
            characterArt,
            speechBox])
        characterPadding = [
            " "*len(character[0]),
            " "*len(character[0]),
        ]
        if player.name == "Esther":
            for _ in range(4): characterPadding.append(" "*len(character[0]))
        elif player.name == "Agnes":
            for _ in range(8): characterPadding.append(" "*len(character[0]))
        currentAct = story.index(storyLine)
        t.printAsciiArt(t.connectAsciiArt([
            art.gameMenuAssets[currentAct][0],
            t.createBox(18, 1, [
                player.name.upper()
            ])+t.createBox(18,2,[
                "OPTIONS:",
                "",
                "[P] Progress",
                "",
                "[R] Skirmish",
                "",
                "[M] Mutate",
                "",
                "[V] View deck",
                "",
                "[T] Ponder",
                "",
                "[O] Options",
                "",
                "[S] Save game",
                "",
                "[Q] Quit game",
                "",
            ])+t.createBox(18,2,[
                f"Radiation: {player.radiation}",
                f"AntiRad: {player.antiRad}",
                f"Decay tonic: {player.decayTonic}",
                f"Health: {player.health} / {player.maxHealth}"
            ]),
            characterPadding+character,
            art.gameMenuAssets[currentAct][1]
        ]))
        print("\n")
    inGameMenu = True
    while inGameMenu:
        player.health = player.maxHealth
        player.alive = True
        visualize()
        gameMenuOption = t.centeredInput("Choose an option: ")
        match gameMenuOption.replace(" ", "").lower():
            case "listen":
                
                def listen():
                    playsound("spooky_scary.wav")
                thread = threading.Thread(target=listen)

                system("cls")
                createDialogue([
                    text.DialogueBox("The Listener", ["*Cough*", "*Cough*"]),
                    text.DialogueBox("The Listener", [f"Hey {player.name} I found some disk laying around."]),
                ], player)

                system("cls")
                print("\n"*3)
                t.printAsciiArt(art.the_listener)
                print("\n")
                t.alert("Let me take a listen...", clear=False)
                print("\n"*5)
                print(t.centerText("💿 SPOOKY SCARY SKELETONS AGGRESSIVE GAMING MIX - unknown artist"))
                print("\n")
                thread.start()
                t.alert("#"*50, sleepTime=2.23, framed=True)
                thread.join()
                print()
                t.centeredInput("Exit [ENTER]")
            case "p":
                inSceneSelector = True

                while inSceneSelector:
                    system("cls")
                    print("\n"*3)
                    t.printAsciiArt(art.sceneSelection)
                    print("\n"*3)
                    for scene in range(min(len(storyLine)+1, progress-storyIndices[selectedAct]+1)):
                        if scene>0:
                            for _ in range(5): 
                                print(t.centerText("┃"))
                                sleep(0.05)
                        if scene<len(storyLine) : t.printAsciiArt(t.createBox(0, 0, [f"[{scene+1}] {storyLine[scene].title}"]))
                        else: t.printAsciiArt(t.createBox(0, 0, ["[N] NEXT ACT"]))
                    print("\n"*3)
                    try:
                        selectedScene = t.centeredInput("Select scene [SCENE NUMBER/0 TO EXIT] ")
                        if selectedScene.upper().replace(" ", "") != "N":
                            selectedScene = int(selectedScene)-1
                            if selectedScene == -1:
                                inSceneSelector = False
                                system("cls")
                            elif selectedScene<len(storyLine) and selectedScene<min(len(storyLine), progress-storyIndices[selectedAct]+1) and selectedScene>=0:
                                inSceneSelector = False
                                system("cls")
                                if returnAct: return (selectedScene, storyLine)
                                return selectedScene
                            else:
                                pass
                        else:
                            if story.index(storyLine)+1<len(story):
                                storyLine = story[story.index(storyLine)+1]
                                return 0
                            else:
                                t.alert("This act is still under construction.", clear=False, lingerTime=0.5)
                                t.alert("Thank you for downloading Winter 2036!", clear=False)
                                system("cls")
                    except IndexError:
                        pass
                    except ValueError:
                        pass
            case "r":
                inSkirmishMenu = True
                print(skirmishTree1)
                print(player.sprogress)
                while inSkirmishMenu:
                    tempSkirmishThemes = [skirmishThemes[skirmishTree1[i][player.sprogress[i]]] for i in range(len(skirmishTree1)) if player.sprogress[i]<skirmishTree1[i][-1]]
                    intelBox = [
                        f"INTEL PER FACTION:",
                        "",
                    ]

                    intelStatus = {
                        True: "O",
                        False: "~"
                    }
                    if progress>8:
                        i = 0
                        for key in tempSkirmishThemes:
                            if tempSkirmishThemes.index(key) >= 0:
                                intelBox.append(f" {intelStatus[player.intel[i] >= 5]} {key["name"].capitalize()}: {player.intel[i]}")
                                if player.intel[i] >= 5: intelBox.append(f" ┗━[{i+1}] {key["name"].capitalize()} climax")
                                intelBox.append("")
                                i += 1
                    else:
                        intelBox.append(" ~ Clear ACT I. to")
                        intelBox.append("   access intel.")

                    intelBox += [
                        "",
                        "[E] Embark on skirmish",
                        "",
                        "[Q] Quit menu",
                    ]

                    system("cls")
                    print("\n"*3)
                    t.printAsciiArt(t.createBox(2,1,[
                        f"SKIRMISH MENU"
                    ]))
                    print("\n"*3)
                    t.printAsciiArt(t.createBox(2,1,intelBox))
                    print("\n"*3)
                    skirmishMenuInput = t.centeredInput("Choose an option: ").upper().replace(" ", "")
                    match skirmishMenuInput:
                        case "E":
                            skirmish(player)
                        case "Q":
                            inSkirmishMenu = False
                        case _:
                            try:
                                cClimax = climaxes[int(skirmishMenuInput)-1]
                                if int(skirmishMenuInput)>0 and player.intel[int(skirmishMenuInput)-1] >= 5 and progress>8:
                                    system("cls")
                                    createDialogue(cClimax["text"], player)
                                    boss = [getEntity(enemies[e]) for e in cClimax["boss"]]
                                    battle(player, boss, radiation=50)
                                    if player.alive: 
                                        inSkirmishMenu = False
                                        player.sprogress[int(skirmishMenuInput)-1] += 1
                                    saveGame(quit=False)
                            except ValueError: pass
                            except IndexError: pass

            case "m":
                inMutationMenu = True
                while inMutationMenu:
                    odds = min(player.radiation, 50)
                    if player.name == "Agnes": odds = floor(player.radiation/2)
                    system("cls")
                    print("\n"*3)
                    t.printAsciiArt(t.createBox(2,1,[
                        f"MUTATION MENU"
                    ]))
                    print("\n"*3)
                    t.printAsciiArt(t.createBox(2,1,[
                        f"Radiation: {player.radiation}",
                        f"AntiRad: {player.antiRad}",
                        f"Decay tonic: {player.decayTonic}",
                        f"Health: {player.health} / {player.maxHealth}"
                    ]))
                    print("\n")
                    t.printAsciiArt(t.createBox(2,1,[
                        f"[M] Mutate ({min(odds, 50)}% rate of success)",
                        "",
                        f"[C] Cure mutation",
                        "",
                        f"[D] Discard equipment",
                        "",
                        "[Q] Quit mutation menu",
                    ]))
                    print("\n")
                    mutationMenuOption = t.centeredInput("Choose an option: ")
                    match mutationMenuOption.replace(" ", "").lower():
                        case "m":
                            if len([c for c in player.deck if c.rarity != 2]) <= 8:
                                cardTypes = ["debuffer", "bleed", "buffer", "shock", "spore", "sustain"]
                                inMutationTypeSelection = True
                                while inMutationTypeSelection:
                                    try:
                                        system("cls")
                                        print("\n"*(floor(t.get_terminal_height()/2)-8))
                                        t.printAsciiArt(art.mutation_selector)
                                        print("\n")
                                        t.printAsciiArt(t.connectAsciiArt([
                                            t.createBox(0, 0, content=[
                                                "[1] With cunning.",
                                                "",
                                                "Increased chance to",
                                                "pick a debuffer card."
                                            ]),
                                            t.createBox(0, 0, content=[
                                                "[2] With brutality.",
                                                "",
                                                "Increased chance to",
                                                "pick a bleed card."
                                            ]),
                                            t.createBox(0, 0, content=[
                                                "[3] With wit.",
                                                "",
                                                "Increased chance to",
                                                "pick a buffer card."
                                            ]),
                                            t.createBox(0, 0, content=[
                                                "[4] With terror.",
                                                "",
                                                "Increased chance to",
                                                "pick a shock card."
                                            ]),
                                            t.createBox(0, 0, content=[
                                                "[5] With determination.",
                                                "",
                                                "Increased chance to",
                                                "pick a spore card."
                                            ]),
                                        ]))
                                        t.printAsciiArt(t.connectAsciiArt([
                                            t.createBox(0, 0, content=[
                                                "[6] With patience.",
                                                "",
                                                "Increased chance to",
                                                "pick a sustian card."
                                            ]),
                                        ]))
                                        print("\n")
                                        print("\n"*3)
                                        cardType = cardTypes[int(t.centeredInput("Choose a card type [CARD NUMBER] "))-1]
                                        inMutationTypeSelection = False
                                    except IndexError: 
                                        t.alert(clear=False, e="Invalid card number.")
                                        continue
                                    except ValueError: continue
                                system("cls")
                                if player.antiRad > 0:
                                    cardChoices = []
                                    mutationAnimation(settings["old_mutation"])
                                    for _ in range(3):
                                        if randint(1, 100) <= odds:
                                            if randint(1, 10)<5: cardChoices.append(choice(mutations[cardType]))
                                            else: cardChoices.append(choice(mutations["commons"]))
                                    system("cls")
                                    print("\n"*(floor(t.get_terminal_height()/2)-8))
                                    t.printAsciiArt(art.reveal_mutation)
                                    print("\n")
                                    t.centeredInput("Reveal [ENTER]")
                                    system("cls")
                                    print("\n"*(floor(t.get_terminal_height()/2)-4))
                                    if len(cardChoices)>0:
                                        gainedATK = False
                                        gainedDEF = False
                                        if randint(1, 10) == 1:
                                            gainedATK = True
                                            player.ATK += 1
                                            print()
                                        if randint(1, 20) == 1:
                                            gainedDEF = True
                                            t.alert(f"{player.name.upper()} GAINED +1 DEF!", clear=False)
                                            player.DEF += 1
                                            print()
                                        inCardPicker = True
                                        while inCardPicker:
                                            try:
                                                visualizedCardChoices = []
                                                for i in range(len(cardChoices)):
                                                    system("cls")
                                                    print("\n"*(floor(t.get_terminal_height()/2)-16))
                                                    visualizedCardChoices.append(createCard(cardChoices[i], i+1))
                                                    t.printAsciiArt(t.connectAsciiArt(visualizedCardChoices[:i+1]))
                                                print()
                                                if gainedATK: t.alert(f"{player.name.upper()} GAINED +1 ATK!", clear=False)
                                                if gainedDEF: t.alert(f"{player.name.upper()} GAINED +1 DEF!", clear=False)
                                                print("\n"*2)
                                                selectedCard = cardChoices[int(t.centeredInput("Pick one [CARD NUMBER] "))-1]
                                                player.deck.append(selectedCard)
                                            except IndexError: 
                                                t.alert(clear=False, e="Invalid card number.")
                                                continue
                                            except ValueError: continue
                                            t.alert(f"Gained {selectedCard.name}")
                                            player.reshuffle()
                                            inCardPicker = False
                                    else:
                                        t.alert(clear=False, e="Unsuccessful mutation")
                                    player.radiation = max(0, player.radiation-50)
                                    player.antiRad -= 1
                                    print("\n"*3)
                                    t.printAsciiArt(t.createBox(2, 1, [f"[ENTER] Continue"]))
                                    # t.printAsciiArt(t.createBox(2, 1, [f"[ENTER] Continue | [R] Remove card from deck"]))
                                    print("\n"*3)
                                    mutationMenuOption2 = t.centeredInput("Choose: ")
                                    match mutationMenuOption2.replace(" ", "").lower():
                                        case _: pass
                                else: t.alert(clear=False, e="Not enough AntiRad.")
                            else:
                                t.alert("Your body is too weak to handle so many limbs and organs at once.", clear=False)
                                t.alert("You may have no more than 8 mutations at a time")
                        case "c":
                            if player.decayTonic>0:
                                system("cls")
                                viewDeck(player, clear=False, onlyCards=True, mutationOnly=True)
                                cardToRemove = t.centeredInput("Pick a mutation to remove [CARD NUM/ENTER TO EXIT] ")
                                playerMutations = [c for c in player.deck if c.rarity != 2]
                                if type(cardToRemove) != str:
                                    pass
                                else:
                                    try:
                                        cardToRemove = playerMutations[int(cardToRemove)-1]
                                        removingCard = True
                                        while removingCard:
                                            try:
                                                confirmCardRemoval = t.centeredInput(f"Are you sure you want to remove {cardToRemove.name}? [Y/N] ")
                                                if confirmCardRemoval.upper() == "Y":
                                                    removingCard = False
                                                    t.event([
                                                        "The tonic rushes through the part of yourself that you aim to remove, making the surrounding tissue go numb.",
                                                        "You can already feel a part of you decaying.",
                                                        "",
                                                        f"{cardToRemove.name} was removed from your deck."
                                                    ])
                                                    player.deck.remove(cardToRemove)
                                                    player.decayTonic -= 1
                                                elif confirmCardRemoval.upper() == "N":
                                                    removingCard = False
                                                    system("cls")
                                                else: pass
                                            except IndexError: pass
                                            except ValueError: pass
                                    except IndexError: pass
                                    except ValueError: pass
                            else:
                                t.alert("You don't have any decay tonic.")
                        case "d":
                            system("cls")
                            viewDeck(player, clear=False, onlyCards=True, equipmentOnly=True)
                            cardToRemove = t.centeredInput("Pick an equipment to discard [CARD NUM/ENTER TO EXIT] ")
                            playerEquipment = [c for c in player.deck if c.rarity == 2]
                            if type(cardToRemove) != str:
                                pass
                            else:
                                try:
                                    cardToRemove = playerEquipment[int(cardToRemove)-1]
                                    removingCard = True
                                    while removingCard:
                                        try:
                                            confirmCardRemoval = t.centeredInput(f"Are you sure you want to remove {cardToRemove.name}? [Y/N] ")
                                            if confirmCardRemoval.upper() == "Y":
                                                removingCard = False
                                                t.event([
                                                    "You didn't really like this scrap of metal anyway.",
                                                    "",
                                                    f"{cardToRemove.name} was removed from your deck."
                                                ])
                                                player.deck.remove(cardToRemove)
                                            elif confirmCardRemoval.upper() == "N":
                                                removingCard = False
                                                system("cls")
                                            else: pass
                                        except IndexError: pass
                                        except ValueError: pass
                                except IndexError: pass
                                except ValueError: pass
                        case "q":
                            inMutationMenu = False
                            system("cls")
                        case _:
                            pass
            case "v":
                viewDeck(player)
                print("\n")
                t.centeredInput("Exit [ENTER]")
            case "t":
                forcedThought = False
                chosenLine = choice(text.talk[player.name])
                alphas = [c for c in player.deck if c.rarity == 1]
                if len(alphas) and randint(1, 5)==5:
                    cCard:Card = choice(alphas)
                    chosenLine = [
                        "An organ that is not yours",
                        "starts feeding into your",
                        "nervous system, forming",
                        "thoughts that are not your",
                        "own.",
                        "",
                    ]+cCard.forcedThough
                    forcedThought = True
                visualize(True, chosenLine)
                print("\n")
                t.centeredInput("Continue [ENTER]")
                system("cls")
            case "o":
                settingsMenu()
                system("cls")
            case "s":
                saveGame(quit=False)
            case "q":
                confirmation = t.centeredInput("Are you sure you want to quit? [Y/N] ")
                match confirmation.replace(" ", "").lower():
                    case "y":
                        saveGame(quit=True)
                    case _:
                        pass
            case _:
                pass

def settingsMenu():
    inOptions = True
    while inOptions:
        system("cls")
        print("\n"*3)
        t.printAsciiArt(art.title)
        print("\n"*3)
        print(t.centerText("SETTINGS OPTIONS:"))
        print("\n"+t.centerText(f"[1] Auto-DEX checks        {engBoolDict[settings['auto_check']]}"))
        print(""+t.centerText(f"[2] Old mutation animation {engBoolDict[settings['old_mutation']]}"))
        print(""+t.centerText(f"[3] Compressed card view   {engBoolDict[settings['compressed']]}"))
        print("\n"+t.centerText(f"[C] Credits                     "))
        print(""+t.centerText(f"[Q] Quit settings               "))
        print("\n")
        settingsOption = t.centeredInput("Choose an option: ")
        match settingsOption.replace(" ", "").lower():
            case "1": settings["auto_check"] = not settings["auto_check"]
            case "2": settings["old_mutation"] = not settings["old_mutation"]
            case "3": settings["compressed"] = not settings["compressed"]
            case "c":
                system("cls")
                print("\n"*6)
                t.printAsciiArt(art.credits)
                print("\n"*3)
                t.printAsciiArt(t.createBox(2, 1, [
                    "Developed by: Insidious Goat Wizard",
                    "",
                    "Written by: Insidious Goat Wizard",
                    "",
                    "Art by: Insidious Goat Wizard",
                    "",
                    "",
                    "Help with movesets & cards: Fate",
                    "",
                    "Help with characters & playtesting: Chili_Hog",
                    "",
                    "Creator of the Stellar skirmish theme: Dumblord ",
                    "",
                    "Creator of Featherfiend: Bewtato",
                    "",
                    "",
                    "\"Future\" ASCII font from: https://patorjk.com/software/taag",
                    # "",
                    # "DNA animation used in the mutation menu: https://inventwithpython.com/bigbookpython/project21.html",
                    "",
                    "ASCII art converter: https://www.asciiart.eu/image-to-ascii",
                ]))
                print("\n"*3)
                t.centeredInput("Quit [ENTER]")
            case "q": 
                saveSettings()
                inOptions = False
            case _: pass

# SECONDARY GLOBALSű

obtainableCards = [getCard(f) for f in Path("./cards").iterdir() if f.is_file()]
obtainablePassives = [getCard(f) for f in Path("./passives").iterdir() if f.is_file()]
# print(obtainableCards)
# print(obtainablePassives)
# input()

user1.deck=[ #0,0,0,1,1,1,2,3
        deepcopy(obtainableCards[0]),
        deepcopy(obtainableCards[0]),
        deepcopy(obtainableCards[0]),
        deepcopy(obtainableCards[1]),
        deepcopy(obtainableCards[1]),
        deepcopy(obtainableCards[1]),
        deepcopy(obtainableCards[2]),
        deepcopy(obtainableCards[3]),
        # Self-bleeder deck: 9,9,13,13,10,10,34,34,35,35,36,37,13
        # Shock deck: 7, 11, 11, 11, 8, 8, 8, 5,
]
user1.passives=[obtainablePassives[17]]

user2.deck=[ #18,18,18,19,19,20,20,21
        deepcopy(obtainableCards[12]),
        deepcopy(obtainableCards[12]),
        deepcopy(obtainableCards[12]),
        deepcopy(obtainableCards[18]),
        deepcopy(obtainableCards[18]),
        deepcopy(obtainableCards[20]),
        deepcopy(obtainableCards[20]),
        deepcopy(obtainableCards[21]),
]

story = [
    [
        Scene(text.chapter1scene1, [
            user1, 
            [
                getEntity(enemies["raywolf"]),
                getEntity(enemies["rayelk"]),
                getEntity(enemies["raywolf"])
            ],
            True
        ], art.scene1, user1, "In medias res"),
        Scene(text.chapter1scene2, None, art.scene2, user1, "Complication"),
        Scene(text.chapter1scene3, [
            user1,
            [
                getEntity(enemies["ironstork"]),
                getEntity(enemies["dreadbear"]),
                getEntity(enemies["rayelk"])
            ]
        ], art.scene3, user1, "Stillness"),
        Scene(text.chapter1scene4, [
            user1,
            [
                getEntity(enemies["ironstork"]),
                getEntity(enemies["rayelk"]),
                getEntity(enemies["ironstork"]),
            ]
        ], art.scene4, user1, "Hope dies last"),
        Scene(None, [
            user1,
            [
                getEntity(enemies["ironstork"]),
                getEntity(enemies["bloodfinch"]),
                getEntity(enemies["bloodfinch"])
            ]
        ], art.scene5, user1, "Forced march I."),
        Scene(text.chapter1scene6, [
            user1,
            [
                getEntity(enemies["hivedeer"]),
                getEntity(enemies["ant_swarm"]),
                getEntity(enemies["ant_swarm"]),
            ]
        ], art.scene6, user1, "Forced march II."),
        Scene(text.chapter1scene7, None, art.scene7, user1, "Forced march III."),
        Scene(text.chapter1scene8, [
            user1,
            [
                getEntity(enemies["the_listener"]),
            ]
        ], art.scene8, user1, "Esther ante portas"),
        Scene(text.chapter1conclusion, None, art.act1conclusion, user1, "Farkas leszek, azt várom"),
    ],
    # [
    #     Scene(text.chapter2scene1a, [
    #         user2, 
    #         [
    #             getEntity(enemies["grandfather"]),
    #         ],
    #         False,
    #         0,
    #         False,
    #         True
    #     ], art.act2scene1, user2, "A thousand shards", text.chapter2scene1b),
    # ],
]

storyLine = story[0]

alive = True
equipment = [
    obtainableCards[2],
    obtainableCards[3],
    obtainableCards[21],
    obtainableCards[28],
    obtainableCards[29],
    obtainableCards[30],
    obtainableCards[31],
]
mutations = {
    "commons": [
        obtainableCards[4],
        obtainableCards[5],
        obtainableCards[6],
        obtainableCards[8],
        obtainableCards[9],
        obtainableCards[10],
        obtainableCards[11],
        obtainableCards[12],
        obtainableCards[13],
        obtainableCards[15],
        obtainableCards[16],
        obtainableCards[17],
        obtainableCards[22],
        obtainableCards[24],
        obtainableCards[26],
        obtainableCards[27],
        obtainableCards[32],
        obtainableCards[33],
        obtainableCards[38],
        obtainableCards[41],
    ],
    "debuffer": [
        obtainableCards[5],
        obtainableCards[6],
        obtainableCards[14],
        obtainableCards[15],
        obtainableCards[16],
        obtainableCards[25],
        obtainableCards[41],
    ],
    "bleed": [
        obtainableCards[9],
        obtainableCards[10],
        obtainableCards[13],
        obtainableCards[34],
        obtainableCards[35],
        obtainableCards[37],
        obtainableCards[44],
    ],
    "buffer": [
        obtainableCards[4],
        obtainableCards[8],
        obtainableCards[12],
        obtainableCards[17],
        obtainableCards[22],
        obtainableCards[23],
        obtainableCards[24],
        obtainableCards[36],
        obtainableCards[39],
    ],
    "shock": [
        obtainableCards[7],
        obtainableCards[11],
        obtainableCards[26],
        obtainableCards[27],
        obtainableCards[43],
    ],
    "spore": [
        obtainableCards[16],
        obtainableCards[22],
        obtainableCards[23],
        obtainableCards[32],
        obtainableCards[33],
        obtainableCards[40],
    ],
    "sustain": [
        obtainableCards[42]
    ]
}

categories = {
    "debuffer": [
        obtainableCards[1],
        obtainableCards[5],
        obtainableCards[6],
        obtainableCards[14],
        obtainableCards[15],
        obtainableCards[16],
        obtainableCards[25],
        obtainableCards[41],
    ],
    "bleed": [
        obtainableCards[9],
        obtainableCards[10],
        obtainableCards[13],
        obtainableCards[20],
        obtainableCards[34],
        obtainableCards[35],
        obtainableCards[37],
        obtainableCards[44],
    ],
    "buffer": [
        obtainableCards[4],
        obtainableCards[8],
        obtainableCards[12],
        obtainableCards[17],
        obtainableCards[22],
        obtainableCards[23],
        obtainableCards[24],
        obtainableCards[36],
        obtainableCards[39],
    ],
    "shock": [
        obtainableCards[7],
        obtainableCards[11],
        obtainableCards[26],
        obtainableCards[27],
        obtainableCards[43],
    ],
    "spore": [
        obtainableCards[16],
        obtainableCards[22],
        obtainableCards[23],
        obtainableCards[32],
        obtainableCards[33],
        obtainableCards[40],
    ],
    "sustain": [
        obtainableCards[42]
    ]
}

passivePool = [
    obtainablePassives[0],
    obtainablePassives[2],
    obtainablePassives[3],
    obtainablePassives[5],
    obtainablePassives[6],
    obtainablePassives[8],
    obtainablePassives[13],
    obtainablePassives[15],
]

#GAME LOGIC

system("cls")
inConfig = True
while inConfig:
    print("\n"*6)
    print(t.centerText("Resize the terminal (ctrl+/-) until this line fits perfectly into the terminal window."))
    print("\n"*3)
    t.printAsciiArt(art.ideal_width_indicator)
    print("\n"*3)
    # print(t.centerText("START GAME [Y] | ASSET LOADER [A]")+"\n"*2)
    # isOptimal = t.centeredInput("Select an option: ")
    isOptimal = t.centeredInput("START GAME [Y]")
    print("\n"*3)
    match isOptimal.replace(" ", "").lower():
        case "y": inConfig = False
        # case "a": t.alert("This feature is still in development.")
        case _: pass
    system("cls")

system("cls")
print("\n"*3)
t.printAsciiArt(art.title)
print("\n"*3)
t.centeredInput("Begin [ENTER]")

loadSettings()
cProgress = progress

inMenu = True
while inMenu:
    shuffle(user1.drawPile)
    shuffle(user2.drawPile)
    system("cls")
    print("\n"*3)
    t.printAsciiArt(art.title)
    print("\n"*3)
    print(t.centerText("MENU OPTIONS:"))
    print("\n")
    t.printAsciiArt(t.createBox(2, 1, ["[B] Begin new game       "]))
    if status["isSaved"]: t.printAsciiArt(t.createBox(2, 1, ["[L] Load game            "]))
    else: t.printAsciiArt(t.createBox(2, 1, ["[-] Load game (NO SAVES) "]))
    t.printAsciiArt(t.createBox(2, 1, ["[S] Settings             "]))
    t.printAsciiArt(t.createBox(2, 1, ["[Q] Quit game            "]))
    if randint(1, 100)==100:
        print("\n")
        t.printAsciiArt(art.harHarHarHar)
        sleep(3)
        system("cls")
        continue
    print("\n")
    mainMenuOption = t.centeredInput("Choose an option: ")
    match mainMenuOption.replace(" ", "").lower():
        case "b":
            system("cls")
            inMenu = False
        case "l":
            if status["isSaved"]:
                loadGame()
                t.alert("Loading game...")
                system("cls")
                inMenu = False
                # if shit happens: progress -> cProgress
                progress = status["progress"]
                if progress>1:
                    selectedActIndex = 0
                    for act in range(len(storyIndices)):
                        if progress>storyIndices[act]:
                            try: storyLine = story[act]
                            except IndexError: pass
                            selectedActIndex = storyIndices[act]
                    if progress<=len(storyLine)+selectedActIndex:
                        # battle(user1, [getEntity(enemies["starvation"])])
                        # battle(user1, [getEntity(enemies["jeffrey"])])
                        # battle(user1, [getEntity(enemies["alpha_raywolf"])])
                        # battle(user1, [getEntity(enemies["the_governor"])])
                        # battle(user1, [getEntity(enemies["the_listener"])])
                        # battle(user1, [getEntity(enemies["featherfiend"])])
                        # battle(user1, [getEntity(enemies["sixth_sprite"]),getEntity(enemies["sixth_sprite_shield"])])
                        inActSelector = True
                        doVisualize = True
                        system("cls")
                        while inActSelector:
                            if doVisualize:
                                print("\n"*3)
                                t.printAsciiArt(art.actSelection)
                                print("\n"*3)
                                maxAct = 0
                                for act in range(len(storyIndices)):
                                    if act>0:
                                        for _ in range(5): 
                                            print(t.centerText("┃"))
                                            sleep(0.05)
                                    if progress > storyIndices[act]: 
                                        t.printAsciiArt(t.createBox(0, 0, [f"[{act+1}] {storyTitles[act]}"]))
                                        maxAct = act
                                    else: t.printAsciiArt(t.createBox(0, 0, [f"[-] NOT UNLOCKED"]))
                                print("\n"*3)
                                doVisualize = False
                            try:
                                selectedAct = int(t.centeredInput("Select act [ACT NUMBER] ", clear=True))-1
                                if selectedAct<=maxAct and selectedAct>=0:
                                    storyLine = story[selectedAct]
                                    inActSelector = False
                                    # player = story[selectedAct][0].user
                            except IndexError:
                                if len(story) != len(storyTitles):
                                    t.alert("This act is still in development.", clear=False, lingerTime=0.5)
                                    t.alert("Thank you for downloading Winter 2036!", clear=False)
                                    doVisualize = True
                                    system("cls")
                                else:
                                    pass
                            except ValueError:
                                pass

                        startMenu = gameMenu(storyLine, storyLine[0].user, True)
                        cProgress = startMenu[0]
                        storyLine = startMenu[1]
        case "s":
            settingsMenu()
        case "q":
            saveGame(quit=True)
        case _: pass

while alive:
    selectedActIndex = 0
    for act in storyIndices:
        if progress>act: selectedActIndex = act
    try:
        if progress<=len(storyLine)+selectedActIndex:
            player = storyLine[cProgress].user
            print("\n"*(floor(t.get_terminal_height()/2)-8))
            t.printAsciiArt(t.createBox(2, 3, storyLine[cProgress].art))
            print("\n")
            t.centeredInput(f"Load scene {cProgress+1} [ENTER]")
            system("cls")
            if storyLine[cProgress].text != None: createDialogue(storyLine[cProgress].text, player)
            if progress == 1 and cProgress == 1:
                mutationAnimation(settings["old_mutation"])
                system("cls")
                print("\n"*(floor(t.get_terminal_height()/2)-8))
                print()
                print(t.centerText("NEW MUTATION AQUIRED:"))
                print()
                starterMutation = deepcopy(obtainableCards[choice(mutations["commons"]).getAttackIndex()])
                t.printAsciiArt(createCard(starterMutation, 0))
                print()
                t.centeredInput("Continue [ENTER]")
                player.deck.append(starterMutation)
                manual([
                    art.radiation0,
                    art.radiation1,
                    art.radiation2
                ])
                player.radiation = 0
                player.antiRad = 3
            battleRad = 0
            if storyLine[cProgress].battleInfo != None:
                battleRad = battle(*storyLine[cProgress].battleInfo)
            if storyLine[cProgress].endText != None: createDialogue(storyLine[cProgress].endText, player)
            if progress == 10 and cProgress == 10:
                system("cls")
                manual([
                    art.agnesGuide
                ])
            if progress == 8 and cProgress == 8:
                mutationAnimation(settings["old_mutation"])
                system("cls")
                print("\n"*(floor(t.get_terminal_height()/2)-8))
                print()
                print(t.centerText("NEW PASSIVE UNLOCKED:"))
                print()
                newPassive = deepcopy(choice(passivePool))
                t.printAsciiArt(createCard(newPassive, 0))
                print()
                t.centeredInput("Continue [ENTER]")
                player.passives.append(newPassive)
                manual([
                    art.act1completion
                ])
            if progress == 9 and cProgress == 0:
                system("cls")
                print("\n"*(floor(t.get_terminal_height()/2)-1))
                t.alert("The grandfather will accompany you from now on.")
                system("cls")
                print("\n"*(floor(t.get_terminal_height()/2)-8))
                print()
                print(t.centerText("NEW PASSIVE UNLOCKED:"))
                print()
                newPassive = deepcopy(obtainablePassives[7])
                t.printAsciiArt(createCard(newPassive, 0))
                print()
                t.centeredInput("Continue [ENTER]")
                player.passives.append(newPassive)
            if cProgress == progress:
                progress += 1
                player.radiation += battleRad
            if progress>1:
                cProgress = gameMenu(storyLine, player)
            else:
                cProgress += 1
        else:
            system("cls")
            print("\n"*3)
            print(t.centerText("You've reached the end of the game so far."))
            print(t.centerText("Thank you for downloading and playing Winter 2036"))
            print("\n"*3)
            t.centeredInput("Exit [ENTER]")
            saveGame(quit=True, isSaved=False)
    except UnboundLocalError:
    # except IndexError:
        t.alert(clear=False, e="Something went wrong with Python indices. Please report issue at the itch.io page.")
        saveGame(quit=True)