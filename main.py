def main():
    path =  "github.com/bookbot/books/frankenstein.txt"
    with open(path) as f:
        text = f.read()
    word_count = count_words(text)
    dict = count_characters(text, count_words(text))

    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in this document")
    print("")
    print_dict(dict)
    
def count_words(text):
    text_words = text.split()
    count = 0
    for words in text_words:
        count += 1
    
    return count

def count_characters(text, num):
    text = text.lower()
    char_count = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0,
                  'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0,
                  'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0,
                  'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0,
                  'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0,
                  'z':0}
    characters_list = ['a', 'b', 'c', 'd', 'e', 'f',
                       'g', 'h', 'i', 'j', 'k', 'l',
                       'm', 'n', 'o', 'p', 'q', 'r',
                       's', 't', 'u', 'v', 'w', 'x',
                       'y', 'z']
    for i in range(0, len(text)):
        if(text[i] in characters_list):
            char_count[text[i]] = char_count[text[i]] + 1
    
    return char_count
    
def print_dict(dict):
    characters_list = ['a', 'b', 'c', 'd', 'e', 'f',
                       'g', 'h', 'i', 'j', 'k', 'l',
                       'm', 'n', 'o', 'p', 'q', 'r',
                       's', 't', 'u', 'v', 'w', 'x',
                       'y', 'z']
    for char in characters_list:
        print(f"The '{char}' character was found {dict[char]} times" ) 


    

main()