def main():
    
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    
    print(f"--- Begin report of {book_path} ---")
    
    number_of_words = count_words(text)
    print(f"{number_of_words} words found in the document")
    
    number_of_characters = count_char(text)
    
    character_list = []
    
    for char, count in number_of_characters.items():
        if char.isalpha():
            character_list.append({"char": char, "count": count})
    
    character_list.sort(reverse=True, key=sort_on)   
    
    for item in character_list:
        print(f"The '{item['char']}' character was found {item['count']} times")
    
    print(f"--- End report ---")
    
        
def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_words(str):
    word_list = str.split()
    return len(word_list)

def count_char(str):
    character_count = {}
    lowercase_str = str.lower()
    
    for char in lowercase_str:
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1

    return character_count

def sort_on(dict):
    return dict['count']

main()