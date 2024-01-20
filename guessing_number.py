import random


def game(n=10):
    print(f"""Think the number from 0 to 1000 and I will guess it as quickly as possible. {n} attempts."
          ENTER Start""")
    list_computer = []
    list_computer_min = []
    list_computer_max = []
    while len(list_computer) < n:
        user_input = input()
        if user_input == "Start":
            computer = random.randint(0, 1000)
            list_computer.append(computer)
            print(list_computer)
            continue
        if user_input == "Too small":
            random_min = max(list_computer_min, default=0)
            random_max = max(list_computer_max, default=1000)
            computer = random.randint(random_min, random_max)
            list_computer_min.append(computer)
            print(list_computer_min + list_computer_max)
            continue
        if user_input == "Too big":
            random_min = max(list_computer_min, default=0)
            random_max = max(list_computer_max, default=1000)
            computer = random.randint(random_min, random_max)
            list_computer_max.append(computer)
            print(list_computer_min + list_computer_max)
            continue
        if user_input == "You win":
            print("Thank you for the game")
            print("I'm win!")
            break
        if user_input == "Stop":
            break
        else:
            print("I'm sorry. I'm not understand")
            continue


game()
