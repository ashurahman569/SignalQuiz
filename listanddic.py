# ============================================================================
# COMPLETE GUIDE TO PYTHON LISTS AND DICTIONARIES
# ============================================================================

# ============================================================================
# PART 1: LISTS
# ============================================================================

# --- 1. Creating Lists ---
empty_list = []
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True, None]
nested = [[1, 2], [3, 4], [5, 6]]
from_range = list(range(5))  # [0, 1, 2, 3, 4]
from_string = list("hello")  # ['h', 'e', 'l', 'l', 'o']
list_comprehension = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]

print("Created lists:", numbers, mixed)

# --- 2. Accessing Elements ---
fruits = ["apple", "banana", "cherry", "date"]
first = fruits[0]  # "apple"
last = fruits[-1]  # "date"
second_last = fruits[-2]  # "cherry"
print(f"First: {first}, Last: {last}")

# --- 3. Slicing ---
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
slice1 = nums[2:5]      # [2, 3, 4]
slice2 = nums[:4]       # [0, 1, 2, 3]
slice3 = nums[6:]       # [6, 7, 8, 9]
slice4 = nums[::2]      # [0, 2, 4, 6, 8] (every 2nd)
slice5 = nums[1::2]     # [1, 3, 5, 7, 9]
slice6 = nums[::-1]     # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] (reversed)
slice7 = nums[7:2:-1]   # [7, 6, 5, 4, 3]
print("Slice examples:", slice1, slice6)

# --- 4. Modifying Lists ---
colors = ["red", "green", "blue"]
colors[1] = "yellow"          # Replace element
colors[0:2] = ["pink", "orange"]  # Replace slice
print("Modified:", colors)

# --- 5. Adding Elements ---
animals = ["cat", "dog"]
animals.append("bird")            # Add to end
animals.insert(1, "fish")         # Insert at index
animals.extend(["lion", "tiger"]) # Add multiple
combined = animals + ["bear"]     # Concatenation (new list)
print("After adding:", animals)

# --- 6. Removing Elements ---
items = ["a", "b", "c", "d", "e", "c"]
items.remove("c")        # Remove first occurrence
popped = items.pop()     # Remove and return last
popped_idx = items.pop(1) # Remove and return at index
del items[0]             # Delete by index
items.clear()            # Remove all elements
print(f"Removed elements: {popped}, {popped_idx}")

# --- 7. Searching and Counting ---
data = [10, 20, 30, 20, 40, 20]
idx = data.index(30)           # Find index (raises error if not found)
count = data.count(20)         # Count occurrences
exists = 30 in data            # Check membership
not_exists = 50 not in data
print(f"Index of 30: {idx}, Count of 20: {count}")

# --- 8. Sorting and Reversing ---
nums = [3, 1, 4, 1, 5, 9, 2]
nums.sort()                    # Sort in place
print("Sorted:", nums)
nums.sort(reverse=True)        # Sort descending
print("Descending:", nums)

original = [3, 1, 4]
sorted_copy = sorted(original) # Returns new sorted list
print("Original unchanged:", original, "Sorted copy:", sorted_copy)

nums.reverse()                 # Reverse in place
reversed_copy = list(reversed([1, 2, 3]))  # Returns iterator
print("Reversed:", nums)

# --- 9. List Methods Summary ---
methods_list = [1, 2, 3]
length = len(methods_list)
minimum = min([5, 2, 8, 1])
maximum = max([5, 2, 8, 1])
total = sum([1, 2, 3, 4, 5])
print(f"Length: {length}, Min: {minimum}, Max: {maximum}, Sum: {total}")

# --- 10. Copying Lists ---
original = [1, 2, 3]
shallow_copy1 = original.copy()
shallow_copy2 = original[:]
shallow_copy3 = list(original)

import copy
nested_orig = [[1, 2], [3, 4]]
shallow = nested_orig.copy()      # Shallow: nested lists are shared
deep = copy.deepcopy(nested_orig) # Deep: completely independent
shallow[0][0] = 999
print("Original after shallow copy modification:", nested_orig)
deep[0][0] = 888
print("Deep copy is independent:", nested_orig, deep)

# --- 11. List Comprehensions ---
squares = [x**2 for x in range(10)]
evens = [x for x in range(20) if x % 2 == 0]
pairs = [(x, y) for x in range(3) for y in range(3)]
matrix = [[i*3 + j for j in range(3)] for i in range(3)]
words = ["hello", "world", "python"]
upper = [w.upper() for w in words]
print("Comprehensions:", squares[:5], evens[:5])

# --- 12. Unpacking ---
a, b, c = [1, 2, 3]
first, *middle, last = [1, 2, 3, 4, 5]  # first=1, middle=[2,3,4], last=5
*start, end = [1, 2, 3]  # start=[1,2], end=3
print(f"Unpacked: a={a}, middle={middle}, end={end}")

# --- 13. Iterating ---
for item in ["a", "b", "c"]:
    print(item, end=" ")
print()

for idx, val in enumerate(["x", "y", "z"]):
    print(f"{idx}: {val}", end=" ")
print()

for i in range(len([10, 20, 30])):
    pass  # Access by index if needed

# --- 14. Nested Lists ---
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
element = matrix[1][2]  # 6
row = matrix[0]         # [1, 2, 3]
flat = [item for row in matrix for item in row]
print(f"Matrix element: {element}, Flattened: {flat}")

# --- 15. Advanced Operations ---
list1 = [1, 2, 3]
list2 = [3, 4, 5]
union = list(set(list1) | set(list2))      # [1, 2, 3, 4, 5]
intersection = list(set(list1) & set(list2))  # [3]
difference = list(set(list1) - set(list2))    # [1, 2]

from itertools import chain
chained = list(chain([1, 2], [3, 4], [5, 6]))  # [1, 2, 3, 4, 5, 6]

zipped = list(zip([1, 2, 3], ['a', 'b', 'c']))  # [(1,'a'), (2,'b'), (3,'c')]
print("Zipped:", zipped)


# ============================================================================
# PART 2: DICTIONARIES
# ============================================================================

# --- 1. Creating Dictionaries ---
empty_dict = {}
person = {"name": "Alice", "age": 30, "city": "NYC"}
from_pairs = dict([("a", 1), ("b", 2)])
from_kwargs = dict(x=1, y=2, z=3)
dict_comp = {x: x**2 for x in range(5)}
fromkeys = dict.fromkeys(["a", "b", "c"], 0)  # All values = 0
print("Created dict:", person)

# --- 2. Accessing Values ---
age = person["age"]              # Raises KeyError if not found
name = person.get("name")        # Returns None if not found
country = person.get("country", "USA")  # Default value
print(f"Age: {age}, Country: {country}")

# --- 3. Adding and Modifying ---
person["email"] = "alice@example.com"  # Add new key
person["age"] = 31                     # Modify existing
person.update({"phone": "123-456", "age": 32})  # Add/update multiple
print("Updated person:", person)

# --- 4. Removing Items ---
sample = {"a": 1, "b": 2, "c": 3, "d": 4}
value = sample.pop("b")          # Remove and return value
value_default = sample.pop("z", None)  # With default
last_item = sample.popitem()     # Remove and return (key, value)
del sample["a"]                  # Delete by key
sample.clear()                   # Remove all
print(f"Popped: {value}, Last item: {last_item}")

# --- 5. Checking Keys ---
user = {"username": "bob", "email": "bob@test.com"}
has_email = "email" in user           # True
no_phone = "phone" not in user        # True
print(f"Has email: {has_email}")

# --- 6. Dictionary Views ---
data = {"x": 10, "y": 20, "z": 30}
keys = data.keys()        # dict_keys(['x', 'y', 'z'])
values = data.values()    # dict_values([10, 20, 30])
items = data.items()      # dict_items([('x', 10), ('y', 20), ('z', 30)])
print("Keys:", list(keys), "Items:", list(items)[:2])

# --- 7. Iterating ---
scores = {"Alice": 95, "Bob": 87, "Charlie": 92}

for key in scores:
    print(f"{key}: {scores[key]}", end=" ")
print()

for key in scores.keys():
    pass  # Same as above

for value in scores.values():
    print(value, end=" ")
print()

for key, value in scores.items():
    print(f"{key}={value}", end=" ")
print()

# --- 8. Dictionary Methods ---
config = {"debug": True, "timeout": 30}
length = len(config)
all_keys = list(config.keys())
all_values = list(config.values())
print(f"Dict length: {length}")

# --- 9. Copying Dictionaries ---
original = {"a": 1, "b": 2}
shallow_copy = original.copy()
shallow_copy2 = dict(original)

nested_dict = {"user": {"name": "Alice", "age": 30}}
shallow = nested_dict.copy()
deep = copy.deepcopy(nested_dict)
shallow["user"]["name"] = "Bob"  # Affects original
print("Original after shallow:", nested_dict)

# --- 10. Merging Dictionaries ---
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

# Python 3.9+
merged = dict1 | dict2  # {"a": 1, "b": 3, "c": 4}
dict1 |= dict2          # In-place merge

# Python 3.5+
merged2 = {**dict1, **dict2}

# update() method
dict1.update(dict2)
print("Merged:", merged)

# --- 11. Nested Dictionaries ---
database = {
    "user1": {"name": "Alice", "age": 30, "scores": [85, 90, 95]},
    "user2": {"name": "Bob", "age": 25, "scores": [80, 85, 90]}
}
alice_age = database["user1"]["age"]
bob_scores = database["user2"]["scores"][0]
print(f"Alice age: {alice_age}, Bob first score: {bob_scores}")

# --- 12. Dictionary Comprehensions ---
squares_dict = {x: x**2 for x in range(6)}
filtered = {k: v for k, v in squares_dict.items() if v > 10}
swapped = {v: k for k, v in {"a": 1, "b": 2}.items()}
from_lists = {k: v for k, v in zip(["a", "b", "c"], [1, 2, 3])}
print("Dict comprehension:", filtered)

# --- 13. Default Values ---
from collections import defaultdict

dd = defaultdict(int)  # Default value is 0
dd["count"] += 1
dd["other"] += 5

dd_list = defaultdict(list)
dd_list["items"].append(1)
dd_list["items"].append(2)

dd_dict = defaultdict(dict)
dd_dict["user"]["name"] = "Alice"
print("Defaultdict:", dict(dd), dict(dd_list))

# setdefault method
regular = {}
regular.setdefault("key", []).append(1)
print("After setdefault:", regular)

# --- 14. OrderedDict (maintains insertion order) ---
from collections import OrderedDict
# Note: Regular dicts maintain order in Python 3.7+
ordered = OrderedDict([("first", 1), ("second", 2)])
ordered["third"] = 3
ordered.move_to_end("first")  # Move to end
print("OrderedDict:", ordered)

# --- 15. Counter (counting hashable objects) ---
from collections import Counter

word_counts = Counter(["apple", "banana", "apple", "cherry", "banana", "apple"])
letter_counts = Counter("mississippi")
most_common = word_counts.most_common(2)  # [('apple', 3), ('banana', 2)]

c1 = Counter(["a", "b", "c"])
c2 = Counter(["b", "c", "d"])
combined = c1 + c2  # Counter({'b': 2, 'c': 2, 'a': 1, 'd': 1})
print("Counter:", word_counts, "Most common:", most_common)

# --- 16. Advanced Dictionary Operations ---
inventory = {"apples": 5, "bananas": 3, "oranges": 0}

# Filter dictionary
in_stock = {k: v for k, v in inventory.items() if v > 0}

# Transform values
doubled = {k: v * 2 for k, v in inventory.items()}

# Invert dictionary (if values are unique)
inverted = {v: k for k, v in {"a": 1, "b": 2}.items()}

# Get with computed default
def expensive_operation():
    return 42

result = inventory.get("pears") or expensive_operation()

print("In stock:", in_stock)

# --- 17. Dictionary as Switch/Case ---
def operation(op, x, y):
    operations = {
        "add": lambda a, b: a + b,
        "sub": lambda a, b: a - b,
        "mul": lambda a, b: a * b,
        "div": lambda a, b: a / b if b != 0 else None
    }
    return operations.get(op, lambda a, b: None)(x, y)

result = operation("add", 5, 3)  # 8
print("Operation result:", result)

# --- 18. ChainMap (combine multiple dicts) ---
from collections import ChainMap

defaults = {"color": "red", "size": "medium"}
overrides = {"size": "large"}
combined = ChainMap(overrides, defaults)  # overrides takes precedence
print("ChainMap:", dict(combined))


# ============================================================================
# PRACTICAL EXAMPLES
# ============================================================================

# Example 1: Group items by category
items = [
    {"name": "apple", "category": "fruit"},
    {"name": "carrot", "category": "vegetable"},
    {"name": "banana", "category": "fruit"}
]

grouped = {}
for item in items:
    cat = item["category"]
    if cat not in grouped:
        grouped[cat] = []
    grouped[cat].append(item["name"])
print("Grouped:", grouped)

# Example 2: Word frequency counter
text = "the quick brown fox jumps over the lazy dog the fox"
word_freq = {}
for word in text.split():
    word_freq[word] = word_freq.get(word, 0) + 1
print("Word frequency:", word_freq)

# Example 3: List of dicts operations
users = [
    {"name": "Alice", "age": 30, "city": "NYC"},
    {"name": "Bob", "age": 25, "city": "LA"},
    {"name": "Charlie", "age": 35, "city": "NYC"}
]

# Filter
nyc_users = [u for u in users if u["city"] == "NYC"]

# Sort
sorted_users = sorted(users, key=lambda u: u["age"])

# Extract field
names = [u["name"] for u in users]

print("NYC users:", len(nyc_users), "Names:", names)

print("\n=== All examples completed successfully! ===")