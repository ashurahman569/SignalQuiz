# ============================================================================
# PYTHON CONTROL FLOW EXAMPLES: LOOPS, IF-ELSE, AND SWITCH-CASE
# ============================================================================

# ============================================================================
# SECTION 1: IF-ELSE STATEMENTS
# ============================================================================

print("=" * 60)
print("IF-ELSE STATEMENTS")
print("=" * 60)

# Basic if statement
x = 10
if x > 5:
    print(f"1. Basic if: {x} is greater than 5")

# If-else statement
age = 18
if age >= 18:
    print("2. If-else: You are an adult")
else:
    print("2. If-else: You are a minor")

# If-elif-else statement (multiple conditions)
score = 75
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print(f"3. If-elif-else: Score {score} = Grade {grade}")

# Nested if statements
num = 15
if num > 0:
    if num % 2 == 0:
        print(f"4. Nested if: {num} is positive and even")
    else:
        print(f"4. Nested if: {num} is positive and odd")
else:
    print(f"4. Nested if: {num} is not positive")

# Multiple conditions with logical operators (and, or, not)
temperature = 25
humidity = 60
if temperature > 20 and humidity < 70:
    print("5. Logical AND: Weather is comfortable")

if temperature < 10 or temperature > 35:
    print("5. Logical OR: Extreme temperature!")
else:
    print("5. Logical OR: Temperature is moderate")

is_raining = False
if not is_raining:
    print("5. Logical NOT: No umbrella needed")

# Ternary operator (conditional expression)
a, b = 10, 20
max_val = a if a > b else b
print(f"6. Ternary operator: Max of {a} and {b} is {max_val}")

# Checking membership with 'in'
fruits = ["apple", "banana", "cherry"]
if "banana" in fruits:
    print("7. Membership test: Banana is in the list")

# Checking multiple values
color = "red"
if color in ["red", "green", "blue"]:
    print(f"8. Multiple values: {color} is a primary color")

# Checking None, empty sequences, and truthiness
empty_list = []
if not empty_list:
    print("9. Truthiness: List is empty")

value = None
if value is None:
    print("10. Identity check: Value is None")

# ============================================================================
# SECTION 2: FOR LOOPS
# ============================================================================

print("\n" + "=" * 60)
print("FOR LOOPS")
print("=" * 60)

# Basic for loop with range
print("1. Basic for loop (0 to 4):")
for i in range(5):
    print(f"   i = {i}")

# For loop with start, stop, step
print("\n2. For loop with step (0 to 10, step 2):")
for i in range(0, 11, 2):
    print(f"   i = {i}")

# For loop with negative step (countdown)
print("\n3. Countdown (5 to 1):")
for i in range(5, 0, -1):
    print(f"   {i}...")

# Iterating over a list
print("\n4. Iterating over a list:")
colors = ["red", "green", "blue"]
for color in colors:
    print(f"   Color: {color}")

# Iterating with index using enumerate
print("\n5. Using enumerate (index + value):")
for idx, color in enumerate(colors):
    print(f"   Index {idx}: {color}")

# Enumerate with custom start index
print("\n6. Enumerate with start=1:")
for idx, color in enumerate(colors, start=1):
    print(f"   #{idx}: {color}")

# Iterating over a dictionary
print("\n7. Iterating over dictionary:")
person = {"name": "Alice", "age": 30, "city": "New York"}
for key, value in person.items():
    print(f"   {key}: {value}")

# Iterating over dictionary keys only
print("\n8. Dictionary keys:")
for key in person.keys():
    print(f"   Key: {key}")

# Iterating over dictionary values only
print("\n9. Dictionary values:")
for value in person.values():
    print(f"   Value: {value}")

# Nested for loops
print("\n10. Nested loops (multiplication table 3x3):")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"   {i} x {j} = {i*j}")

# List comprehension (compact for loop)
print("\n11. List comprehension:")
squares = [x**2 for x in range(1, 6)]
print(f"   Squares: {squares}")

# List comprehension with condition
print("\n12. List comprehension with condition (even numbers):")
evens = [x for x in range(10) if x % 2 == 0]
print(f"   Even numbers: {evens}")

# Iterating over strings
print("\n13. Iterating over string:")
for char in "Python":
    print(f"   {char}")

# Using zip to iterate over multiple sequences
print("\n14. Using zip (parallel iteration):")
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"   {name} is {age} years old")

# Break statement (exit loop early)
print("\n15. Break statement (stop at 3):")
for i in range(10):
    if i == 3:
        break
    print(f"   i = {i}")

# Continue statement (skip iteration)
print("\n16. Continue statement (skip odd numbers):")
for i in range(6):
    if i % 2 != 0:
        continue
    print(f"   i = {i}")

# Else clause with for loop (executes if loop completes normally)
print("\n17. For-else (else executes if no break):")
for i in range(3):
    print(f"   i = {i}")
else:
    print("   Loop completed without break")

# For-else with break
print("\n18. For-else with break:")
for i in range(5):
    if i == 2:
        print("   Breaking at i = 2")
        break
else:
    print("   This won't print because of break")

# ============================================================================
# SECTION 3: WHILE LOOPS
# ============================================================================

print("\n" + "=" * 60)
print("WHILE LOOPS")
print("=" * 60)

# Basic while loop
print("1. Basic while loop:")
count = 0
while count < 3:
    print(f"   Count: {count}")
    count += 1

# While loop with break
print("\n2. While loop with break:")
n = 0
while True:
    print(f"   n = {n}")
    n += 1
    if n >= 3:
        break

# While loop with continue
print("\n3. While loop with continue (skip 2):")
i = 0
while i < 5:
    i += 1
    if i == 2:
        continue
    print(f"   i = {i}")

# While-else (else executes if loop completes normally)
print("\n4. While-else:")
counter = 0
while counter < 3:
    print(f"   counter = {counter}")
    counter += 1
else:
    print("   While loop completed")

# User input simulation (processing until condition)
print("\n5. Processing items until empty:")
items = ["apple", "banana", "cherry"]
while items:
    item = items.pop()
    print(f"   Processing: {item}")

# Infinite loop with sentinel value (commented to prevent actual infinite loop)
print("\n6. Sentinel pattern example:")
print("   # Simulating: while True with break condition")
commands = ["start", "process", "exit"]
for cmd in commands:
    print(f"   Command: {cmd}")
    if cmd == "exit":
        print("   Exiting loop")
        break

# ============================================================================
# SECTION 4: SWITCH-CASE (MATCH-CASE in Python 3.10+)
# ============================================================================

print("\n" + "=" * 60)
print("SWITCH-CASE (MATCH-CASE) - Python 3.10+")
print("=" * 60)

# Basic match-case
print("1. Basic match-case:")
day = 3
match day:
    case 1:
        print("   Monday")
    case 2:
        print("   Tuesday")
    case 3:
        print("   Wednesday")
    case 4:
        print("   Thursday")
    case 5:
        print("   Friday")
    case 6 | 7:  # Multiple patterns
        print("   Weekend!")
    case _:  # Default case
        print("   Invalid day")

# Match with multiple values (OR pattern)
print("\n2. Match with multiple values:")
status_code = 404
match status_code:
    case 200 | 201 | 204:
        print("   Success")
    case 400 | 404:
        print("   Client error")
    case 500 | 503:
        print("   Server error")
    case _:
        print("   Unknown status")

# Match with conditions (guard clauses)
print("\n3. Match with guard clauses:")
value = 15
match value:
    case x if x < 0:
        print("   Negative number")
    case x if x == 0:
        print("   Zero")
    case x if x < 10:
        print("   Small positive number")
    case x if x < 100:
        print("   Medium number")
    case _:
        print("   Large number")

# Match with tuples (structural pattern matching)
print("\n4. Match with tuples:")
point = (0, 5)
match point:
    case (0, 0):
        print("   Origin")
    case (0, y):
        print(f"   On Y-axis at y={y}")
    case (x, 0):
        print(f"   On X-axis at x={x}")
    case (x, y):
        print(f"   Point at ({x}, {y})")

# Match with lists
print("\n5. Match with lists:")
data = [1, 2, 3]
match data:
    case []:
        print("   Empty list")
    case [x]:
        print(f"   Single element: {x}")
    case [x, y]:
        print(f"   Two elements: {x}, {y}")
    case [x, y, *rest]:
        print(f"   First: {x}, Second: {y}, Rest: {rest}")

# Match with dictionaries
print("\n6. Match with dictionaries:")
user = {"name": "Alice", "role": "admin"}
match user:
    case {"role": "admin"}:
        print("   Admin user detected")
    case {"role": "user"}:
        print("   Regular user")
    case _:
        print("   Unknown role")

# Match with classes (structural pattern)
print("\n7. Match with class patterns:")
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(0, 0)
match p:
    case Point(x=0, y=0):
        print("   Point at origin")
    case Point(x=0, y=y):
        print(f"   Point on Y-axis: y={y}")
    case Point(x=x, y=0):
        print(f"   Point on X-axis: x={x}")
    case Point(x=x, y=y):
        print(f"   Point at ({x}, {y})")

# ============================================================================
# ALTERNATIVE TO MATCH-CASE (for Python < 3.10)
# ============================================================================

print("\n" + "=" * 60)
print("DICTIONARY-BASED SWITCH (Python < 3.10)")
print("=" * 60)

# Using dictionary for switch-like behavior
print("1. Dictionary switch:")
def switch_day(day):
    switcher = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
    return switcher.get(day, "Invalid day")

print(f"   Day 3: {switch_day(3)}")
print(f"   Day 8: {switch_day(8)}")

# Dictionary with functions
print("\n2. Dictionary switch with functions:")
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b if b != 0 else "Error: Division by zero"

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

operator = "*"
result = operations.get(operator, lambda a, b: "Invalid operator")(10, 5)
print(f"   10 {operator} 5 = {result}")

# ============================================================================
# ADVANCED EXAMPLES
# ============================================================================

print("\n" + "=" * 60)
print("ADVANCED EXAMPLES")
print("=" * 60)

# Nested loops with break and continue
print("1. Finding prime numbers (nested loops):")
for num in range(2, 20):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"   {num} is prime")

# Loop with else to detect completion
print("\n2. Searching with for-else:")
search_list = [10, 20, 30, 40, 50]
search_value = 35
for item in search_list:
    if item == search_value:
        print(f"   Found {search_value}")
        break
else:
    print(f"   {search_value} not found in list")

# Combining multiple control structures
print("\n3. Grade calculation system:")
students = [
    {"name": "Alice", "score": 92},
    {"name": "Bob", "score": 76},
    {"name": "Charlie", "score": 58},
    {"name": "Diana", "score": 88}
]

for student in students:
    name = student["name"]
    score = student["score"]
    
    if score >= 90:
        grade = "A"
        status = "Excellent"
    elif score >= 80:
        grade = "B"
        status = "Good"
    elif score >= 70:
        grade = "C"
        status = "Satisfactory"
    elif score >= 60:
        grade = "D"
        status = "Needs improvement"
    else:
        grade = "F"
        status = "Failed"
    
    print(f"   {name}: {score} → Grade {grade} ({status})")

print("\n" + "=" * 60)
print("ALL EXAMPLES COMPLETED!")
print("=" * 60)