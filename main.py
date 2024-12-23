import sys
from typing import List, Dict


def read_file(file_path: str):
    try:
        with open(file_path) as f:
            file_contents = f.read()
        return file_contents
    except FileNotFoundError as e:
        print(e)
        sys.exit(1)


def count_words(text: str) -> int:
    return len(text.split())


def count_char_occurences(
    text: str,
) -> Dict:
    out = {}
    text = text.lower()
    for char in set(text):
        out[char] = text.count(char)
    return out


def reorder_chars(chars: Dict):
    return [{k: v} for k, v in chars.items()]


def sort_chars(chars: List[Dict]):
    return sorted(chars, key=lambda x: list(x.values())[0], reverse=True)


def main():
    file_path = "books/frankenstein.txt"
    file_contents = read_file(file_path)
    num_words = count_words(file_contents)
    chars = sort_chars(reorder_chars(count_char_occurences(file_contents)))

    print(f"--- Begin report of {file_path} ---")
    print(f"Number of words: {num_words}")
    print("")

    for char in chars:
        for k, v in char.items():
            if k.isalpha():
                print(f"Character {k} was found {v} times")


if __name__ == "__main__":
    main()
