def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    
    return contents

def count_words(contents):
    word_list = contents.split()
    word_count = len(word_list)

    return word_count

def count_characters(book_text): #Function that iterates through a string and returns the number of appearances each character makes

    lower_text = book_text.lower() #turn the string into all lower case
    char_count = {} #define empty dictionary

    for char in lower_text: #iterate through each character in the string
        if char in char_count: # if a character (key) already exists in the dictionary
            char_count[char] += 1 # update its value by 1
        else:
            char_count[char] = 1 #else, create a key by setting its value to 1
    
    return char_count

def return_num(item):
    return item["num"]

def sort_dict(char_count):
    
    char_list = []

    for char, count in char_count.items():
        char_list.append({"char": char, "num": count})

    char_list.sort(reverse=True, key=return_num)
    
    return char_list