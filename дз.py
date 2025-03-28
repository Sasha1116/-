import random

def winner(user, computer):
    if user == computer:
        return "Ничья!"
    elif (user == "камень" and computer == "ножницы") or \
         (user == "ножницы" and computer == "бумага") or \
         (user == "бумага" and computer == "камень"):
        return "Вы выиграли!"
    else:
        return "Вы проиграли!"

def pick_computer_choice():
    return random.choice(["камень", "ножницы", "бумага"])

def play_game():
    user_choice = input("Выберите: камень, ножницы или бумага: ").lower()
    if user_choice not in ["камень", "ножницы", "бумага"]:
        print("Некорректный ввод, попробуйте снова.")
        return

    computer_choice = pick_computer_choice()
    print(f"Компьютер выбрал: {computer_choice}")
    print(winner(user_choice, computer_choice))


if __name__ == "__main__":
    while True:
        play_game()
        again = input("Хотите сыграть еще раз? (да/нет): ").lower()
        if again != "да":
            print("Спасибо за игру!")
            break
