from functools import reduce

numbrs = [1, 2, 3, 4, 5] 

def reducer (acd, var):
    print("a = ", a)
    print("b = ", b)
    print("a + b = ", a+b)
    return a+b
print(reduce(sum, numbrs, 10))