import sys

TARGET_SUM = 141
TARGET_PRODUCT = 98136


def find_matching_sum_and_product(
        target_sum: int,
        target_product: int,
        ) -> list[tuple[int, int, int]]:
    """Find the triplets that match the sum and product

    Args:
        target_sum (int): The sum of the triplet
        target_product (int): The product of the triplet

    Returns:
        list[tuple[int, int, int]]: The triplets that match the sum and product
    """
    find_matching_triplets = []
    for a in range(1, target_sum):
        for b in range(1, target_sum):
            for c in range(1, target_sum):
                if a + b + c == target_sum and a * b * c == target_product:
                    find_matching_triplets.append((a, b, c))
    return find_matching_triplets


if __name__ == "__main__":
    args = sys.argv[1:]
    target_sum = int(args[0]) if len(args) > 0 and args[0].isdigit() else TARGET_SUM
    target_product = int(args[1]) if len(args) > 1 and args[1].isdigit() else TARGET_PRODUCT
    triplets = find_matching_sum_and_product(target_sum, target_product)
    print(f"Les triplets sont les suivants: {', '.join(str(t) for t in triplets)}")
