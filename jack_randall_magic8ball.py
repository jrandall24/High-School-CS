import random

while True:
    question = input("What do you want to ask? ")
    responses = ["Yes", "Nope", "I'm not sure", "Ask later, I need to calculate my answer", "Without a doubt", "My sources say no", "Uh oh, I'm getting word that the answer is no"]
    print(random.choice(responses))
