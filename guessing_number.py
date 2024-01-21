import random


def game(n=10):
    print(f"""Think the number from 0 to 1000 and I will guess it as quickly as possible. {n} attempts."
          ENTER Start""")
    user_input = input()
    if user_input == "Start":
        pass
    try:
        min_number = 0
        max_number = 1000
        list_computer = []
        while len(list_computer) <= n * 2 - 2:
            computer = random.randint(min_number, max_number)
            list_computer.append(computer)
            print(computer)
            user_input = input()
            if user_input == "Too small":
                min_number = computer + 1
                list_computer.append(min_number)
            elif user_input == "Too big":
                max_number = computer - 1
                list_computer.append(max_number)
            elif user_input == "You win":
                print(f"I'm win in {len(list_computer) / 2 + 0.5} attempt")
                break
            elif user_input == "Stop":
                print("Interrupted by user")
                break
            else:
                print("I didn't understand")
            if len(list_computer) == n * 2:
                print(list_computer)
                print("I lost game")
                break
    except ValueError:
        print("You cheating.")
    except KeyboardInterrupt:
        print("Interrupted by user")


game()
