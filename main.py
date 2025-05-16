import sys
from stats import count_words, character_counts, generate_report

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    
    word_count = count_words(book_path)
    counts_dict = character_counts(book_path)
    print_list = generate_report(counts_dict)
    
    # print report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    [print(s) for s in print_list]
    print("============= END ===============")

main()