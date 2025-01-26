# Import the random library to use for the dice later
import random

# Define Variables
numLives = 10           # number of player's lives remaining
mNumLives = 12          # number of monster's lives remaining

diceOptions = list(range(1,7))

weapons = ["Fist", "knife", "Club", "Gun", "Bomb", "Nuclear bomb"]
print("Available weapons:")
for x, weapon in enumerate(weapons, start=1):
    print(f"{x} {weapon}")
combatStrength = int(input("\nEnter your combat Strength(Number between 1-6): "))

if(combatStrength < 1 or combatStrength > 6):
    print("Input must be an integer between 1-6")
else:
    mCombatStrength = int(input("Enter the monster's combat Strength: "))
    if(mCombatStrength  < 1 or mCombatStrength > 6):
        print("Input must be an integer between 1-6")
    else:
        input("\nRoll the dice for your health points (Press enter): ")
healthPoints = random.choice(diceOptions)
print("You rolled " + str(healthPoints) + " health points")

input("Roll the dice for the monster's health points (Press enter): ")
mHealthPoints = random.choice(diceOptions)
print("You rolled " + str(mHealthPoints) + " health points for the monster")

input("Roll the dice to see if you find a healing potion (Press enter): ")
healingPotion = random.choice([0, 1])
print("Have you found a healing potion?: " + str(bool(healingPotion)))

#Battle layout
print("\nBattle Sequence:")
for j in range(1, 20):
    print(f"\nRound {j}:")
    
    #Roll dice for hero and monster
    hRoll = random.choice(diceOptions)
    mRoll = random.choice(diceOptions)
    
    #Add dice roll to combat strength
    hero_strength = combatStrength + hRoll
    monster_strength = mCombatStrength + mRoll
    
    #Selected weapon for both hero and monster
    heroWeapon = min(hRoll - 1, len(weapons) - 1)
    monsterWeapon = min(mRoll - 1, len(weapons)- 1) 
    hSelectedWeapon = weapons[heroWeapon]
    mSelectedWeapon = weapons[monsterWeapon]
    print(f"Hero's weapon: {hSelectedWeapon}")
    print(f"Monster's weapon: {mSelectedWeapon}")

    
    # Determine winner
    if hero_strength > monster_strength:
        winner = "Hero"
    elif hero_strength < monster_strength:
        winner = "Monster"
    else:
        winner = "Draw"
    
    # Print battle details
    print(f"Hero strength: {hero_strength}")
    print(f"Monster strength: {monster_strength}")
    print(f"Winner: {winner}")
    
    # Break condition
    if j == 11:
        print("\nSudden Battle Truce! The fight ends here.")
        break