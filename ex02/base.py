from collections import Counter

ciphers = int(input("Donner le nombre de chiffres voulu : "))


def smallest_multiple_congruent_1(p, q, max_iterations=10000000):
    k = 1
    while (p * k) % q != 1:
        k += 1
        if k > max_iterations:
            return None  # Abandonner et retourner None si la limite est atteinte
    return p * k


Kaprekar_numbers = []


def dec(n):
    Result = [1]  # Ajouter 1 comme facteur initial
    d = 2  # Commencez par 2, le plus petit facteur premier
    while n % d == 0:
        Result.append(d)
        n //= d
    d = 3
    while d * d <= n:
        while n % d == 0:
            Result.append(d)
            n //= d
        d += 2
    if n > 1:
        Result.append(n)

    # Regrouper les facteurs par puissance
    counter = Counter(Result)
    grouped_factors = [factor ** count for factor, count in counter.items()]

    # Vérifier que grouped_factors n'est pas vide
    if not grouped_factors:
        raise ValueError("grouped_factors ne doit pas être vide.")

    from itertools import combinations
    all_factors = set(grouped_factors)
    num_factors = len(grouped_factors)

    # On parcourt toutes les combinaisons possibles de facteurs premiers
    for n in range(1, num_factors + 1):
        for combo in combinations(grouped_factors, n):
            product = 1
            for factor in combo:
                product *= factor
            all_factors.add(product)
    
    sorted_all_factors = sorted(all_factors)
    print(sorted_all_factors)

    # Retourner grouped_factors
    return sorted_all_factors

if ciphers <= 2:
    for k in range(ciphers, ciphers + 1):
        number = 10**k - 1
        grouped_factors = dec(number)
        print(f"Facteurs regroupés de {number} : {grouped_factors}")
        for valeur in grouped_factors:
            p = valeur
            q = number // p
            g_value = smallest_multiple_congruent_1(p, q)
            if g_value is None:
                continue  # Passer au suivant si on abandonne
            if len(str(number)) == ciphers:
                Kaprekar_numbers.append(number)
            else:
                continue
            # Ajouter le nombre lui-même s'il est congru à 1 modulo 1
            if number % 1 == 1 or number == 1:
                Kaprekar_numbers.append(number)
            if len(str(g_value)) == ciphers:
                Kaprekar_numbers.append(g_value)
            else:
                continue
else:
    for k in range(ciphers-1, ciphers + 2):
        number = 10**k - 1
        grouped_factors = dec(number)
        print(f"Facteurs regroupés de {number} : {grouped_factors}")
        for valeur in grouped_factors:
            p = valeur
            q = number // p
            g_value = smallest_multiple_congruent_1(p, q)
            if g_value is None:
                continue  # Passer au suivant si on abandonne
            if len(str(g_value)) == ciphers:
                Kaprekar_numbers.append(number)
            else:
                continue
            # Ajouter le nombre lui-même s'il est congru à 1 modulo 1
            if number % 1 == 1 or number == 1:
                Kaprekar_numbers.append(number)
            if len(str(g_value)) == ciphers:
                Kaprekar_numbers.append(g_value)
            else:
                continue

for number in Kaprekar_numbers[:]: 
    if len(str(number)) != ciphers:
        Kaprekar_numbers.remove(number)

print("Les nombres de Kaprekar en base 10 à", ciphers, "chiffres sont :", sorted(set(Kaprekar_numbers)))
print("Il y en a d'ailleurs", str(len(sorted(set(Kaprekar_numbers)))))
