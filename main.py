#!/usr/bin/env python3

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_characters = character_count(text)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document\n")
    for char in sorted(num_characters.keys()):
        print(f"The '{char}' character was found {num_characters[char]} times")
    print("--- End report ---")

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def character_count(text):
    character_dict = {}
    for letter in text.lower():
        if letter.isalpha():
            if letter in character_dict:
                character_dict[letter] += 1
            else:
                character_dict[letter] = 1
    return character_dict

main()
