class DialogueBox:
    def __init__(self, character="Dummy", message=["SDIYBT"]):
        self.character = character
        self.message = message

talk = {
    "Esther": [
        [
            "What if instead of Julius Caesar",
            "he was called Julius ze/zir",
            "and everyone in anicent Rome",
            "used neopronouns?",
        ],
        [
            "Do sheep feel cold",
            "after being sheared?",
            "Furthermore, are there",
            "official statistics",
            "about the mortaility",
            "rate of sheep that died of",
            "cold?",
        ],
        [
            "Does a centaur taste",
            "like a horse?",
        ],
    ],
    "Agnes": [
        [
            "My name is Agnes I made the Winter game."
        ]
    ]
}

placeholderStory = [
    DialogueBox("Zsombor Bodó", [
        "Hallottad-e a citrom és a pap legendáját?"
    ]),
]

climax1 = [
    DialogueBox("...", [
        "The forest is dead silent as always.",
    ]),
    DialogueBox("...", [
        "Well, to be fair, even in this frozen landscape,",
        "some creatures can still be heard.",
    ]),
    DialogueBox("...", [
        "But today, not a single one.",
        "The only sound that echoes through the seemingly endless hall",
        "of pine trees is that of your own clumsy feet trying to make it through the snow.",
    ]),
    DialogueBox("...", [
        "Then suddently, you hear something breathe behind you.",
        "Had you not stepped aside swiftly, the creature behind you would have caused a far",
        "greater injury.",
    ]),
    DialogueBox("Esther", [
        "Oh come on!",
        "Must I not have a moment of peace in this forest?",
    ]),
    DialogueBox("...", [
        "The thing that just tried to attack you is a man, almost skeletal",
        "but still quite toned in build, his body hidden behind rags and a layer of",
        "clothes.",
        "A pair of elytras flap keenly from his back, along with two pairs",
        "of some strange limbs that seem to end in some sort of suction caps, covered with",
        "sharp teeth.",
    ]),
    DialogueBox("...", [
        "A body built for predation, in its entirety."
    ]),
    DialogueBox("Starving man", [
        "Shush!"
    ]),
    DialogueBox("Starving man", [
        "Can you hear that?"
    ]),
    DialogueBox("Esther", [
        "Hear what?"
    ]),
    DialogueBox("Starving man", [
        "Nothing.",
        "Silence.",
        "The forest is empty.",
    ]),
    DialogueBox("Starving man", [
        "There is barely anything left thanks to your unending butchery.",
        "We are starving, all thanks to you.",
    ]),
    DialogueBox("Esther", [
        "Excuse me?",
        "These little joyous critters of yours attacked ME!",
        "Am I really in the wrong for defending myself?",
    ]),
    DialogueBox("Starving man", [
        "Don't you dare lie to me!",
        "A lie told to me is a lie told to the great Lady Holle.",
    ]),
    DialogueBox("...", [
        "The man is becoming more and more impatient by the minute.",
        "His body is trembling, and his elytras are flapping frantically.",
    ]),
    DialogueBox("Esther", [
        "Lady who?",
        "Actually doesn't matter, I do not serve any lady that I know of.",
        "So you leave me alone and I'll leave you and your little zoo alone.",
    ]),
    DialogueBox("Starving man", [
        "Too late now.",
        "I am starving, and so is She.",
    ]),
    DialogueBox("Starving man", [
        "You will only leave through my guts, lass.",
    ]),
]

climax2 = [
    DialogueBox("...", [
        "After you rampage through another camp of the pursits, you beat their knight to a pulp.",
        "This is almost a routine at that point.",
    ]),
    DialogueBox("Esther", [
        "Just how many of you are left?",
        "Each camp looks feels a car full of infinite clowns.",
    ]),
    DialogueBox("Esther", [
        "Just how many of you are left?",
        "Going through each camp looks feels a car full of infinite clowns.",
    ]),
    DialogueBox("...", [
        "The knight is coughing blood, but is still livid enough to form a cough into a spit,",
        "directed at your boots.",
    ]),
    DialogueBox("Purist knight", [
        "Why bother talking to something as far from human as you are?",
    ]),
    DialogueBox("...", [
        "Now you are far from the wrathful type but you still decide to kick into his ribs, just",
        "to feel who's in charge.",
    ]),
    DialogueBox("Esther", [
        "I can't believe how everyone has to have some sort of grand belief about this world 'round here.",
        "Come on.",
        "It's not that deep.",
        "Who cares wether I'm human or not?",
        "I asked a question and you answer. Simple as that.",
    ]),
    DialogueBox("Purist knight", [
        "I will not answer the question of a creature full of vileness and ill intent.",
    ]),
    DialogueBox("Esther", [
        "Excuse me?",
        "Look, I'm sorry for having to do all of this. There is truly nothing personal involved.",
        "But somehow I gotta survive don't I? Same for you, and the same for every one of those looney",
        "folks who run around with all those weird limbs for some reason.",
    ]),
    DialogueBox("Purist knight", [
        "You don't need to survive. Humans do. They have a life to care for. A life full of joy and pleasure.",
        "You are no longer one of us.",
    ]),
    DialogueBox("...", [
        "You kick him in the side again, this time breaking at least a few ribs.",
    ]),
    DialogueBox("Esther", [
        "Well I worked on the serum that makes me who I am in this very moment.",
        "I think I have more right to decide wether I am or am not the human after consuming my own product.",
    ]),
    DialogueBox("Purist knight", [
        "So it was you who released this curse upon us?",
    ]),
    DialogueBox("Esther", [
        "Curse? I have saved lives. Countless more than you could.",
    ]),
    DialogueBox("Purist knight", [
        "...and taken countless more than I could ever take right after.",
    ]),
    DialogueBox("Esther", [
        "Correct. Not out of malice. I simply need to survive. All of us do. And this makes me",
        "quite a bit human don't you think?",
    ]),
    DialogueBox("Purist knight", [
        "Even a rat is a human if the threshold is this low.",
    ]),
    DialogueBox("...", [
        "You kneel on his back and force him into the ground as you shove your pistol into",
        "his neck.",
    ]),
    DialogueBox("Esther", [
        "I don't care wether I am human or not then. Look at me as an animal, look at me as a human, I do not care",
        "what some dying bald retard thinks about me in this very moment. I do however care about where your leader is.",
    ]),
    DialogueBox("...", [
        "You pull back the firing pin. His head trembles as he feels the cylinder rotate and click.",
    ]),
    DialogueBox("Esther", [
        "You oughta have one. So point me to it. I can make your death short or more painful than it is comfortable for",
        "the both of us.",
    ]),
    DialogueBox("Purist knight", [
        "Fine, you disgusting cur. But the path isn't that easy. Someone gotta lead you.",
    ]),
    DialogueBox("Esther", [
        "Okie-dokie. Lead the way then, but don't do anything stupid.",
    ]),
    DialogueBox("...", [
        "You take a bundle of ropes and tie him up properly, disarming him completely.",
        "As you do so, you hear a strange rattle nearby. The sound of a few chains shaking and something",
        "bashing against wood forcefully.",
    ]),
    DialogueBox("Esther", [
        "Will you bother explaining what that sound is?",
    ]),
    DialogueBox("Purist knight", [
        "...",
    ]),
    DialogueBox("Purist knight", [
        "Let's call it a... prisoner...",
    ]),
    DialogueBox("Esther", [
        "Prisoner huh?",
    ]),
    DialogueBox("Purist knight", [
        "I wish no good fortune for something as disgusting as you are but...",
        "you really shouldn't get near that thing.",
    ]),
    DialogueBox("Esther", [
        "I am taking no advice from some looney folk like you regarding what is safe and what is not.",
    ]),
    DialogueBox("...", [
        "The knight lets out a loud sigh, but he knows that there is no point in trying to stop you anymore.",
        "Without him interrupting, you lift the plank blocking the cage near the knight's quarters.",
    ]),
    DialogueBox("...", [
        "Various mutant creatures rush out of the cage with obvious ill intent, mainly against their captor.",
        "You either defend him, or lose all the information required to find some juicier loot at his higher-up.",
    ]),
    DialogueBox("...", [
        "Your choice is obvious.",
    ]),
]

climax2outro = [
    DialogueBox("...", [
        "Due to your bravery, the knight remains unscratched by those creatures.",
    ]),
    DialogueBox("Esther", [
        "If I wasn't there these things would have got you slain.",
        "Why do you even keep these right next to your quarters?",
        "Are you geniuinely out of your mind?",
    ]),
    DialogueBox("Purist knight", [
        "Due to orders..."
    ]),
    DialogueBox("Esther", [
        "I guess...",
    ]),
    DialogueBox("...", [
        "The sound of chains rattling still remains. Something in a dark corner of the room keeps shaking its",
        "chains furiously.",
    ]),
    DialogueBox("Esther", [
        "Oh look! We forgot one!",
    ]),
    DialogueBox("Purist knight", [
        "I will not go near that thing.",
    ]),
    DialogueBox("Esther", [
        "Well too bad, because I will.",
    ]),
    DialogueBox("...", [
        "The emergency flashlight of your suit flickers, and its light is quite dim by now, but it's still strong",
        "enough to reveal the strange creature in the corner.",
    ]),
    DialogueBox("...", [
        "Their asymmetric face - more akin to a three-eyed lynx than a human face - contorts in a disgusted",
        "grimace as you blind the poor thing with your flashlight.",
    ]),
    DialogueBox("...", [
        "However, the disgust fades almost immediately as they see that it is not the knight entering the cell,",
        "but their saviour.",
    ]),
    DialogueBox("Esther", [
        "Will you try to beat me to a pulp too if I set you free as well?",
    ]),
    DialogueBox("...", [
        "You say to yourself sarcastically but to your surprise, the creature starts clearing their throat.",
        "The sound of a quiet engine growl can be heard as he speaks.",
    ]),
    DialogueBox("Ultramagister", [
        "How scandalous!",
        "How vile!",
        "None shall speak ill of the grand Ultramagister!",
        "I am as kind as I am humble, and even though I certainly could, I would never evaporate you...",
    ]),
    DialogueBox("Ultramagister", [
        "...lest you cross my will, that is.",
        "Say. Are you here to free me? Or to make a god suffer some more?",
    ]),
    DialogueBox("...", [
        "Though your non-schalance is unrivaled, even you seem to be a little surprised to see this thing with your own eyes..",
        "Not because of how the creature acts, or how it looks like, but the fact that it is...",
        "not even a living being at its core.",
        "The last time you've seen anything like this was at the lab you worked in.",
    ]),
    DialogueBox("...", [
        "The way the parts of its skin merges, the way it is constructed, none of it can be caused by something mutating this far.",
        "This is certainly a being made by a WM-230 Geneweaver. A machine used to construct new tissue in real time, based on inputted genetic data."
    ]),
    DialogueBox("Esther", [
        "God forbid.",
        "I'm here to free you... but say...",
    ]),
    DialogueBox("Esther", [
        "What is this quiet roar?",
    ]),
    DialogueBox("Ultramagister", [
        "The thumping of my heart you mean, dear?",
        "Well if inquiring about the intestines of this powerful sorcerer is what's your greatest interest",
        "at the moment, you are nothing short of a fool.",
    ]),
    DialogueBox("Ultramagister", [
        "Of course I could rip these chains apart myself, but with such a grand surge of wild forces,",
        "I may mean a threat to you as well.",
        "Set me free, dear.",
    ]),
    DialogueBox("Esther", [
        "Don't call me dear... it's quite a bit uncanny.",
    ]),
    DialogueBox("...", [
        "You untangle its chains, and its body collapses on the ground before rising back up within the blink of an eye.",
    ]),
    DialogueBox("...", [
        "It wears a large wizard hat, probably scavanged from one of the nearby abandoned villages.",
        "The robe that covers its entire body, consisting of multiple rags and carpets stitched together, suits the role of the \"sorcerer\" quite well as well.",
        "Its frame is robust, with multiple limbs peeking out from the cloak in a shy manner. Even in appearence, it holds many secrets.",
    ]),
    DialogueBox("Ultramagister", [
        "Oh!",
        "How could I depart without my arcane chalice!",
    ]),
    DialogueBox("Esther", [
        "Your what now?",
    ]),
    DialogueBox("...", [
        "It picks up shards a shattered wine glass from the ground, followed by a gaze of disstatisfaction.",
    ]),
    DialogueBox("Ultramagister", [
        "Bugger...",
    ]),
    DialogueBox("...", [
        "The shards disappear under its cloak and come anew as a new glass, held together by some resin-like gluey liquid.",
    ]),
    DialogueBox("Esther", [
        "Are you done?",
        "Or do you have any other object you want to put your goo on?",
    ]),
    DialogueBox("Ultramagister", [
        "I can assure you that I have a much greater task now.",
        "Say... where is the Bald Imp?",
    ]),
    DialogueBox("Esther", [
        "The Bald... OH the knight?",
        "He's laying on the ground, next to this cell.",
        "I need him for something though so... do not lay a finger on-",
    ]),
    DialogueBox("...", [
        "The Ultramagister rushes out of the shed furiously, before you could do anything to stop its stride.",
        "Worried, you rush after the surprisingly agile creature.",
    ]),
    DialogueBox("...", [
        "You can't do much but stare as it takes the injured man and drags it inside its robes,",
        "with many limbs tearing him apart.",
    ]),
    DialogueBox("Purist knight", [
        "CUR!",
        "HELP ME!",
        "WE HAD AN AGREEMENT!",
    ]),
    DialogueBox("Ultramagister", [
        "You little spawn of the devil...",
        "I told you not to infuriate the grand wizard no?",
        "I did. And you did not listen.",
    ]),
    DialogueBox("...", [
        "As the knight is dragged inside the grand cloak, the many limbs begin to move in a strange sort of weaving",
        "movement. As if many little needles got ran through a thick woolen fabric.",
        "The sound of clattering from its chest begins to intensify, to the degree where it is comparable to the sound of a car starting.",
    ]),
    DialogueBox("...", [
        "Eventually though, the dead body of the knight gets thrown out. Seemingly no major damage, only an array of tiny",
        "deep holes all across the corpse."
    ]),
    DialogueBox("Ultramagister", [
        "Look at you.",
        "Even your body is useless... and a bit bitter... eww...",
    ]),
    DialogueBox("...", [
        "You take a disappointed, but not too surprised sigh."
    ]),
    DialogueBox("Esther", [
        "Good job. Real good job. I was trying to get information out of that idiot.",
        "And you just killed him.",
    ]),
    DialogueBox("Ultramagister", [
        "As the grand Ultramagister, I am lord over life and death!",
        "I decide who deserved nourishment and punishment.",
        "My judgement was flawless, as it would be in any other case.",
    ]),
    DialogueBox("Esther", [
        "Good to know that my geneweaver has ideals of its own."
    ]),
]

climax3 = [
    DialogueBox("...", [
        "The night is dark, as it is always.",
        "A swarm of winged priests gather around a lake nearby."
    ]),
    DialogueBox("...", [
        "This time though, they carry no sacrifices, nor are they",
        "accompanied by newly indoctrinated acolytes.",
    ]),
    DialogueBox("...", [
        "They all look petrified.",
        "All of them march in silence towards the lake.",
    ]),
    DialogueBox("...", [
        "Then, all of a sudden, a large flying creature casts its shadow upon the lake's water.",
    ]),
    DialogueBox("...", [
        "For but a moment, the air cools from the beat of the mysterious being's wings.",
        "Then, a crackling sound can be heard as the ground shakes from a nearby impact.",
    ]),
    DialogueBox("...", [
        "The loud noise fills you with tremor, from the bottom of your feet to your last strand of hair.",
        "The priests however, only cheer."
    ]),
    DialogueBox("...", [
        "Crowds start running towards the prophet, much to his annoyment."
    ]),
    DialogueBox("...", [
        "In this chaotic mess, not a single soul notices you.",
    ]),
    DialogueBox("...", [
        "You take a bold step forward, to inspect this heroic figure of theirs.",
        "He is more owl than man. A true angel sculpted from flesh and feathers.",
        "Not a beautiful or a graceful one, but sure as hell a mighty one.",
    ]),
    DialogueBox("Jeffrey", [
        "CHILDREN!",
        "Calm yourselved at once!",
    ]),
    DialogueBox("Jeffrey", [
        "This gathering must have a good reason to have been called.",
        "Otherwise, all of you would be crossing the will of the Stars themselves.",
    ]),
    DialogueBox("High Priestess Claudia", [
        "Five of our fellow high priests have joined the Stars above.",
        "In a single week or so.",
    ]),
    DialogueBox("Jeffrey", [
        "Outrageous!",
        "Simply unacceptable!",
    ]),
    DialogueBox("Jeffrey", [
        "The Stars themselves chose them to lead their parliament.",
        "Stating that not one but FIVE of them had failed their divine duties is nothing short",
        "of an act of blasphemy!",
    ]),
    DialogueBox("...", [
        "Not being able to convince her superior, the high priestess whips out something from a sack.",
        "Upon seeing it, the crowd lowers its voice again, as well as Jeffrey, the prophet.",
    ]),
    DialogueBox("Jeffrey", [
        "Is that wing...",
        "all that remained?",
    ]),
    DialogueBox("High Priestess Claudia", [
        "...of his body, yes.",
        "His soul however may shine above us for all of eternity.",
    ]),
    DialogueBox("Jeffrey", [
        "Who...",
        "WHO COULD BE RESPONSIBLE FOR SUCH HERESY?",
    ]),
    DialogueBox("...", [
        "The crowd starts whispering things again.",
        "They start to describe some sort of horrific creature.",
    ]),
    DialogueBox("...", [
        "Not a single pair of descriptions align.",
        "Some claim that it had tentacles, some claim it had huge needles,",
        "and some claim that the thing that attacked them had wings just like them.",
    ]),
    DialogueBox("...", [
        "One thing is present in all of the descriptions though.",
        "It was a woman wearing a coat of white."
    ]),
    DialogueBox("Jeffrey", [
        "Then...",
        "Give me two priests and I shall enforce the will of the stars with my own beak.",
    ]),
    DialogueBox("...", [
        "After gaining some lift, he flies high above the trees again,",
        "disappearing from your line of sight.",
    ]),
    DialogueBox("...", [
        "Though you decide to flee, withing a few hours two priests cross your path.",
    ]),
    DialogueBox("...", [
        "Not long after, something crashes into the ground right behind you.",
        "It's not that hard to guess who that could be.",
    ]),
]

the_alpha = [
    DialogueBox("...", [
        "You see a pack of raywolves approaching."
    ]),
    DialogueBox("...", [
        "All of them growl, but none of them dares to get",
        "close to you.",
    ]),
    DialogueBox("...", [
        "From the crowd, you see an especially big wolf",
        "approaching. Scars cover his face all over."
    ]),
    DialogueBox("...", [
        "The pack begins to march around you in circles,",
        "cutting your escape routes off."
    ]),
    DialogueBox("...", [
        "The big one however, taunts you.",
        "He wants a duel for dominance."
    ]),
]

deereater = [
    DialogueBox("...", [
        "While walking through the snow, you see a carcass."
    ]),
    DialogueBox("...", [
        "That of a deer.",
        "A large specimen, and not a young one.",
        "She probably lived a long and full life (as long and full as one can live",
        "after the third great war)."
    ]),
    DialogueBox("...", [
        "The deer's corpse is nothing like a rayelk, however.",
        "It is clean, it is beautiful...",
        "...and it is fresh.",
        "You haven't eaten fresh meat in months.",
        "Your stomach beings to growl.",
    ]),
    DialogueBox("...", [
        "You hear a voice.",
        "That of an elderly woman.",
    ]),
    DialogueBox("???", [
        "\"Come...\"",
        "\"Have a taste...\"",
        "\"I dare you...\"",
    ]),
]

the_listening_deer = [
    DialogueBox("...", [
        "A piercing screech echoes from the depths of the forest,",
        "and shortly after a deer with long, pointy spires of bone and",
        "tin crowning its head emerges from the snow.",
    ]),
    DialogueBox("...", [
        "With no eyes to see, the thing still looks straight at you",
        "and charges visiously."
    ]),
]

purification = [
    DialogueBox("...", [
        "You see two squires in a camp. Both are unarmed right now.",
        "One of them is holding some sort of crude surgical instrument.",
    ]),
    DialogueBox("...", [
        "The other...",
        "They seem to have some sort of a short horn-like thing bulging out of their forehead."
    ]),
    DialogueBox("Purist medic", [
        "So you've lost your purity.",
        "Such a shame.",
    ]),
    DialogueBox("Mutant squire", [
        "Please... you're not making this any better...",
        "Just- just chop it off already!",
    ]),
    DialogueBox("Purist medic", [
        "I'll chop it off, surely.",
        "But what if your mind got altered as well?",
        "Should I let a savage roam in our camp freely?",
    ]),
    DialogueBox("Mutant squire", [
        "PLEASE! I am not a goddamn savage!",
        "I am as sane as it gets! I swear I am!",
        "Just please get rid of this little impurity for me...",
        "I- I am too weak to do it myself...",
    ]),
    DialogueBox("Purist medic", [
        "...and that's what makes you impure.",
    ]),
    DialogueBox("...", [
        "You didn't really come here to deal with such dramatic moments",
        "but the medical supplies in the camp could come in handy."
    ]),
    DialogueBox("...", [
        "This is the moment where both of them had lost hope of ever working together again.",
        "This is your chance to act on the behalf of the mutant if you wish to do so.",
    ]),
]

prisoner_no_more = [
    DialogueBox("...", [
        "You hear sounds of battle a few tents away.",
    ]),
    DialogueBox("...", [
        "The noises fade soon enough.",
        "Sounds of flesh being torn replace the clatters and screams.",
    ]),
    DialogueBox("...", [
        "As you approach, you see some sort of broken torture device,",
        "at least five dead squires and..."
    ]),
    DialogueBox("...", [
        "...something...",
    ]),
    DialogueBox("...", [
        "The thing that feasts on the still warm corpses looks at you and leaps onto you immediately."
    ]),
]

hermit = [
    DialogueBox("...", [
        "Rushing through the camp, you see an old man.",
        "He can barely stand on his own feet without leaning on his staff.",
    ]),
    DialogueBox("Old purist", [
        "Child...",
        "I beg you to leave.",
    ]),
    DialogueBox("Old purist", [
        "Leave, and I will reward you.",
        "You're not a murderer, child."
    ])
]

show_us_how_you_shine = [
    DialogueBox("...", [
        "Three stellar priests descend upon you out of the blue."
    ]),
    DialogueBox("Priest", [
        "We heard you can shine! Like a star!"
    ]),
    DialogueBox("Priest", [
        "Yes! Yes! Like a star!"
    ]),
    DialogueBox("...", [
        "Having no idea what they're talking about, you start to wonder",
        "if it's even worth your time to negotiate with them.",
    ]),
]

ritual = [
    DialogueBox("...", [
        "On a frozen lake, you see a priestess with her gaze",
        "fixated on the still shrouded sky.",
        "She seems harmless, and that's a big word coming from your own almost-paranoid mind.",
    ]),
    DialogueBox("Stellar Priestess", [
        "Greetings, sister.",
    ]),
    DialogueBox("...", [
        "Sister? Who the hell does she think you are?",
    ]),
    DialogueBox("Stellar Priestess", [
        "You have lost your ways haven't you?",
        "You have hope in the stars no more, I can feel it...",
    ]),
    DialogueBox("Stellar Priestess", [
        "...for I have too. They will never shine upon us due to the weight of our sins."
    ]),
    DialogueBox("...", [
        "She's on the brink of crying.",
    ]),
]

featherfiend = [
    DialogueBox("...", [
        "Amidst the thick snow, you see someone.",
    ]),
    DialogueBox("...", [
        "They look clumsy, and seem to lack good",
        "posture from this great of a distance.",
    ]),
    DialogueBox("...", [
        "Their movements are slow and careful,",
        "but certainly not graceful, with them",
        "stumbling from one step to the other.",
    ]),
    DialogueBox("...", [
        "You shout at them but you get no", 
        "response in return.", 
    ]),
]

chapter1scene1 = [
    DialogueBox("...", [
        "You're sitting next to a campfire in the foot-deep snow in the forest, deep within the region",
        "you once knew as Transylvania..."
        ]),
    DialogueBox("...", [
        "...back when men and women still roamed the face of the earth, leaving their marks",
        "on every hill and every lake, that was."
        ]),
    DialogueBox("...", [
        "But thanks to their insatiable greed and mutual hatered towards eachother,",
        "these men and women decided to leave one last mark on this world before",
        "going down with it."
        ]),
    DialogueBox("...", [
        "Pillars of fire scorched the face of America, then the Middle east, then the rest of the earth.",
        "But these pillars of all-consuming flames did not last."
        ]),
    DialogueBox("...", [
        "Within minutes, their fire was gone.",
        "Within days, the clouds standing so proud above those millions of corpses had vanished too.",
        "And after a couple of weeks, it began to snow."
        ]),
    DialogueBox("...", [
        "It has been snowing ever since."
        ]),

    DialogueBox("Esther", [
        "Let's see...",
    ]),
    DialogueBox("...", [
        "Quite the funny contraption, you can't deny it.",
        "Who would have thought that aiming a gun would be this hard?",
    ]),
    DialogueBox("...", [
        "You murmur as you flip through the pages of your pistol's manual.",
    ]),
    DialogueBox("...", [
        "You used to practice shooting with your coworker back in the day.",
        "As a well trained mercenary she had no issues with using that weapon,",
        "even though she wasn't familiar with that exact model.",
        "The practice did not seem to be sufficient though.",
    ]),
    DialogueBox("...", [
        "With slightly more confidence, you raise your pistol and shoot at a hole in a tree.",
        "(for the third time already)",
    ]),
    DialogueBox("Esther", [
        "Man this is some bullshit.",
    ]),
    DialogueBox("...", [
        "You say as you miss the shot again.",
    ]),
    DialogueBox("...", [
        "It's probably not just your fault, that weapon is practically a living fossil, you've",
        "inherited from a relative who used it back during the first truly great conflict",
        "that humanity had to overcome without purging itself.",
    ]),
    DialogueBox("Esther", [
        "Well damn.",
        "Can't even hit a static target.",
        "*Sigh*",
    ]),
    DialogueBox("...", [
        "You toss the pistol to a nearby log.",
        "Enough practice for today...",
    ]),
    DialogueBox("...", [
        "This cycle repeats day after day as you wander across the forest, seeking for food and shelter.",
    ]),
    DialogueBox("...", [
        "One day though...",
    ]),
    DialogueBox("Wienmetall AntiRad suit", [
        "*Geiger counter clicking*",
    ]),
    DialogueBox("Esther", [
        "Huh? I tuned down your sensitivity a while ago buddy.",
        "What could possibly be so urgent of an issue that-",
    ]),
    DialogueBox("...", [
        "You barely move out of the way as some kind of a wild beast charges at you from behind.",
    ]),
    DialogueBox("...", [
        "You immediately grab your gun and knife.",
    ]),
]

chapter1scene2 = [
    DialogueBox("...", [
        "The beasts are now dead, their corpses fall to the ground.",
        "You breathe out in relief as they are no longer a threat to you."
    ]),
    DialogueBox("Wienmetall AntiRad suit", [
        "*Geiger counter screeching audibly*",
    ]),
    DialogueBox("...", [
        "However, there is a much greater problem than some animals trying to bite you.",
        "You notice a wide cut on your suit, letting a considerable ammount of radiation",
        "flow freely inside your body."
    ]),
    DialogueBox("...", [
        "There is one more trick up your sleeve that may let you survive this incident.",
        "You trigger a switch on the side of your suit, lounging a needle inside your ribcage.",
    ]),
    DialogueBox("Esther", [
        "GGGAAHHHHHH!",
    ]),
    DialogueBox("...", [
        "This substance will reduce the chances of radiation poisoning.",
        "For the next week or so, you're safe.",
    ]),
    DialogueBox("...", [
        "You have to find a cache of this substance immedately if you want to live longer."
    ]),
]

chapter1scene3 = [
    DialogueBox("...", [
        "As you sit by the campfire, its radiating warmth fills your almost frostbitten body.",
    ]),
    DialogueBox("...", [
        "For the first time in days, you can finally eat and rest properly."
    ]),
    DialogueBox("...", [
        "The heated can of beef and beans you used to chow on nourished you just enough to keep going.",
        "A slight hint of annoyance shows in your eyes as you notice that you don't have any more",
        "of those cans at your disposal."
    ]),
    DialogueBox("...", [
        "You decide that it is not worth panicking over starvation. You are way too tired for that anyway."
    ]),
    DialogueBox("...", [
        "You lay down next to the bright flames.",
        "The needle's punctured wound still hurts as you lay on your side, but it's nothing you can't get over."
    ]),
    DialogueBox("...", [
        "In this more or less cozy state, your ever so busy mind finally gets a bit numbber."
    ]),
    DialogueBox("...", [
        "You stop worrying about the present, and start remembering the past."
    ]),
    DialogueBox("...", [
        "Each and every night you think about her.",
        "How close she used to hold you. How safe you felt under her arms.",
    ]),
    DialogueBox("...", [
        "How her soft voice used to soothe you.",
        "How sweet her kiss tasted even when she smelt like a whole pack of freshly smoked cigars.",
    ]),
    DialogueBox("...", [
       "Who knows where she is now?",
       "This question is the only thing keeping you awake.",
    ]),
    DialogueBox("...", [
        "It takes an awfully long time before you can finally shut your eyes and fall asleep."
    ]),
    DialogueBox("...", [
        "Amongst the dense, dark branches of the forest, the last surviving rays of sunlight",
        "that managed to seep through the thick and murky clouds get lost eventually."
    ]),
    DialogueBox("...", [
        "Without a single eye noticing, the sun's light is slowly replaced by the even dimmer",
        "moonlight."
    ]),
    DialogueBox("...", [
        "Cold but still gentle winds start caressing your face as you rest by the dying fire.",
    ]),
    DialogueBox("...", [
        "Eventually, the fire is blown away and its embers begin to fade away.",
    ]),
    DialogueBox("...", [
        "Goodnight Esther."
    ]),
]

chapter1scene4 = [
    DialogueBox("...", [
        "What a bloody fight that was...",
    ]),
    DialogueBox("...", [
        "Radiation seems to twist everything in ways you would have never thought to be possible.",
    ]),
    DialogueBox("...", [
        "Regardless, you did get enough sleep to keep going.",
        "You don't want to risk shutting your eyes again for a while after this encounter.",
    ]),
    DialogueBox("...", [
        "Not getting enough sleep is only one issue though.",
        "The greater problem is the lack of livestock.",
    ]),
    DialogueBox("...", [
        "By using specialized equipment, you are able to filter radiation and harmful particles from",
        "the snow around you, so thirst should not be a problem.",
    ]),
    DialogueBox("...", [
        "But it's nearly impossible to get to any kind of food by any means.",
        "The best you can do is hope that you'll be lucky enough to find somewhere to scavange cans from."
    ]),
    DialogueBox("...", [
        "You search for hours, wandering deep in the forest until sunrise..."
    ]),
    DialogueBox("...", [
        "...and to much of your surprise, the dusky sky is just bright enough to",
        "illuminate what seems to be a trail of smoke in the distance."
    ]),
    DialogueBox("...", [
        "A day or two of navigating the woods and you'll get to live just a bit longer",
        "You will stay alive, no matter what it takes.",
    ]),
    DialogueBox("...", [
        "With these thoughts in your head, you embark on your journey to the potential food source.",
        "Whatever may cross your path, you must fight off fiercefully."
    ]),
]

chapter1scene6 = [
    DialogueBox("...", [
        "Your stomach growls as you march through the forest.",
        "The smoke signal from earlier came from the side of a mountain, which you are forced to climb."
    ]),
    DialogueBox("...", [
        "The mountainous terrain is hard to navigate, with each rock being slippery from the thick layer of",
        "ice and condensed snow on it."
    ]),
    DialogueBox("...", [
        "The biome changes too, with the sickly birch and oak trees being replaced by tall and proud pines.",
        "You are driven across the woods solely by hunger, like a starving wolf not ceasing it's pursuit",
        "until it gets to tear it's prey apart."
    ]),
    DialogueBox("...", [
        "Moments later, you see a deer staring at you from a great distance.",
        "Vines cling from it's thick hide on every spot.",
    ]),
    DialogueBox("...", [
        "Its eyes are large, covered by lush and healthy looking eyebrows."
        "The beautiful eyes of a weak and fair doe used to symbolize innocence in the old world.",
    ]),
    DialogueBox("...", [
        "Its graceful leaps among the rocks covered by thick snow truly amaze you.",
        "How can such beauty be found in a world so cruel?"
    ]),
    DialogueBox("...", [
        "Sadly, you find your answer quite quickly.",
        "As you move closer, the doe does not move an inch, and as you try to touch her",
        "fair face, it starts to twitch."
    ]),
    DialogueBox("...", [
        "Huge black ants swarm out of it in masses.",
        "The doe braces it's antlers, preparing them for engagement."
    ]),
]

chapter1scene7 = [
    DialogueBox("...", [
        "The burning acid is searing your skin and flesh form your last encounter.",
        "Even though it doesn't leave that much damage, it stings like hell."
    ]),
    DialogueBox("...", [
        "A long session of cursing is enough for you to come back to your senses however."
    ]),
    DialogueBox("...", [
        "You finally find a proper road on the mountain, making travel a bit less difficult.",
    ]),
    DialogueBox("...", [
        "With the time passing by, the sky takes a more reddish hue.",
        "Night begins to settle in, and the house is emmiting smoke once again.",
    ]),
    DialogueBox("...", [
        "The once distant pillar of smoke is now almost within arm's reach.",
    ]),
    DialogueBox("...", [
        "As you walk up the road, a group of raywolves ambush you, but the moment",
        "they see what's behind you, they all back down."
    ]),
    DialogueBox("...", [
        "What could be so intimidating that it scares even a pack of raywolves away?",
        "You look behind your back and are met with an answer."
    ]),
    DialogueBox("...", [
        "Piles.",
        "Towering piles of animal corpses. From raywolves to hivedeer, no one",
        "was left out of the carnage."
    ]),
    DialogueBox("...", [
        "Some corpses are still fresh, some are just a collection of bones.",
        "One thing unites them all though: death by blunt damage.",
    ]),
    DialogueBox("...", [
        "Who could be responsible for this kind of butchery?",
        "Well, you're about to find out soon..."
    ]),
]

chapter1scene8 = [
    DialogueBox("...", [
        "There you are.",
        "The source of the smoke.",
        "A small cabin in the woods, it's windows blocked by wooden planks.",
    ]),
    DialogueBox("...", [
        "*THUMP*",
        "*THUMP*",
        "*THUMP*",
    ]),
    DialogueBox("...", [
        "This is all you can hear from inside.",
        "A monotonous bashing noise.",
    ]),
    DialogueBox("The Listener", [
        "WHO ARE YOU?",
        "BE GONE!",
        "SILENCE!"
    ]),
    DialogueBox("...", [
        "An old man is screeching furiously from the small cabin.",
        "The fury in his voice is mixed with quite a bit of agony too."
    ]),
    DialogueBox("Esther", [
        "Just give me some food, and we're done here.",
    ]),
    DialogueBox("The Listener", [
        "DO YOU NOT HEAR ME?",
        "BE GONE!",
        "SHUT UP! SHUT UP!"
    ]),
    DialogueBox("...", [
        "He screeches as if he couldn't hear a single word you're saying.",
    ]),
    DialogueBox("Esther", [
        "As I just said, I will go away once you GIVE ME FOOD!",
    ]),
    DialogueBox("The Listener", [
        "GET THE FUCK AWAY FROM ME!",
    ]),
    DialogueBox("...", [
        "He screams from the top of his lungs.",
        "The thumping ceases for a second..."
    ]),
    DialogueBox("...", [
        "...until a copper pipe smashes one of the windows to pieces.",
        "What you see is a naked old man with huge metallic antennas",
        "poking out of his head, and a huge bloody crack on his forehead.",
        "A constant radio noise-like sound is emmited from his head."
    ]),
    DialogueBox("...", [
        "He is basically a walking skeleton, having barely anything under his skin.",
        "Despite this fact, he still manages to leap at you, swinging the",
        "pipe recklessly."
    ])
]

chapter1conclusion = [
    DialogueBox("...", [
        "After a long and exhausting fight, you pin him to the ground. You feel a good bit",
        "of pity towards the old man, though."
    ]),
    DialogueBox("...", [
        "He just lays there, motionless, only breathing and staring at you as the humming",
        "noise from his antennas still fill the air."
    ]),
    DialogueBox("Esther", [
        "I told you.",
        "All I wanted was to eat."
    ]),
    DialogueBox("...", [
        "He manages to whisper a few words so quiet that they barely stay afloat in the",
        "sea of static noise.",
    ]),
    DialogueBox("The Listener", [
        "...Lost...",
        "...my...",
        "...temper...",
        "...there...",
    ]),
    DialogueBox("Esther", [
        "Lost your temper?",
        "I could be dead thanks to this little tantrum you just threw you fucking moron.",
        "Are you out of your mind? All I wanted was food.",
    ]),
    DialogueBox("Esther", [
        "FOOD.",
    ]),
    DialogueBox("Esther", [
        "Is beating me half dead with a metal pipe really the most rational thing you could have",
        "come up with?",
    ]),
    DialogueBox("...", [
        "He seemed incredibly frustrated even before the fight, and now realizing",
        "the weights of his actions, he breaks completely.",
    ]),
    DialogueBox("The Listener", [
        "...I...",
        "...beg...",
        "...for...",
        "...your...",
        "...pardon...",
    ]),
    DialogueBox("Esther", [
        "*Sigh*",
        "I do not know who you are, but if there is a god, you definitely",
        "got to be his most unserious creation.",
        "(you mutter to yourself)",
    ]),
    DialogueBox("Esther", [
        "Well... you're a bit late with that.",
        "Your wounds look fatal to me.",
        "And bandages are quite scarce around here you know...",
    ]),
    DialogueBox("The Listener", [
        "...That's...",
        "...not much...",
        "...of an issue...",
    ]),
    DialogueBox("...", [
        "He curls up on the ground, holding his knees against his face as he",
        "keeps grabbing his forehead.",
    ]),
    DialogueBox("The Listener", [
        "...it still...",
        "",
        "...hurts...",
    ]),
    DialogueBox("Esther", [
        "What could posibly hurt so much.",
    ]),
    DialogueBox("The Listener", [
        "...The noise...",
    ]),
    DialogueBox("The Listener", [
        "...Please...",
        "...make...",
        "...the noise...",
        "...cease...",
    ]),
    DialogueBox("Esther", [
        "Ah. Makes sense.",
    ]),
    DialogueBox("Esther", [
        "Did it take you this long to ask though?",
        "If I were you I'd have done it myself already.",
    ]),
    DialogueBox("The Listener", [
        "...I am...",
        "...a coward...",
    ]),
    DialogueBox("The Listener", [
        "...I could not do it myself...",
    ]),
    DialogueBox("The Listener", [
        "...Please...",
    ]),
    DialogueBox("...", [
        "Every waking second you spend looking at the old man makes you",
        "feel worse and worse for him.",
        "He silently groans in pain even as he lays on the floor.",
    ]),
    DialogueBox("Esther", [
        "You poor thing...",
        "Are you sure you want me to do this?",
    ]),
    DialogueBox("...", [
        "The old man, with what little remains of his strength, nods.",
        "His eyelids close for the very last time.",
    ]),
    DialogueBox("...", [
        "You take your knife and slit his throat in the blink of an eye."
    ]),
    DialogueBox("...", [
        "This marks the first time you voluntarily killed a person.",
    ]),
    # DialogueBox("*STATIC*", [
    #     "░▒▓▒▓▓▒░░▒▓▓▓▒▒░▓▓░▒░░▓░░▒▓▓▒░░░▒░▓░▒░▒▓▒░░▒▓▒▒▓▓░░▒▓▒░░▒▒▓▒",
    #     "░▒▓▓▒░░░▒░▓░▒░▒▓▒░░▒▓▒▒▓▓░░▒▓▒░░▒▒▓▒░▒▓▒▓▓▒░░▒▓▓▓▒▒░▓▓░▒░░▓░",
    #     "▒▓▓░░▒▓▒░░▒▒▓▒░▒▓▒▓▓▒░░▒▓▓░▒▓▓▒░░░▒░▓░▒░▒▓▒░▓▒▒░▓▓░▒░░▓░░▒▓▒",
    #     "░▒░▓▓░▒░▓▓▒░▒░▓░▒░▒▓▒░░▓░░▒▓▓▒░░▒▓▒▓▓▒░░▒▓░▒▓▒▒▓▓░░▒▓▒░░▒▒▓▒",
    #     "▒▓▓░░▒▓▒░▓▒░░░▒░▓░▒░▒▓▒░▓▒▒░▓▓░▒░░▒▒▓▒░▒▓▒▓▓▒░░▒▓▓░▒▓░▓░░▒▓▒",
    #     "░▒▓▓▒░░░▒░▓░▒░▒▓▒░░▒▓▒▒▓▓░░▒▓▒░░▒▒▓▒░▒▓▒▓▓▒░░▒▓▓▓▒▒░▓▓░▒░░▓░",
    # ]),
    # DialogueBox("...", [
    #     "With the death of the old man, the noise coming from his head finally clears up, tuning to a",
    #     "single radio channel."
    # ]),
    # DialogueBox("???", [
    #     "▒▓▓░░▒▓▒░░░▓▒░▓▒░▒▓▒░▒░▒▒░░▒▓▒...",
    #     "▒▓▓░e▒▓▒░░░▓▒░▓▒░▒▓▒░▒░▒▒░░n▓▒...",
    #     "▒▓▓░e▒▓▒░░░▓▒░▓▒s▒▓▒░▒░▒m░░n▓▒...",
    #     "▒▓▓░e▒▓▒f ░▓▒░▓▒s▒▓▒░▒░ me░n▓▒...",
    # ]),
    # DialogueBox("...", [
    #     "That familiar soprano voice...",
    #     "It'd be so sweet to hear it after such a long time.",
    #     "But this voice is most definitely not a gleeful one.",
    # ]),
    # DialogueBox("Agnes", [
    #     "▒▓▓he▒▓▒f m▓▒░i▒s ▓▒░▒e me n▓▒...",
    #     "F▓▓he▒ ▒f m▓rci▒s ▓e░▒e me n▓▒...",
    #     "Fa▓her ▒f merci▒s le░ve me n▓t...",
    #     "Fa▓her of merci▒s leave me not...",
    # ]),
    # DialogueBox("...", [
    #     "It is her.",
    #     "Who once was your knight in shining armor.",
    #     "Completely broken, and weeping.",
    # ]),
    # DialogueBox("...", [
    #     "Your heart skips a beat.",
    # ]),
    # DialogueBox("...", [
    #     "You almost forget how you're teetering on the brink of starvation from the dread you feel in",
    #     "this very second.",
    #     "You waste no time and gather all the livestock you can find in the cabin."
    # ]),
    # DialogueBox("...", [
    #     "You must find her immedately, no matter what it takes."
    # ]),
    # DialogueBox("...", [
    #     "Before you go, you slice the old man's head clean off, carrying his skull with you from now on to hear her voice.",
    # ]),
]

chapter2scene1a = [
    DialogueBox("...", [
        "The icy wind roars between the ruined blocks of flats.",
        "Tiny flakes of snow move at such velocity that it feels like if they were cutting through",
        "your skin.",
        "The thick layers of rags and coats stacked on eachother provide enough warmth for you to",
        "not freeze to death, though you are still shivering with each step you take.",
    ]),
    DialogueBox("...", [
        "It is not only your body that is freezing though.",
        "Shivers of guilt shake your soul as well.",
    ]),
    DialogueBox("...", [
        "This dammn cold wouldn't be such a bother if it wasn't for a single press of a button.",
        "But it was bound to happen eventually no?"
    ]),
    DialogueBox("...", [
        "We kept delaying the final resolution of all problems.",
        "Humanity was destined to push the button and face the consequences.",
    ]),
    DialogueBox("...", [
        "It might sound like a cruel statement, but nuclear war almost seemed like a necessary",
        "step in achievinng progress.",
    ]),
    DialogueBox("...", [
        "Some of you still live after all.",
        "Twisted and distorted, with your survival being pushed to its limits, but you most",
        "certainly live on.",
    ]),
    DialogueBox("...", [
        "But if it is truly so that the war to end all wars was an event that was carved into stone",
        "ever since man learned to split the atom, why do you feel that guilt?",
    ]),
    DialogueBox("...", [
        # Conclusion: It might be due to the fact that you were destined to live this fate. Humanity is not a virtue but a flaw, one that leads to the demise of oneself.
        "Arriving into the heart of the once popolous city, the buildings seem to get larger.",
        "They reach high, so high that you can't even see their tops in the densely falling snow.",
    ]),
    DialogueBox("...", [
        "Almost all of the windows were shattered by the shockwaves of the nukes, their",
        "million shards scattered all across the empty streets.",
        "When the weather is calmer, they sparkle with the dense snow in the dim sunlight.",
        "It is a sight that is pleasing to the soul.",
    ]),
    DialogueBox("...", [
        "Today, their glitter is silenced by the frantic snowstorm.",
        "You're desperately seeking shelter from the storm.",
        "It is not only the storm you want to cower from, however."
    ]),
    DialogueBox("...", [
        "The snow cracks behind you, all of the little shards of galss adding to the noise.",
        "Someone is behind you.",
        "Someone has been following you for a while.",
    ]),
    DialogueBox("...", [
        "A little girl.",
        "Barely 10 years old.",
    ]),
    DialogueBox("...", [
        "An old gas mask covers her face.",
        "She looks lost, and her intentions seem to be pure.",
    ]),
    DialogueBox("Agnes", [
        "Hey! Are you okay there?",
    ]),
    DialogueBox("...", [
        "The last time you met anyone was weeks ago, and even then that was far from a friendly encounter.",
        "This brief moment of human interaction makes you able to break your focus on self loathing.",
    ]),
    DialogueBox("Little girl", [
        "...",
    ]),
    DialogueBox("...", [
        "She approaches you in a slow, clumsy manner, barely being able to lift her legs in the thick snow.",
        "You come closer to the girl in turn. You try to reach for her hand to help her get up from the snow.",
    ]),
    DialogueBox("...", [
        "...but as soon as you touch her hand, buckshot pellets drive into the thick layer of snow under your feet.",
        "Spooked by the loud shot, you take a leap backwards, and the little girl crouches down in fear.",
    ]),
    DialogueBox("...", [
        "A tall, burly man charges at you with gun in hand."
    ]),
]

chapter2scene1b = [
    DialogueBox("Grandfather", [
        "You...",
        "will not...",
        "hurt...",
        "the child...",
    ]),
    DialogueBox("...", [
        "Already on the brink of death, the old man forcefully pushes the barrel of",
        "his gun into your temple, and charges the pump.",
    ]),
    DialogueBox("...", [
        "You do not resist, not like it would be of any use anyway.",
        "You just accept your fate as he wraps his fingers around the trigger.",
    ]),
    DialogueBox("Little girl", [
        "No!",
        "Don't do it papa!",
        "It would be silly!",
    ]),
    DialogueBox("...", [
        "The man looks to his left, where the girl drags on his trenchcoat's arm.",
    ]),
    DialogueBox("...", [
        "That was a call way too close.",
        "The old man slowly raises up his gun, with great suspicion lurking on his face still.",
    ]),
    DialogueBox("...", [
        "As he examines your half-dead body more throughoutly, he discovers a small detail on",
        "your right shoulder.",
        "It is a tatoo, covered by a few scars.",
    ]),
    DialogueBox("Grandfather", [
        "...der Schlangenzahn zweites Regiment...",
        "...are you a solider, girl?",
    ]),
    DialogueBox("Agnes", [
        "*you nod slowly*"
    ]),
    DialogueBox("Grandfather", [
        "...fought like one.",
    ]),
    DialogueBox("...", [
        "He searches his pockets for a first aid kit and begins stitching you together.",
        "You faint slowly.",
    ]),
]