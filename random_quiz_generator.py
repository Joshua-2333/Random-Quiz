import random

CAPITALS = {
    'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
    'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
    'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise',
    'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines',
    'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge',
    'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston',
    'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson',
    'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln',
    'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
    'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville',
    'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier',
    'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston',
    'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne',
}


for quiz_num in range(35):

    quiz_file = open(
        f"capitals_quiz_{quiz_num + 1}.txt",
        "w",
        encoding="utf-8"
    )

    answer_file = open(
        f"capitals_quiz_answers_{quiz_num + 1}.txt",
        "w",
        encoding="utf-8"
    )

    quiz_file.write("Name:\n\n")
    quiz_file.write("Date:\n\n")
    quiz_file.write("Period:\n\n")

    quiz_file.write(
        "                    "
        f"State Capitals Quiz (Form {quiz_num + 1})\n\n"
    )

    states = list(CAPITALS.keys())
    random.shuffle(states)


    for question_num in range(50):

        state = states[question_num]
        correct_answer = CAPITALS[state]

        wrong_answers = list(CAPITALS.values())
        wrong_answers.remove(correct_answer)

        wrong_answers = random.sample(wrong_answers, 3)

        answer_options = wrong_answers + [correct_answer]

        random.shuffle(answer_options)

        quiz_file.write(
            f"{question_num + 1}. What is the capital of {state}?\n"
        )

        letters = ["A", "B", "C", "D"]

        for i in range(4):
            quiz_file.write(
                f"    {letters[i]}. {answer_options[i]}\n"
            )

        quiz_file.write("\n")

    quiz_file.close()
    answer_file.close()