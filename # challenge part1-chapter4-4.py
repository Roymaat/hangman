# challenge part1-chapter4-4

def step_1 (i):
    return i%13

def step_2 (y):
    return y*4

x = int(input("x="))
print(step_2(step_1(x)))
