def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

def calculator():
    should_accumulate = True
    first_number = float(input('Type the first number: '))

    while should_accumulate:
        for op in operations:
            print(op)
        op_choice = input("Type the operation: ")
        second_number = float(input("Type the second number: "))

        result = operations[op_choice](first_number, second_number)
        print(f'{first_number} {op_choice} {second_number} = {result}\n')
        
        keep_going = input("Do you want to continue working with the result? 'yes' or 'no'\n").lower()
        if keep_going == 'no':
            should_accumulate = False
            print('\n'*100)
            calculator()
        else:
            first_number = result

calculator()
