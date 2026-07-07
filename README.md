# Random Quiz Generator 

A Python program that automatically creates randomized US state capitals quizzes and answer keys.

This project was built using concepts from **Automate the Boring Stuff with Python** and demonstrates working with dictionaries, files, loops, and the random module.

## Features

- Generates 35 unique quiz files
- Generates 35 matching answer key files
- Creates 50 multiple-choice questions per quiz
- Randomizes the order of questions
- Randomizes answer choices
- Provides 1 correct answer and 3 random incorrect answers
- Automatically creates answer keys

## How It Works

The program stores US states and their capitals in a Python dictionary.

Example:

```python
CAPITALS = {
    "California": "Sacramento",
    "Texas": "Austin"
}
```

The program then:

1. Creates quiz and answer key text files
2. Shuffles the list of states
3. Generates 50 questions
4. Creates four answer choices:
   - One correct capital
   - Three random incorrect capitals
5. Shuffles the answer choices
6. Writes the quiz and answer key to files

## Example Quiz Output

```
Name:

Date:

Period:

                    State Capitals Quiz (Form 1)

1. What is the capital of Vermont?
    A. Trenton
    B. Montpelier
    C. Baton Rouge
    D. Topeka
```

## Example Answer Key

```
1. B
2. C
3. A
```

## Installation

Clone this repository:

```bash
git clone git@github.com:Joshua-2333/Random-Quiz.git
```

Navigate into the project:

```bash
cd Random-Quiz
```

Run the program:

```bash
python random_quiz_generator.py
```

## Generated Files

The program creates:

```
capitals_quiz_1.txt
capitals_quiz_2.txt
...
capitals_quiz_35.txt

capitals_quiz_answers_1.txt
capitals_quiz_answers_2.txt
...
capitals_quiz_answers_35.txt
```

## Technologies Used

- Python 3
- random module
- File handling
- Dictionaries
- Loops

## What I Learned

Through this project I practiced:

- Reading and writing files with Python
- Using dictionaries to store structured data
- Generating randomized content
- Automating repetitive tasks
- Creating programs that generate useful documents

## Future Improvements

Possible improvements:

- Add support for different quiz topics
- Allow the user to choose the number of quizzes
- Add a graphical user interface (GUI)
- Export quizzes as PDFs
- Add difficulty levels
