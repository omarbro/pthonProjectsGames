import random
from termcolor import cprint

quiz=[
    {
        'question':'What is the capital of France?',
        'options':['A. NICE', 'B. LYON', 'C.DHAKA', 'D.PARIS'],
        'answer': 'D'
    },
    {
        'question':'What is the capital of Finland?',
        'options':['A. NICE' , 'B. LYON', 'C.HELSINKI', 'D.PARIS'],
        'answer': 'C'
    },
    {
        'question':'What is the capital of NORWAY?',
        'options':['A. NICE', 'B. OSLO', 'C.DHAKA', 'D.PARIS'],
        'answer': 'B'
    }
]

random.shuffle(quiz)
score=0

for index, item in enumerate(quiz, 1):
    print(f'{index}: {item["question"]}')
    for option in item['options']:
        cprint(f'{option}', 'blue')

    answer = input("Give you answer (A/B/C/D: )").upper().strip()
    if answer == item['answer']:
        cprint("Correct!", 'green' )
        score=score+1
    else:
        print(f"Sorry, that's not correct.Correct answer is : {item['answer']}", 'red')


print(f"Your final score is {score}/{len(quiz)}")


