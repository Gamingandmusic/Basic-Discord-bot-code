from random import choice, randint


def get_response(user_input: str) -> str:
    lowerd: str = user_input.lower()

    if lowerd == "well,you're awfully silent...":
        return "Well, you're awfully silent..."
    elif "hello" in lowerd:
        return "Hello!"  # noqa: F706
    elif "goodbye" in lowerd:
        return "Goodbye!"
    elif "how are you" in lowerd:
        return "Good, how are you?"
    elif "roll dice" in lowerd:
        return str(randint(1, 6))
    else:
        return choice(
            [
                "I'm sorry, I don't understand",
                "I'm not sure what you mean by that",
                "Could you rephrase that?",
            ]
        )
