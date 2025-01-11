import time

def is_kaprekar_number(n, base):
    n_squared = n ** 2
    str_n_squared = str(n_squared).zfill(base * 2)
    left = int(str_n_squared[:base]) if str_n_squared[:base] else 0
    right = int(str_n_squared[base:])
    return n == left + right, left, right

def find_kaprekar_numbers():
    kaprekar_numbers = []
    kaprekar_proofs = []
    total_numbers = 100000000 - 10000000  # Nombre total à parcourir
    start_time = time.time()  # Temps de début

    for count, number in enumerate(range(10000000, 100000000)):
        for base in range(1, 9):
            is_kaprekar, left, right = is_kaprekar_number(number, base)
            if is_kaprekar:
                kaprekar_numbers.append(number)
                kaprekar_proofs.append(f"{number}^2 = {number**2}, {left} + {right} = {number}")
                break  # Arrêter de vérifier d'autres bases une fois que nous avons trouvé une correspondance
        
        # Calculer le temps restant toutes les 10000 itérations pour éviter de ralentir le programme
        if count % 10000 == 0:
            elapsed_time = time.time() - start_time
            time_per_number = elapsed_time / (count + 1)
            estimated_total_time = time_per_number * total_numbers
            remaining_time = estimated_total_time - elapsed_time
            remaining_minutes = remaining_time / 60
            print(f"Temps restant estimé : {remaining_minutes:.2f} minutes")

    return kaprekar_numbers, kaprekar_proofs

kaprekar_numbers, kaprekar_proofs = find_kaprekar_numbers()
print("Les nombres de Kaprekar à 8 chiffres sont : ", kaprekar_numbers)
print("Les preuves des nombres de Kaprekar sont : ", kaprekar_proofs)
