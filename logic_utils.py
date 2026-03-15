import random


def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def reset_game_state(state, low: int, high: int):
    """Reset a Streamlit session state to start a new game.

    This is used by the New Game button and is kept as a pure helper so it can be
    unit tested without running Streamlit.
    """

    state["attempts"] = 1
    state["secret"] = random.randint(low, high)
    state["status"] = "playing"
    state["history"] = []
    state["score"] = 0


def parse_guess(raw: str):
    """Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """

    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def validate_guess(raw: str, low: int, high: int):
    """Validate user guess input and enforce range bounds.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    ok, guess_int, err = parse_guess(raw)
    if not ok:
        return ok, guess_int, err

    if guess_int < low or guess_int > high:
        return False, guess_int, f"Guess must be between {low} and {high}."

    return True, guess_int, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    if guess == secret:
        return "Win", "🎉 Correct!"

    try:
        # FIX: Refactored logic into logic_utils.py and fixed bug where "Go HIGHER!" and "Go LOWER!" hints were reversed using Copilot Agent mode
        if guess > secret:
            return "Too High", "📉 Go LOWER!"
        else:
            return "Too Low", "📈 Go HIGHER!"
    except TypeError:
        g = str(guess)
        if g == secret:
            return "Win", "🎉 Correct!"
        if g > secret:
            return "Too High", "📉 Go LOWER!"
        return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")
