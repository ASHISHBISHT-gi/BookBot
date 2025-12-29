from stats import count_words,count_characters


def get_book_text(path):
    # open and read file
    with open(path) as f:
        return f.read()


def main():
    count_words()
    data=count_characters(get_book_text("./books/frankenstein.txt"))
    print(data)
    
if __name__ == "__main__":
    main()

