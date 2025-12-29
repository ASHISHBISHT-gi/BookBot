
def count_words():
    from main import get_book_text
    print(f"Found {len((get_book_text("./books/frankenstein.txt").split()))} tota    l words")

# count characters
def count_characters(line):
    lower_line=line.lower()
    unq_list=list(set(lower_line))
    # creating dictionary
    out_dict=dict.fromkeys(unq_list)
    for i in unq_list:
        out_dict[i]=lower_line.count(i)

    return out_dict














