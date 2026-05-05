#1-importa random madule
import random
#2-create subjects
subjects = [
    "Shahrukh khan ",
    "Babar azam",
    "A group of footballers",
    "Cab driver from islo",
]
actions = [
    "Eats goll ghappy",
    "Declare war",
    "Orders",
    "Celebrates",
]
places_or_things = [
    "At daman e koh",
    "At shaker parian",
    "At faisal mosque",
    "At bari imam",
] 

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    places_or_thing = random.choice(places_or_things)

    headline = f"BREAKING NEWS: {subject} {action} {places_or_thing}"
    print ("\n" + headline)

    user_input = input("\n do you want another headline? (yes/no)").strip().lower()
    if user_input =="no":
        print("\n Thanks for using fake headline generator have a fun day")
        break
    