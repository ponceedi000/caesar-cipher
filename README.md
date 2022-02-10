# Caeser Cipher

**Author**: Ediberto Ponce
**Version**: 1.0.0

- [PR Link]()

## Overview

Today I will be tackling a cryptographic classic - the Caesar Cipher. My job is to to devise a method to encrypt a message that can then be decrypted when supplied with the corresponding key. I will also need to devise a way to decipher the encrypted message event when you do NOT have the key!

## Feature Tasks and Requirements
- Create an `encrypt` function that takes in a plain text phrase and a numeric shift.
  * the phrase will then be `shifted` that many letters.
    * E.g. encrypt(‘abc’,1) would return ‘bcd’. = E.g. encrypt(‘abc’, 10) would return ‘klm’.
  * shifts that exceed 26 should wrap around.
    * E.g. encrypt(‘abc’,27) would return ‘bcd’.
- shifts that push a letter out or range should wrap around.
  * E.g. encrypt(‘zzz’,1) would return ‘aaa’.
- Create a `decrypt` function that takes in encrypted text and numeric shift which will restore the encrypted text back to its original form when correct key is supplied.
- create a `crack` function that will decode the cipher so that an encrypted message can be transformed into its original state WITHOUT access to the key.
- Devise a method for the computer to determine if code was broken with minimal human guidance.


## Architecture

- Python 3
- Pytest
- Poetry
- nltk (Natural Language Toolkit)


## Credit and Collaborations

- Brandon Mitzutani
- Alex Payne
- Connor Boyce


## Resources

- [Caesar Cipher in Cryptography](https://www.geeksforgeeks.org/caesar-cipher-in-cryptography/)
- [Caesar Cipher in Python (Text encryption tutorial)](https://likegeeks.com/python-caesar-cipher/)
- [NLTK](https://www.nltk.org/)

## Name of feature: Encrypt, Decrypt, Crack functions

- Estimate of time needed to complete: 4

- Start time: 6:30pm

- Finish time: 

- Actual time needed to complete:
