def game():
    answers = []
    correct_answer = 0
    question_num = 1
    print("there are four qutions to be answered")
    for key in questions:
        print("--------------------------------------------------")
        print(key)
        print("--------------------------------------------------")
        for i in options[question_num-1]:
            print(i)

        my_answer = input("enter (A, B, C, D): ").upper()
        answers.append(my_answer)
        correct_answer += answer_checker(questions.get(key), my_answer)
        question_num += 1
    display_scores(correct_answer, answers)



def answer_checker(ans, answer):


    if ans == answer:
        print('correct!')
        return 1
    else:
        print('wrong!')
        return 0


def display_scores(correct_answer, answers):
    print("-----------------------------")
    print("RESULTS")
    print("-----------------------------")
    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end="  ")
    print()

    print("My_Answers: ", end="")
    for i in answers:
        print(i, end="  ")
    print()

    score = int(correct_answer/len(questions)*100)
    print(f"your score is {score}%")


def play_again():
    response = input("Do you want to play again? (yes or no): ").upper()
    if response == "YES":
        return True
    else:
        return False
# --------------------------------------------------
# dictionary of questions and their correct options
questions = {

    "1. what is Formation evaluation": "C",
    "2. what is capillarity": "A",
    "3. state newton's third law": "B",
    "4. what are the types of source rocks we have": "D"
}
# options for the questions nested list
options = [["A. formation evaluation is the evaluation of formation",
            "B. formation evaluation is the process where by evaluate formations to get information",
            "C. formation evaluation is the process of interpreting a combination of measurement taken from the well bore to detect and quantify oil and gas reserve in the rock adjacent to the well",
            "D. none of the above"],
           ["A. capillarity is the tendency of a liquid to rise or fall in a narrow tube",
            "B. it is the ability id a liquid to wet glass",
            "C. it is the properity of the liquid that describe hw it burns in air",
            "D. none of the above"],
           ["A. sum of forces equals to zero",
            "B. for every action, there is equal but opposite reaction",
            "C. upward forces are parallel to downward forces",
            "D. none of the above"],
           ["A.anticline, salt-dome, limestone",
            "B.mud-rock, silts-and",
            "C. sandstones, conglomerate",
            "D. potential source rock, effective source rock"]]

game()
while play_again():
    game()
print("byeeeeee")