"""
The problem statement and constraints go here
"""


def two_sum_brute(arr: list, target: int) -> bool:
    "A brute force implementation of the two problem"

    for i in arr:
        for j in arr: 
            if i + j == target: 
                return True
    
    return False


test = [1, 2, 3, 4, 5,]
print(two_sum_brute(test, 5))