def is_vowel(a):
    vowel = ["a", "e" "i", "o", "u", "A", "E", "I", "O", "U"]
    if a in vowel:
        return True
    else:
        return False
print("is this 'a' vowel letter?", is_vowel("a"))
print("is this 'b' vowel letter?", is_vowel("b"))
print("is this 'E' vowel letter?", is_vowel("E"))
print("is this 'Z' vowel letter?", is_vowel("Z"))