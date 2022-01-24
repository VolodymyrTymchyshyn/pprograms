NATO_ALPHABET = {
  "A": "Alfa",
  "B": "Bravo",
  "C": "Charlie",
  "D": "Delta",
  "E": "Echo",
  "F": "Foxtrot",
  "G": "Golf",
  "H": "Hotel",
  "I": "India",
  "J": "Juliett",
  "K": "Kilo",
  "L": "Lima",
  "M": "Mike",
  "N": "November",
  "O": "Oscar",
  "P": "Papa",
  "Q": "Quebec",
  "R": "Romeo",
  "S": "Sierra",
  "T": "Tango",
  "U": "Uniform",
  "V": "Victor",
  "W": "Whiskey",
  "X": "X-ray",
  "Y": "Yankee",
  "Z": "Zulu"
}

def translate(textToTranslate):
    translation = ""
    for index, letter in enumerate(textToTranslate):
        if index != 0:
            translation+= " "
        translation += f"{NATO_ALPHABET[letter.upper()]}"
    return translation

textToTranslate = input("Text: ")
print(f"Inputed text: {textToTranslate} \nSpelled text: {translate(textToTranslate)}")