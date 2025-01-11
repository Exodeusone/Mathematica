import time
import sys


MIN_NUMBER = 10000000
MAX_NUMBER = 100000000


def find_kaprekar_numbers_optimized(start: int, end: int) -> list[int]:
    kaprekar_numbers = []
    for number in range(start, end):
        squared_number = number * number
        str_squared_number = str(squared_number)
        len_number = len(str(number))

        # Essayer de diviser le carré en deux parties, où la longueur de la partie droite est égale à la longueur du nombre original
        for split_point in range(len(str_squared_number) - len_number, len(str_squared_number) - len_number + 2):
            if split_point <= 0 or split_point >= len(str_squared_number):
                continue
            left_part = int(str_squared_number[:split_point] or '0')
            right_part = int(str_squared_number[split_point:] or '0')

            if left_part + right_part == number:
                print(f"{number}^2 = {squared_number}, {left_part} + {right_part} = {number}")
                kaprekar_numbers.append(number)
                break

    return kaprekar_numbers


if __name__ == "__main__":
    args = sys.argv[1:]
    min_number = int(args[0]) if len(args) > 0 and args[0].isdigit() else MIN_NUMBER
    max_number = int(args[1]) if len(args) > 1 and args[1].isdigit() else MAX_NUMBER

    base_time = time.time()

    kaprekar_numbers = find_kaprekar_numbers_optimized(min_number, max_number)

    print(time.time() - base_time)
    print(len(kaprekar_numbers))
