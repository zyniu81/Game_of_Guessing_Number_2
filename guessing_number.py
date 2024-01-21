import random


def game(n=10):
    """
    Guess the number from 0 to 1000 as quickly as possible in n attempts.

    Args:
        n (int): Number of attempts. Default is 10.

    Raises:
        ValueError: If user cheats.
        KeyboardInterrupt: If user interrupts the game.

    Examples:
        game(5)
        Think the number from 0 to 1000 and I will guess it as quickly as possible. 5 attempts.
        ENTER Start
        Start
        500
        Too big
        250
        Too big
        125
        Too big
        62
        Too small
        94
        Too big
        78
        Too big
        70
        Too big
        66
        Too big
        [500, 250, 125, 62, 94]
        I lost game
    """
    print(f"""Think the number from 0 to 1000 and I will guess it as quickly as possible. {n} attempts."
          ENTER Start""")
    user_input = input()
    try:
        min_number = 0
        max_number = 1000
        list_computer = []
        while len(list_computer) <= n:
            computer = random.randint(min_number, max_number)
            print(computer)
            if user_input in ["Start", "Too small", "Too big", "You win", "Stop"]:
                list_computer.append(computer)
                print(list_computer)
            else:
                print("I don't understand. Last number not added to list")
            if user_input == "Start":
                pass
            user_input = input()
            if user_input == "Too small":
                min_number = computer + 1
            elif user_input == "Too big":
                max_number = computer - 1
            elif user_input == "You win":
                print(f"I'm win in {len(list_computer)} attempt")
                break
            elif user_input == "Stop":
                print("Interrupted by user")
                break
            if len(list_computer) == n:
                print(list_computer)
                print("I lost game")
                break
    except ValueError:
        print("You cheating.")
    except KeyboardInterrupt:
        print("Interrupted by user")


game()
