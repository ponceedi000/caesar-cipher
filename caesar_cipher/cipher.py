import nltk
from nltk.corpus import words, names
# nltk.download()

def encrypt(plain,key):
    encrypted_text = ""
 
    # traverse text
    for i in range(len(plain)):
        char = plain[i]
 
        # Encrypt uppercase characters
        if (char.isupper()):
          encrypted_text += chr((ord(char) + key-65) % 26 + 65)
 
        # Encrypt lowercase characters
        elif (char.islower()):
          encrypted_text += chr((ord(char) + key - 97) % 26 + 97)

        # Get rid of white space
        elif char == " ":
          encrypted_text += char

        # Handles special characters
        else:
          encrypted_text += char

 
    return encrypted_text
 

def decrypt(encrypted, key):
    return encrypt(encrypted, -key)

def crack(encrypted):
    pass

if __name__ == "__main__":


  encr2 = decrypt('fph')
  assert encr2 == 'dog'
