def print_upper_words(words):
    """Given a list of words, prints out each word in uppercase on separate lines"""
    for word in words:
        print(word.upper())

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"]) 

def print_upper_words2(words):
    """Given a list of words, prints out each word beginning with the letter E or e in uppercase on separate lines"""
    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())
print_upper_words2(["hello", "hey", "elaine", "yo", "yes"]) 

def print_upper_words3(words, must_start_with):
    for word in words:
        for letter in must_start_with:
            if word.startswith(letter) or word.startswith(letter.upper()):
                print(word.upper())
print_upper_words3(["hello", "hey", "elaine", "yo", "yes"], must_start_with={"e","y"})