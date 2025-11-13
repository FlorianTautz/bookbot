import sys
from stats import count_words, count_characters, get_book_text, sort_dict

def main():

    book_name = input("Which book do you want to analyze? ")
    book_path = f"books/{book_name}.txt"
    
    try:        
        book = get_book_text(book_path)
    except FileNotFoundError:
        print(f"Error: no book found at {book_path}")
        return

    character_count = sort_dict(count_characters(book))
    allowed_characters = set("abcdefghijklmnopqrstuvwxyzæâêëô")



    print("============ BOOKBOT ============")
    print("Analyzing book found at -...")
    print("----------- Word Count ----------")
    print (f"Found {count_words(book)} total words")
    print("--------- Character Count -------")

    for item in character_count:
        char = item["char"]
        count = item["num"]

        if char not in allowed_characters:
            continue
    
        print(f"{char}: {count}")



main()
