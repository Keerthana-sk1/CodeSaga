#Check if a number is a power of 3
def power_of_three(num):
    if num <= 0:
        return False
    while num % 3 == 0:
        num /= 3
    return num == 1
