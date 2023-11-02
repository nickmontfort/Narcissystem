#!/usr/bin/python3

import string, re

def each_bit(document):
    """
Describe what we have line by line.
And within each line, proceed token by token,
describing whatever sequences of non-whitespace characters
are found there, separated, of course, by whitespace.
And within each token, describe each ASCII character.
ASCII characters are represented by bytes: eight bits.
Describe what eight bits are each character's one-byte representation.
"""
    text = ''
    initial = True
    for line in document:
        for token in line.split(None):
            category = 'character sequence'
            if initial and token[:3] == '#!/':
                category = 'shebang'        
            if token[:-1].isalpha() and token[-1] in string.punctuation:
                category = 'punctuated word'
            else:
                if token.isalnum():
                    category = 'alphanumeric sequence'
                else:
                    check = token
                    if len(re.sub(r'\W+', '', check)) == 0:
                        category = 'entirely non-alphanumeric sequence'
            if token.isalpha():
                category = 'word'
            if token.isdigit():
                category = 'number'
            if len(token) == 1 and token in string.punctuation:
                text += 'The single punctuation mark that is '
            else:
                text += 'The ' + category + ' "' + token + '" ... consisting of '
            for character in token:
                text += "the ASCII character '" + character + "' which is represented as a byte with the eight bits"
                for bit in format(ord(character), '008b'):
                    text += ' zero' if bit == '0' else ' one'
                text = text[:-4].rstrip() + ' and finally ' + text[-4:].lstrip() + ", followed by "
            text = text[:-14] + '. Some amount of whitespace. '
            initial = False
        if len(line.split(None)) > 0:
            text = text[:-27]
        text += 'A linebreak.\n\n'
    return text[:-2]

print()
print('NARCISSYSTEM')
print('Nick Montfort')
print('November 1, 2023 -- for NaNoGenMo')
print()

try:
    with open("narcissystem.py") as file:
        lines = file.readlines()
except OSError:
    raise IOError("Can't open myself! Where am I?!")

if len(''.join(lines)) != len(''.join(lines).encode()):
    raise IOError("Can't proceed with analysis: I have non-ASCII characters in me! Someone has been messing with me!")

print("I've opened myself up and am ready to examine and describe myself.")
print()
print("Next up:")
print(each_bit.__doc__)
print("Here we go...")
print()
print(each_bit(lines))
