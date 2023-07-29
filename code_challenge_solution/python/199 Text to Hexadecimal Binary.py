def text_to_hex(text):
    return ''.join(hex(ord(c))[2:] for c in text)

def text_to_binary(text):
    return ''.join(format(ord(c), '08b') for c in text)

input_text = input("Enter the text: ")

print("Hexadecimal: ", text_to_hex(input_text))
print("Binary: ", text_to_binary(input_text))
