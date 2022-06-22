# write your code here
import random

MSG_LEVEL = "Which level do you want? Enter a number:"
MSG_LEVEL_1 = "1 - simple operations with numbers 2-9"
MSG_LEVEL_2 = "2 - integral squares of 11-29"
MSG_MARK = "Your mark is"
MSG_SAVE_RESULT = "Would you like to save the result? Enter yes or no."
MSG_NAME = "What is your name?"
MSG_SAVED = 'The results are saved in "results.txt".'
MSG_ERROR_FORMAT = "Incorrect format."
NUMBER_OF_TASKS = 5

op_func = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
}

level_description = {
    1: MSG_LEVEL_1[3:],
    2: MSG_LEVEL_2[3:]
}


class FormatException(Exception):
    def __str__(self):
        return MSG_ERROR_FORMAT


def generate_task(lvl):
    if lvl == 1:
        x = random.randint(2, 9)
        y = random.randint(2, 9)
        op = random.choice([k for k in op_func.keys()])
        return f'{x} {op} {y}'
    elif lvl == 2:
        x = random.randint(11, 29)
        return f'{x}'


def check_answer(answer, task, lvl):
    if lvl == 1:
        answer = int(answer)
        task = task.split()
        x = int(task[0])
        op = task[1]
        y = int(task[2])
        return answer == op_func[op](x, y)
    elif lvl == 2:
        return int(answer) == int(task) ** 2


def print_score(correct_answers):
    print(f'{MSG_MARK} {correct_answers}/{NUMBER_OF_TASKS}.', end=' ')


def validate_answer():
    while True:
        user_answer = input()
        try:
            if not user_answer.lstrip("+-").isnumeric():
                raise FormatException
        except FormatException as err:
            print(err)
        else:
            return user_answer


def validate_level():
    while True:
        lvl = input()
        try:
            if not lvl.isnumeric():
                raise FormatException
            if not 1 <= int(lvl) <= 2:
                raise FormatException
        except FormatException as err:
            print(err)
        else:
            return lvl


def save_score(s, lvl):
    print(MSG_NAME)
    name = input()
    file = open("results.txt", "a+")
    file.write(f'{name}: {s}/{NUMBER_OF_TASKS} in level {lvl} ({level_description[lvl]}).')
    file.close()
    print(f'{MSG_SAVED}')


def handle_tasks():
    correct_answers = 0

    print(f'{MSG_LEVEL}')
    print(f'{MSG_LEVEL_1}')
    print(f'{MSG_LEVEL_2}')
    lvl = int(validate_level())

    for _ in range(NUMBER_OF_TASKS):
        generated_task = generate_task(lvl)
        print(generated_task)
        # Todo: extract to validate_format()
        user_answer = validate_answer()

        result = check_answer(user_answer, generated_task, lvl)
        if result:
            correct_answers += 1
            print("Right!")
        else:
            print("Wrong!")

    return correct_answers, lvl


score, level = handle_tasks()
print_score(score)
print(MSG_SAVE_RESULT)
answer_save_results = input()
if answer_save_results.lower() in "yes":
    save_score(score, level)
