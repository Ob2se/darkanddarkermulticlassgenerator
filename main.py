import DarkClasses
import os

perkCombs = 0
skillCombs = 0

perks = [
    DarkClasses.barbarianPerks,
    DarkClasses.bardPerks,
    DarkClasses.clericPerks,
    DarkClasses.fighterPerks,
    DarkClasses.rangerPerks,
    DarkClasses.roguePerks,
    DarkClasses.warlockPerks,
    DarkClasses.wizardPerks
]

perks = [x for xs in perks for x in xs]

skills = [
    DarkClasses.barbarianSkills,
    DarkClasses.bardSkills,
    DarkClasses.clericSkills,
    DarkClasses.fighterSkills,
    DarkClasses.rangerSkills,
    DarkClasses.rogueSkills,
    DarkClasses.wizardSkills,
    DarkClasses.warlockSkills
]

skills = [x for xs in skills for x in xs]

spells = [
    DarkClasses.wizardSpells,
    DarkClasses.clericSpells,
    DarkClasses.bardSongs,
    DarkClasses.warlockSpells
]

spells = [x for xs in spells for x in xs]

def generateNumber():
    seed = hash(int.from_bytes(os.urandom(12), byteorder="big"))
    seed = (seed * 1103515245 + 12345) % (2 ** 31)
    return seed

def getFactorial(n):
    return 1 if (n==1 or n==0) else n * getFactorial(n - 1)

def calculateCombinations():
    numForBarb = int(len(DarkClasses.barbarianPerks))
    numForBarbSkills = len(DarkClasses.barbarianSkills)
    numForBard = len(DarkClasses.bardPerks)
    numForBardSkills = len(DarkClasses.bardSkills)
    numForCleric = len(DarkClasses.clericPerks)
    numForClericSkills = len(DarkClasses.clericSkills)
    numForFighter = len(DarkClasses.fighterPerks)
    numForFighterSkills = len(DarkClasses.fighterSkills)
    numForRanger = len(DarkClasses.rangerPerks)
    numForRangerSkills = len(DarkClasses.rangerSkills)
    numForRogue = len(DarkClasses.roguePerks)
    numForRogueSkills = len(DarkClasses.rogueSkills)
    numForWarlock = len(DarkClasses.warlockPerks)
    numForWarlockSkills = len(DarkClasses.warlockSkills)
    numForWizard = len(DarkClasses.wizardPerks)
    numForWizardSkills = len(DarkClasses.wizardSkills)

    numberOfPerks = numForBarb + numForBard + numForCleric + numForFighter + numForRanger + numForRogue + numForWarlock + numForWizard
    numberOfSkills = numForBarbSkills + numForBardSkills + numForClericSkills + numForFighterSkills + numForRangerSkills + numForRogueSkills + numForWarlockSkills + numForWizardSkills

    global perkCombs
    global skillCombs

    perkCombs = numberOfPerks - 4
    perkCombs = getFactorial(perkCombs)
    perkCombs = getFactorial(4) * perkCombs
    perkCombs = getFactorial(numberOfPerks) / perkCombs
    print(perkCombs)

    skillCombs = numberOfSkills - 2
    skillCombs = getFactorial(skillCombs)
    skillCombs = getFactorial(2) * skillCombs
    skillCombs = getFactorial(numberOfSkills) / skillCombs
    print(skillCombs)

calculateCombinations()
print(f"""
███╗   ███╗██╗   ██╗██╗  ████████╗██╗ ██████╗██╗      █████╗ ███████╗███████╗     ██████╗ ███████╗███╗   ██╗███████╗██████╗  █████╗ ████████╗ ██████╗ ██████╗ 
████╗ ████║██║   ██║██║  ╚══██╔══╝██║██╔════╝██║     ██╔══██╗██╔════╝██╔════╝    ██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
██╔████╔██║██║   ██║██║     ██║   ██║██║     ██║     ███████║███████╗███████╗    ██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██████╔╝███████║   ██║   ██║   ██║██████╔╝
██║╚██╔╝██║██║   ██║██║     ██║   ██║██║     ██║     ██╔══██║╚════██║╚════██║    ██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗
██║ ╚═╝ ██║╚██████╔╝███████╗██║   ██║╚██████╗███████╗██║  ██║███████║███████║    ╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║
╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝   ╚═╝ ╚═════╝╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝     ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
      There are a possible {int(perkCombs)} perk combinations and a possible {int(skillCombs)} skill combinations!                                                                                                                                                      
      
      -By Ob2se""")


def baseClass():
    print("Choose base class:")
    print("1. Barbarian")
    print("2. Bard")
    print("3. Cleric")
    print("4. Fighter")
    print("5. Ranger")
    print("6. Rogue")
    print("7. Warlock")
    print("8. Wizard")
    print("Select a number: ")
    baseClassChoice(input())


def baseClassChoice(choice):
    match choice:
        case "1":
            classChoice = "Barbarian"
            confirmChoice(classChoice)
        case "2":
            classChoice = "Bard"
            confirmChoice(classChoice)
        case "3":
            classChoice = "Cleric"
            confirmChoice(classChoice)
        case "4":
            classChoice = "Fighter"
            confirmChoice(classChoice)
        case "5":
            classChoice = "Ranger"
            confirmChoice(classChoice)
        case "6":
            classChoice = "Rogue"
            confirmChoice(classChoice)
        case "7":
            classChoice = "Warlock"
            confirmChoice(classChoice)
        case "8":
            classChoice = "Wizard"
            confirmChoice(classChoice)
        case _:
            print("Please select a number 1-8")
            baseClass()


def getASkill():
    randomNumber = generateNumber()
    index = randomNumber % len(skills)
    return index

def getAPerk():
    randomNumber = generateNumber()
    index = randomNumber % len(perks)
    return index

def getClassSkillPerk(cls):
    randomNumber = generateNumber()
    index = randomNumber % len(cls)
    return index

def randomSkills(answer):
    match answer:
        case "1":
            skillIndex = getASkill()
            print("Skill: " + skills[skillIndex])
        case "2":
            skillIndex1 = getASkill()
            skillIndex2 = getASkill()
            print("Skills: " + skills[skillIndex1] + " and " + skills[skillIndex2])
            
def randomPerks(answer):
    match answer:
        case "1":
            perkIndex = getAPerk()
            print("Perk: " + perks[perkIndex])
        case "2":
            perkIndex1 = getAPerk()
            perkIndex2 = getAPerk()
            print("Perks: " + perks[perkIndex1] + " and " + perks[perkIndex2])
        case "3":
            perkIndex1 = getAPerk()
            perkIndex2 = getAPerk()
            perkIndex3 = getAPerk()
            print("Perks: " + perks[perkIndex1] + ", " + perks[perkIndex2] + " and " + perks[perkIndex3])
        case "4":
            perkIndex1 = getAPerk()
            perkIndex2 = getAPerk()
            perkIndex3 = getAPerk()
            perkIndex4 = getAPerk()
            print("Perks: " + perks[perkIndex1] + ", " + perks[perkIndex2] + ", " + perks[perkIndex3] + " and " + perks[perkIndex4])


def confirmChoice(classChoosen):
    print(classChoosen + "? (Y/N)")
    answer = input().lower()
    match answer:
        case "y":
            randomOrSpecific()
        case "n":
            baseClass()


def specificClass():
    print("Choose base class:")
    print("1. Barbarian")
    print("2. Bard")
    print("3. Cleric")
    print("4. Fighter")
    print("5. Ranger")
    print("6. Rogue")
    print("7. Warlock")
    print("8. Wizard")
    print("Select a number: ")
    multiClassChoice(input())


def multiClassChoice(choice):
    
    match choice:
        case "1":

            classChoice = "Barbarian"
            barbarianSkills = list(DarkClasses.barbarianSkills)
            barbarianPerks = list(DarkClasses.barbarianPerks)
            print("How many combinations? (numerical value)")
            numOfCombs = int(input())
            print("How many skills? (1-2)")
            skillsInt = input()
            print("How many perks? (1-4)")
            perksInt = input()
            for i in range(numOfCombs):
                pickedSkills = []
                skillsIndexs = []
                pickedPerks = []
                for x in range(int(skillsInt)):
                    index = getClassSkillPerk(barbarianSkills)
                    pickedSkills.append(barbarianSkills[index])

                for z in range(int(perksInt)):
                    index = getClassSkillPerk(barbarianPerks)
                    pickedPerks.append(barbarianPerks[index])
                
                print("Skills: ", *pickedSkills, sep=', ')

                print("Perks: ", *pickedPerks, sep=', ')
            
        case "2":

            classChoice = "Bard"
            bardSkills = list(DarkClasses.bardSkills)
            bardPerks = list(DarkClasses.bardPerks)
            print("How many combinations? (numerical value)")
            numOfCombs = int(input())
            print("How many skills? (1-2)")
            skillsInt = input()
            print("How many perks? (1-4)")
            perksInt = input()
            for i in range(numOfCombs):
                pickedSkills = []
                pickedPerks = []
                for x in range(int(skillsInt)):
                    pickedSkills.append(bardSkills[getClassSkillPerk(bardSkills)])

                for z in range(int(perksInt)):
                    pickedPerks.append(bardPerks[getClassSkillPerk(bardPerks)])
                
                print("Skills: ", *pickedSkills, sep=', ')

                print("Perks: ", *pickedPerks, sep=', ')
        case "3":

            classChoice = "Cleric"
            clericSkills = list(DarkClasses.clericSkills)
            clericPerks = list(DarkClasses.claricPerks)
            print("How many combinations? (numerical value)")
            numOfCombs = int(input())
            print("How many skills? (1-2)")
            skillsInt = input()
            print("How many perks? (1-4)")
            perksInt = input()
            for i in range(numOfCombs):
                pickedSkills = []
                pickedPerks = []
                for x in range(int(skillsInt)):
                    pickedSkills.append(clericSkills[getClassSkillPerk(clericSkills)])

                for z in range(int(perksInt)):
                    pickedPerks.append(clericPerks[getClassSkillPerk(clericPerks)])
                
                print("Skills: ", *pickedSkills, sep=', ')

                print("Perks: ", *pickedPerks, sep=', ')
        case "4":

            classChoice = "Fighter"
            fighterSkills = list(DarkClasses.fighterSkills)
            fighterPerks = list(DarkClasses.fighterPerks)
            print("How many combinations? (numerical value)")
            numOfCombs = int(input())
            print("How many skills? (1-2)")
            skillsInt = input()
            print("How many perks? (1-4)")
            perksInt = input()
            for i in range(numOfCombs):
                pickedSkills = []
                pickedPerks = []
                for x in range(int(skillsInt)):
                    pickedSkills.append(fighterSkills[getClassSkillPerk(fighterSkills)])

                for z in range(int(perksInt)):
                    pickedPerks.append(fighterPerks[getClassSkillPerk(fighterPerks)])
                
                print("Skills: ", *pickedSkills, sep=', ')

                print("Perks: ", *pickedPerks, sep=', ')
        case "5":

            classChoice = "Ranger"
            rangerSkills = list(DarkClasses.rangerSkills)
            rangerPerks =list(DarkClasses.ranggerPerks)
            print("How many combinations? (numerical value)")
            numOfCombs = int(input())
            print("How many skills? (1-2)")
            skillsInt = input()
            print("How many perks? (1-4)")
            perksInt = input()
            for i in range(numOfCombs):
                pickedSkills = []
                pickedPerks = []
                for x in range(int(skillsInt)):
                    pickedSkills.append(rangerSkills[getClassSkillPerk(rangerSkills)])

                for z in range(int(perksInt)):
                    pickedPerks.append(rangerPerks[getClassSkillPerk(rangerPerks)])
                
                print("Skills: ", *pickedSkills, sep=', ')

                print("Perks: ", *pickedPerks, sep=', ')

        case "6":

            classChoice = "Rogue"
            rogueSkills = list(DarkClasses.rogueSkills)
            roguePerks = list(DarkClasses.roguePerks)
            print("How many combinations? (numerical value)")
            numOfCombs = int(input())
            print("How many skills? (1-2)")
            skillsInt = input()
            print("How many perks? (1-4)")
            perksInt = input()
            for i in range(numOfCombs):
                pickedSkills = []
                pickedPerks = []
                for x in range(int(skillsInt)):
                    pickedSkills.append(rogueSkills[getClassSkillPerk(rogueSkills)])

                for z in range(int(perksInt)):
                    pickedPerks.append(roguePerks[getClassSkillPerk(roguePerks)])
                
                print("Skills: ", *pickedSkills, sep=', ')

                print("Perks: ", *pickedPerks, sep=', ')
        case "7":

            classChoice = "Warlock"
            warlockSkills = list(DarkClasses.warlockSkills)
            warlockPerks = list(DarkClasses.warlockPerks)
            print("How many combinations? (numerical value)")
            numOfCombs = int(input())
            print("How many skills? (1-2)")
            skillsInt = input()
            print("How many perks? (1-4)")
            perksInt = input()
            for i in range(numOfCombs):
                pickedSkills = []
                pickedPerks = []
                for x in range(int(skillsInt)):
                    pickedSkills.append(warlockSkills[getClassSkillPerk(warlockSkills)])

                for z in range(int(perksInt)):
                    pickedPerks.append(warlockPerks[getClassSkillPerk(warlockPerks)])
                
                print("Skills: ", *pickedSkills, sep=', ')

                print("Perks: ", *pickedPerks, sep=', ')
        case "8":

            classChoice = "Wizard"
            wizardSkills = list(DarkClasses.wizardSkills)
            wizardPerks = list(DarkClasses.wizardPerks)
            print("How many combinations? (numerical value)")
            numOfCombs = int(input())
            print("How many skills? (1-2)")
            skillsInt = input()
            print("How many perks? (1-4)")
            perksInt = input()
            for i in range(numOfCombs):
                pickedSkills = []
                pickedPerks = []
                for x in range(int(skillsInt)):
                    pickedSkills.append(wizardSkills[getClassSkillPerk(wizardSkills)])

                for z in range(int(perksInt)):
                    pickedPerks.append(wizardPerks[getClassSkillPerk(wizardPerks)])
                
                print("Skills: ", *pickedSkills, sep=', ')

                print("Perks: ", *pickedPerks, sep=', ')
        case _:
            print("Please select a number 1-8")

def redo():
    print("Go again? (Y/N)")
    again = input().lower()
    if again == 'y':
        randomOrSpecific()
    elif again == 'n':
        print("Exiting...")
        exit()
    else:
        print("invalid option")
        redo()

def randomOrSpecific():
    print("Would you like to multiclass with a all classes, or a specific class? (random/specific)")
    answer = input().lower()
    match answer:
        case "random":
            print("How many combinations? (numerical value)")
            numOfCombs = int(input())
            print("How many skills? (1-2)")
            skillsInt = input()
            print("How many perks? (1-4)")
            perksInt = input()
            for i in range(numOfCombs):
                randomSkills(skillsInt)
                randomPerks(perksInt)
            redo()
        case "specific":
            specificClass()
            redo()

baseClass()