ATBASH = [
    ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"],
    ["Z", "Y", "X", "W", "V", "U", "T", "S", "R", "Q", "P", "O", "N"],
    ]

INITIAL_TEXT = "UNQDBBYKKNHACSYZCIKIUKTRILEKLZOAHNXJTZPFEZPHZVHRSJWWFNEX"


def atbash_uncipher(text: str, start_index: int) -> str:
    uncipher_text = ""
    current_atbash_in_memory = ATBASH.copy()
    for i in range(start_index):
        current_atbash_in_memory[0] = [current_atbash_in_memory[0][-1]] + current_atbash_in_memory[0][:-1]
    text = text[::-1]
    for letter in text:
        if letter in current_atbash_in_memory[0]:
            index = current_atbash_in_memory[0].index(letter)
            current_letter = current_atbash_in_memory[1][index]
        else:
            index = current_atbash_in_memory[1].index(letter)
            current_letter = current_atbash_in_memory[0][index]
        uncipher_text += current_letter
        current_atbash_in_memory[0] = current_atbash_in_memory[0][1:] + [current_atbash_in_memory[0][0]]
    uncipher_text = uncipher_text[::-1]
    return uncipher_text

def atbash_cipher(text: str) -> str:
    ciper_text = ""
    current_atbash_in_memory = ATBASH.copy()
    for i, letter in enumerate(text):
        if letter in current_atbash_in_memory[0]:
            index = current_atbash_in_memory[0].index(letter)
            current_letter = current_atbash_in_memory[1][index]
        else:
            index = current_atbash_in_memory[1].index(letter)
            current_letter = current_atbash_in_memory[0][index]
        ciper_text += current_letter
        if i != len(text) - 1:
            current_atbash_in_memory[0] = [current_atbash_in_memory[0][-1]] + current_atbash_in_memory[0][:-1]
    return ciper_text




if __name__ == "__main__":
    # res = atbash_cipher(INITIAL_TEXT)
    # print(res)
    for i in range(len(INITIAL_TEXT)):
        res = atbash_uncipher(INITIAL_TEXT, i)
        if "RENDEZVOUS" in res:
            print(res)
            break
