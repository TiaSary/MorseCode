# Define a dictionary for converting from text to morse
ttm = {'A' : '.-', 'B' : '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 
       'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 
       'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 
       'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 
       'Y': '-.--', 'Z': '--..', 'a' : '.-', 'b' : '-...', 'c': '-.-.', 'd': '-..', 
       'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 
       'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 
       'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 
       'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..', ' ' : '|', '0': '-----', 
       '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', 
       '7': '--...', '8': '---..', '9': '----.',}



# Define a dictionary from morse to text
mtt = {'.-': 'a', '-...': 'b', '-.-.': 'c', '-..': 'd', '.': 'e', '..-.': 'f', 
       '--.': 'g', '....': 'h', '..': 'i', '.---': 'j', '-.-': 'k', '.-..': 'l', 
       '--': 'm', '-.': 'n', '---': 'o', '.--.': 'p', '--.-': 'q', '.-.': 'r', 
       '...': 's', '-': 't', '..-': 'u', '...-': 'v', '.--': 'w', '-..-': 'x', 
       '-.--': 'y', '--..': 'z',  "|" : " ", '-----': '0', '.----': '1', '..---': '2', 
       '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8', 
       '----.': '9',}



# Define a function that converts text to morse
def text_to_morse(text):
    morse_code = ""

    for text_letter in text:
        morse_letter = ttm.get(text_letter, '#') 
        morse_code += morse_letter + " "
    return morse_code.strip()



# Define a function that converts from morse to text
def morse_to_text(morse_code):
    morse_list = morse_code.split(' ') #splits string of morse to individual sequences
    text = ""
    
    for morse_letter in morse_list:
        text_letter = mtt.get(morse_letter, '#') 
        text += text_letter
    return text.strip()



# Application
print("This application has been designed to encypt your text to Morse Code, and decrypt your Morse Code to text.")

while True:
    print('Enter "E" to encrypt, "D" to decrypt, and "Q" to quit the application.')
    mode = input().upper()

    if mode == "E":
        # Encryption
        print('Encryption mode entered.')
        print('You may only enter english letters and numbers, characters that are not english letters or numbers will be returned as "#".')
        print('The encrypted words will be separated using "|".')
        text = input("Enter text to encrypt to Morse Code: ")

        morse_code = text_to_morse(text)
        print("Morse Code: ", morse_code)

    elif mode == "D":
        # Decryption
        print('Decryption mode entered. ')
        print('Unknown or invalid characters will be returned as "#", a "."(fullstop) is unrecognised and will be returned as an "e". ')
        print('Seperate your morse characters by using " "(space), seperate your words by using " | "(space, shift + backslash, space). ')

        morse_code = input("Enter Morse Code to decrypt to text: ")
        text = morse_to_text(morse_code)
        print("Text = ", text.strip())

    elif mode == "Q":
        print("Quitting the application")
        break

    else:
        print("Please enter a valid response.")






