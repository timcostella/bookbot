def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def count_words(filepath):
    book = get_book_text(filepath)
    word_list = book.split(None)
    print(f"Found {len(word_list)} total words in the document")

def count_characters(filepath):
    book = get_book_text(filepath)
    all_chars_count = {}
    for char in book:
        char = char.lower()
        if char not in all_chars_count:
            all_chars_count[char] = 1
        else:
            all_chars_count[char] +=1
    
    return all_chars_count


def count_characters_report(filepath):
    char_dict = count_characters(filepath)
    char_dict_list = []
    for key in char_dict:
        temp_dict = {}
        temp_dict[key] = char_dict[key]
        char_dict_list.append(temp_dict)
    char_dict_list.sort(reverse=True,key=lambda x: list(x.values())[0])
    for Tdict in char_dict_list:
        for key in Tdict:
            print(f"{key}: {Tdict[key]}")


def create_report(filepath):
    # print the header
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    count_words(filepath)
    print("--------- Character Count -------")
    count_characters_report(filepath)
    print("============= END ===============")
    
    