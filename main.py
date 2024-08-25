def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_letters(text):    
    dictionary = {}

    for letter in text:
        letter = letter.lower()
        if letter in dictionary.keys():
            dictionary[f"{letter}"] += 1
        else:
            dictionary[f"{letter}"] = 1
    
    return dictionary

def sort_on(dict):
    return dict[1]

def print_report(char_list, book_path, num_words):
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print("")
    for entry in char_list:
        if not entry[0].isalpha():
            continue
        key = entry[0]
        value = entry[1]
        print(f"The '{key}' character was found {value} times")
    print("--- End report ---")

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    num_words = get_num_words(text)
    #print(f"{num_words} words found in the document")
    char_dict = count_letters(text)
    #print(char_dict)
    char_list = list(char_dict.items())
    char_list.sort(reverse=True, key=sort_on)
    #print(char_list)
    print_report(char_list, book_path, num_words)

main()