# write your code here

op_func = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y
}


num1, op, num2 = input().split()

print(op_func[op](int(num1), int(num2)))
