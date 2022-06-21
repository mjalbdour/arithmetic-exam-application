# write your code here
import random

op_func = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y
}


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


generated_task = generate_task()
print(generated_task)
user_answer = input()
result = check_answer(user_answer, generated_task)
print("Right!") if result else print("Wrong!")
