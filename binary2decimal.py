import timeit

"""
Convert binary value (in string) to decimal value. 
This module codes 3 fucntions which convert given 
binary string to decimal. Each function’s 
speed/performance is measured(using timeit) and 
compared againt its equivalent Library function: 
int(binary,2).
"""

B = "11010001010111001010101110101"

def b2d_enum_slice(B):
    """
    (fastest)
    Reverse binary string using slice(stride), 
    enumerate it to get bit postions and 
    compute decimal value.
    """
    sum = 0
    for i,c in enumerate(B[::-1]):
        if c == "1":
            sum += 2**i
    return sum

def b2d_range_index(B):
    """
    Use range to get bit positions, 
    index binary string and 
    compute decimal value.
    """
    MSB = len(B) - 1
    sum = 0
    for i in range(0, MSB+1):
        if B[i] == "1":
            sum += 2**(MSB-i) 
    return sum

def b2d_map_multiply(B):
    """
    Convert binary string to 
    integers(0,1) via map, and 
    compute decimal value (by multiplication).
    """
    sum = 0
    for d in map(int,B):
        sum = sum*2 + d
    return sum

print("BINARY:", B)
print("DECIMAL:")
print("Library: ", int(B,2))
print("b2d_range_index:", b2d_range_index(B))
print("b2d_enum_slice:", b2d_enum_slice(B))
print("b2d_map_multiply:", b2d_map_multiply(B))
print("-" * 60)

iter = 1000
rep = 5
print("Iterations: %s" % iter)
print("Repetitions: %s" % rep)
print("-" * 60)
print("-" * 60)

t0 = timeit.repeat("int(B,2)", setup="from __main__ import B", number=iter, repeat=rep) 
print("Library time: %s" % min(t0))
print("-" * 60)

t1 = timeit.repeat("b2d_enum_slice(B)", setup="from __main__ import b2d_enum_slice; from __main__ import B;", number=iter, repeat=rep)
print("b2d_enum_slice: %s" % min(t1))
print("b2d_enum_slice/Library: %s" % (min(t1)/min(t0)))
print("-" * 60)

t2 = timeit.repeat("b2d_range_index(B)", setup="from __main__ import b2d_range_index; from __main__ import B;", number=iter, repeat=rep)
print("b2d_range_index: %s" % min(t2))
print("b2d_range_index/Library: %s" % (min(t2)/min(t0)))
print("-" * 60)

t3 = timeit.repeat("b2d_map_multiply(B)", setup="from __main__ import b2d_map_multiply; from __main__ import B;", number=iter, repeat=rep)
print("b2d_map_multiply: %s" % min(t3))
print("b2d_map_multiply/Library: %s" % (min(t3)/min(t0)))
print("-" * 60)

"""
output:
BINARY: 11010001010111001010101110101
DECIMAL:
Library:  439063925
b2d_range_index: 439063925
b2d_enum_slice: 439063925
b2d_map_multiplication: 439063925
————————————————————
Iterations: 1000
Repetitions: 5
————————————————————
————————————————————
Library time: 0.0006716666684951633
————————————————————
b2d_enum_slice: 0.015914250005153008
b2d_enum_slice/Library: 23.69367239974572
————————————————————
b2d_range_index: 0.017540083325002342
b2d_range_index/Library: 26.11426790657939
————————————————————
b2d_map_multiply: 0.019134166665025987
b2d_map_multiply/Library: 28.487592972113923
————————————————————
"""

