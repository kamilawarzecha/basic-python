def div(a, b):
    """The function returns a list of numbers in the given range that are divided by 2 and not divided by 3"""
    try:
        numbers = []
        for i in range(a, b + 1):
            if i % 2 == 0 and i % 3 != 0:
                numbers.append(i)
        return numbers
    except TypeError:
        return "Enter numbers separated by a space."


print(div(1, 2))
print(div(0,20 ))
print(div("kot", "pies"))