import random
from termcolor import cprint





def ask_question(index, question, options):
    print(f'{index}: {question}')
    for option in options:
        cprint(f'{option}', 'blue')

    return input("Give you answer (A/B/C/D: )").upper().strip()

def run_quiz(quiz):
    score=0
    random.shuffle(quiz)
    for index, item in enumerate(quiz, 1):
        answer=ask_question(index, item["question"], item["options"])
        if answer == item['answer']:
            cprint("Correct!", 'green' )
            score=score+1
        else:
           cprint(f"Sorry, that's not correct. Correct answer is : {item['answer']}", 'red')
        print("\n")
    print(f"Your final score is {score}/{len(quiz)}")


def main():
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

    run_quiz(quiz)


if __name__ == '__main__':
    main()