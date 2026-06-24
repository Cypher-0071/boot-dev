import sys
from stats import count_words,get_num_words

def get_book_text(filepath:str)-> str:
    with open(filepath) as f:
        file_contents:str = f.read()
    return file_contents

def print_report(filepath, count, num_count):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for value in num_count:
        print("{0}: {1}".format(value[0], value[1]))

def main():
    if len(sys.argv)<2:
        print("Usage: python3 main.py <path_to_book>")        
        sys.exit(1)
    path = sys.argv[1]
    
    book = get_book_text(path)
    count = count_words(book)
    num_words = get_num_words(book)
    print_report(path, count, num_words)
main()