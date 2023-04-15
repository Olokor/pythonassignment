from words import words
import random
import string

import requests
from bs4 import BeautifulSoup

def search_sentence(word):
    url = f"https://www.google.com/search?q={word}&tbm=nws"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    results = soup.find_all('div', {'class': 'BNeawe s3v9rd AP7Wnd'})
    for result in results:
        if word.lower() in result.text.lower():
            return result.text
    return None

def get_valid_word(words):
    word = random.choice(words)
    while '-' in words or ' ' in words:
        word = random.choice(words)

    return word

def game():
    word = get_valid_word(words)
    word_letter = set(word)
    alphabete = set(string.ascii_lowercase)#all the alphabet in uppercase
    used_letters = set()#keeps track of already used letter
    lives = 5
    while len(word_letter) > 0 and lives != 0:

        #show user already used letter

        print("you have used the following letters", ",".join(used_letters))
        print(f"you have {lives} lives")
        # some hint!
        print("this is some hint you should think about")
        # show current word i.e(w__r_d)
        sentence = search_sentence(word)
        print(sentence)
        word_list = [letter if letter in used_letters else '-' for letter in word]

        print("Current word: ", ' '.join(word_list))



        # print(word)
        user_letter = input("guess the letter:  ").casefold()
        if user_letter in alphabete - used_letters:#(if the use letter is in the alphabe - already used letter)
            used_letters.add(user_letter)
            if user_letter in word_letter:
                word_letter.remove(user_letter)
                lives += 1
            else:
                lives -= 1
                print("you've guess wrong")

        elif user_letter in used_letters:
            print("you already guess that letter, try something else")

        else:
            print("you entered an invalid character!!")
    if lives == 0:
        print("you lost!, thr word was", word)
    else:
        print("you've guess the word correctly", word)



game()


