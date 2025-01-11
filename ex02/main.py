import time
import sys


MIN_NUMBER = 10000000
MAX_NUMBER = 100000000


def find_kaprekar_numbers(start: int, end: int) -> list[int]:
    """Find all Kaprekar numbers between start and end.

    Args:
        start (int): The start of the range.
        end (int): The end of the range.

    Returns:
        list[int]: The list of Kaprekar numbers.
    """
    kaprekar_numbers = []
    for number in range(start, end):
        squared_number = number * number
        str_squared_number = str(squared_number)
        len_number = len(str(number))

        for split_point in range(len(str_squared_number) - len_number, len(str_squared_number) - len_number + 2):
            if split_point <= 0 or split_point >= len(str_squared_number):
                continue
            left_part = int(str_squared_number[:split_point] or '0')
            right_part = int(str_squared_number[split_point:] or '0')

            if left_part + right_part == number:
                kaprekar_numbers.append(number)
                break

    return kaprekar_numbers


if __name__ == "__main__":
    args = sys.argv[1:]
    min_number = int(args[0]) if len(args) > 0 and args[0].isdigit() else MIN_NUMBER
    max_number = int(args[1]) if len(args) > 1 and args[1].isdigit() else MAX_NUMBER

    base_time = time.time()

    kaprekar_numbers = find_kaprekar_numbers(min_number, max_number)

    print(f"Il y a {len(kaprekar_numbers)} nombres de Kaprekar entre {min_number} et {max_number}")
    if len(kaprekar_numbers) > 0:
        print(f"Les nombres de Kaprekar sont les suivants: {', '.join(str(number) for number in kaprekar_numbers)}")