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



# Define a function to check if the input text contains valid characters
def valid_text(input_text):
    valid_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 ")
    return all(char in valid_characters for char in input_text)



# Define a function to check if the input Morse code contains valid characters
def valid_morse(input_morse):
    valid_morse_characters = set(".-| ")
    return all(char in valid_morse_characters for char in input_morse)



# Define a function to handle errors during text input
def valid_text_input():
    while True:
        text = input("Enter text to encrypt to Morse Code: ")
        if valid_text(text):
            return text
        else:
            print("Invalid characters. Please enter only English letters, numbers, and spaces.")



# Define a function to handle errors during Morse code input
def valid_morse_input():
    while True:
        morse_code = input("Enter Morse Code to decrypt to text: ")
        if valid_morse(morse_code):
            return morse_code
        else:
            print("Invalid characters. Please enter only Morse code characters (., -, |, and space).")



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



if __name__ == '__main__': 
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

            text = valid_text_input()
            morse_code = text_to_morse(text)
            print("Morse Code: ", morse_code)


        elif mode == "D":
            # Decryption
            print('Decryption mode entered. ')
            print('Unknown or invalid characters will be returned as "#", a "."(full stop) is unrecognised and will be returned as an "e". ')
            print('Separate your morse characters by using " "(space), separate your words by using " | "(space, shift + backslash, space). ')
            
            morse_code = valid_morse_input()
            text = morse_to_text(morse_code)
            print("Text: ", text.strip())


        elif mode == "Q":
            print("Quitting the application")
            break


        else:
            print("Please enter a valid response.")






