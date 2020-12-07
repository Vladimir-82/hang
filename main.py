import random


def letter_being_alredy(current_letter, lst):#еще не задействована
    if current_letter in lst:
        print('Вы уже называли эту букву')
        return False
    else:
        return True

def russian_letter():
    letter_list = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т',
                   'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ь', 'ы', 'э', 'ю', 'я']
    current_letter=None
    while True:
        if current_letter not in letter_list or len(current_letter)>1:
            current_letter=input('Введите букву русского алфавита:')

        else:
            return current_letter

def display(HANGMAN_PICS, WORDS):

    choes = random.randint(0, len(WORDS) - 1)
    current_word = WORDS[choes]
    show_current_word = '*' * len(current_word)
    print((HANGMAN_PICS[0]))
    print(show_current_word)
    #being_alredy_list = []
    index_hangman = 1
    Lost = None

    while '*' in show_current_word:
        if Lost==True:
            break
        current_letter=russian_letter()
        #being_alredy_list.append(current_letter)

        if current_letter in current_word:

            for index_letter in range(len(current_word)):
                if current_word[index_letter]==current_letter:
                    show_current_word = show_current_word[0:index_letter:] + current_letter + show_current_word[index_letter + 1::]
                    print(show_current_word)
                    want_say_word=input('Хотите назвать слово? (Да, Нет):').lower()
                    if want_say_word=='y' or want_say_word=='yes' or want_say_word=='д' or want_say_word=='да':
                        word=input('Назовите слово:').lower()
                        if word==current_word:
                            show_current_word=word
                        else:
                            Lost=True
                            print('YOU LOST')
                            print((HANGMAN_PICS[-1]))
                            print('Неразгаданное слово:', current_word)


                    if '*' not in show_current_word:
                        print('YOU WON')

        else:
            print((HANGMAN_PICS[index_hangman]))
            print(show_current_word)
            if index_hangman==len(HANGMAN_PICS)-1:
                print('YOU LOST')
                print('Неразгаданное слово:', current_word)
                break
            index_hangman+=1

WORDS = 'кот ёжик собака корова лошадь тигр лев шакал пантера слон жираф носорог бегемот броненосец медведь лиса волк заяц кролик кобан рысь'.split()
HANGMAN_PICS=["""
 +---+
     |
     |
     |
    ===""", """
 +---+
 o   |
     |
     |
    ===""", """
 +---+
 o   |
 |   |
     |
    ===""", """
 +---+
 o   |
/|   |
     |
    ===""", """
 +---+
 o   |
/|\  |
     |
    ===""", """
 +---+
 o   |
/|\  |
/    |
    ===""", """
 +---+
 o   |
/|\  |
/ \  |
    ==="""]



print('Начнем!')
print()
print('Попробуйте отгадать животное, или будете повешаны!!!')
while True:
    display(HANGMAN_PICS, WORDS)
    game=input('Поиграем еще? (Да, Нет):').lower()
    if game=='y' or game=='yes' or game=='д' or game=='да':
        print('Ok!')
    else:
        print('Goodbuy!')
        break
