print('Enter the english message to translate in Pig Latin:')
message=input()
VOWELS = ('a','e','i','o','u','y')
piglatin=[]
for word in message.split():
    prefixnonletters =''
    while len(word) >0 and not word[0].isalpha():
        prefixnonletters +=word[0]
        word = word[1:]
    if len(word)==0:
        piglatin.append(prefixnonletters)
        continue
    suffixNonLetters=''
    while not word[-1].isalpha():
        suffixNonLetters += word[-1]
        word = word[:-1]

    # Remember if the word was in uppercase or title case.
    wasUpper = word.isupper()
    wasTitle = word.istitle()

    word = word.lower() # Make the word lowercase for translation.

    # Separate the consonants at the start of this word:
    prefixConsonants = ''
    while len(word) > 0 and not word[0] in VOWELS:
        prefixConsonants += word[0]
        word = word[1:]

    # Add the Pig Latin ending to the word:
    if prefixConsonants != '':
        word += prefixConsonants + 'ay'
    else:
        word += 'yay'

    # Set the word back to uppercase or title case:
    if wasUpper:
        word = word.upper()
    if wasTitle:
        word = word.title()

    # Add the non-letters back to the start or end of the word.
    piglatin.append(prefixnonletters + word + suffixNonLetters)

# Join all the words back together into a single string:
print(' '.join(piglatin))