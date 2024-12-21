


def encrypt(text,shift):
    '''
    INPUT: A shifted message and the integer shift value
    OUTPUT: The plain text original message.
    '''
    # create a normal plain alaphabet
    import string
    alphabet = string.ascii_lowercase

    #create a shifted version of this alaphabet with the shift volume
    first_half =  alphabet[:-shift]
    second_half = alphabet[-shift:]
    cipher = second_half + first_half

    encrypted_message=''
    for i,letter in enumerate(text.lower()):
        if letter in alphabet:
            original_index = alphabet.index(letter)
            new_letter = cipher[original_index]
            encrypted_message += new_letter
        else:
            encrypted_message += letter

    return encrypted_message


def decrypt(text,shift):
    '''
    INPUT: A shifted message and the integer shift value
    OUTPUT: The plain text original message.
    '''
    import string
    alphabet = string.ascii_lowercase

    #create a shifted version of this alaphabet with the shift volume
    first_half =  alphabet[:-shift]
    second_half = alphabet[-shift:]
    cipher = second_half + first_half

    decrypted_message = ''
    for i,letter in enumerate(text.lower()):
        if letter in cipher:
            original_index = cipher.index(letter)
            new_letter = alphabet[original_index]
            decrypted_message += new_letter
        else:
            decrypted_message += letter

    return decrypted_message



def brute_force(message):
    """
    INPUT: A shifted message
    OUTPUT: Prints out every possible shifted message.
            One of the printed outputs should be readable.
    """
    import string
    alphabet = string.ascii_lowercase

    for i in range(26):
        print('Using shift value of {}'.format(i))
        print(decrypt(message, i))
        print('\n')


normal_text = 'Get this message to the main server'
shift = 13
encrypted_message = encrypt(normal_text,shift)#encrypt the message
decrypted_message = encrypt(encrypted_message,shift) #dencrypt the message

print(normal_text)
print("**"*25)
print(encrypted_message)
print("**"*25)
print(decrypted_message)
print("**"*25)
brute_force(encrypted_message)
