from collections import Counter
from itertools import combinations
import sys


def smallest_multiple_congruent_1(num: int, mod: int, max_iterations: int = 10000000) -> int | None:
    """Find the smallest multiple of num that is congruent to 1 modulo mod.

    Args:
        num (int): The number to multiply.
        mod (int): The modulo.
        max_iterations (int, optional): The maximum number of iterations. Defaults to 10000000.

    Returns:
        int | None: The smallest multiple of num that is congruent to 1 modulo mod.
    """
    multiplier = 1
    while (num * multiplier) % mod != 1:
        multiplier += 1
        if multiplier > max_iterations:
            return None
    return num * multiplier


def find_all_divisors(number: int) -> list[int]:
    """Find all divisors of a number.

    Args:
        number (int): The number to find the divisors of.

    Returns:
        list[int]: The list of divisors.
    """
    if number <= 0:
        raise ValueError("number must be positive")

    factors = [1]
    for prime_number in [2] + list(range(3, int(number**0.5) + 1, 2)):
        while number % prime_number == 0:
            factors.append(prime_number)
            number //= prime_number
    if number > 1:
        factors.append(number)

    factors_counts = Counter(factors)
    unique_factors = [factor**count for factor, count in factors_counts.items()]

    all_divisors = set()

    for n in range(1, len(unique_factors) + 1):
        for combo in combinations(unique_factors, n):
            product = 1
            for factor in combo:
                product *= factor
            all_divisors.add(product)

    return sorted(all_divisors)


def find_kaprekar_numbers(ciphers: int) -> list[int]:
    """Find all Kaprekar numbers based on the number of ciphers.

    Args:
        ciphers (int): The number of ciphers.

    Returns:
        list[int]: The list of Kaprekar numbers.
    """
    kaprekar_numbers = []
    for k in range(ciphers, ciphers + (1 if ciphers <= 2 else 2)):
        large_number = 10 ** (k or 1) - 1
        divisors = find_all_divisors(large_number)
        for num in divisors:
            mod = large_number // num
            g_value = smallest_multiple_congruent_1(num, mod)
            if not g_value or (
                len(str(large_number)) != ciphers
                and len(str(g_value)) != ciphers
            ):
                continue
            if (
                len(str(large_number)) == ciphers
                or large_number % 1 == 1
                or large_number == 1
            ):
                kaprekar_numbers.append(large_number)
            if len(str(g_value)) == ciphers:
                kaprekar_numbers.append(g_value)

    return kaprekar_numbers


if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) != 1 or not args[0].isdigit():
        print("Usage: python base.py <number of ciphers>")
        sys.exit(1)
    ciphers = int(args[0])
    kaprekar_numbers = sorted(set(find_kaprekar_numbers(ciphers)))
    print(f"Les nombres de Kaprekar en base 10 à {ciphers} chiffres sont au nombre de {len(kaprekar_numbers)}: \n{kaprekar_numbers}")
