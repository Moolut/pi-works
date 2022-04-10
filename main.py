def main():
    # Combines all the function and returns the results
    first_question_triangle = convert_txt_to_2D_array("first_triangle.txt")
    second_question_triangle = convert_txt_to_2D_array("second_triangle.txt")

    first_question_max_sum = calculate_max_path(first_question_triangle)
    second_question_max_sum = calculate_max_path(second_question_triangle)

    print(f"First Question Max Path Sum With Non-Prime Numbers = {first_question_max_sum}")
    print(f"Second Question Max Path Sum With Non-Prime Numbers = {second_question_max_sum}")


def convert_txt_to_2D_array(file_name):
    # Reads the txt file and returns a 2D array
    # Takes a file_name as an argument
    # file_name -> string
    return [[int(i) for i in line.split()] for line in open(file_name)]


def calculate_max_path(triangle):
    # Calculates the max sum path from the bottom up
    # Takes a 2D array as an argument
    # triangle -> 2D array

    prime_triangle = replace_prime_number(triangle)
    path = prime_triangle[-1]
    for row in prime_triangle[-2::-1]:
        path = [0 if n == 0 or (a, b) == (0, 0) else n + max(a , b)
                for n, a, b in zip(row, path, path[1:])]

    return path[0]

def check_prime(number):
    # Checks whether the number is prime or not and return boolean
    # Takes a number as an argument
    # number -> integer
    is_prime = True

    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                is_prime = False
                break
    else:
        is_prime = False

    return  0 if is_prime else number



def replace_prime_number(triangle):
    # Replaces the prime numbers with None in the 2D array and returns it back
    # Takes a triangle as an argument
    # triangle -> 2D array

    prime_array = []
    rows = len(triangle)

    for i in range(rows):
        columns = len(triangle[i])
        prime_row = []
        for j in range(columns):
            prime_row.append(check_prime(triangle[i][j]))
        prime_array.append(prime_row)
    return  prime_array


main()

