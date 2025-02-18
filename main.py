def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    char_recurrence = get_char_recurrance(text)
    aggregate_report = get_aggregate_data(word_count, char_recurrence)
    # print(text)
    # print(word_count)
    #print(char_recurrance)



def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(string):
    words = string.split()
    word_count = len(words)
    return word_count

def get_char_recurrance(string):
    lowered_string = string.lower()
    character_dictionary = {};
    for char in lowered_string:
        if (char in character_dictionary):
            character_dictionary[char] += 1
        else:
            character_dictionary[char] = 1
    return character_dictionary

def sorting_key(dict):
        return dict['num']

def get_aggregate_data(count, chars):
    report = '--- Begin report of books/frankenstein.txt ---\n'
    report += f'{count} words found in the document\n\n'

    alphabet_chars = []

    for char in chars:
        if char.isalpha():
            alphabet_chars.append({'name': char, 'num': chars[char]})
    
    

    alphabet_chars.sort(reverse=True, key=sorting_key)

    for char in alphabet_chars:
        report += f"The '{char['name']}' character was found {char['num']} times\n"

    print(report)

main()


