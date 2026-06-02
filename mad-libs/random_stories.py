import random

# Step 1: Ask for words
adj1 = input("Enter an adjective: ")
noun1 = input("Enter a noun: ")
verb = input("Enter a verb: ")
adverb = input("Enter an adverb (ends in -ly): ")
place = input("Enter a place: ")
adj2 = input("Enter another adjective: ")
noun2 = input("Enter another noun: ")

# Step 2: List of story templates
stories = [
    f"""
    Today, I saw a {adj1} {noun1} at the {place}.
    It started to {verb} {adverb} and grabbed a {adj2} {noun2}.
    Everyone was shocked!
    """,

    f"""
    In {place}, a {adj1} {noun1} decided to {verb} {adverb}.
    Suddenly, a {adj2} {noun2} appeared out of nowhere!
    It was the weirdest day ever.
    """,

    f"""
    Once upon a time, a {adj1} {noun1} lived in {place}.
    Every day, it would {verb} {adverb} with a {adj2} {noun2}.
    They became best friends!
    """
]

# Step 3: Pick a random story
story = random.choice(stories)

# Step 4: Print it
print(story)
