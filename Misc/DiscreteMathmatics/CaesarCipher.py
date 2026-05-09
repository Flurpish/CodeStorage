def CaesarCipher(text, shift: int):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet.split()
    output = []
    shift %= 26
    
    for x in text:
        current = alphabet.find(x)
        if current != -1:
            output.append(alphabet[(current + shift) % 26])
        else:
            output.append(x)

    return "".join(output)


print(CaesarCipher("STOP POLLUTION", 4))
print(CaesarCipher("STOP POLLUTION", 21))
print(CaesarCipher("STOP POLLUTION", 22))

print(CaesarCipher("EOXH MHDQV", -3))
print(CaesarCipher("WHVW WRGDB", -3))
print(CaesarCipher("HDW GLP VXP", -3))
