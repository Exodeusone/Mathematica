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
    triplets = find_matching_sum_and_product(target_sum=141, target_product=98136)
    print(f"Les triplets sont les suivants: {', '.join(str(t) for t in triplets)}")
