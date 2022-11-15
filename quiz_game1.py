questions = {
    "Who created Python?: ": "A",
    "What year was Python created?: ": "B",
    "Python is tributed to which comedy group?: ": "C",
    "Is the Earth round?: ": "A"
}

options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
           ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
           ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
           ["A. True", "B. False", "C. sometimes", "D. What's Earth?"]]


def new_game():

    questions_num = 1
    quesses = []
    correct_answer = 0
    for key in questions:
        print(key)
        print('________________')
        for el in options[questions_num - 1]:
            print(el)
        print('________________')
        quess = input("Please enter answer (A, B, C, D) :").upper()
        quesses.append(quess)
        correct_answer += check_answer(questions.get(key), quess)
        questions_num += 1
    display_score(correct_answer, len(quesses))


def check_answer(answer, quess):
    if answer == quess:
        print("CORRECT !")
        return 1
    else:
        print("WRONG !")
        return 0


def display_score(correct_ans, quesses):
    total = (correct_ans / quesses) * 100
    print("your total score is :", total, "%")


def play_again():
    response = input("Do you wanna play again? (yes, no) : ").upper()
    if response == "YES":
        return True
    elif response == 'NO':
        return False


new_game()


def main():
    while play_again():
        new_game()
    print("BYEEE!")


main()