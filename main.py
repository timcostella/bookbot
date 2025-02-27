import sys

from stats import count_words, count_characters, create_report

def main():
    if len(sys.argv) != 2:
        print ("Usage: python3 main.py <path to book>")
        sys.exit(1)
    else:
        filepath = sys.argv[1]

        #count_words(filepath)
        #count_characters(filepath)
        create_report(filepath)

main()
