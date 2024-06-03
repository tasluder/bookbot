def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    character_count = get_character_count(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the book.")
    print (" ")
    print_character_counts(character_count)
    print (" ")
    print("--- End of report ---")

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_character_count(text):
    character_count = {}
    for c in text:
        lowered = c.lower()
        if lowered in character_count:
            character_count[lowered] += 1
        else:
            character_count[lowered] = 1
    return character_count

def print_character_counts(character_dict):
    for char in character_dict:
        if not char.isalpha():
            continue
        print(f"The {char} character was found {character_dict[char]} time(s).")
    

main()