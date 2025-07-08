def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def decrypt(cipher, shift):
    return encrypt(cipher, -shift)

message = "Hello World"
shift = 3

encrypted = encrypt(message, shift)
decrypted = decrypt(encrypted, shift)

print(f"Original: {message}")
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")
