import random

def roll(number_of_dice, number_of_sides=6, modifier=0):
    possible_dice = [3, 4, 6, 8, 10, 12, 100]
    if number_of_sides not in possible_dice:
        raise Exception('No such dice! (Choose from ' + str(possible_dice) + ')')
    try:
        score = 0
        for i in range(number_of_dice):
            score += random.randint(1, number_of_sides)
        score += modifier
        return score
    except Exception:
        return


print(roll(2))
print(roll(4, 10, 7))
print(roll(1, 2))
