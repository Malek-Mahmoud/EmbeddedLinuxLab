def isVowel(letter):
    vowels={"a","e","i","o","u"}
    if letter in vowels:
        return True
    else:
        return False


letter = input("please enter the letter: ")

letter = letter.lower()

if isVowel(letter):
    print("Yes, It is a vowel")
else:
    print("No, it is a consonant")
