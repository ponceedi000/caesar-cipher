import nltk
# Below import for pytest
from caesar_cipher.corpus import names_list, words_list
#Below import for running python file
# from corpus import names_list, words_list
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
 
# Simply inverses key to bring characters back to it's orignal state
def decrypt(encrypted, key):
    return encrypt(encrypted, -key)

# First we loop through the length of alphabet(26 characters) and create word counter variable, assign words variable to our encrypt() function and split said function
# The next for loop iterates through our list and adds to word counter. It also utilizes the nltk .names and .words from it's library to help decrpyt with brute force
# Finally, if our word count / length of list (encypted message) is moire than 50%, then returned the joined characters with decrpyted message
# Otherwise, return uncracked string
def crack(encrypted):
  for i in range(26):
      word_count = 0
      words = encrypt(encrypted, i)
      list = words.split()
      for text in list:
          if text in names_list or text.lower() in words_list:
              word_count += 1
      
      if (word_count/len(list)) > .5:
          return " ".join(list)

  return ""
# Proof of concept below
if __name__ == '__main__':
  print(encrypt('dog', 1))
  print(decrypt('eph', 1))
  print(crack('J mjlf epht'))

