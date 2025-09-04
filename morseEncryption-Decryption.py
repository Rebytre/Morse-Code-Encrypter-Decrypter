#Morse Encrypter / Decrypter
#By: Rebytre
#A python program designed encrypt plaintext into Morse code and decrypt Morse code into plaintext.

#Morse to Plaintext:

def convertMorseToPlaintext():
    global morseCode
    singleMorseCharacter = ""
    output = ""
    charactersSearched = 0
    while charactersSearched != len(morseCode):
        skipSpaces = avoidSpaces(charactersSearched)
        charactersSearched += skipSpaces
        singleMorseCharacter, charactersSearched = findMorseCharacter(charactersSearched)
        output += convertMorseToPlaintextCharacter(singleMorseCharacter)
        if charactersSearched == len(morseCode): break
        else: singleMorseCharacter = ""
    return output

def findMorseCharacter(charactersSearched):
    global morseCode
    charactersSearchedPlusI = charactersSearched
    morseCharacter = ""
    for i in range(charactersSearched, len(morseCode)):
        if morseCode[i] == " ":
            break
        else: 
            charactersSearchedPlusI += 1
            morseCharacter += morseCode[i]
    return morseCharacter, charactersSearchedPlusI

def avoidSpaces(charactersSearched):
    global morseCode
    spacesFound = 0
    for i in range(charactersSearched,len(morseCode)):
        if morseCode[i] == " ":
            spacesFound += 1
        else:
            break
    return spacesFound
        

def convertMorseToPlaintextCharacter(singleMorseCharacter):
    if len(singleMorseCharacter) <= 4:
        #Alphabet:
        if singleMorseCharacter[0] == ".":
            if len(singleMorseCharacter) == 1: return "e"
            elif singleMorseCharacter[1] == ".":
                if len(singleMorseCharacter) == 2: return "i"
                elif singleMorseCharacter[2] == ".":
                    if len(singleMorseCharacter) == 3: return "s"
                    elif singleMorseCharacter[3] == ".": return "h"
                    elif singleMorseCharacter[3] == "-": return "v"
                    else: return "[?]"
                elif singleMorseCharacter[2] == "-":
                    if len(singleMorseCharacter) == 3: return "u"
                    elif singleMorseCharacter[3] == ".": return "f"
                    else: return "[?]"
                else: return "[?]"
            elif singleMorseCharacter[1] == "-":
                if len(singleMorseCharacter) == 2: return "a"
                elif singleMorseCharacter[2] == ".":
                    if len(singleMorseCharacter) == 3: return "r"
                    elif singleMorseCharacter[3] == ".": return "l"
                    else: return "[?]"
                elif singleMorseCharacter[2] == "-":
                    if len(singleMorseCharacter) == 3: return "w"
                    elif singleMorseCharacter[3] == ".": return "p"
                    elif singleMorseCharacter[3] == "-": return "j"
                    else: return "[?]"
                else: return "[?]"
            else: return "[?]"
        elif singleMorseCharacter[0] == "-":
            if len(singleMorseCharacter) == 1: return "t"
            elif singleMorseCharacter[1] == ".":
                if len(singleMorseCharacter) == 2: return "n"
                elif singleMorseCharacter[2] == ".":
                    if len(singleMorseCharacter) == 3: return "d"
                    elif singleMorseCharacter[3] == ".": return "b"
                    elif singleMorseCharacter[3] == "-": return "x"
                    else: return "[?]"
                elif singleMorseCharacter[2] == "-":
                    if len(singleMorseCharacter) == 3: return "k"
                    elif singleMorseCharacter[3] == ".": return "c"
                    elif singleMorseCharacter[3] == "-": return "y"
                    else: return "[?]"
                else: return "[?]"
            elif singleMorseCharacter[1] == "-":
                if len(singleMorseCharacter) == 2: return "m"
                elif singleMorseCharacter[2] == ".":
                    if len(singleMorseCharacter) == 3: return "g"
                    elif singleMorseCharacter[3] == ".": return "z"
                    elif singleMorseCharacter[3] == "-": return "q"
                    else: return "[?]"
                elif singleMorseCharacter[2] == "-":
                    if len(singleMorseCharacter) == 3: return "o"
                    else: return "[?]"
                else: return "[?]"
            else: return "[?]"
        elif singleMorseCharacter[0] == "/": return " "
        else: return "[?]"
    elif len(singleMorseCharacter) == 5:
        #Numbers + 5len Symbols:
        if singleMorseCharacter[0] == ".":
            if singleMorseCharacter[1] == ".":
                if singleMorseCharacter[2] == ".":
                    if singleMorseCharacter[3] == ".":
                        if singleMorseCharacter[4] == ".": return "5"
                        elif singleMorseCharacter[4] == "-": return "4"
                        else: return "[?]"
                    elif singleMorseCharacter[3] == "-": return "3"
                    else: return "[?]"
                elif singleMorseCharacter[2] == "-": return "2"
                else: return "[?]"
            elif singleMorseCharacter[1] == "-":
                if singleMorseCharacter[2] == "-": return "1"
                elif singleMorseCharacter[2] == ".": return "&"
                else: return "[?]"
            else: return "[?]"
        elif singleMorseCharacter[0] == "-":
            if singleMorseCharacter[1] == "-":
                if singleMorseCharacter[2] == "-":
                    if singleMorseCharacter[3] == "-":
                        if singleMorseCharacter[4] == "-": return "0"
                        elif singleMorseCharacter[4] == ".": return "9"
                        else: return "[?]"
                    elif singleMorseCharacter[3] == ".": return "8"
                    else: return "[?]"
                elif singleMorseCharacter[2] == ".": return "7"
                else: return "[?]"
            elif singleMorseCharacter[1] == ".": 
                if singleMorseCharacter[2] == ".":
                    if singleMorseCharacter[3] == ".":
                        if singleMorseCharacter[4] == ".": return "6"
                        elif singleMorseCharacter[4] == "-": return "\n"
                        else: return "[?]"
                    elif singleMorseCharacter[3] == "-": return "/"
                    else: return "[?]"
                elif singleMorseCharacter[2] == "-": return "("  
                else: return "[?]"
            else: return "[?]"
        else: return "[?]"
    elif len(singleMorseCharacter) == 6:
        #6len Symbols
        if singleMorseCharacter[0] == ".":
            if singleMorseCharacter[1] == ".": return "?"
            elif singleMorseCharacter[1] == "-":
                if singleMorseCharacter[2] == ".":
                    if singleMorseCharacter[3] == ".": return "\""
                    elif singleMorseCharacter[3] == "-": return "."
                    else: return "[?]"
                elif singleMorseCharacter[2] == "-": return "\'"
                else: return "[?]"
            else: return "[?]"
        elif singleMorseCharacter[0] == "-":
            if singleMorseCharacter[1] == ".":
                if singleMorseCharacter[2] == ".": return "-"
                elif singleMorseCharacter[2] == "-":
                    if singleMorseCharacter[3] == ".":
                        if singleMorseCharacter[5] == ".": return ";"
                        elif singleMorseCharacter[5] == "-": return "!"
                        else: return "[?]"
                    elif singleMorseCharacter[3] == "-": return ")"
                    else: return "[?]"
                else: return "[?]"
            elif singleMorseCharacter[1] == "-":
                if singleMorseCharacter[2] == ".": return ","
                elif singleMorseCharacter[2] == "-": return ":"
                else: return "[?]"
            else: return "[?]"
        else: return "[?]"
    else: return "[?]"

#Plaintext to Morse
def convertPlaintextToMorse():
    global plaintext
    plaintext = plaintext.lower()
    output = ""
    for i in range(0, len(plaintext)):
        if plaintext[i] == " ": output += "/"
        elif plaintext[i] == "e": output += "."
        elif plaintext[i] == "t": output += "-"
        elif plaintext[i] == "a": output += ".-"
        elif plaintext[i] == "o": output += "---"
        elif plaintext[i] == "i": output += ".."
        elif plaintext[i] == "n": output += "-."
        elif plaintext[i] == "s": output += "..."
        elif plaintext[i] == "r": output += ".-."
        elif plaintext[i] == "h": output += "...."
        elif plaintext[i] == "d": output += "-.."
        elif plaintext[i] == "l": output += ".-.."
        elif plaintext[i] == "u": output += "..-"
        elif plaintext[i] == "c": output += "-.-."
        elif plaintext[i] == "m": output += "--"
        elif plaintext[i] == "f": output += "..-."
        elif plaintext[i] == "y": output += "-.--"
        elif plaintext[i] == "w": output += ".--"
        elif plaintext[i] == "g": output += "--."
        elif plaintext[i] == "p": output += ".--."
        elif plaintext[i] == "b": output += "-..."
        elif plaintext[i] == "v": output += "...-"
        elif plaintext[i] == "k": output += "-.-"
        elif plaintext[i] == "x": output += "-..-"
        elif plaintext[i] == "q": output += "--.-"
        elif plaintext[i] == "j": output += ".---"
        elif plaintext[i] == "z": output += "--.."
        elif plaintext[i] == "0": output += "-----"
        elif plaintext[i] == "1": output += ".----"
        elif plaintext[i] == "2": output += "..---"
        elif plaintext[i] == "3": output += "...--"
        elif plaintext[i] == "4": output += "....-"
        elif plaintext[i] == "5": output += "....."
        elif plaintext[i] == "6": output += "-...."
        elif plaintext[i] == "7": output += "--..."
        elif plaintext[i] == "8": output += "---.."
        elif plaintext[i] == "9": output += "----."
        elif plaintext[i] == "&": output += ".-..."
        elif plaintext[i] == ";": output += "-.-.-."
        elif plaintext[i] == ":": output += "---..."
        elif plaintext[i] == ",": output += "--..--"
        elif plaintext[i] == "(": output += "-.--."
        elif plaintext[i] == ")": output += "-.--.-"
        elif plaintext[i] == "!": output += "-.-.--"
        elif plaintext[i] == ".": output += ".-.-.-"
        elif plaintext[i] == "-": output += "-....-"
        elif plaintext[i] == "\"": output += ".-..-."
        elif plaintext[i] == "\'": output += ".----."
        elif plaintext[i] == "?": output += "..--.."
        elif plaintext[i] == "/": output += "-..-."
        else: output += "[?]"
        output += " "
    return output

#Main Program:
while True:
    eOrD = input("Input \"e\" to encrypt plaintext into Morse code, or \"d\" to decrypt Morse code into plaintext.\n")
    eOrD = eOrD.lower()
    if eOrD == "e" or eOrD == "d": break
    else: print ("Invalid input. Please try again.\n")
if eOrD == "d":
    morseCode = str(input("Please insert the international Morse code you want to decrypt here:   \n\n"))
    convertedOutput = convertMorseToPlaintext()
    print (f"\n\nThe inputted international Morse code translates to: \"{convertedOutput}\"\n")
elif eOrD == "e":
    plaintext = str(input("Please insert the plaintext you want to encrypt here:   \n\n"))
    convertedOutput = convertPlaintextToMorse()
    print (f"\n\nHere is the plaintext you provided encrypted into international Morse code: \"{convertedOutput}\"\n")
else: print ("Invalid input.")


