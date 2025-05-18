# OJIMBA CHIBUIKE FRANKLIN 22CN031552  COMPUTER ENGINEERING
# ASSIGNMENT 2
message = input("Enter the message to encrypt: ")

key = int(input("Enter the shift value (an integer): "))

encrypted_message = ""

for character in message:
    if character.isalpha():
        ascii_value = ord(character)

        if character.isupper():
            base = ord('A')
        else:
            base = ord('a')

        position = ascii_value - base
        new_position = (position + key) % 26
        new_ascii_value = base + new_position
        new_character = chr(new_ascii_value)
    else:
        new_character = character

    encrypted_message = encrypted_message + new_character

print("Encrypted message:", encrypted_message)
