# Example for n = 5:
# *****
# *   *
# *   *
# *   *
# *****
def hollow_square(n):
    star = n * "*" + "\n"
    space = "*" + ((n - 2) * " ") + "*" + "\n"
    result = ""

    if n == 1:
        result = star

    else:
        result += star + (n - 2)*(space) + star
        
    return result.strip() # strip() removes all spaces from both ends, while rstrip() removes trailing spaces (so only at the end)

# 1
# 12
# 123
# 1234
def number_pattern(n):
    number = ""
    line = ""
    count = 1

    while count <= n:
        line += str(count)
        number += line + "\n"
        count += 1
    # for i in range(1, n + 1):
    #     line += str(i)
    #     number += line + "\n"

    return number.rstrip()

# Example: For n = 5, sum = 1 + 2 + 3 + 4 + 5 = 15
def sum_of_natural_numbers(n):
    count = 0
    sum = 0

    while count <= n:
        sum += count
        count += 1

    return sum

# Example for n = 4:
#    *
#   ***
#  *****
# *******
def centered_star_pyramid(n):
    star = ""
    space = ""
    pyramid = ""

    for j in range (1, n + 1):
        space = ((n - j) * " ")
        star = (((2 * j) - 1) * "*")
        pyramid += space + star + "\n"

    return pyramid.rstrip()