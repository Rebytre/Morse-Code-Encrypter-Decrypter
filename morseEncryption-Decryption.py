#Morse (International) to English
#By: Rebytre
#A python program designed to convert morse code into English.

def convert():
    global morseCode
    singleMorseCharacter = ""
    output = ""
    charactersSearched = 0
    while charactersSearched != len(morseCode):
        skipSpaces = avoidSpaces(charactersSearched)
        charactersSearched += skipSpaces
        singleMorseCharacter, charactersSearched = findMorseCharacter(charactersSearched)
        output += convertCharacter(singleMorseCharacter)
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
        

def convertCharacter(singleMorseCharacter):
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

#Main Program:
while True:
    morseCode = str(input("Please insert the international morse code you want to translate here:   \n\n"))
    convertedOutput = convert()
    print (f"\n\nThe inputted international morse code translates to: \"{convertedOutput}\"\n")
    print ("If you want to translate another message:")