from .constants import PLAYER_ANSWERS


def ask_yes_or_no_question(question: str) -> bool:
    while True:
        answer = input(f'{question} (y/n) ')

        if answer not in PLAYER_ANSWERS.keys():
            print('Use only "y" or "n". Let me ask you one more time...')
            continue

        does_player_want = PLAYER_ANSWERS[answer]
        return does_player_want
