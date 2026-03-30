import numpy as np  

#1. Creating Arrays
#1.1 From Python data
# Create a 1D array from a Python list  
a = np.array([1, 2, 3])  
print(a)          # [1 2 3]  
print(a.dtype)    # Typically int64 or int32 depending on your system  
print(a.shape)    # (3,) -> 1D array of length 3  
  
# Create a 2D array (matrix) from a nested list  
b = np.array([[1, 2, 3],  
              [4, 5, 6]])  
print(b)          # 2x3 matrix  
print(b.shape)    # (2, 3)  
  
# Specify data type explicitly (float64)  
c = np.array([1, 2, 3], dtype=np.float64)  
print(c)          # [1. 2. 3.]  
print(c.dtype)    # float64  

#1.2 Zeros, ones, full
# Array of zeros with shape (2, 3)  
zeros = np.zeros((2, 3))  
print(zeros)  
  
# Array of ones with shape (2, 3) and integer dtype  
ones = np.ones((2, 3), dtype=int)  
print(ones)  
  
# Array filled with a constant value 7  
full = np.full((2, 3), fill_value=7)  
print(full)  

#1.3 Identity / eye / diag
# 3x3 identity matrix (ones on the main diagonal)  
I = np.eye(3)  
print(I)  
  
# Rectangular "eye": 3 rows, 4 cols  
eye = np.eye(3, 4)  
print(eye)  
  
# Create a diagonal matrix from a 1D array  
diag_from_vec = np.diag([1, 2, 3])  
print(diag_from_vec)  
  
# Extract the diagonal of a 2D array as a 1D array  
diag_from_mat = np.diag([[1, 2],  
                         [3, 4]])  
print(diag_from_mat)  # [1 4]  

#1.4 Ranges: arange, linspace, logspace
# arange(start, stop, step): stop is EXCLUSIVE  
ar = np.arange(0, 10, 2)  
print(ar)  # [0 2 4 6 8]  
  
# linspace(start, stop, num): includes both endpoints  
ls = np.linspace(0, 1, 5)  
print(ls)  # [0.   0.25 0.5  0.75 1.  ]  
  
# logspace: logarithmically spaced numbers between 10^start and 10^stop  
log = np.logspace(0, 3, 4)  
print(log)  # [   1.   10.  100. 1000.]  

#1.5 Random arrays (Generator API)
# Create a random number generator with a fixed seed for reproducibility  
rng = np.random.default_rng(seed=42)  
  
# Uniform in [0, 1), shape (2, 3)  
uniform = rng.random((2, 3))  
print(uniform)  
  
# Normal (Gaussian) with mean 0 and std dev 1, shape (2, 3)  
normal = rng.normal(0, 1, (2, 3))  
print(normal)  
  
# Random integers from 0 to 9 (high is exclusive), shape (2, 3)  
integers = rng.integers(0, 10, size=(2, 3))  
print(integers)  
  
# Random choice from a 1D array, with replacement, shape (5,)  
choice = rng.choice([10, 20, 30], size=5, replace=True)  
print(choice)  

#1.6 empty, empty_like, zeros_like, ones_like
# Start from a base array  
x = np.arange(6).reshape(2, 3)  
print(x)  
  
# empty: allocates memory but does NOT initialize values (garbage data)  
e = np.empty((2, 3))  
print(e)  
  
# zeros_like: zeros with same shape & dtype as x  
zl = np.zeros_like(x)  
print(zl)  
  
# ones_like: ones with same shape & dtype as x  
ol = np.ones_like(x)  
print(ol)  
  
# empty_like: uninitialized values with same shape & dtype as x  
el = np.empty_like(x)  
print(el)  


#2. Inspecting Arrays
x = np.arange(12).reshape(3, 4)  
print(x)  
  
print("ndim:", x.ndim)         # number of dimensions, here 2  
print("shape:", x.shape)       # (3, 4): 3 rows, 4 columns  
print("size:", x.size)         # total number of elements: 12  
print("dtype:", x.dtype)       # e.g. int64  
print("itemsize:", x.itemsize) # bytes per element  
print("nbytes:", x.nbytes)     # total bytes = size * itemsize  
print("strides:", x.strides)   # byte steps between elements in each dimension  


#3. Indexing & Slicing
#3.1 Basic indexing & slicing (1D)
a = np.arange(10)  
print(a)           # [0 1 2 3 4 5 6 7 8 9]  
  
print(a[0])        # first element -> 0  
print(a[-1])       # last element  -> 9  
  
# slice: [start:stop:step]  
print(a[2:7:2])    # from index 2 up to (not including) 7, step 2 -> [2 4 6]  
  
print(a[:3])       # from start to index 3 (exclusive) -> [0 1 2]  
print(a[5:])       # from index 5 to end -> [5 6 7 8 9]  
print(a[::2])      # every 2nd element -> [0 2 4 6 8]  

#3.1b Basic indexing & slicing (2D)
b = np.arange(12).reshape(3, 4)  
print(b)  
# [[ 0  1  2  3]  
#  [ 4  5  6  7]  
#  [ 8  9 10 11]]  
  
print(b[0, 0])    # element at row 0, col 0 -> 0  
print(b[1, 2])    # element at row 1, col 2 -> 6  
  
print(b[0])       # entire row 0 -> [0 1 2 3]  
print(b[:, 1])    # entire column 1 -> [1 5 9]  
  
# rows 1..end, cols 0..1  
print(b[1:, :2])  
# [[4 5]  
#  [8 9]]  

#3.2 Boolean masking
c = np.arange(10)  
print("c:", c)  
  
# Create boolean mask: True where element is even  
mask = c % 2 == 0  
print("mask:", mask)  
  
# Use mask to select only even elements  
print("even:", c[mask])  
  
# Modify selected elements in-place (set evens to -1)  
c[c % 2 == 0] = -1  
print("modified c:", c)  
 
# 2D boolean mask:
d = np.arange(12).reshape(3, 4)  
print(d)  
  
# Mask True where element is > 5  
mask2 = d > 5  
print("mask2:\n", mask2)  
  
# Using mask with array returns 1D array of selected elements  
print("elements > 5:", d[mask2])  

#3.3 Fancy indexing (integer arrays)
e = np.arange(10) * 10  
print("e:", e)    # [ 0 10 20 30 40 50 60 70 80 90]  
  
# Pick elements at the given indices  
idx = [0, 3, 5, 7]  
print(e[idx])     # [ 0 30 50 70]  
  
# 2D advanced indexing: arrays of row and col indices  
f = np.arange(12).reshape(3, 4)  
print(f)  
# [[ 0  1  2  3]  
#  [ 4  5  6  7]  
#  [ 8  9 10 11]]  
  
row_idx = np.array([0, 1, 2])  
col_idx = np.array([1, 2, 3])  
# Picks f[0,1], f[1,2], f[2,3]  
print(f[row_idx, col_idx])  # [ 1  6 11]  

#3.4 Mixing slices and fancy indexing
g = np.arange(24).reshape(4, 6)  
print(g)  
  
# Select rows by fancy indexing  
rows = [1, 3]  
  
# Slice for columns: from 2 to 5 (exclusive of 5)  
cols_slice = slice(2, 5)  
  
# Result is a 2x3 subarray: rows 1 & 3, columns 2,3,4  
sub = g[rows, cols_slice]  
print(sub)  

#4. Dtypes & Casting
#4.1 Specifying and converting dtype
# Create array with int32 dtype  
a = np.array([1, 2, 3], dtype=np.int32)  
print(a, a.dtype)  
  
# Convert (cast) to float64  
b = a.astype(np.float64)  
print(b, b.dtype)  

#4.2 Common dtypes
int_arr = np.array([1, 2, 3], dtype=np.int64)  
print(int_arr, int_arr.dtype)  
  
float_arr = np.array([1.0, 2.0], dtype=np.float32)  
print(float_arr, float_arr.dtype)  
  
complex_arr = np.array([1+2j, 3+4j], dtype=np.complex128)  
print(complex_arr, complex_arr.dtype)  
  
bool_arr = np.array([True, False, True])  
print(bool_arr, bool_arr.dtype)  
  
# Fixed-length strings (each element has a fixed max length)  
str_arr = np.array(["a", "b", "c"], dtype=np.str_)  
print(str_arr, str_arr.dtype)  
  
# Object array can hold arbitrary Python objects (slower, but flexible)  
obj_arr = np.array([1, "a", None], dtype=object)  
print(obj_arr, obj_arr.dtype)  

#4.3 Inspecting numeric limits
# Integer type limits: min, max  
print(np.iinfo(np.int32))  
  
# Floating point info: eps, max, min, etc.  
print(np.finfo(np.float64))  

#5. Reshaping, Stacking, Splitting
#5.1 Reshape, ravel, flatten
x = np.arange(12)  
print("x:", x)  
  
# Reshape 1D array (length 12) into 3 rows, 4 columns  
X = x.reshape(3, 4)  
print("X:\n", X)  
  
# Use -1 to let NumPy infer the other dimension: 2 rows, 6 columns  
Y = x.reshape(2, -1)  
print("Y:\n", Y)  
  
# ravel returns a 1D *view* whenever possible (shares data)  
flat_view = X.ravel()  
print("flat_view:", flat_view)  
  
# flatten always returns a *copy* (independent data)  
flat_copy = X.flatten()  
print("flat_copy:", flat_copy)  

#5.2 Transpose & swapaxes
A = np.arange(12).reshape(3, 4)  
print("A:\n", A)  
  
# Transpose (swap rows and columns)  
print("A.T:\n", A.T)  
  
B = np.arange(24).reshape(2, 3, 4)  
print("B shape:", B.shape)  # (2, 3, 4)  
  
# transpose with custom axes order  
B_trans = B.transpose(1, 0, 2)  
print("B_trans shape:", B_trans.shape)  # (3, 2, 4)  
  
# swapaxes swaps two specific axes  
B_swapped = B.swapaxes(0, 2)  
print("B_swapped shape:", B_swapped.shape)  # (4, 3, 2)  

#5.3 Concatenate, stack, vstack, hstack
a = np.arange(6).reshape(2, 3)  
b = np.arange(6, 12).reshape(2, 3)  
print("a:\n", a)  
print("b:\n", b)  
  
# concatenate along rows (axis=0) -> 4x3  
cat0 = np.concatenate([a, b], axis=0)  
print("cat0:\n", cat0)  
  
# concatenate along columns (axis=1) -> 2x6  
cat1 = np.concatenate([a, b], axis=1)  
print("cat1:\n", cat1)  
  
# stack adds a new axis (here axis=0) -> shape (2, 2, 3)  
stack0 = np.stack([a, b], axis=0)  
print("stack0 shape:", stack0.shape)  
  
# vstack: vertical stack = concatenate along axis=0  
v = np.vstack([a, b])  
print("vstack:\n", v)  
  
# hstack: horizontal stack = concatenate along axis=1  
h = np.hstack([a, b])  
print("hstack:\n", h)  

#5.4 Split, vsplit, hsplit
x = np.arange(12).reshape(3, 4)  
print("x:\n", x)  
  
# Split into 2 equal parts along axis=1 (columns)  
s = np.split(x, 2, axis=1)  
print("split equal parts:")  
for part in s:  
    print(part)  
  
# Split at indices: [1, 3] -> [0], [1,2], [3..end] along axis=1  
s2 = np.split(x, [1, 3], axis=1)  
print("split at indices [1, 3]:")  
for part in s2:  
    print(part)  
  
# vsplit: split rows  
vs = np.vsplit(x, 3)  # 3 parts, each shape (1, 4)  
print("vsplit:")  
for part in vs:  
    print(part)  
  
# hsplit: split columns  
hs = np.hsplit(x, 2)  # 2 parts, each shape (3, 2)  
print("hsplit:")  
for part in hs:  
    print(part)  

#6. Vectorized Operations & Broadcasting
#6.1 Elementwise arithmetic
x = np.array([1, 2, 3])  
y = np.array([10, 20, 30])  
  
# All these operations are elementwise  
print(x + y)   # [11 22 33]  
print(x - y)   # [-9 -18 -27]  
print(x * y)   # [10 40 90]  
print(y / x)   # [10. 10. 10.]  
print(x ** 2)  # [1 4 9]  

#6.2 Universal functions (ufuncs)
# 5 evenly spaced points between 0 and pi  
z = np.linspace(0, np.pi, 5)  
print("z:", z)  
  
# Apply trig functions elementwise  
print("sin(z):", np.sin(z))  
print("cos(z):", np.cos(z))  
  
# Exponential and logarithm (avoid log(0))  
print("exp(z):", np.exp(z))  
print("log(z[1:]):", np.log(z[1:]))  

#6.3 Broadcasting rules examples
# A is 3x4 matrix of ones  
A = np.ones((3, 4))  
print("A:\n", A)  
  
# b is 1D array of length 4  
b = np.array([1, 2, 3, 4])  
print("b:", b)  
  
# b is broadcast across rows to shape (3, 4)  
print("A + b:\n", A + b)  
  
# c is 3x1 column vector  
c = np.array([[1], [2], [3]])  
print("c:\n", c)  
  
# c is broadcast across columns to shape (3, 4)  
print("A + c:\n", A + c)  

#6.4 In-place operations
x = np.arange(5, dtype=float)  
print("original x:", x)  
  
# Add 10 to each element in-place  
x += 10  
print("after += 10:", x)  
  
# Multiply each element by 2 in-place  
x *= 2  
print("after *= 2:", x)  

#7. Reductions & Statistics
#7.1 Basic reductions
x = np.arange(1, 7).reshape(2, 3)  
print("x:\n", x)  
# [[1 2 3]  
#  [4 5 6]]  
  
# Sum of all elements  
print("sum:", x.sum())  
  
# Sum along axis=0 (columns)  
print("sum axis=0 (columns):", x.sum(axis=0))  
  
# Sum along axis=1 (rows)  
print("sum axis=1 (rows):", x.sum(axis=1))  
  
# Product of all elements  
print("prod:", x.prod())  
  
# Minimum and maximum element values  
print("min:", x.min(), "max:", x.max())  
  
# Indices (in flattened array) of min and max  
print("argmin:", x.argmin(), "argmax:", x.argmax())  

#7.2 Means, std, var
# Mean of all elements  
print("mean:", x.mean())  
  
# Mean per column  
print("mean axis=0:", x.mean(axis=0))  
  
# Mean per row  
print("mean axis=1:", x.mean(axis=1))  
  
# Standard deviation and variance  
print("std:", x.std(), "var:", x.var())  

#7.3 Cumulative operations
y = np.array([1, 2, 3, 4])  
print("y:", y)  
  
# Cumulative sum: running total  
print("cumsum:", np.cumsum(y))   # [ 1  3  6 10]  
  
# Cumulative product: running product  
print("cumprod:", np.cumprod(y)) # [ 1  2  6 24]  

#7.4 Logical reductions
b = np.array([True, True, False])  
  
# any: True if at least one element is True  
print("any:", b.any())  
  
# all: True if all elements are True  
print("all:", b.all())  
  
M = np.array([[1, 2],  
              [3, 4]])  
print("M:\n", M)  
  
# Check if any element > 2 in each column  
print("(M > 2).any(axis=0):", (M > 2).any(axis=0))  
  
# Check if all elements > 2 in each row  
print("(M > 2).all(axis=1):", (M > 2).all(axis=1))  

#8. Linear Algebra (np.linalg)
A = np.array([[1, 2],  
              [3, 4]])  
b = np.array([5, 6])  
  
print("A:\n", A)  
print("b:", b)  

#8.1 Matrix multiply & dot
# Matrix-vector multiplication using @ operator  
print("A @ b:", A @ b)  
  
# Matrix-matrix multiplication  
print("A @ A:\n", A @ A)  
  
# np.dot is equivalent for 1D and 2D cases  
print("np.dot(A, b):", np.dot(A, b))  

#8.2 Solve linear system
# Solve Ax = b for x  
x_sol = np.linalg.solve(A, b)  
print("solution x:", x_sol)  
  
# Verify that A @ x == b (within floating point error)  
print("A @ x_sol:", A @ x_sol)  

#8.3 Inverse, determinant, eigenvalues
# Matrix inverse (A must be square and non-singular)  
A_inv = np.linalg.inv(A)  
print("A_inv:\n", A_inv)  
  
# Determinant of A  
det = np.linalg.det(A)  
print("det(A):", det)  
  
# Eigenvalues (w) and eigenvectors (v) of A  
w, v = np.linalg.eig(A)  
print("eigenvalues:", w)  
print("eigenvectors (columns):\n", v)  

#8.4 Norms, SVD
v = np.array([3, 4])  
  
# Euclidean (L2) norm: sqrt(3^2 + 4^2) = 5  
print("norm(v):", np.linalg.norm(v))  
  
# Singular Value Decomposition: A = U * diag(S) * Vt  
U, S, Vt = np.linalg.svd(A)  
print("U:\n", U)  
print("S (singular values):", S)  
print("Vt:\n", Vt)  

#9. Random Numbers (more details)
# Create a reproducible RNG  
rng = np.random.default_rng(123)  
  
# Uniform [0, 1), shape (2, 2)  
print("uniform:\n", rng.random((2, 2)))  
  
# Normal distribution (mean=0, std=1), 1D array length 5  
print("normal:", rng.normal(loc=0, scale=1, size=5))  
  
# Random integers in [0, 10), 1D array length 5  
print("integers:", rng.integers(low=0, high=10, size=5))  
  
# Bernoulli trials: 10 samples, success prob=0.3  
bernoulli = rng.binomial(n=1, p=0.3, size=10)  
print("bernoulli:", bernoulli)  
  
# Multivariate normal with given mean and covariance  
mean = [0, 0]  
cov = [[1, 0.5],  
       [0.5, 2]]  
mv = rng.multivariate_normal(mean, cov, size=5)  
print("multivariate normal:\n", mv)  

#10. I/O: Saving & Loading
#10.1 np.save / np.load (.npy binary format)
x = np.arange(10)  
print("x:", x)  
  
# Save to a binary .npy file  
np.save("array.npy", x)  
  
# Load it back (dtype and shape preserved)  
loaded = np.load("array.npy")  
print("loaded:", loaded)  

#10.2 np.savez / np.savez_compressed (multiple arrays)
a = np.arange(5)  
b = np.linspace(0, 1, 5)  
  
# Save multiple arrays into a single .npz file with names  
np.savez("arrays.npz", arr1=a, arr2=b)  
  
# Load .npz: acts like a dict of arrays  
data = np.load("arrays.npz")  
print("arr1:", data["arr1"])  
print("arr2:", data["arr2"])  

#10.3 Text formats: savetxt, loadtxt, genfromtxt
X = np.arange(9).reshape(3, 3)  
print("X:\n", X)  
  
# Save as plain text, with integer format  
np.savetxt("array.txt", X, fmt="%d")  
  
# Load from text file (assuming consistent format)  
Y = np.loadtxt("array.txt", dtype=int)  
print("Y loaded with loadtxt:\n", Y)  
  
# genfromtxt is more flexible (handles missing values, etc.)  
Z = np.genfromtxt("array.txt", dtype=int)  
print("Z loaded with genfromtxt:\n", Z)  

#11. Misc / Advanced Tools
#11.1 where
x = np.arange(10)  
print("x:", x)  
  
# Condition: True where x is even  
cond = x % 2 == 0  
print("cond:", cond)  
  
# np.where(cond) returns tuple of indices where cond is True  
idx = np.where(cond)  
print("indices where even:", idx)  
  
# Ternary selection: if cond True -> -1, else -> x  
out = np.where(cond, -1, x)  
print("where result:", out)  

#2D where:
A = np.arange(9).reshape(3, 3)  
print("A:\n", A)  
  
# Indices where elements > 4  
rows, cols = np.where(A > 4)  
print("rows:", rows)  
print("cols:", cols)  
  
# Values at those positions  
print("A[rows, cols]:", A[rows, cols])  

#11.2 unique, bincount, histogram
x = np.array([1, 2, 2, 3, 3, 3])  
print("x:", x)  
  
# Unique values (sorted)  
u = np.unique(x)  
print("unique:", u)  
  
# Unique values and their counts  
u2, counts = np.unique(x, return_counts=True)  
print("values:", u2)  
print("counts:", counts)  
  
# bincount: fast counting for non-negative integer data  
bc = np.bincount(x)  
print("bincount:", bc)  
# Index is the value, value is the count  
# For x=[1,2,2,3,3,3], bincount=[0,1,2,3]  
  
# histogram: counts per bin  
hist, bin_edges = np.histogram(x, bins=3)  
print("hist:", hist)  
print("bin_edges:", bin_edges)  

#11.3 Sorting, argsort, partition
x = np.array([3, 1, 4, 1, 5, 9])  
print("x:", x)  
  
# Sorted copy  
sorted_x = np.sort(x)  
print("sorted_x:", sorted_x)  
  
# Indices that would sort x  
idx = np.argsort(x)  
print("argsort indices:", idx)  
  
# Reordering x using these indices matches sorted_x  
print("x[idx]:", x[idx])  
  
# In-place sort modifies x  
x.sort()  
print("x after in-place sort:", x)  
  
# partition: partially sorts so that element at index k is in final sorted position  
y = np.array([7, 2, 1, 6, 8, 5, 3, 4])  
print("y:", y)  
  
k = 3  
part = np.partition(y, k)  
print("partitioned:", part)  
print(f"k-th smallest element (k={k}):", part[k])  

#11.4 meshgrid & indices
# 1D coordinate vectors  
x = np.linspace(-1, 1, 3)  
y = np.linspace(-1, 1, 3)  
print("x:", x)  
print("y:", y)  
  
# meshgrid: create 2D grids for x and y coordinates  
X, Y = np.meshgrid(x, y)  
print("X:\n", X)  
print("Y:\n", Y)  
  
# indices: create grid of indices for an array of shape (2, 3)  
idx = np.indices((2, 3))  
print("indices shape:", idx.shape)   # (2, 2, 3)  
print("row indices:\n", idx[0])  
print("col indices:\n", idx[1])  

#11.5 einsum (compact tensor ops)
A = np.arange(6).reshape(2, 3)  
B = np.arange(6, 12).reshape(3, 2)  
print("A:\n", A)  
print("B:\n", B)  
  
# Matrix multiply: A(2x3) * B(3x2) -> C(2x2)  
C = np.einsum('ik,kj->ij', A, B)  
print("C = A @ B via einsum:\n", C)  
  
# Dot product of two vectors  
v = np.array([1, 2, 3])  
w = np.array([4, 5, 6])  
dp = np.einsum('i,i->', v, w)  
print("dot product via einsum:", dp)  
  
# Row sums of A using einsum  
s = np.einsum('ij->i', A)  
print("row sums via einsum:", s)  

#11.6 vectorize & frompyfunc
# Define a plain Python function operating on scalars  
def myfunc(x, y):  
    return x**2 + y**2  
  
# vectorize wraps it so it can accept NumPy arrays  
vec_myfunc = np.vectorize(myfunc)  
  
X = np.arange(3)  
Y = np.arange(3, 6)  
print("X:", X)  
print("Y:", Y)  
print("vec_myfunc(X, Y):", vec_myfunc(X, Y))  
  
# frompyfunc creates a ufunc that returns an object array (very general)  
# parameters: (callable, num_inputs, num_outputs)  
ufunc = np.frompyfunc(lambda x, y: f"{x}-{y}", 2, 1)  
print("frompyfunc result:", ufunc(X, Y))  

#11.7 Masked arrays (np.ma)
data = np.arange(5, dtype=float)  
print("original data:", data)  
  
# Introduce a "bad" value (NaN) at index 2  
data[2] = np.nan  
print("with NaN:", data)  
  
# Create a mask: True where value is NaN  
mask = np.isnan(data)  
print("mask:", mask)  
  
# Wrap in masked array: NaNs (or other masked values) ignored in computations  
marr = np.ma.array(data, mask=mask)  
print("masked array:", marr)  
  
# Mean ignoring masked entries  
print("masked mean:", marr.mean())  

#11.8 Copy vs view: copy, view
x = np.arange(6)  
print("x:", x)  
  
y = x          # y is just another reference to x (no new array)  
z = x.view()   # z is a new array object but shares the same underlying data  
w = x.copy()   # w is a true copy with its own data  
  
# Modify x  
x[0] = 99  
  
print("x:", x)  # changed  
print("y:", y)  # same data as x, so also changed  
print("z:", z)  # view, so also changed  
print("w:", w)  # independent copy, unchanged  