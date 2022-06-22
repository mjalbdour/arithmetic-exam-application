# write your code here
import random

MSG_MARK = "Your mark is"
MSG_ERROR_FORMAT = "Incorrect format."
NUMBER_OF_TASKS = 5
op_func = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y
}


class FormatException(Exception):
    def __str__(self):
        return MSG_ERROR_FORMAT


def generate_task():
    x = random.randint(2, 9)
    y = random.randint(2, 9)
    op = random.choice([k for k in op_func.keys()])
    return f'{x} {op} {y}'


def check_answer(answer, task):
    answer = int(answer)
    task = task.split()
    x = int(task[0])
    op = task[1]
    y = int(task[2])
    return answer == op_func[op](x, y)


def print_score(correct_answers):
    print(f'{MSG_MARK} {correct_answers}/{NUMBER_OF_TASKS}.')


def handle_tasks():
    correct_answers = 0
    for _ in range(NUMBER_OF_TASKS):
        generated_task = generate_task()
        print(generated_task)
        while True:
            user_answer = input()
            try:
                if not user_answer.lstrip("+-").isnumeric():
                    raise FormatException
            except FormatException as err:
                print(err)
            else:
                break

        result = check_answer(user_answer, generated_task)
        if result:
            correct_answers += 1
            print("Right!")
        else:
            print("Wrong!")

    return correct_answers


score = handle_tasks()
print_score(score)
