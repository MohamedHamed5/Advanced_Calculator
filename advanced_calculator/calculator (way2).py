

# By: Mohamed Hamed
# Date: 2/7
# advanced calculator (way 2)
import math

def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def power(x, y): 
    if x == 0 and y == 0:
        raise ValueError("Math error: 0 ** 0 is undefined.")
    elif x == 0 and y == -1:
        raise ZeroDivisionError("Math error: Cannot raise 0 to a negative power.")
    else:
        return x ** y
def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Division by zero is undefined.")
    return x / y
def floor_div(x, y):
    if y == 0:
        raise ZeroDivisionError("Division by zero is undefined.")
    return x // y

basic_ops = {
    "addition": add,
    "+": add,
    "1": add,
    "subtraction": subtract,
    "-": subtract,
    "2": subtract,
    "multiplication": multiply,
    "*": multiply,
    "3": multiply,
    "power": power,
    "**": power,
    "4": power,
    "division": divide,
    "/": divide,
    "5": divide,
    "floor division": floor_div,
    "//": floor_div,
    "6": floor_div
}

def get_angle_in_radians():
    mode_input = normalize_input(input("Angle mode (deg/rad)? "))
    if mode_input == "rad":
        return float(input("Enter angle in radians: "))
    elif mode_input == "deg":
        return math.radians(float(input("Enter angle in degrees: ")))
    else:
        raise ValueError("Invalid angle mode. Please enter 'deg' or 'rad'.")

def sin_func():
    x = get_angle_in_radians()
    result = round(math.sin(x), 5)
    print(f"Result: sin({round(math.degrees(x), 5)}°) = {result}")

def cos_func():
    x = get_angle_in_radians()
    result = round(math.cos(x), 5)
    print(f"Result: cos({round(math.degrees(x), 5)}°) = {result}")

def tan_func():
    x_deg = float(input("Enter the angle in degrees: "))
    if x_deg % 180 == 90:
        raise ValueError("tan(90° + 180°k) is undefined.")
    x_rad = math.radians(x_deg)
    result = round(math.tan(x_rad), 5)
    print(f"Result: tan({x_deg}°) = {result}") 

def asin_func():
    x = float(input("Enter a value between -1 and 1 for asin: "))
    if x < -1 or x > 1:
        raise ValueError("asin is only defined for -1 ≤ x ≤ 1.")
    result = round(math.asin(x), 5)
    print(f"Result: asin({x}) = {round(math.degrees(result), 5)}°")

def acos_func():
    x = float(input("Enter a value between -1 and 1 for acos: "))
    if x < -1 or x > 1:
        raise ValueError("acos is only defined for -1 ≤ x ≤ 1.")
    result = round(math.acos(x), 5)
    print(f"Result: acos({x}) = {round(math.degrees(result), 5)}°")

def atan_func():
    x = float(input("Enter a number for atan: "))
    result_rad = math.atan(x)
    result_deg = round(math.degrees(result_rad), 5)
    print(f"Result: atan({x}) = {result_deg}°")

trig_funcs = {
    "10": sin_func,
    "sin": sin_func,
    "sine": sin_func,
    "11": cos_func,
    "cos": cos_func,
    "cosine": cos_func,
    "12": tan_func,
    "tan": tan_func,
    "tangent": tan_func
}
invers_funcs = {
    "13": asin_func,
    "asin": asin_func,
    "asine": asin_func,
    "14": acos_func,
    "acos": acos_func,
    "acosine": acos_func,
    "15": atan_func,
    "atan": atan_func,
    "atangent": atan_func
}

def normalize_input(text):
    return text.strip().lower()

print("Your Advanced Calculator")
while True:
    try:
        operation_input = normalize_input(input(
            "Choose the operation:\n"
            "0. Exit\n"
            "1. Addition\n"
            "2. Subtraction\n"
            "3. Multiplication\n"
            "4. Power\n"
            "5. Division\n"
            "6. Floor Division\n"
            "7. Logarithm\n"
            "8. Factorial\n"
            "9. Square Root\n"
            "10. Sine\n"
            "11. Cosine\n"
            "12. Tan\n"
            "13. asin\n"
            "14. acos\n"
            "15. atan\n"
            "Enter your choice (number or name or symbol): "
        ))

        other_operations = {
            "7": "logarithm", "logarithm": "logarithm", "log": "logarithm",
            "8": "factorial", "fact": "factorial", "!": "factorial",
            "9": "square root", "square root": "square root",
            "0": "exit", "exit": "exit"
        }

        operations2_list = ["factorial", "square root"]

        chosen = other_operations.get(operation_input)
        if not chosen:
            if operation_input in basic_ops:
                chosen = operation_input
            elif operation_input in trig_funcs:
                chosen = operation_input
            elif operation_input in invers_funcs:
                chosen = operation_input

        if chosen == "exit":
            print("Exiting the calculator. Goodbye!")
            break

        if chosen in basic_ops:
            try:
                number1 = float(input("Enter the first number: "))
                number2 = float(input("Enter the second number: "))
                result = basic_ops[chosen](number1, number2)
                print(f"The result of {chosen} = {result}")
            except ZeroDivisionError as zde:
                print(f"Math Error: {zde}")
            continue

        elif chosen == "logarithm":
            try:
                number1 = float(input("Enter the result of logarithm: "))
                number2 = float(input("Enter the base of logarithm: "))

                if number1 <= 0 or number2 <= 0 or number2 == 1:
                    raise ValueError("Logarithm undefined for number1 <= 0, number2 <= 0, or base = 1.")

                result = math.log(number1, number2)
                print(f"The result of logarithm of {number1} to the base {number2} = {result}")

            except ValueError as ve:
                print(f"Math Error: {ve}")
            except Exception as e:
                print(f"Unexpected error: {e}")
            continue
        
        if chosen in operations2_list:
            
            if chosen == "factorial":
                try:
                    n = int(input("Enter a non-negative integer: "))
                    result = 1
                    for i in range(2, n+1):
                        result *= i
                    print(f"{n}! = {result}")
                except ValueError as ve:
                    print(f"Math Error: {ve}")
                continue

            elif chosen == "square root":
                try:
                    number = float(input("Enter the number: "))
                    result = math.sqrt(number)
                    print(f"Square Root of {number} = {result}")
                except ValueError:
                    print("The root of a negative number cannot be found in real numbers. ")
                continue

        elif chosen in trig_funcs:
            try:
                trig_funcs[chosen]()
            except Exception as e:
                print(f"Math Error: {e}")
        
        elif chosen in invers_funcs:
            try:
                invers_funcs[chosen]()
            except Exception as e:
                print(f"Math Error: {e}")

        else:
            print("Invalid operation. Please choose a valid option.")

    except ValueError:
        print("Invalid input. Please enter numeric values.")
