import requests

ATBASH = [
    ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"],
    ["Z", "Y", "X", "W", "V", "U", "T", "S", "R", "Q", "P", "O", "N"],
    ]

INITIAL_TEXT = "UNQDBBYKKNHACSYZCIKIUKTRILEKLZOAHNXJTZPFEZPHZVHRSJWWFNEX"


def load_french_words() -> list[str]:
    '''
    Load a list of French words from a remote text file.

    Returns:
        list[str]: A list containing French words loaded from the remote file.

    Raises:
        Exception: If there is an error loading or processing the remote file.
    '''
    try:
        response = requests.get("https://raw.githubusercontent.com/eymenefealtun/all-words-in-all-languages/main/French/French.txt")
        response.raise_for_status()
        return response.text.split(',')
    except Exception as e:
        print(e)
        exit(1)


def custom_atbash_uncipher(text: str, start_index: int) -> str:
    '''
    Uncipher a text using the Atbash cipher.

    Args:
        text (str): The text to uncipher.
        start_index (int): The index to start the unciphering from.

    Returns:
        str: The unciphered text.
    '''
    uncipher_text = ""
    for _ in range(start_index):
        ATBASH[0] = [ATBASH[0][-1]] + ATBASH[0][:-1]
    text = text[::-1]
    for letter in text:
        if letter in ATBASH[0]:
            index = ATBASH[0].index(letter)
            current_letter = ATBASH[1][index]
        else:
            index = ATBASH[1].index(letter)
            current_letter = ATBASH[0][index]
        uncipher_text += current_letter
        ATBASH[0] = ATBASH[0][1:] + [ATBASH[0][0]]
    uncipher_text = uncipher_text[::-1]
    return uncipher_text


def custom_atbash_cipher(text: str) -> str:
    '''
    Encipher a text using the Atbash cipher.

    Args:
        text (str): The text to encipher.

    Returns:
        str: The enciphered text.
    '''
    ciper_text = ""
    current_atbash_in_memory = ATBASH
    for letter in text:
        if letter in current_atbash_in_memory[0]:
            index = current_atbash_in_memory[0].index(letter)
            current_letter = current_atbash_in_memory[1][index]
        else:
            index = current_atbash_in_memory[1].index(letter)
            current_letter = current_atbash_in_memory[0][index]
        ciper_text += current_letter
    return ciper_text


def detect_if_more_than_3_words_are_in_text(text: str, french_words: list[str]) -> bool:
    '''
    Detect if more than 3 words are in the text.

    Args:
        text (str): The text to detect words in.

    Returns:
        bool: True if more than 3 words are in the text, False otherwise.
    '''
    nb_detected_words = 0
    for word in french_words:
        if len(word) > 3 and word in text.lower():
            nb_detected_words += 1
    return nb_detected_words > 3


if __name__ == "__main__":
    french_words = load_french_words()
    for i in range(len(INITIAL_TEXT)):
        uncipher_text = custom_atbash_uncipher(INITIAL_TEXT, i)
        if detect_if_more_than_3_words_are_in_text(text=uncipher_text, french_words=french_words):
            print(f"La phrase déchiffrée est: {uncipher_text}")
            break
