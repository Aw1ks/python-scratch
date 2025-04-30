import random

LETTER_SCORES = {
    "А": 1,
    "Б": 3,
    "В": 1,
    "Г": 3,
    "Д": 2,
    "Е": 1,
    "Ё": 3,
    "Ж": 5,
    "З": 5,
    "И": 1,
    "Й": 4,
    "К": 2,
    "Л": 2,
    "М": 2,
    "Н": 1,
    "О": 1,
    "П": 2,
    "Р": 1,
    "С": 1,
    "Т": 1,
    "У": 2,
    "Ф": 10,
    "Х": 5,
    "Ц": 5,
    "Ч": 5,
    "Ш": 8,
    "Щ": 10,
    "Ъ": 10,
    "Ы": 4,
    "Ь": 3,
    "Э": 8,
    "Ю": 8,
    "Я": 3,
}


def get_random_letter():
    return random.choice(list(LETTER_SCORES.keys()))


def get_word_with_letter(letter):
    while True:
        word = input(f'Введите слово на букву {letter}: ').upper()
        if word and word[0] == letter:
            return word
        print(f'Слово начинается с буквы "{letter}". Попробуйте еще раз!')


def calculate_score(word):
    """Вычисляет сумму очков для слова на основе LETTER_SCORES."""
    all_scores = []
    for letter in word:
        scores = LETTER_SCORES.get(letter, 0)
        all_scores.append(scores)
    sum_scores = sum(all_scores)
    return sum_scores


def main():
    """Основная функция, управляющая игровым процессом."""
    letter = get_random_letter()

    print(f'Начальная буква: "{letter}"')

    print('Игрок 1')
    player_one_word = get_word_with_letter(letter)

    print('Игрок 2')
    player_two_word = get_word_with_letter(letter)

    player_one_score = calculate_score(player_one_word) 
    player_two_score = calculate_score(player_two_word) 

    print(f"Игрок 1 набрал {player_one_score} очков")
    print(f"Игрок 2 набрал {player_two_score} очков")

    if player_one_score > player_two_score:
        print(f'Победил игрок 1 со счетом: {player_one_score}.')
    elif player_one_score < player_two_score:
        print(f'Победил игрок 2 со счетом: {player_two_score}.')
    else:
        print('Победила дружба!')


if __name__ == '__main__':
    main()
