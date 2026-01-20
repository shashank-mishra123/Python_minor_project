# create a fake new generator 

# using random method
import random

# for subject creating a list
subjects=[
    "Rahul Gandhi",
    "Akhilesh yadav",
    "Sachin Tendurker",
    "Abhay",
    "Gaurv",
    "Monkey"
]

# for action create list
actions =[
    "eating",
    "danching",
    "runing",
    "cry",
    "play",
    "happy",
    "laugh",
]

# for object create list
objects= [
    "river",
    "red fort",
    "allahabad",
    "stadium",
    "noida"
]

# using while loop
while True:
    subject=random.choice(subjects)
    action=random.choice(actions)
    object=random.choice(objects)

    fake_news=f"Breaking news {subject} {action} {object} "
    print(fake_news)

    user=input("you want another news (yes/no)").strip().lower()
    if user=="no":
        break




