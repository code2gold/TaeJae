# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def run_calculator():
    # Use a breakpoint in the code line below to debug your script.
    while True:
        print("""This is the Calculator.
        Enter the operation first.
        1. Add
        2. Subtract
        3. Multiply
        4. Divide
        5. Close the calculator
        """)

        operation_input = input("You selected: ")
        if not operation_input.isdigit():
            print("You have to type only 1 to 5")
            continue

        num_operation = int(operation_input)
        if num_operation == 5:
            break

        if num_operation == 1:
            print("Add operation is selected")
        elif num_operation == 2:
            print("Subtract opertion is selected")
        elif num_operation == 3:
            print("Multiply opertion is selected")
        elif num_operation == 4:
            print("Divide opertion is selected")
        else:
            print("You have to type only 1 to 5")

        while True:
            first_operand = input("Enter the first integer type operand:")
            if not first_operand.isdigit():
                print("Enter the first integer type operand.\n")
                continue

            second_operand = input("Enter the second integer type operand:")
            if not second_operand.isdigit():
                print("Enter the second integer type operand.\n")
                continue

            result = 0

            if num_operation == 1:
                result = int(first_operand) + int(second_operand)
            elif num_operation == 2:
                result = int(first_operand) - int(second_operand)
            elif num_operation == 3:
                result = int(first_operand) * int(second_operand)
            elif num_operation == 4: # Divide
                if int(second_operand) == 0:
                    print("Dividing by zero is not allowed")
                    continue
                result = int(first_operand) / int(second_operand)

            print("Your result is:")
            print(result)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run_calculator()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
