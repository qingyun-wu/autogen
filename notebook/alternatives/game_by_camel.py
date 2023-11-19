import random


def generate_random_hint():
    hints = [
        "Try exploring the northern part of the map.",
        "Check the abandoned house for a hidden passage.",
        "Use your special ability to reveal hidden objects.",
        "Talk to the NPC in the town square for a clue.",
        "Look for a symbol on the wall near the dungeon entrance.",
    ]
    random_hint = random.choice(hints)
    return random_hint


def analyze_gaming_style():
    preferences = {}

    print("Please answer the following questions to help us analyze your gaming style and preferences:")

    preferences["difficulty"] = input("What difficulty level do you usually prefer? (Easy, Medium, Hard): ")
    preferences["playstyle"] = input(
        "Do you prefer a more aggressive or defensive playstyle? (Aggressive, Defensive): "
    )
    preferences["genre"] = input("What is your favorite game genre? ")

    return preferences


def provide_real_time_hint(preferences):
    hints = {
        "Easy": "Consider exploring more challenging areas to find hidden treasures.",
        "Medium": "Try interacting with different NPCs to uncover secret quests.",
        "Hard": "Look for hidden paths and shortcuts to progress further in the game.",
        "Aggressive": "Focus on offensive abilities and take down enemies quickly.",
        "Defensive": "Utilize defensive tactics and strategies to survive tough encounters.",
        "Genre": "In your favorite genre, there might be hidden easter eggs or references to discover.",
    }

    hint = ""

    for key, value in preferences.items():
        if value in hints:
            hint += hints[value] + " "

    return hint.strip()
