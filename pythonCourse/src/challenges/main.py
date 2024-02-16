from src.challenges.challenge_1 import challenge_1
from src.challenges.challenge_2 import challenge_2
from src.challenges.challenge_3 import challenge_3
from src.challenges.challenge_4 import challenge_4
from src.challenges.challenge_5 import challenge_5
from src.challenges.challenge_6 import challenge_6
from src.challenges.challenge_7 import challenge_7
from src.challenges.challenge_8 import challenge_8
from src.challenges.challenge_9 import challenge_9


def run_challenge(number: int):
    """Run the challenge"""
    match number:
        case 1:
            challenge_1()
        case 2:
            challenge_2()
        case 3:
            challenge_3()
        case 4:
            challenge_4()
        case 5:
            challenge_5()
        case 6:
            challenge_6()

        case 7:
            challenge_7()
        case 8:
            challenge_8()
        case 9:
            challenge_9()
        case _:
            print("NOT NOT\n")


challenges = [
    "challenge one: strings\n",
    "\nchallenge two: exceptions and if/else statement\n",
    "\nchallenge three: lists and for loop\n",
    "\nchallenge four: dictionaries\n",
    "\nchallenge five: dictionaries\n",
    "\nchallenge six: classes\n",
    "\nchallenge seven: methods\n",
    "\nchallenge eight: imports and composition\n",
    "\nchallenge nine: classes and inheritance\n",
]


def run_challenges():
    """run all challenges"""
    print("------------------ CHALLENGES ------------------\n")
    for i, challenge_name in enumerate(challenges):
        print(challenge_name)
        run_challenge(number=i)


def main():
    """The main function responsible to run challenges"""
    run_challenges()


if __name__ == "__main__":
    main()
