import random


def game(n=10):
    print(f"""Think the number from 0 to 1000 and I will guess it as quickly as possible. {n} attempts."
          ENTER Start""")
    list_computer = []
    while len(list_computer) < n:
        user_input = input()
        if user_input == "Start":
            computer = random.randint(0, 1000)
            list_computer.append(computer)
            print(list_computer)
            continue
        if user_input == "Too small":
            random_min = list_computer[-1] + 1
            random_max = 1000
            computer = random.randint(random_min, random_max)
            list_computer.append(computer)
            print(list_computer)
            continue
        if user_input == "Too big":
            random_min = 0
            random_max = list_computer[-1] - 1
            computer = random.randint(random_min, random_max)
            list_computer.append(computer)
            print(list_computer)
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
