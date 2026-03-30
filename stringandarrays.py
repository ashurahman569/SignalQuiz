# ============================================================================
# COMPLETE GUIDE TO PYTHON STRINGS AND ARRAYS
# ============================================================================

# ============================================================================
# PART 1: STRINGS
# ============================================================================

# --- 1. Creating Strings ---
single_quote = 'Hello'
double_quote = "World"
triple_single = '''Multi
line
string'''
triple_double = """Another
multi-line"""
raw_string = r"C:\new\path"  # Raw string (no escape)
formatted = f"Value: {42}"   # f-string
empty = ""
print("Created strings:", single_quote, formatted)

# --- 2. String Concatenation ---
str1 = "Hello"
str2 = "World"
concat1 = str1 + " " + str2
concat2 = " ".join([str1, str2])
concat3 = f"{str1} {str2}"
repeated = "Ha" * 3  # "HaHaHa"
print("Concatenation:", concat1, repeated)

# --- 3. String Indexing and Slicing ---
text = "Python Programming"
first_char = text[0]        # 'P'
last_char = text[-1]        # 'g'
substring = text[0:6]       # 'Python'
from_start = text[:6]       # 'Python'
to_end = text[7:]           # 'Programming'
every_second = text[::2]    # 'Pto rgamn'
reversed_str = text[::-1]   # 'gnimmargorP nohtyP'
step_slice = text[1:10:2]   # 'yhno'
print(f"First: {first_char}, Reversed: {reversed_str[:10]}...")

# --- 4. String Length ---
message = "Hello World"
length = len(message)  # 11
print(f"Length: {length}")

# --- 5. String Methods - Case Conversion ---
text = "Hello World"
upper = text.upper()           # "HELLO WORLD"
lower = text.lower()           # "hello world"
title = text.title()           # "Hello World"
capitalize = text.capitalize() # "Hello world"
swapcase = text.swapcase()     # "hELLO wORLD"
casefold = "ß".casefold()      # "ss" (aggressive lowercase)
print(f"Upper: {upper}, Title: {title}")

# --- 6. String Methods - Searching ---
sentence = "The quick brown fox jumps over the lazy fox"
index1 = sentence.index("fox")      # 16 (raises ValueError if not found)
index2 = sentence.find("fox")       # 16 (returns -1 if not found)
index3 = sentence.find("cat")       # -1
rindex = sentence.rindex("fox")     # 40 (last occurrence)
rfind = sentence.rfind("fox")       # 40
count = sentence.count("fox")       # 2
starts = sentence.startswith("The") # True
ends = sentence.endswith("fox")     # True
print(f"Find: {index2}, Count: {count}, Starts: {starts}")

# --- 7. String Methods - Checking Content ---
s1 = "hello123"
s2 = "hello"
s3 = "123"
s4 = "Hello World"
s5 = "   "

is_alpha = s2.isalpha()      # True (all letters)
is_digit = s3.isdigit()      # True (all digits)
is_alnum = s1.isalnum()      # True (letters + digits)
is_space = s5.isspace()      # True (all whitespace)
is_lower = s2.islower()      # True
is_upper = s2.isupper()      # False
is_title = s4.istitle()      # True
is_numeric = "½".isnumeric() # True (includes fractions)
is_decimal = "123".isdecimal() # True
is_identifier = "var_name".isidentifier() # True (valid variable name)
print(f"Is alpha: {is_alpha}, Is digit: {is_digit}, Is space: {is_space}")

# --- 8. String Methods - Whitespace Handling ---
text = "   Hello World   "
stripped = text.strip()       # "Hello World"
lstripped = text.lstrip()     # "Hello World   "
rstripped = text.rstrip()     # "   Hello World"
custom_strip = "***Hello***".strip("*")  # "Hello"
print(f"Stripped: '{stripped}'")

# --- 9. String Methods - Splitting ---
sentence = "apple,banana,cherry"
split1 = sentence.split(",")           # ['apple', 'banana', 'cherry']
split2 = "one  two   three".split()    # ['one', 'two', 'three'] (any whitespace)
split3 = "a-b-c-d".split("-", 2)       # ['a', 'b', 'c-d'] (max splits)
rsplit = "a-b-c-d".rsplit("-", 1)      # ['a-b-c', 'd'] (split from right)
splitlines = "Line1\nLine2\nLine3".splitlines()  # ['Line1', 'Line2', 'Line3']
partition = "a=b=c".partition("=")     # ('a', '=', 'b=c')
rpartition = "a=b=c".rpartition("=")   # ('a=b', '=', 'c')
print(f"Split: {split1}, Partition: {partition}")

# --- 10. String Methods - Joining ---
words = ["Python", "is", "awesome"]
joined1 = " ".join(words)        # "Python is awesome"
joined2 = "-".join(words)        # "Python-is-awesome"
joined3 = "".join(["a", "b", "c"])  # "abc"
print(f"Joined: {joined1}")

# --- 11. String Methods - Replacement ---
text = "Hello World World"
replaced1 = text.replace("World", "Python")      # "Hello Python Python"
replaced2 = text.replace("World", "Python", 1)   # "Hello Python World" (max 1)
print(f"Replaced: {replaced1}")

# --- 12. String Methods - Alignment and Padding ---
text = "Hello"
centered = text.center(20)        # "       Hello        "
centered2 = text.center(20, "*")  # "*******Hello********"
ljust = text.ljust(20)            # "Hello               "
rjust = text.rjust(20)            # "               Hello"
zfill = "42".zfill(5)             # "00042"
print(f"Centered: '{centered2}', Zfill: {zfill}")

# --- 13. String Formatting ---
name = "Alice"
age = 30
price = 19.99

# f-strings (Python 3.6+)
f1 = f"Name: {name}, Age: {age}"
f2 = f"Price: ${price:.2f}"
f3 = f"{name.upper()}"
f4 = f"{10 + 5}"

# format() method
fmt1 = "Name: {}, Age: {}".format(name, age)
fmt2 = "Name: {0}, Age: {1}".format(name, age)
fmt3 = "Name: {n}, Age: {a}".format(n=name, a=age)
fmt4 = "{:.2f}".format(price)

# % formatting (old style)
old1 = "Name: %s, Age: %d" % (name, age)
old2 = "Price: %.2f" % price

# Advanced formatting
f5 = f"{age:05d}"        # "00030" (padding)
f6 = f"{price:10.2f}"    # "     19.99" (width)
f7 = f"{price:<10.2f}"   # "19.99     " (left align)
f8 = f"{price:>10.2f}"   # "     19.99" (right align)
f9 = f"{price:^10.2f}"   # "  19.99   " (center)
print(f"Formatting: {f2}, {f5}")

# --- 14. String Encoding and Decoding ---
text = "Hello"
encoded = text.encode("utf-8")        # b'Hello'
encoded2 = text.encode("ascii")       # b'Hello'
decoded = encoded.decode("utf-8")     # "Hello"

unicode_text = "Héllo"
utf8_bytes = unicode_text.encode("utf-8")
print(f"Encoded: {encoded}, Type: {type(encoded)}")

# --- 15. String Escape Sequences ---
newline = "Line1\nLine2"
tab = "Column1\tColumn2"
backslash = "C:\\Users\\Name"
quote = "He said \"Hello\""
unicode_char = "\u0041"  # 'A'
hex_char = "\x41"        # 'A'
print("Escape sequences:", repr(newline), repr(tab))

# --- 16. String Comparison ---
s1 = "apple"
s2 = "Apple"
s3 = "banana"

equal = s1 == s2          # False (case-sensitive)
not_equal = s1 != s3      # True
less = s1 < s3            # True (alphabetical)
greater = s3 > s1         # True
case_insensitive = s1.lower() == s2.lower()  # True
print(f"Comparison: {equal}, Case-insensitive: {case_insensitive}")

# --- 17. String Membership ---
text = "Hello World"
contains = "World" in text      # True
not_contains = "Python" not in text  # True
print(f"Contains: {contains}")

# --- 18. String Iteration ---
word = "Hello"
for char in word:
    print(char, end=" ")
print()

for idx, char in enumerate(word):
    print(f"{idx}:{char}", end=" ")
print()

chars = [c for c in word]  # ['H', 'e', 'l', 'l', 'o']
print(f"Chars list: {chars}")

# --- 19. String Immutability ---
original = "Hello"
# original[0] = "h"  # TypeError! Strings are immutable
modified = "h" + original[1:]  # Create new string
print(f"Modified: {modified}")

# --- 20. Multi-line Strings ---
multi = """
This is a
multi-line
string
"""
multi2 = ("This is also "
          "a multi-line "
          "string")
print(f"Multi-line length: {len(multi)}")

# --- 21. String Methods - Advanced ---
text = "hello"
expandtabs = "1\t2\t3".expandtabs(4)  # Replace tabs with spaces
translate_table = str.maketrans("aeiou", "12345")
translated = "hello".translate(translate_table)  # "h2ll4"
print(f"Translated: {translated}")

# --- 22. String Interpolation ---
template = "Hello {name}, you are {age} years old"
result = template.format(name="Bob", age=25)
print(f"Template: {result}")

from string import Template
tmpl = Template("Hello $name, you are $age years old")
result2 = tmpl.substitute(name="Charlie", age=35)
print(f"Template class: {result2}")

# --- 23. Regular Expressions with Strings ---
import re

text = "The price is $19.99 and $29.99"
matches = re.findall(r"\$\d+\.\d+", text)  # ['$19.99', '$29.99']
replaced = re.sub(r"\d+", "XX", text)
split = re.split(r"\s+", "one  two   three")  # ['one', 'two', 'three']
print(f"Regex matches: {matches}")

# --- 24. String Constants ---
import string

ascii_letters = string.ascii_letters  # 'abcd...xyzABC...XYZ'
ascii_lowercase = string.ascii_lowercase  # 'abcdef...xyz'
ascii_uppercase = string.ascii_uppercase  # 'ABCDEF...XYZ'
digits = string.digits  # '0123456789'
hexdigits = string.hexdigits  # '0123456789abcdefABCDEF'
punctuation = string.punctuation  # '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
whitespace = string.whitespace  # ' \t\n\r\x0b\x0c'
printable = string.printable  # All printable characters
print(f"Digits: {digits}, Punctuation: {punctuation[:10]}...")


# ============================================================================
# PART 2: ARRAYS (using array module and numpy)
# ============================================================================

# --- 1. Python array module (typed arrays) ---
import array

# Create arrays (must specify type code)
int_array = array.array('i', [1, 2, 3, 4, 5])  # 'i' = signed int
float_array = array.array('f', [1.1, 2.2, 3.3])  # 'f' = float
char_array = array.array('u', 'hello')  # 'u' = unicode char

print(f"Int array: {int_array}, Type: {int_array.typecode}")

# Type codes:
# 'b' = signed char, 'B' = unsigned char
# 'h' = signed short, 'H' = unsigned short
# 'i' = signed int, 'I' = unsigned int
# 'l' = signed long, 'L' = unsigned long
# 'q' = signed long long, 'Q' = unsigned long long
# 'f' = float, 'd' = double
# 'u' = unicode character

# --- 2. Array Operations ---
arr = array.array('i', [1, 2, 3])
arr.append(4)              # Add element
arr.insert(0, 0)           # Insert at index
arr.extend([5, 6])         # Add multiple
arr.remove(3)              # Remove first occurrence
popped = arr.pop()         # Remove and return last
arr.reverse()              # Reverse in place
count = arr.count(2)       # Count occurrences
index = arr.index(2)       # Find index
print(f"Array after ops: {arr}")

# --- 3. Array to/from List ---
arr = array.array('i', [1, 2, 3])
as_list = arr.tolist()
from_list = array.array('i', [4, 5, 6])
print(f"Array to list: {as_list}")

# --- 4. Array to/from Bytes ---
arr = array.array('i', [1, 2, 3, 4])
byte_data = arr.tobytes()          # Convert to bytes
arr2 = array.array('i')
arr2.frombytes(byte_data)          # Load from bytes
print(f"Array from bytes: {arr2}")

# --- 5. Array to/from File ---
import tempfile
arr = array.array('i', [1, 2, 3, 4, 5])
with tempfile.NamedTemporaryFile(mode='wb', delete=False) as f:
    arr.tofile(f)
    temp_name = f.name

arr2 = array.array('i')
with open(temp_name, 'rb') as f:
    arr2.fromfile(f, 5)  # Read 5 integers
print(f"Array from file: {arr2}")

import os
os.unlink(temp_name)

# --- 6. Array Properties ---
arr = array.array('d', [1.1, 2.2, 3.3])
typecode = arr.typecode        # 'd'
itemsize = arr.itemsize        # Size in bytes of one element
length = len(arr)              # Number of elements
buffer_info = arr.buffer_info()  # (address, length)
print(f"Itemsize: {itemsize}, Length: {length}")


# ============================================================================
# PART 3: NUMPY ARRAYS (if numpy is installed)
# ============================================================================

try:
    import numpy as np
    
    # --- 1. Creating NumPy Arrays ---
    arr1 = np.array([1, 2, 3, 4, 5])
    arr2 = np.array([[1, 2, 3], [4, 5, 6]])
    arr3 = np.array([1, 2, 3], dtype=float)
    
    zeros = np.zeros(5)                    # [0. 0. 0. 0. 0.]
    ones = np.ones((3, 3))                 # 3x3 array of ones
    full = np.full((2, 3), 7)              # 2x3 array filled with 7
    empty = np.empty((2, 2))               # Uninitialized array
    arange = np.arange(10)                 # [0 1 2 3 4 5 6 7 8 9]
    arange2 = np.arange(1, 10, 2)          # [1 3 5 7 9]
    linspace = np.linspace(0, 1, 5)        # [0. 0.25 0.5 0.75 1.]
    eye = np.eye(3)                        # 3x3 identity matrix
    random_arr = np.random.rand(3, 3)      # Random values [0, 1)
    random_int = np.random.randint(0, 10, 5)  # Random integers
    
    print(f"NumPy array: {arr1}, Shape: {arr1.shape}")
    
    # --- 2. Array Properties ---
    arr = np.array([[1, 2, 3], [4, 5, 6]])
    shape = arr.shape          # (2, 3)
    ndim = arr.ndim            # 2 (dimensions)
    size = arr.size            # 6 (total elements)
    dtype = arr.dtype          # dtype('int64') or similar
    itemsize = arr.itemsize    # Size of each element in bytes
    nbytes = arr.nbytes        # Total bytes consumed
    print(f"Shape: {shape}, Size: {size}, Dtype: {dtype}")
    
    # --- 3. Array Indexing ---
    arr = np.array([10, 20, 30, 40, 50])
    first = arr[0]             # 10
    last = arr[-1]             # 50
    
    arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    element = arr2d[1, 2]      # 6 (row 1, col 2)
    row = arr2d[0]             # [1 2 3]
    col = arr2d[:, 1]          # [2 5 8]
    print(f"2D element: {element}, Column: {col}")
    
    # --- 4. Array Slicing ---
    arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    slice1 = arr[2:5]          # [2 3 4]
    slice2 = arr[:5]           # [0 1 2 3 4]
    slice3 = arr[5:]           # [5 6 7 8 9]
    slice4 = arr[::2]          # [0 2 4 6 8]
    slice5 = arr[::-1]         # [9 8 7 6 5 4 3 2 1 0]
    
    arr2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    sub_array = arr2d[:2, 1:3]  # [[2 3], [6 7]]
    print(f"Sliced: {slice1}, 2D slice:\n{sub_array}")
    
    # --- 5. Array Reshaping ---
    arr = np.arange(12)
    reshaped = arr.reshape(3, 4)     # 3x4 array
    reshaped2 = arr.reshape(2, 2, 3) # 3D array
    flattened = reshaped.flatten()   # 1D array (copy)
    ravel = reshaped.ravel()         # 1D array (view if possible)
    transposed = reshaped.T          # Transpose
    print(f"Reshaped shape: {reshaped.shape}")
    
    # --- 6. Array Stacking and Splitting ---
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    
    vstack = np.vstack((a, b))       # [[1 2 3], [4 5 6]]
    hstack = np.hstack((a, b))       # [1 2 3 4 5 6]
    column_stack = np.column_stack((a, b))  # [[1 4], [2 5], [3 6]]
    
    arr = np.arange(9).reshape(3, 3)
    vsplit = np.vsplit(arr, 3)       # Split into 3 rows
    hsplit = np.hsplit(arr, 3)       # Split into 3 columns
    print(f"VStack:\n{vstack}")
    
    # --- 7. Array Mathematics ---
    arr = np.array([1, 2, 3, 4, 5])
    
    # Element-wise operations
    add = arr + 10              # [11 12 13 14 15]
    multiply = arr * 2          # [2 4 6 8 10]
    power = arr ** 2            # [1 4 9 16 25]
    sqrt = np.sqrt(arr)
    exp = np.exp(arr)
    log = np.log(arr)
    sin = np.sin(arr)
    
    # Array operations
    arr1 = np.array([1, 2, 3])
    arr2 = np.array([4, 5, 6])
    sum_arr = arr1 + arr2       # [5 7 9]
    diff = arr1 - arr2          # [-3 -3 -3]
    prod = arr1 * arr2          # [4 10 18]
    div = arr2 / arr1           # [4. 2.5 2.]
    
    print(f"Power: {power}, Sum: {sum_arr}")
    
    # --- 8. Array Aggregations ---
    arr = np.array([1, 2, 3, 4, 5])
    total = arr.sum()
    mean = arr.mean()
    median = np.median(arr)
    std = arr.std()              # Standard deviation
    var = arr.var()              # Variance
    minimum = arr.min()
    maximum = arr.max()
    argmin = arr.argmin()        # Index of min
    argmax = arr.argmax()        # Index of max
    
    arr2d = np.array([[1, 2, 3], [4, 5, 6]])
    sum_all = arr2d.sum()        # 21
    sum_axis0 = arr2d.sum(axis=0)  # [5 7 9] (sum columns)
    sum_axis1 = arr2d.sum(axis=1)  # [6 15] (sum rows)
    print(f"Mean: {mean}, Max: {maximum}, Sum axis0: {sum_axis0}")
    
    # --- 9. Boolean Indexing ---
    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    mask = arr > 5               # [False False False False False True True True True True]
    filtered = arr[mask]         # [6 7 8 9 10]
    filtered2 = arr[arr % 2 == 0]  # [2 4 6 8 10]
    
    arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    filtered3 = arr2d[arr2d > 5]  # [6 7 8 9]
    print(f"Filtered: {filtered}, Filtered 2D: {filtered3}")
    
    # --- 10. Array Comparison ---
    arr1 = np.array([1, 2, 3, 4, 5])
    arr2 = np.array([1, 2, 4, 4, 6])
    
    equal = arr1 == arr2         # [True True False True False]
    greater = arr1 > arr2        # [False False False False False]
    all_equal = np.array_equal(arr1, arr2)  # False
    all_close = np.allclose(arr1, arr2)     # False
    print(f"Element-wise equal: {equal}")
    
    # --- 11. Array Copying ---
    original = np.array([1, 2, 3])
    view = original[:]           # View (shares memory)
    copy = original.copy()       # Deep copy
    view[0] = 99
    print(f"Original after view change: {original}, Copy: {copy}")
    
    # --- 12. Array Broadcasting ---
    arr = np.array([[1, 2, 3], [4, 5, 6]])
    scalar = arr + 10            # Add 10 to all elements
    
    arr1 = np.array([[1], [2], [3]])  # 3x1
    arr2 = np.array([10, 20, 30])     # 1x3
    result = arr1 + arr2              # 3x3 (broadcasting)
    print(f"Broadcasted result:\n{result}")
    
    # --- 13. Advanced Indexing ---
    arr = np.array([10, 20, 30, 40, 50])
    indices = [0, 2, 4]
    selected = arr[indices]      # [10 30 50]
    
    arr2d = np.array([[1, 2], [3, 4], [5, 6]])
    rows = np.array([0, 1, 2])
    cols = np.array([1, 0, 1])
    selected2 = arr2d[rows, cols]  # [2 3 6]
    print(f"Fancy indexing: {selected}, 2D: {selected2}")
    
    # --- 14. Linear Algebra ---
    a = np.array([[1, 2], [3, 4]])
    b = np.array([[5, 6], [7, 8]])
    
    dot_product = np.dot(a, b)       # Matrix multiplication
    mat_mul = a @ b                  # Alternative syntax (Python 3.5+)
    det = np.linalg.det(a)           # Determinant
    inv = np.linalg.inv(a)           # Inverse
    eigenvalues = np.linalg.eigvals(a)  # Eigenvalues
    
    print(f"Matrix multiplication:\n{dot_product}")
    
    # --- 15. Array Sorting ---
    arr = np.array([3, 1, 4, 1, 5, 9, 2, 6])
    sorted_arr = np.sort(arr)        # Returns sorted copy
    arr.sort()                       # Sort in-place
    argsort = np.argsort([3, 1, 2])  # [1 2 0] (indices that would sort)
    
    arr2d = np.array([[3, 2, 1], [6, 5, 4]])
    sorted_axis0 = np.sort(arr2d, axis=0)  # Sort each column
    sorted_axis1 = np.sort(arr2d, axis=1)  # Sort each row
    print(f"Sorted: {sorted_arr}")
    
    # --- 16. Unique and Set Operations ---
    arr = np.array([1, 2, 2, 3, 3, 3, 4])
    unique = np.unique(arr)          # [1 2 3 4]
    unique_counts = np.unique(arr, return_counts=True)  # Values and counts
    
    arr1 = np.array([1, 2, 3, 4])
    arr2 = np.array([3, 4, 5, 6])
    intersection = np.intersect1d(arr1, arr2)  # [3 4]
    union = np.union1d(arr1, arr2)             # [1 2 3 4 5 6]
    diff = np.setdiff1d(arr1, arr2)            # [1 2]
    print(f"Unique: {unique}, Intersection: {intersection}")
    
    # --- 17. Array I/O ---
    arr = np.array([1, 2, 3, 4, 5])
    np.save('array.npy', arr)        # Save to file
    loaded = np.load('array.npy')    # Load from file
    
    np.savetxt('array.txt', arr)     # Save as text
    loaded_txt = np.loadtxt('array.txt')
    
    # Cleanup
    os.unlink('array.npy')
    os.unlink('array.txt')
    print(f"Loaded from file: {loaded}")
    
    print("\n=== NumPy examples completed successfully! ===")
    
except ImportError:
    print("\nNumPy is not installed. Install with: pip install numpy")


# ============================================================================
# PRACTICAL EXAMPLES
# ============================================================================

# Example 1: Password validation
def validate_password(password):
    has_digit = any(c.isdigit() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_special = any(c in string.punctuation for c in password)
    long_enough = len(password) >= 8
    
    return all([has_digit, has_upper, has_lower, has_special, long_enough])

pwd = "MyPass123!"
print(f"Password valid: {validate_password(pwd)}")

# Example 2: Parse CSV line manually
csv_line = "John,Doe,30,New York"
fields = csv_line.split(",")
first_name, last_name, age, city = fields
print(f"Parsed: {first_name} {last_name}, {age}, {city}")

# Example 3: Clean text
text = "  Hello   World!  "
cleaned = " ".join(text.split())
print(f"Cleaned text: '{cleaned}'")

# Example 4: Extract numbers from string
text = "The prices are $19.99 and $29.99"
numbers = [float(s.strip("$")) for s in re.findall(r"\$\d+\.\d+", text)]
print(f"Extracted numbers: {numbers}")

# Example 5: Title case with exceptions
def smart_title(text):
    small_words = {'a', 'an', 'and', 'as', 'at', 'but', 'by', 'for', 'in', 'of', 'on', 'or', 'the', 'to'}
    words = text.lower().split()
    result = []
    for i, word in enumerate(words):
        if i == 0 or word not in small_words:
            result.append(word.capitalize())
        else:
            result.append(word)
    return ' '.join(result)

title = smart_title("the lord of the rings")
print(f"Smart title: {title}")

print("\n=== All string and array examples completed successfully! ===")