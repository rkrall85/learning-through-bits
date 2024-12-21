

import string
import random


class Encryption():
    def __init__(self, seed):
        # Set a random seed and a self.seed attribute
        random.seed(seed)
        self.seed = seed

        #Create an empty string attribute to hold the encrypted phrase
        self.encrypted_phrase = ''

        # Use the string and random libraries to create two attributes
        # One is the correct alphabet, another is a shuffled alphabet (hint: random.sample())
        alphabet = list(string.ascii_lowercase)
        cipher = random.sample(population=alphabet, k= len(alphabet))
        self.alphabet = alphabet
        self.cipher = cipher


    def encryption(self,message):
        encrypted_message = '' #creating local variable
        reverse_message= ''
        output = ''
        ################################################################
        ### STEP 1: REPLACE EVERY OTHER LETTER WITH A RANDOM LETTER ###
        ##############################################################
        for i in range(len(message)):
            encrypted_message += message[i]
            encrypted_message += random.sample(self.alphabet,1)[0]

        #################################################
        ### STEP 2: REVERSE THE STRING  ################
        ###############################################
        encrypted_message = list(encrypted_message)
        #book solution
        reverse_message = encrypted_message[::-1]
        '''
        for i in range(len(encrypted_message)-1,-1,-1):
            reverse_message += encrypted_message[i]
        '''
        ##########################################################################
        ##### STEP 3: USE THE RANDOM SHUFFLED ALPHABET FOR A CEASER CIPHER ######
        ########################################################################
        for i,letter in enumerate(reverse_message):
            if letter in self.alphabet:
                original_index = self.alphabet.index(letter)
                new_letter = self.cipher[original_index]
                output += new_letter
            else:
                output += letter

        return output #output encrypted_message

    def decrypted_message(self, message, seed):
        random.seed(seed)
        decrypted_message = ''
        reverse_message = ''
        output = ''
        #################################################
        #### Step 1: use cipher text to put back in order
        #################################################
        for i,letter in enumerate(message.lower()):
            if letter in self.cipher:
                original_index = self.cipher.index(letter)
                new_letter = self.alphabet[original_index]
                decrypted_message += new_letter
            else:
                decrypted_message += letter

        ###################################################
        ###### Step 3: reverse letters
        ##################################################
        for i in range(len(decrypted_message)-1,-1,-1):
            reverse_message += decrypted_message[i]

        ###################################################
        ###### Step 4: Remove every other letters
        ###################################################
        for i in range(len(reverse_message)):
            if i % 2 == 0:
                output += reverse_message[i]

        return output

user_seed = 20
user_text = "hello world"
e = Encryption(user_seed)
encryption_text = e.encryption(user_text)
decrypted_text = e.decrypted_message(encryption_text,user_seed)
print(user_text)
print(encryption_text)
print(decrypted_text)
