# Strings, Bytes, and Character Encodings

# Words and sentences in text are created from characters e.g.  the Latin letter á or the Chinese ideograph 請
# Characters that are needed for a specific purpose are grouped into a character set (also called a repertoire)
# To refer to characters in an unambiguous way, each character is associated with a number, called a code point. eg. the decimal code point value for the letter é is 233.
# Characters are stored in the computer as one or more bytes. Basically, you can visualise this (a byte) as a special code
# A character encoding provides a key to unlock (ie. crack) the code.
# It is a set of mappings between the bytes in the computer and the characters in the character set. Without the key, the data looks like garbage.
# So, when you input text using a keyboard, for example, the character encoding maps characters you choose to specific bytes in computer memory
# , and then to display the text it reads the bytes back into characters
# Unfortunately, there are many different character sets and character encodings, ie. many different ways of mapping between bytes, code points and characters.
# But content is stored in a computer as a sequence of bytes, which are numeric values.
# Sometimes more than one byte is used to represent a single character.
# Like codes used in espionage, the way that the sequence of bytes is converted to characters depends on what key was used to encode the text.
# In this context, that key is called a character encoding.
# There are three different Unicode character encodings: UTF-8, UTF-16 and UTF-32.
# A Unicode-based encoding such as UTF-8 can support many languages and can accommodate pages and forms in any mixture of those languages.
# the same code point represents the Cyrillic character щ.
# Unicode. Unicode is a universal character encoding standard, by which each letter, digit, or symbol is assigned a unique numeric value that applies across different platforms and programs.

# We'll write a script that will take bytes written in a byte string an convert them into the UTF-8 (or other) code specified by you.
import sys
script, input_encoding, error = sys.argv


def main(language_file, encoding, errors): # define a function "main" with three parameters: language_file, encoding, errors
    line = language_file.readline() # .readline() reads a single line from the file "language_file", line as file handle

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)


def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)


languages = open("languages.txt", encoding="utf-8")

main(languages, input_encoding, error)
