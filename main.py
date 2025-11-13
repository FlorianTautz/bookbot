import sys
from stats import count_words, count_characters, get_book_text, sort_dict

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    
    book = get_book_text(sys.argv[1])

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
