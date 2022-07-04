morse_code_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
                    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}

running = True
while running:
    message = input("Type message to be converted to Morse code(Type 'QUIT' to stop): ").upper()
    if message == "QUIT":
        running = False
    else:
        message_in_morse = []
        message_list = list(message)
        for item in message_list:
            if item in morse_code_dict:
                message_in_morse.append(f"{morse_code_dict[item]}  ")
        print("".join(message_in_morse))
