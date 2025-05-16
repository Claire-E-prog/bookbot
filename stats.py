def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    # print(file_contents)
    return file_contents

def count_words(filepath):
    count = 0
    splitstring = get_book_text(filepath).split()
    for word in splitstring:
        count += 1
    # print(f"{count} words found in the document")
    return count

def character_counts(filepath):
    alphabet = {}
    string = get_book_text(filepath).split()
    for word in string:
        letter_count = 0
        for letter in word:
            if letter.lower() not in alphabet:
                alphabet[letter.lower()] = 0
            alphabet[letter.lower()] += 1
    return alphabet

def generate_report(some_dictionary):
    string_list = []
    # l = list(some_dictionary.items())
    pairs = [(v, k) for (k, v) in some_dictionary.items()]
    pairs.sort(reverse=True)
    # print(pairs)
    for t in pairs:
        char = f"{t[1]}"
        if char.isalpha():
            string_list.append(f"{t[1]}: {t[0]}")
    return string_list
    
            

