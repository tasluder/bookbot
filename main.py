def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    character_count = get_character_count(text)
    print(f"{num_words} words found in the document.")
    print(character_count)

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_character_count(text):
    character_count = {}
    lowercase_text = text.lower()
    split_lowercase_text = lowercase_text.split()
    for i in range(0, len(split_lowercase_text)):
        characters = list(split_lowercase_text[i])
        for i in range(0,len(characters)):
            if characters[i] in character_count:
                character_count[characters[i]] += 1
            else:
                character_count[characters[i]] = 1
    return character_count

main()